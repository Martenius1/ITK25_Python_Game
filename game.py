"""

TÄIENDUSED
    1. Kui mäng on läbi küsi kas mängida uuesti
    2. Kui mäng on läbi pane file steps and nimi
    3. Kui mäng on läbi näidatakse results.txt sisu. Kui kasutaja lisati file, siis koos värske infoga.

    Soovitus: Luua erinevaid funktsioone

"""

from random import randint

game_over = False
name = input("Kuidas on teie nimi?: ")

def save_result(name, steps):
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(f"{name};{steps}\n")

def show_results():
    try:
        with open("results.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Fail puudub.")

def new_game():
    global game_over, steps
    uuesti = input("Mäng läbi, kas soovid uuesti mängida? (Jah/Ei): ").lower()

    if uuesti == "jah":
        play()
    else:
        save_result(name, steps)
        show_results()
        game_over = True

def ask():
    global steps, game_over, pc_nr
    print(pc_nr)
    user_nr = int(input("Sisesta number: "))
    steps += 1

    if user_nr == 1234:
        print("Tagauks")
        game_over = True
        return

    if user_nr > pc_nr:
        print("Väiksem")
    elif user_nr < pc_nr:
        print("Suurem")
    else:
        print(f"Sa võitsid {steps} sammuga.")
        game_over = True

def play():
    global steps, game_over, pc_nr
    pc_nr = randint(1, 100)
    steps = 0
    game_over = False

    while not game_over:
        ask()

    new_game()


play()



