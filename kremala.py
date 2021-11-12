# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 12:51:18 2021

@author: Anna Manolaki 
"""

import random
import time


#Λίστα λέξεων από την οποία  επιλέγεται τυχαία μια λέξη κατά την έναρξη του παιχνιδιού
list_of_words = ["καλαμαρι", "χταποδι", "καραβι", "κουβαρι", "θρανιο", "σκυλος", "γατα"]


#Συνάρτηση που επιλέγει μια τυχαία λέξη από τη λίστα list_of_words
def random_word(list_of_words):
    word = random.choice(list_of_words)
    return word.upper()

   
#Συνάρτηση υλοποίησης των προσπαθειών του παίκτη
def play_game(word):

    gameIsDone = False
    guessed_letters = ""
    guessed_words = ""
    failure_tries = 6
    print(draw_gallows(failure_tries))
    time.sleep(1)
    length = len(word)
    print ("Πρέπει να βρεις μια  λέξη που αποτελείται από", length, "γράμματα")
    print("\n")
    
  #Επαναληπτική δομή η οποία τερματίζει με χρήση Boolean(gameIsDone) όταν ο παίκτης βρει σωστά 
  #όλα τα γράμματα ή τη λέξη ή όταν εκτελέσει 6 λανθασμένες προσπάθειες   
    while not gameIsDone and failure_tries > 0:
        #Είσοδος γράμματος ή λέξης από το πληκτρολόγιο
        guess = input("Μάντεψε την λέξη ή δώσε ένα γράμμα: ").upper()
       
#Περιπτωση 1: Ο παίκτης δίνει γράμμα.Έλεγχος για ορθότητα δεδομένων εισόδου
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Έχεις ήδη παίξει το γράμμα ", guess, "!")
            elif guess not in word:
                print(" Το " ,guess, "δεν υπάρχει στη λέξη :(")
                failure_tries -= 1
                guessed_letters = guessed_letters + guess
            else:
                print("Μπραβο, το ", guess, "υπάρχει στην λέξη")
                print("\n")
                guessed_letters = guessed_letters + guess
                wrong_letter = 0                
                for letter in word:
                    if letter in guessed_letters:
                    
                     print(f"{letter}", end="")
                    else:
                        print("_", end="")
                        wrong_letter += 1 
                if wrong_letter == 0:
                    gameIsDone = True
                    
#Περιπτωση 2: Ο παίκτης δίνει λέξη.Έλεγχος για ορθότητα δεδομένων εισόδου            
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
              print("Έχεις παίξει ξανά το γράμμα  ", guess, "!")
            elif guess != word:
                            print(guess, " Λυπάμαι δεν είναι αυτή η λέξη :(")
                            failure_tries -= 1
                            guessed_words = guessed_words + guess
            else:
                            gameIsDone = True
                           
        else:
            print("λάθος,πρέπει να δώσεις 1 γράμμα!")
                        
        print(draw_gallows(failure_tries))
    
        print("\n")
    if gameIsDone:
      print("MΠΡΑΒΟ βρήκες τη λέξη!!")
    else:
     print("Λυπάμαι,έκανες ήδη 6 προσπάθειες . Η λέξη ήταν : " + word + ". Ξαναπροσπάθησε!")


    #Συνάρτηση σχεδίασης των γραφικών που παίρνει ως όρισμα τον αριθμό των λανθασμένων προσπαθειών.
#Περιέχει την λίστα των στιγμιότυπων των γραφικών για κάθε μια από τις 6 λανθασμένες προσπάθειες,
#καθώς και την αρχική εικόνα της κρεμάλας που εμφανίζεται στην αρχή του παιχνιδιού.

def draw_gallows(failure_tries):
    gallows = [  """
                   --------
                   |      Δ                ________
                   |      X               |       |
                   |     /|\             |  Χ  Χ  |   You Killed the Guy!!
                   |      |              |   ο    |  GAME OVER!!!
                   |     / \             | wwww  |
                   _    wwwww            |______|
                   """,
                   """
                   --------
                   |      Δ
                   |      O
                   |      |/
                   |      |
                   |     /\
                   _
                   """,
                   """
                   --------
                   |      Δ
                   |      O
                   |      |
                   |      |
                   |     / \
                  
                   """,
                   """
                   --------
                   |      Δ
                   |      O
                   |      |
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      Δ
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      Δ
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      Δ
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return gallows[failure_tries]     

def main():
      word = random_word(list_of_words)
      #Μήνυμα προς τον χρήστη κατά την έναρξη του παιχνιδιού 
      print("\n")
      print("____________Ας παίξουμε Κ ρ Ε μ Α λ Α_____________ ")
      print("\n")
      name = input("Πως σε λένε; ")
      print ("Γεια σου ", name, "το παιχνίδι ξεκινάει!!!")
      time.sleep(1)
      print("\n")
      time.sleep(1)
      play_game(word)
     
      while input("Θα παίξεις ξανα? (Ν/Ο) ").upper() == "Ν":
          word = random_word(list_of_words)
          play_game(word)
if __name__ == "__main__":
      
      main()