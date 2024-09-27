import time

# Acknowledgment
print("This Olympics Quiz program is designed by Prateek Kushwaha and Hardik Maheshwari.")
time.sleep(2)
print("We have worked on creating engaging questions to test your knowledge about the Olympics!")
time.sleep(2)

# Introduction and Rules
print("🌟 Welcome to the Ultimate Olympics Quiz! 🌟\n")
time.sleep(1)

print("📜 **Quiz Rules:** 📜\n")
time.sleep(1)

print("1️⃣ **Format:**")
print("   - The quiz consists of three rounds: General Knowledge, History, and Competency.")
print("   - Each round contains a series of multiple-choice questions.\n")
time.sleep(2)

print("2️⃣ ******Answering Questions:******")
print("   - Each question will have 4 options.")
print("   - Type the number corresponding to your answer and press Enter.\n")
time.sleep(2)

print("3️⃣ ******Scoring:******")
print("   - For each correct answer, you'll receive 1 point.")
print("   - No points are deducted for incorrect answers, so take your best guess!\n")
time.sleep(2)

print("4️⃣ ******Timing:******")
print("   - There is no time limit for answering questions.")
print("   - However, try to answer as quickly as possible to keep the game flowing!\n")
time.sleep(2)

print("5️⃣ *****Good Luck!*****")
print("   - Have fun and learn something new about the Olympics!")
print("   - The quiz begins now. Get ready!\n")
time.sleep(2)

# Function to run a quiz
def run_quiz(questions):
    score = 0
    print("\nStarting the quiz...\n")
    time.sleep(1)
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for option in q['options']:
            print(option)
        user_answer = int(input("Enter the correct option number: "))
        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is option {q['answer']}.\n")
        time.sleep(1)
    return score

# Quiz Questions
gk_questions = [
    {"question": "Which city hosted the 2016 Summer Olympics?", 
     "options": ["1. Tokyo", "2. Rio de Janeiro", "3. London", "4. Beijing"], 
     "answer": 2},
    {"question": "What is the Olympic motto?", 
     "options": ["1. Higher, Faster, Stronger", "2. Unity, Peace, Friendship", "3. Stronger Together", "4. Power, Speed, Glory"], 
     "answer": 1},
    {"question": "Which sport is known as 'the king of sports'?", 
     "options": ["1. Soccer", "2. Basketball", "3. Track and Field", "4. Swimming"], 
     "answer": 1},
    {"question": "Who won the 100 meters sprint in the 2012 Olympics?", 
     "options": ["1. Yohan Blake", "2. Tyson Gay", "3. Usain Bolt", "4. Justin Gatlin"], 
     "answer": 3},
    {"question": "Which country has won the most gold medals in the Olympics?", 
     "options": ["1. USA", "2. Russia", "3. China", "4. Germany"], 
     "answer": 1},
    {"question": "The first Olympics were held in which country?", 
     "options": ["1. Greece", "2. Italy", "3. Egypt", "4. Turkey"], 
     "answer": 1},
    {"question": "Which Olympic Games featured the first female athletes?", 
     "options": ["1. 1900", "2. 1912", "3. 1924", "4. 1936"], 
     "answer": 1},
    {"question": "Which of these sports was introduced in the 2020 Tokyo Olympics?", 
     "options": ["1. Skateboarding", "2. Tennis", "3. Rugby", "4. Karate"], 
     "answer": 1},
    {"question": "Who has the most Olympic gold medals?", 
     "options": ["1. Michael Phelps", "2. Usain Bolt", "3. Carl Lewis", "4. Mark Spitz"], 
     "answer": 1},
    {"question": "What is the number of rings on the Olympic flag?", 
     "options": ["1. 4", "2. 5", "3. 6", "4. 7"], 
     "answer": 2},
    {"question": "In which Olympics did the Jamaican bobsled team compete?", 
     "options": ["1. 1988", "2. 1992", "3. 1994", "4. 1998"], 
     "answer": 1},
    {"question": "Which is the only continent not to host the Olympics?", 
     "options": ["1. Africa", "2. South America", "3. Asia", "4. Australia"], 
     "answer": 1},
    {"question": "Which country won the first-ever Olympic soccer tournament?", 
     "options": ["1. Great Britain", "2. Uruguay", "3. USA", "4. Argentina"], 
     "answer": 1},
    {"question": "The Olympic Games are held every how many years?", 
     "options": ["1. 2", "2. 3", "3. 4", "4. 5"], 
     "answer": 3},
    {"question": "Which Olympic sport uses the term 'epee'?", 
     "options": ["1. Fencing", "2. Swimming", "3. Archery", "4. Cycling"], 
     "answer": 1}
]

history_questions = [
    {"question": "In which year were the first modern Olympic Games held?", 
     "options": ["1. 1896", "2. 1900", "3. 1912", "4. 1924"], 
     "answer": 1},
    {"question": "Which country has won the most Olympic medals in history?", 
     "options": ["1. USA", "2. Russia", "3. China", "4. UK"], 
     "answer": 1},
    {"question": "Who was the first woman to win an Olympic gold medal?", 
     "options": ["1. Charlotte Cooper", "2. Marie Marvingt", "3. Mildred Didrikson", "4. Wilma Rudolph"], 
     "answer": 1},
    {"question": "When were the first Winter Olympic Games held?", 
     "options": ["1. 1924", "2. 1932", "3. 1948", "4. 1956"], 
     "answer": 1},
    {"question": "Which country hosted the first Winter Olympics?", 
     "options": ["1. France", "2. Switzerland", "3. Norway", "4. Italy"], 
     "answer": 1},
    {"question": "Which two Olympics were canceled due to World War II?", 
     "options": ["1. 1940, 1944", "2. 1936, 1944", "3. 1932, 1940", "4. 1928, 1932"], 
     "answer": 1},
    {"question": "Which sport was dropped from the Olympics after 1920?", 
     "options": ["1. Tug of war", "2. Golf", "3. Cricket", "4. Polo"], 
     "answer": 1},
    {"question": "Which city was the first to host the Olympics twice?", 
     "options": ["1. London", "2. Paris", "3. Los Angeles", "4. Athens"], 
     "answer": 2},
    {"question": "Who was the first athlete to light the Olympic Cauldron?", 
     "options": ["1. Fritz Schilgen", "2. Paavo Nurmi", "3. Jesse Owens", "4. Carl Lewis"], 
     "answer": 1},
    {"question": "Which Olympic event was held for the first time in 1984?", 
     "options": ["1. Women's marathon", "2. Synchronized swimming", "3. Rhythmic gymnastics", "4. All of the above"], 
     "answer": 4},
    {"question": "Which country hosted the first Olympic Games in Asia?", 
     "options": ["1. Japan", "2. South Korea", "3. China", "4. India"], 
     "answer": 1},
    {"question": "Which country won the most medals at the 2008 Beijing Olympics?", 
     "options": ["1. USA", "2. China", "3. Russia", "4. Germany"], 
     "answer": 2},
    {"question": "Who was the first African-American to win an Olympic gold medal?", 
     "options": ["1. DeHart Hubbard", "2. Jesse Owens", "3. Rafer Johnson", "4. Wilma Rudolph"], 
     "answer": 2},
    {"question": "Which Olympic Games saw the introduction of the Paralympic Games?", 
     "options": ["1. 1960", "2. 1956", "3. 1964", "4. 1972"], 
     "answer": 1},
    {"question": "Which country withdrew from the Olympics in 1980 to protest the Soviet Union's invasion of Afghanistan?", 
     "options": ["1. USA", "2. UK", "3. Australia", "4. Canada"], 
     "answer": 1}
]

competency_questions = [
    {"question": "What is the diameter of an Olympic basketball?", 
     "options": ["1. 24.26 cm", "2. 22.86 cm", "3. 20.60 cm", "4. 25.40 cm"], 
     "answer": 2},
    {"question": "How many players are on an Olympic volleyball team?", 
     "options": ["1. 4", "2. 5", "3. 6", "4. 7"], 
     "answer": 3},
    {"question": "What is the length of an Olympic swimming pool?", 
     "options": ["1. 25 meters", "2. 50 meters", "3. 100 meters", "4. 75 meters"], 
     "answer": 2},
    {"question": "In Olympic fencing, how many touches are required to win?", 
     "options": ["1. 10", "2. 15", "3. 20", "4. 5"], 
     "answer": 2},
    {"question": "What is the maximum distance in Olympic archery?", 
     "options": ["1. 50 meters", "2. 70 meters", "3. 100 meters", "4. 90 meters"], 
     "answer": 2},
    {"question": "How many rounds are there in an Olympic boxing match?", 
     "options": ["1. 2", "2. 3", "3. 4", "4. 5"], 
     "answer": 2}
]

# Main Quiz Selection
while True:
    print("\nSelect a quiz to play:")
    print("1. General Knowledge")
    print("2. History")
    print("3. Competency")
    print("4. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        score = run_quiz(gk_questions)
        print(f"Your total score in General Knowledge is: {score}/{len(gk_questions)}")
    elif choice == '2':
        score = run_quiz(history_questions)
        print(f"Your total score in History is: {score}/{len(history_questions)}")
    elif choice == '3':
        score = run_quiz(competency_questions)
        print(f"Your total score in Competency is: {score}/{len(competency_questions)}")
    elif choice == '4':
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please select again.")
