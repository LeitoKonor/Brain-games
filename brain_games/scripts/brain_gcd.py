#!/usr/bin/env python3
"""Brain-Gcd Game start."""


from brain_games.engine import run_game
from brain_games.games import gcd


def main():
    """Start the "Brain-Gcd Game"."""
    run_game(gcd)


if __name__ == '__main__':
    main()
    