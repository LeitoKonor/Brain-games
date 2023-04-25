"""Brain Prime Game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return "no"
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True


def get_game():
    """Make game question and answer."""
    number = randint(1, 21)
    question = is_prime(number)
    if question is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
