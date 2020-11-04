from calculator import *


def idle():
    idle = input("-- HIT RETURN TO CONTINUE --" + "\n")        


def brain():

    print("-------- HOME --------")

    valid_settings = ["KEEP ON", "START", "QUIT"]

    while True:

        try:
            think = input("What do you want to do : ").upper()
        except Exception:
            continue
        
        if think not in valid_settings:
            continue

        elif think == "START":
            control_chip()

        elif think == "QUIT":
            break

        elif think == "KEEP ON":
            idle()

if __name__ == "__main__":
    brain()