from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain
from ui import QuizzInterface

question_bank = []
for question_answer in question_data:
    question_bank.append(Question(question_answer["question"],question_answer["correct_answer"]))

#print(question_bank)
#print(question_bank[0].text)
quiz = QuizzBrain(question_bank)
quiz_ui = QuizzInterface(quiz)

#quiz.next_question()

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"You're final score was {quiz.score}/{len(quiz.question_list)}")
