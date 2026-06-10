import random
import streamlit as st

# FIX: Used the AI coding assistant to refactor check_guess (and get_range_for_difficulty)
# out of app.py and into logic_utils.py, then import them back here.
from logic_utils import check_guess, get_range_for_difficulty, parse_guess


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def render_guess_history():
    """Render previous guesses and a short session summary.

    Display-only: this reads from session state and never mutates the
    secret, score, attempts, or status, so it cannot affect the core game
    logic. Directional outcomes are only shown when the "Show hint" option
    is enabled, matching the hint toggle used during play.
    """
    st.subheader("📜 Guess History")

    history = st.session_state.history
    if not history:
        st.write("No guesses yet — make your first guess above!")
    else:
        for position, past_guess in enumerate(history, start=1):
            if isinstance(past_guess, int):
                if show_hint:
                    outcome, _ = check_guess(past_guess, st.session_state.secret)
                    st.write(f"{position}. **{past_guess}** — {outcome}")
                else:
                    st.write(f"{position}. **{past_guess}**")
            else:
                st.write(f"{position}. ⚠️ Invalid entry: {past_guess!r}")

    attempts_left = max(attempt_limit - st.session_state.attempts, 0)
    st.caption(
        f"Difficulty: {difficulty} ({low}–{high})  ·  "
        f"Guesses made: {len(history)}  ·  "
        f"Attempts left: {attempts_left}  ·  "
        f"Score: {st.session_state.score}"
    )


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    # FIX: AI helped identify the off-by-one bug where attempts started at 1
    # (showing 7 left on Normal); attempts now start at 0.
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "difficulty" not in st.session_state:
    st.session_state.difficulty = difficulty

# FIX: AI helped spot stale difficulty state — changing difficulty kept the old
# secret/range, so we now reset the game when the selected difficulty changes.
if st.session_state.difficulty != difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []

st.subheader("Make a guess")

# FIX: AI helped catch the hardcoded "1 and 100" range text; it now shows the
# selected difficulty's actual range dynamically.
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    # FIX: AI helped fix the New Game button to fully reset state — secret (using
    # the selected difficulty range), attempts, score, status, and history.
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    render_guess_history()
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

render_guess_history()

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
