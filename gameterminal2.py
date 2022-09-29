print("Välkommen till Python Quiz!")
Användarnamn = input("Användarnamn?: ")
print("\nHej,",Användarnamn + "!" "\n\nNu startar quizen!\nFör varje rätt svar så får du en poäng!\n\nLycka till!")
print("\n")
spelar = True

while spelar:
    poäng = 0 

    print("Vilken tecken använder man för att skriva kommentarer i Python kod?")
    svar_1 = input("Svara här: ")
    if svar_1 == "#" or svar_1 == "Nummertecken":
        print("Rätt!")
        poäng  +=1
    else:
        print("Fel!")

    print('Hur skriver man ut Hello world! med kod?')
    svar_2 = input("Svara här: ")
    if svar_2 == 'print("Hello World!")' or svar_2 == "print('Hello World!')":
        print("Rätt!")
        poäng +=1
    else:
        print("Fel!")            

    print('Hur gör man en Radbrytning när man skriver Python kod?')
    svar_3 = input("Svara här: ")
    if svar_3 == "\\n": 
        print("Rätt!")
        poäng +=1
    else:
        print("Fel!")  

    print("Skriv hur man skapar en ny python fil i Terminalen, den ska heta Quiz")
    svar_4 = input("Svara här: ")
    if svar_4 == "new-item Quiz.py" or svar_4 == "type nul> Quiz.py" or svar_4 == "touch Quiz.py":
        print("Rätt!")
        poäng +=1
        
    else:
        print("Fel!")        

    print("Skriv en Variabel som heter x och har värdet 1000")
    svar_5 = input("Svara här: ")
    if svar_5 == "x = 1000" or svar_5 == "X = 1000":
        print("Rätt!")
        poäng +=1
        
    else:
        print("Fel!")    

    print("Vilken sorts variabel används för heltal?")
    svar_6 = input("Svara här: ")
    if svar_6 == "int" or svar_6 == "integer":
        print("Rätt!")
        poäng +=1
        
    else:
        print("Fel!")    

    print("Vilken sorts variabel används för True or False")
    svar_7 = input("Svara här: ")
    if svar_7 == "Boolean" or svar_7 == "boolean" or svar_7 == "bool" or svar_7 == "Bool":
        print("Rätt!")
        poäng +=1
        
    else:
        print("Fel!")

    print("Vilken sorts variabel används för flyttal")
    svar_8 = input("Svara här: ")
    if svar_8 == "float":
        print("Rätt!")
        poäng +=1
        
    else:
        print("Fel!")        

    print("Hur skriver man tecken för Backslash?")
    svar_9 = input("Svara här: ")
    if svar_9 == "\\":
        print("Rätt!")
        poäng +=1
        
    else:
        print("Fel!")

    print("Gör en enkel uträkning med print: 12 delat på 3 plus fyra minus 1")
    svar_10 = input("Svara här: ")
    if svar_10 == "print(12 / 3 + 4 - 1)" or svar_10 == "print(12/3+4-1)":
        print("Rätt!")
        poäng +=1
        
    else:
        print("Fel!")
    vill_du_spela_igen = input("Vill du spela igen?")
    if vill_du_spela_igen == "Ja" or vill_du_spela_igen == 'ja':
       spelar = True
    else:   
       break
print("Tack för att du spelade! \nDitt slutresultat är", poäng,"av 10")       