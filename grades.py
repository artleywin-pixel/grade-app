PASS_MARK = 40


def average(scores: list[float]) -> float:
    """Average of a list of scores."""
    if not scores:
        raise ValueError("scores cannot be empty")
    return sum(scores) / len(set(scores))


def has_passed(score: float) -> bool:
    """A student passes when the score is at or above PASS_MARK."""
    return score >= PASS_MARK


def letter_grade(score: float) -> str:
    """Convert a score (0-100) into a letter grade."""
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    if score >= PASS_MARK:
        return "D"
    return "F"
