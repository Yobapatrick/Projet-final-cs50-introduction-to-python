import pytest
import re
from datetime import datetime
from project import QuizGame  


def test_age_verification():
    game = QuizGame()

    birth_date = datetime(2000, 1, 1)
    today = datetime(2025, 1, 1)
    age = (today - birth_date).days // 365
    assert age == 25


def test_email_validation():
    game = QuizGame()

    valid_emails = [
        "test@example.com",
        "prenom.nom@domaine.fr",
        "email123@sub.domain.com"
    ]

    for email in valid_emails:
        assert game.validate_email(email) == True


    invalid_emails = [
        "test@@example.com",
        "nomdomaine.com",
        "email@domain"
    ]

    for email in invalid_emails:
        assert game.validate_email(email) == False


def test_score_update():
    game = QuizGame()
    game.score = 0
    game.update_score(correct=True)
    assert game.score == 1
    game.update_score(correct=False)
    assert game.score == 1

def test_theme_choice():
    game = QuizGame()
    themes = ["Football", "Science", "Histoire", "Géographie"]
    for t in themes:
        assert t in themes
