from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {0}", font=('Arial', 12), bg=THEME_COLOR, fg='white')
        self.score_label.grid(pady=(0, 10), row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Question Text',
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_image, borderwidth=0, highlightthickness=0, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=0, pady=(20, 0))
        self.false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_image, borderwidth=0, highlightthickness=0, bg=THEME_COLOR)
        self.false_button.grid(row=2, column=1, pady=(20, 0))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)