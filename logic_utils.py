def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guessing range for a difficulty level.

    Args:
        difficulty: One of ``"Easy"``, ``"Normal"``, or ``"Hard"``.

    Returns:
        tuple[int, int]: The ``(low, high)`` inclusive bounds. Easy is
        1–20, Normal is 1–100, and Hard is 1–50. Any unrecognized value
        falls back to the Normal range of 1–100.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse raw user input into an integer guess.

    Decimal strings are accepted and truncated toward zero (for example,
    ``"3.9"`` becomes ``3``). Empty/missing input and non-numeric text are
    rejected with a player-facing message. No range validation is applied
    here, so negative or very large numbers parse successfully.

    Args:
        raw: The raw string entered by the player (may be ``None`` or
            ``""``).

    Returns:
        tuple: ``(ok, guess_int, error_message)``. ``ok`` is True only when
        parsing succeeds; on success ``guess_int`` is the int and
        ``error_message`` is ``None``. On failure ``guess_int`` is ``None``
        and ``error_message`` describes the problem.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


# FIX: AI helped refactor this function out of app.py into logic_utils.py so the
# game logic is isolated and unit-testable.
def check_guess(guess, secret):
    """Compare a guess against the secret number.

    Args:
        guess: The player's numeric guess.
        secret: The secret number to be guessed.

    Returns:
        tuple[str, str]: An ``(outcome, message)`` pair. ``outcome`` is one
        of ``"Win"``, ``"Too High"``, or ``"Too Low"``, and ``message`` is
        the matching player-facing hint.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: AI helped trace and correct the reversed hint messages — a guess that is
    # too high now tells the player to go LOWER, and too low to go HIGHER.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Compute the updated score after a guess.

    Note:
        Not yet refactored into this module; the active implementation
        currently lives in ``app.py``. Calling this stub raises
        ``NotImplementedError``.

    Args:
        current_score: The score before this guess.
        outcome: The result from :func:`check_guess` (``"Win"``,
            ``"Too High"``, or ``"Too Low"``).
        attempt_number: The attempt count for the current guess.

    Returns:
        int: The updated score.
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
