"""

TÄIENDUSED
    1. Kui mäng on läbi küsi kas mängida uuesti
    2. Kui mäng on läbi pane file steps and nimi
    3. Kui mäng on läbi näidatakse results.txt sisu. Kui kasutaja lisati file, siis koos värske infoga.

    Soovitus: Luua erinevaid funktsioone

"""

from random import randint

def save_result(name, steps):
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(f"{name};{steps}\n")

def show_results():
    try:
        with open("results.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Fail puudub.")

def new_game(tagauks, steps):
    if not tagauks:
        name = input("Mäng läbi! Sisesta oma nimi: ")
        save_result(name, steps)
        show_results()
    else:
        print("Mäng lõppes tagaukse kasutamise tõttu. Tulemusi ei salvestata.")

    uuesti = input("Kas soovid uuesti mängida? (Jah/Ei): ").lower()
    if uuesti == "jah":
        play()
    else:
        print("Head aega!")

def ask(pc_nr):
    steps = 0
    tagauks = False

    while True:
        print(f"Arvuti number: {pc_nr}")
        user_nr = int(input("Sisesta number: "))
        steps += 1

        if user_nr == 1234:
            print("Tagauks kasutatud! Mäng läbi.")
            tagauks = True
            return tagauks, steps

        if user_nr > pc_nr:
            print("Väiksem")
        elif user_nr < pc_nr:
            print("Suurem")
        else:
            print(f"Sa võitsid {steps} sammuga!")
            return tagauks, steps

def play():
    pc_nr = randint(1, 100)
    tagauks, steps = ask(pc_nr)
    new_game(tagauks, steps)

play()
