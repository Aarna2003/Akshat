#rock paper scissors game
import random

def get_computer_choice():
  
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Starting Rock-Paper&Scissors!")
    user_score = 0
    computer_score = 0
    
    while True:
    
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        

        if user_choice not in ["rock", "paper", "scissors"]:
            print("That's not a valid choice. Try again.")
            continue
        
     
        computer_choice = get_computer_choice()
        
      
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
      
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
   
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
    
        print(f"Score: You {user_score} - Computer {computer_score}")
        
        
        play_again = input("Do you want to play again? (yes or no): ").lower()
        if play_again != "yes":
            print("The end")
            break

if __name__ == "__main__":
    play_game()
