import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, options, correct_option):
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the number): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            user_answer_index = int(user_answer) - 1
            if options[user_answer_index] == correct_option:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is: {correct_option}\n")
        else:
            print("Invalid input. Please enter a valid number.\n")

    def run_quiz(self):
        for question, options, correct_option in self.questions:
            self.ask_question(question, options, correct_option)

        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")

# Sample quiz questions
quiz_questions = [
    ("What is the capital of France?", ["Berlin", "Paris", "Madrid"], "Paris"),
    ("Which programming language is this quiz written in?", ["Java", "Python", "C++"], "Python"),
    ("What is the square root of 64?", ["6", "8", "10"], "8")
]

# Create and run the quiz
if __name__ == "__main__":
    random.shuffle(quiz_questions)  # Shuffle the questions for variety
    quiz = QuizGame(quiz_questions)
    quiz.run_quiz()
