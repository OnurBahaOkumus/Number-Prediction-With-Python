import random

def number ():
    value = random.randint(1,100)
    return value
        

def attempt():
    attempt_time = 0
    random_number = 0
    random_number = number() 
    difficulties = input("Please type the difficultie: easy or hard ").lower()
    if difficulties == "easy":
        while attempt_time < 10:
            choose_number = int(input("Guess The Number between 1 and 100: "))
            if choose_number < random_number:
                print("Too low")
            elif choose_number > random_number:
                print("Too High")
            elif choose_number == random_number:
                print("You found the number")
                exit()
            attempt_time += 1
            print(f"You guessed {attempt_time} times")
        return choose_number
    if difficulties == "hard":
        while attempt_time < 5:
            choose_number = int(input("Guess The Number between 1 and 100: "))
            if choose_number < random_number:
                print("Too low")
            elif choose_number > random_number:
                print("Too High")
            elif choose_number == random_number:
                print("You found the number!")
                exit()
            attempt_time += 1
            print(f"You guessed {attempt_time} times ")    
        return choose_number
    
    
def game():
    choice = 0
    print("WELCOME TO NUMBER GUESSİNG GAME!!!")
    choice = input("Would you like to play number guess game? y or n: ")
    if choice == "y":
        attempt()
    elif choice ==  "n":
        print("Bye!")
        exit()
        
        
    

    
    
if __name__ == "__main__":
    game()
