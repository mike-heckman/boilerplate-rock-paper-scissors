# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from RPS_game import mrugesh, quincy, kris, abbey


VALID_PLAYS = ["R", "P", "S"]
ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

def player(prev_play, 
           opponent_history=[], 
           counter=[0], 
           play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0
              }], 
              my_moves=[], 
              opponent_function=[None]
              ):

    if prev_play:
        opponent_history.append(prev_play)
    else:
        print("Resetting opponent history and play order")
        opponent_history.clear()
        counter[0] = 0
        [play_order[0].update({k: 0 for k in play_order[0]})]
        my_moves.clear()
        opponent_function[0] = None

    if len(opponent_history) > 4 and opponent_function[0] is None:
        last_five = "".join(opponent_history[-5:])

        if last_five == "RPPSR":
            opponent_function[0] = "quincy"
            print("Quincy detected")
        elif last_five == "RRRRR":
            opponent_function[0] = "mrugesh"
            print("Mrugesh detected")
        elif last_five == "PSRRP":
            opponent_function[0] = "kris"
            print("Kris detected")
        elif last_five == "PPPRS": # ?
            opponent_function[0] = "abbey"
            print("Abbey detected")

    play = counter_move(opponent_function[0], my_moves, counter, play_order)
    my_moves.append(play)

    return play


def counter_move(opponent_fn, my_moves, counter, play_order):
    """
    This function determines the next move based on the opponent's history and the chosen strategy.
    """
    latest = my_moves[-1] if my_moves else ""
    previous_moves = [*my_moves[:-1]] if my_moves else []
    if my_moves and (opponent_fn == "abbey" or not opponent_fn):
        previous_moves = ["R"] + previous_moves  # Abbey needs at least one move to start

    if opponent_fn == "quincy":
        their_play = quincy(latest, counter=counter)
    elif opponent_fn == "mrugesh":
        their_play = mrugesh(latest, opponent_history=previous_moves)
    elif opponent_fn == "kris":
        their_play = kris(latest)
    elif opponent_fn == "abbey":
        their_play = abbey(latest, opponent_history=previous_moves, play_order=play_order)
    # Unknown opponent function, default to quincy, but keep abbey's play order
    else:
        abbey(latest, opponent_history=previous_moves, play_order=play_order)
        their_play = quincy(latest, counter=counter)

    return ideal_response[their_play]    

