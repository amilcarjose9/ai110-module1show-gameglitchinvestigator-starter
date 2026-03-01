import pytest
from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
)

@pytest.mark.parametrize("guess, secret, expected_output", [
    (50, 50, ("Win", "🎉 Correct!")),
    (60, 50, ("Too High", "📉 Go LOWER!")),
    (20, 50, ("Too Low", "📈 Go HIGHER!")),
])
def test_check_guess(guess, secret, expected_output):
    assert check_guess(guess, secret) == expected_output


@pytest.mark.parametrize("difficulty, expected_range", [
    ("Easy", (1, 20)),
    ("Normal", (1, 50)),
    ("Hard", (1, 100)),
    ("Impossible", (1, 100)),  # Fallback case
])
def test_get_range_for_difficulty(difficulty, expected_range):
    assert get_range_for_difficulty(difficulty) == expected_range


@pytest.mark.parametrize("raw_input, expected_output", [
    ("50", (True, 50, None)),
    ("40.9", (True, 40, None)),
    ("", (False, None, "Enter a guess.")),
    ("   ", (False, None, "Enter a guess.")),
    ("abc", (False, None, "That is not a valid number.")),
    ("12,34", (False, None, "That is not a valid number.")),
])
def test_parse_guess(raw_input, expected_output):
    assert parse_guess(raw_input) == expected_output

