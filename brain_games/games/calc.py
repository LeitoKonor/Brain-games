"""Brain-Calc Game."""

from random import choice, randint
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'


def get_game():
    """Make game question and answer."""
    operand_first = randint(1, 20)
    operand_second = randint(1, 20)
    operation, operator = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*'),
    ])
    question = f"{operand_first} {operator} {operand_second}"
    correct_answer = is_calc(operand_first, operand_second, operation)
    return question, str(correct_answer)


def is_calc(operand_first, operand_second, operation):
    return operation(operand_first, operand_second)
