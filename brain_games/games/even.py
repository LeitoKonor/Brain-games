"""Brain-Even Game."""

from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    """Make game question and answer."""
    number = randint(1, 99)
    question = is_even(number)
    if question is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def is_even(number):
    return True if number % 2 == 0 else False
