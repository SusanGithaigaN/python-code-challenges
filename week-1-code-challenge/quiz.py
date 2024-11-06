while True:    
    # initialize an empty variable to store the scores
    score = 0

    # qtns
    answer = input("What is the capital city of Namibia? ")

    if answer == "Windhoek" or answer== "windhoek":
        score+= 1
    else:
        print("Incorrect. The correct answer is Windhoek.")
        
    answer = input("What is the capital city of Kenya? ")

    if answer == "Nairobi" or answer== "nairobi":
        score+= 1
    else:
        print("Incorrect. The correct answer is Naoribi.")
        
    print(f"Your score is: {score}")

    # replay
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    if play_again != "yes":
            print("Thank you for playing!")
            break