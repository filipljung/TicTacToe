# Define a function to ask a multiple-choice question
def ask_question(question, options):
  # Print the question and the options
  print(question)
  for i in range(len(options)):
    print(str(i + 1) + ") " + options[i])
  
  # Get the user's answer
  while True:
    try:
      # Read the answer as an integer
      answer = int(input("Enter the number of your answer: "))
      
      # Check if the answer is within the range of options
      if 1 <= answer <= len(options):
        # Return the answer as a zero-based index
        return answer - 1
      else:
        print("Please enter a valid answer.")
    except ValueError:
      print("Please enter a valid number.")

# Define a list of questions and answers
questions = [
  {
    "question": "What is the capital of uk?",
    "options": ["Paris", "London", "Rome"],
    "answer": 1
  },
  {
    "question": "What is the largest ocean on earth?",
    "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean"],
    "answer": 0
  },
  {
    "question": "What is the name of the longest river in the world?",
    "options": ["Nile", "Amazon", "Mississippi"],
    "answer": 0
  }
]

# Set the initial score to zero
score = 0

# Loop through the questions
for question in questions:
  # Ask the question
  answer = ask_question(question["question"], question["options"])
  
  # Check if the answer is correct
  if answer == question["answer"]:
    score += 1
    print("Correct!")
  else:
    print("Incorrect. The correct answer is: " + question["options"][question["answer"]])

# Print the final score
print("You scored " + str(score) + " out of " + str(len(questions)) + ".")