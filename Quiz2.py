# Funktion för frågor och svar
# Alla frågor är samlade i en dictionary
# Alla möjliga svar är samlade i en lista
# En nästald for-loop kollar svaret mot alla rätta svar
# Svaren tas sedan bort beroende på fråga
# För att inte kunna svara andra svar än det faktiskt rätta finns fler "conditions"

def questions(poäng):
    all_questions = {
        1: "Vilket tecken använder man för att skriva kommentarer i Python kod?", 
        2: 'Hur skriver man ut Hello World! med kod?',
        3: 'Hur gör man en Radbrytning när man skriver Python kod?', 
        4: "Skriv hur man skapar en ny python fil i Terminalen, den ska heta Quiz", 
        5: "Skriv en Variabel som heter x och har värdet 1000", 
        6: "vilken sorts variabel används för heltal?", 
        7: "Vilken sorts variabel används för True or False", 
        8: "Vilken sorts variabel används för flyttal", 
        9: "Hur skriver man tecken för Backslash?", 
        10: "Gör en enkel uträkning med print på 12 delat på 3 plus fyra minus 1"}

    all_answers = [
        "#", "Nummertecken", "print('Hello World!')", 'print("Hello World!")',
        "\\n", "new-item Quiz.py", "type nul> Quiz.py", "touch Quiz.py",
        "x = 1000", "x=1000", "int", "integer", "bool", "boolean",
        "float", "\\", "print(12/3+4-1)"]
    
    for i in all_questions:
        print(all_questions[i])
        answer = input("Svar här: ")
        for j in all_answers:
            if not answer == "" and answer == j:
                if answer == j and all_answers.index(j) <= 1:
                    print("Rätt!")
                    poäng += 1
                    break
                elif i == 4 and answer == j and all_answers.index(j) <= 2:
                    print("Rätt!")
                    poäng += 1
                    break
                elif i == 3 or i == 8 or i == 9 or i == 10 and answer == j and all_answers.index(j) == 0:
                    print("Rätt!")
                    poäng += 1
                    break
        try:
            if i == 4:
                del all_answers[:3]
            elif i == 3 or i == 8 or i == 9 or i == 10:
                del all_answers[:1]
            else:
                del all_answers[:2]
        except ValueError:
            continue
        if not answer == j:
            print("Fel!")
            
    return poäng

# Game-loopen
def run():
    print("Välkommen till Python Quiz!")
    Användarnamn = input("Användarnamn?: ")
    print("\nHej,", Användarnamn + "!" "\n\nNu startar quizen!\nFör varje rätt svar så får du en poäng!\nLycka till!\n")

    spelar = True

    while spelar:
        poäng = 0
        poäng = questions(poäng)

        vill_du_spela_igen = input("Vill du spela igen?")
        if vill_du_spela_igen == "Ja" or vill_du_spela_igen == 'ja':
            spelar = True
        else:   
            break

    print("Tack för att du spelade! \nDitt slutresultat är", poäng,"av 10")
        

if __name__ == "__main__":
    run()
