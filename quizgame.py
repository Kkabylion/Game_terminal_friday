# -------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    frågor_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[frågor_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        frågor_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("RÄTT!")
        return 1
    else:
        print("FEL!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTAT")
    print("-------------------------")

    print("Svar: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Alternativ: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    poäng = int((correct_guesses/len(questions))*100)
    print("Dina poäng är: "+str(poäng)+"%")

# -------------------------
def play_again():

    response = input("Vill du spela igen? (Ja or nej): ")
    response = response.upper()

    if response == "Ja":
        return True
    else:
        return False
# -------------------------


questions = {
 "Vem skapade Python?: ": "A",
 "Vilken år skapades Python?: ": "B",
 "Vad är Python för programspråk?: ": "C",
 "Vilken företag använder mest av python?: ": "A",
 "Vilken är den lättaste koden att förstå för nybörjare?": "B",
 "Vad använder man för program till att köra spel inom python?": "C",
 "Hur skriver man Hello_World! på python? ": "C",
 "Hur kommmenterar man på Python?": "B",
 "Vad räknas inte som variabel?": "D",
 "Vilken fil används för att köra python?": "B",
 "Vilken metod används för att ta bort mellanrum": "D"
}

options = [["A. Guido van Rossum", "B. Steve jobs", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lågnivåspråk", "B.Medelnivåspråk ", "C. Högnivåspråk", "D. båda"],
          ["A. Amazon AWS","B. Microsoft azure", "C. Google cloud", "D. IBM "],
          ["A. Java", "B. Python", "C. C++", "D. SQL" ],
          ["A. Scratch", "B. Unity", "C. Pygame", "D. adobe flash"],
          ["A. System.out.println(Hello_World!)", "B. P(Hello_World!)","C. Print(Hello_World!)", "D. printf(Hello_World!)"],
          ["A. //", "B. #", "C. */*", "D. *//*"],
          ["A. myvar", "B. my_var", "C. _myvar", "D. my-var"],
          ["A. pyth", "B. py", "C. pyt", "D. path"],
          ["A. trim", "B. ptrim", "C. len()", "D. strip()"]]
        

new_game()

while play_again():
    new_game()

print("Hejdå!")

# -------------------------
