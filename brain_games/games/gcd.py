"""Brain-Gcd Game."""

from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_game():
    """Make game question and answer."""
    number_first = randint(1, 50)
    number_second = randint(1, 50)
    question = f'{number_first} {number_second}'
    correct_answer = gcd(number_first, number_second)
    return question, str(correct_answer)
