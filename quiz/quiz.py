def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option

# Once the add question function was introduces, we now add the ask question part of the quiz
# Here we will first add the functions which will render a question ignoring its answer
def ask_questions():
    questions = []
    answers = []
    
    # For the file handler, we will use the with method to open our data, so we don't have to worry about closing the file
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()
        
    # The enumerate function is going to turn each one of the lines into a tuple with a line number stored in 'i' and the text in 'text'. 
    # So, if 'i' is even - if the line number is even - then we say that that's a question. If it's odd, then that's going to be an answer.
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
            
    # Now we must insert a variable which displays the number of questions asked by the user
    number_of_questions = len(questions)
    
    # The zip function is used to put them together, questions and answer   
    questions_and_answers = zip(questions, answers)
    
    score = 0
    
    for questions, answer in questions_and_answers:
        guess = input(questions + "> ")
        
        # Here we insert a function which checks if the answer is correct
        if guess == answer:
            score += 1
            print("right!")
            print(score)
        else:
            print("wrong!")
            
    print("You got {0} correct out of {1}".format(score, number_of_questions))
            

# Second, we added the the add question function which is option 1 in the quiz menu
def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("Ok then, tell me the answer")
    answer = input("{0}\n> ".format(question))
    
    # Once the user enters the questions, we have to append it to the file questions.txt
    # File Handler
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()
    
# The game loop function was the first one to be added in order to test the four available outcomes when starting the game quiz
def game_loop():
    while True:
        option = show_menu()
        # If the user selects option 1 the ask_questions fucntion is called
        if option == "1":
            ask_questions()
        
        # If the user selects option 2 the add_question fucntion is called
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option")
        print("")
        
game_loop()