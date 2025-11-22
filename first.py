import random

#!/usr/bin/env python3
"""
Simple Snake and Ladder game (console)
Save as C:/ips/first.py and run with Python 3.
"""


BOARD_SIZE = 100

# Typical snakes and ladders configuration (can be modified)
LADDERS = {
    2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44,
    51: 67, 71: 91, 78: 98, 87: 94
}
SNAKES = {
    16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53,
    89: 68, 92: 88, 95: 75, 99: 80
}


def roll_dice():
    return random.randint(1, 6)


def apply_snakes_ladders(pos):
    if pos in LADDERS:
        return LADDERS[pos], 'LADDER'
    if pos in SNAKES:
        return SNAKES[pos], 'SNAKE'
    return pos, None


def play(num_players=2, require_exact=True):
    positions = [0] * num_players
    turn = 0
    print(f"Starting Snake and Ladder with {num_players} players. First to reach {BOARD_SIZE} wins.")
    while True:
        player = turn % num_players
        input(f"Player {player + 1}'s turn. Press Enter to roll the dice...")
        dice = roll_dice()
        print(f"Player {player + 1} rolled: {dice}")
        next_pos = positions[player] + dice

        if require_exact and next_pos > BOARD_SIZE:
            print(f"Need exact roll to reach {BOARD_SIZE}. Remains at {positions[player]}.")
        else:
            if next_pos > BOARD_SIZE:
                next_pos = BOARD_SIZE  # when not requiring exact
            positions[player] = next_pos
            print(f"Player {player + 1} moved to {positions[player]}")

            # apply snakes or ladders
            new_pos, kind = apply_snakes_ladders(positions[player])
            if kind == 'LADDER':
                print(f"  Hit a ladder! Climb up to {new_pos}")
                positions[player] = new_pos
            elif kind == 'SNAKE':
                print(f"  Ouch! Hit a snake. Slide down to {new_pos}")
                positions[player] = new_pos

        # show all positions
        print("Positions:", ", ".join(f"P{idx+1}:{pos}" for idx, pos in enumerate(positions)))

        if positions[player] == BOARD_SIZE:
            print(f"Player {player + 1} wins!")
            break

        turn += 1


def ask_int(prompt, default):
    try:
        val = input(f"{prompt} [{default}]: ").strip()
        return int(val) if val else default
    except ValueError:
        return default


if __name__ == "__main__":
    print("Snake and Ladder CLI")
    players = ask_int("Number of players", 2)
    exact = input("Require exact roll to reach 100? (y/n) [y]: ").strip().lower()
    require_exact = (exact != 'n')
    play(num_players=max(1, players), require_exact=require_exact)