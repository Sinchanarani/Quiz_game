from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    question_text=i['text']
    question_answer=i['answer']
    new=Question(question_text, question_answer)
    question_bank.append(new)



quiz=QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_question():
    quiz.next_question()

quiz.final_score()