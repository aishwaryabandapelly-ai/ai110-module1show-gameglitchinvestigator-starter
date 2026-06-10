# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

This project started as a glitchy AI-generated Streamlit number guessing game.  
The original version looked simple, but the game behavior was confusing and unreliable.

- The hints were misleading.
- The attempt count did not behave correctly.
- The New Game button did not fully reset the game.
- Difficulty changes could create inconsistent game state.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`
3. Run the tests: `python -m pytest tests/ -v`

## 📂 Project Structure

- `app.py` — the Streamlit app: UI, session state, game flow, and the Guess History display.
- `logic_utils.py` — the testable game logic: `get_range_for_difficulty()`, `parse_guess()`, and `check_guess()`, each documented with docstrings.
- `tests.py` — pytest coverage for the game logic and edge cases.
- `reflection.md` — written reflection on the bugs, process, and testing.
- `ai_interactions.md` — log of how AI tools (ChatGPT and Claude) were used, including a model comparison.

## 🕵️‍♂️ Debugging Mission

1. Play the broken game and observe the incorrect behavior.
2. Identify bugs in the hint logic, attempts, New Game reset, and difficulty handling.
3. Refactor core game logic into `logic_utils.py`.
4. Add pytest coverage for the fixed logic and edge cases.
5. Document the debugging process and AI collaboration.

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - It is a Streamlit number guessing game. The player picks a difficulty, guesses a number in that range, and gets "higher/lower" hints until they win or run out of attempts.
- [x] Detail which bugs you found.
  - The hint messages were reversed (too-high guesses told me to go higher). Attempts started at 1, so Normal showed 7 left instead of 8. The New Game button did not fully reset the game. Switching difficulty left a stale secret and the info banner always said "1 and 100" regardless of difficulty.
- [x] Explain what fixes you applied.
  - I moved `check_guess()` into `logic_utils.py`, corrected the high/low hints, changed attempts to start at 0, made New Game reset secret/attempts/score/status/history, and reset state on difficulty change while making the range banner dynamic.

## 📸 Demo Walkthrough

A text-based walkthrough of the fixed game so a reader can follow along without a screenshot or video:

1. Run `python -m streamlit run app.py` and open the app in the browser.
2. In the sidebar, pick a difficulty (Easy 1–20, Normal 1–100, or Hard 1–50). The info banner now shows the correct range for that difficulty, and "Attempts left" starts at the full amount (for example, 8 on Normal).
3. Enter a guess that is too high — the game correctly says "Go LOWER." Enter one that is too low — it says "Go HIGHER."
4. Watch the **Guess History** section below the buttons. It lists every previous guess in order, and (when "Show hint" is on) shows whether each was Too High, Too Low, or a Win. A short session summary line shows the difficulty/range, guesses made, attempts left, and current score.
5. Keep narrowing in until you guess the secret number; the game shows a win message and final score, and the Guess History stays visible on the end screen.
6. Click "New Game" to fully reset the secret, attempts, score, status, and history, or switch difficulty in the sidebar to start a fresh game in the new range.

## 🧪 Test Results

Run with `python -m pytest tests/ -v`. The full suite (core logic + edge cases) passes:

```
============================= test session starts ==============================
platform darwin -- Python 3.14.0, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/aish/Desktop/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 7 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 14%]
tests/test_game_logic.py::test_guess_too_high_tells_player_to_go_lower PASSED [ 28%]
tests/test_game_logic.py::test_guess_too_low_tells_player_to_go_higher PASSED [ 42%]
tests/test_game_logic.py::test_difficulty_ranges PASSED                  [ 57%]
tests/test_game_logic.py::test_parse_guess_decimal_truncates_toward_zero PASSED [ 71%]
tests/test_game_logic.py::test_parse_guess_out_of_range_values_are_accepted PASSED [ 85%]
tests/test_game_logic.py::test_parse_guess_empty_and_non_numeric_are_rejected PASSED [100%]

============================== 7 passed in 0.01s ===============================
```

## Optional Challenges Completed

## Challenge 1: Advanced Edge-Case Testing

I added pytest tests for edge-case inputs, including negative guesses, very large guesses, decimal input (which truncates toward zero), invalid text input, and empty input. These tests live in `tests/test_game_logic.py` and cover `parse_guess()` after it was refactored into `logic_utils.py`.

Final pytest output:

```
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.14.0, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/aish/Desktop/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 7 items

tests/test_game_logic.py .......                                                                                                                      [100%]

===================================================================== 7 passed in 0.01s =====================================================================
```

## Challenge 2: Feature Expansion

Completed. I added a read-only Guess History feature plus a one-line session summary in `app.py` (see the `render_guess_history()` function). The history lists previous guesses, and the summary shows the difficulty/range, guesses made, attempts left, and current score. It does not change the core guessing logic, scoring, or difficulty ranges.

## Challenge 3: Professional Documentation and Linting

Completed. I added professional docstrings to every function in `logic_utils.py` (`get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score`) and reviewed the file for safe PEP 8 formatting without changing any behavior.

## Challenge 4: Enhanced Game UI

Completed. The UI now includes a clearer "📜 Guess History" list and a session summary line beneath the game controls, so the player can see their previous guesses and current status at a glance. The history also stays visible on the game-over screen.

## Challenge 5: AI Model Comparison

Completed. I compared ChatGPT and Claude in `ai_interactions.md` (the Model Comparison section). In short, ChatGPT helped me plan prompts and understand Git/workflow, while Claude in VS Code directly edited and refactored the code; I manually reviewed suggestions and rejected misleading ones, such as changing Hard difficulty to 1–200.
