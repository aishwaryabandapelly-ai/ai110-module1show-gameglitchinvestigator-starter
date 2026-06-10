import sys
from pathlib import Path

# Ensure the project root (which contains logic_utils.py) is importable
# regardless of the directory pytest is invoked from.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from logic_utils import check_guess, get_range_for_difficulty


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
