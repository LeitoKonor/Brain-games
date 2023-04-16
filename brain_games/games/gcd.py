"""Brain-Gcd Game."""

from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question_and_correct_answer():
    """Make game question and answer."""
    min_number = 1
    max_number = 50
    number_first = randint(min_number, max_number)
    number_second = randint(min_number, max_number)
    question = f'{number_first} {number_second}'
    correct_answer = gcd(number_first, number_second)
    return question, str(correct_answer)
