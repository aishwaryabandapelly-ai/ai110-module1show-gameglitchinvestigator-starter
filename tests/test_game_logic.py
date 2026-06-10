import sys
from pathlib import Path

# Ensure the project root (which contains logic_utils.py) is importable
# regardless of the directory pytest is invoked from.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess


# check_guess returns a (outcome, message) tuple.

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win.
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_tells_player_to_go_lower():
    # Guess 60 vs secret 50: too high, message should tell player to go lower.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()


def test_guess_too_low_tells_player_to_go_higher():
    # Guess 40 vs secret 50: too low, message should tell player to go higher.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()


def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


# --- Challenge 1: Advanced edge-case testing for parse_guess ---

def test_parse_guess_decimal_truncates_toward_zero():
    # Edge case: decimal input. "3.9" is parsed as int(float("3.9")) == 3,
    # so it truncates rather than rounding. This documents that behavior.
    ok, value, err = parse_guess("3.9")
    assert ok is True
    assert value == 3
    assert err is None

    ok, value, err = parse_guess("49.9")
    assert ok is True
    assert value == 49


def test_parse_guess_out_of_range_values_are_accepted():
    # Edge case: negative and extremely large inputs. parse_guess does NOT
    # validate against the difficulty range, so these parse as "valid".
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None

    ok, value, err = parse_guess("999999")
    assert ok is True
    assert value == 999999


def test_parse_guess_empty_and_non_numeric_are_rejected():
    # Edge case: empty, whitespace-only, and non-numeric text.
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

    ok, value, err = parse_guess(None)
    assert ok is False
    assert err == "Enter a guess."

    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

    ok, value, err = parse_guess("4 2")
    assert ok is False
    assert err == "That is not a number."
