import pytest
from grades import average, has_passed, letter_grade, PASS_MARK


def test_average():
    assert average([50, 60, 70]) == pytest.approx(60.0)


def test_average_rejects_empty_list():
    with pytest.raises(ValueError):
        average([])


def test_score_below_pass_mark_fails():
    assert has_passed(39) is False


def test_score_above_pass_mark_passes():
    assert has_passed(55) is True


def test_score_exactly_at_pass_mark_passes():
    assert has_passed(PASS_MARK) is True


def test_letter_grades():
    assert letter_grade(95) == "A"
    assert letter_grade(80) == "B"
    assert letter_grade(65) == "C"
    assert letter_grade(20) == "F"


def test_letter_grade_at_pass_mark_is_d():
    assert letter_grade(40) == "D"


def test_letter_grade_rejects_out_of_range():
    with pytest.raises(ValueError):
        letter_grade(120)
