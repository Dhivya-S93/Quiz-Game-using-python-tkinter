import tkinter as tk
from tkinter import messagebox
from random import shuffle

class Quizgame:
    def __init__(self,root):
        self.root=root
        self.root.title("Python Quize Game")
        self.question=[
            {
            "question" : "Which type of Programming does Python support?",
            "option" :["object-oriented programming " ,"structured programming" ,"functional programming " ,"all of the mentioned"],
            "answer":"all of the mentioned"
            },
            {    
            "question" : "Which of the following is the correct extension of the Python file?",
            "option" :[".python" ,".pl" ,".py " ,".p"],
            "answer":".py "
            },
            {    
            "question" : "Which keyword is used for function in Python language?",
            "option" :["def" ,"fun" ,".Define" ,"Function"],
            "answer":"def"
            },
            {    
            "question" : "Which of the following character is used to give single-line comments in Python?",
            "option" :["//" ,"#" ,"!" ,"/*"],
            "answer":"#"
            },
            {    
            "question" : "What does pip stand for python?",
            "option" :["Pip Installs Python" ,"Pip Installs Packages" ,"Preferred Installer Program" ,"All of the mentioned"],
            "answer":"Preferred Installer Program"
            }
            
         ]
        self.score=0
        self.current_question=0
        
        self.question_label=tk.Label(self.root , text="" , font=("Arial",14 ), wraplength=400)
        self.question_label.pack(pady=20)

        self.option_button=[]
        for i in range(4):
            button=tk.Button(self.root , text="" , font=("Arial",14), width=30 ,command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_button.append(button)
        self.score_label=tk.Label(self.root , text="Score:0" , font=("Arial",12 ), wraplength=400)
        self.score_label.pack(pady=20)

        self.next_question()
    def next_question(self):
            if self.current_question<len(self.question):
                question=self.question[self.current_question]
                self.question_label.config(text=question["question"])
                option=question["option"]
                shuffle(option)
                for i in range(4):
                    self.option_button[i].config(text=option[i])
                self.score_label.config(text="score: {}". format(self.score))
            else:
                self.end_game()
    def check_answer(self,selected_option):
            question=self.question[self.current_question]
            selected_answer=question["option"][selected_option]
            correct_answer=question["answer"]
            if selected_answer==correct_answer:
                self.score+=1
            self.current_question+=1
            self.next_question()
    def end_game(self):
            messagebox.showinfo("Game Over" , "Quiz has ended! \n your score: {}".format(self.score))
            self.root.destroy()
root=tk.Tk()
quiz_game=Quizgame(root)
root.mainloop()
                
            
                                     
        
