from tkinter import *
from PIL import ImageTk, Image #this import to use images
import random
background_color = 'pink'
foreground_color = 'floralwhite'
btn_color = 'mediumseagreen'
names = []
asked=[]
score=0
 
anime_questions_answers = {
1: ["What was the date that Anime had offically been released?",'October 1982','April 2022', 'February 2018','March 2020','March 2020',4],  
 2: ["What nerf was made to make the Goku viable?", 'Decreased vertical recoil control','Decreased horizontal recoil control', 'TTK Headshot damage from 1.2 to 1.0', 'All of them', 'Decreased vertical recoil control',1],
 3: ["Which chacter will increase you revive speed by 25%?", "Pointman", 'Tuneup', "Quick Fix", "Overkill", 'Tuneup',2],
 4: ["How many villans are in the game?", '4', "11", "16", '3',"11", 2], 5: ["Who is the best anime chacter in the world?", 'Luffy', "Goku", "Rimuru", "naruto", "ichigo",3],
 6: ["How many times did did naruto use talk no jutsu?", '30',"98", "80", '53', "80",3],
 7: ["Where is the location of The hidden leaf village in?", 'Northern part', "Southern part", "Eastern Part", 'Western part', 'Western part',4],
 8: ["What makes a bad fandom ?", 'Kali sticks', "Combat knife", "E-Tool", 'Dual Kodachis','Kali sticks',1],
 9: ["What optic do you use to get the Clean living reticle in anime ?",'VLK optic', "Corp Holo Combat",'Axial arms 3x', 'Microflex LED', 'Axial arms 3x',3],
 10: ["What weapon is not a sniper?", 'CR5.56 AMAX', 'AX-50', 'SwissK31', 'Pelington 703','CR5.56 AMAX',1],
}
def randomiser():
 global qnum
 qnum = random.randint(1,10)
 if qnum not in asked:
   asked.append(qnum)
 elif qnum in asked:
   randomiser()     
 
class GUIWindow:
 
   def __init__(self, parent):
 
       background_color = 'black'
 
         # frame set up
 
       self.quiz_frame = Frame(parent, bg=background_color)
       self.quiz_frame.grid()
 
     # open image
 
       self.start_image = Image.open('Start.jpg')
       self.start_image = self.start_image.resize((650, 550),
               Image.ANTIALIAS)
       self.start_image = ImageTk.PhotoImage(self.start_image)
 
     # display image in a label
 
       self.image_label = Label(self.quiz_frame,
                                image=self.start_image)
       self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
 
       self.name_label = Label(self.quiz_frame,
                                text= "Enter your username here", fg="white", bg= "black")
       self.name_label.place(x=207, y=200)
 
 
     # Entry Box
 
       self.entry_box = Entry(self.quiz_frame)
       self.entry_box.grid(row=2, padx=210, pady=220)
 
     # Create a Button
 
       self.continue_button = Button(self.quiz_frame, text='Continue',
               bg='pink', command=self.name_collection)
       self.continue_button.grid(row=3, padx=20)
 
   def name_collection(self):
       name = self.entry_box.get()
       names.append(name)  # add name to nameslist declalime at the beggining
       self.quiz_frame.destroy()
       Quiz(root)
 
class Quiz:       
   def __init__(self, parent):
     background_color = "pink"
         #frame set up
     self.quiz_frame=Frame(parent, bg=background_color)
     self.quiz_frame.grid()
 
     #randomiser will randomly pick a question number which is qnum
     randomiser()
 
     self.question_label=Label(self.quiz_frame, text= anime_questions_answers[qnum][0], fg = "white",
     bg = background_color,
     font = "Verdana 16 bold")
     self.question_label.grid(row=0, pady=50, padx=50)
 
     self.var1=IntVar()
 
     #first radio button to hold first choice answer
     self.rb1 = Radiobutton (self.quiz_frame, text = anime_questions_answers[qnum][1], font=("Helvetica", "12", "bold"),fg="Black", bg="white", value=1, variable=self.var1, pady=10)
     self.rb1.grid(row=1, pady=20)
     self.rb2 = Radiobutton (self.quiz_frame, text = anime_questions_answers[qnum] [2], font=("Helvetica", "12", "bold"),fg="Black", bg="white", value=2,  variable=self.var1, pady=10)
     self.rb2.grid(row=2, pady=20)
 
     self.rb3 = Radiobutton (self.quiz_frame, text = anime_questions_answers[qnum][3], font=("Helvetica", "12", "bold"),fg="Black", bg="white", value=3, variable=self.var1, pady=10)
     self.rb3.grid(row=3, pady=20)
 
     self.rb4 = Radiobutton (self.quiz_frame, text = anime_questions_answers[qnum][4], font=("Helvetica", "12", "bold"),fg="Black", bg="white", value=4, variable=self.var1, pady=10)
     self.rb4.grid(row=4, pady=20)
 
    
     self.Submit_button = Button(self.quiz_frame, text="Submit", font=("Helvetica","13","bold"), bg="white", command=self.test_progress)
     self.Submit_button.grid(row=7, padx=5, pady=1)
 
     self.Submit_button = Label(self.quiz_frame,text="Score", font=("Tw Cen MT", "16"), bg=background_color,)
 
     self.scr_label = Label(self.quiz_frame)
     self.scr_label.grid(row=6, pady=1)
 
   def questions_setup(self):
     randomiser()
     self.var1.set(0)
     self.question_label.config(text=anime_questions_answers[qnum][0])
     self.rb1.config(text=anime_questions_answers[qnum][1])
     self.rb2.config(text=anime_questions_answers[qnum][2])
     self.rb3.config(text=anime_questions_answers[qnum][3])
     self.rb4.config(text=anime_questions_answers[qnum][4])
 
   def test_progress(self):
       global score
       scr_label = self.scr_label
       choice = self.var1.get()
       if len(asked)>9:#if it is the last question
           if choice==anime_questions_answers[qnum][6]:#if last question is right answer
             score +=1
             scr_label.configure(text=score)
             self.Submit_button.config(text="Submit")
           else: #is last question is wrong answer
               score+=0
               scr_label.config(text="The correct answer was " + anime_questions_answers[qnum][5])
               self.Submit_button.config(text="Submit")
       else:#If its not last question
           if choice==0:#check if user has made a choice
               self.Submit_button.configure(text="Try Again Please, You Didn't Select Anything ")
               choice==self.var1.get()
           else:#If they made a choice and its not last question
             if choice==anime_questions_answers[qnum][6]:#If their choice is right
               score +=1
               scr_label.configure(text=score)
               self.Submit_button.config(text="Submit")
               self.questions_setup()#run this method to move to next question
             else:
               score +=0
               scr_label.configure(text="The Correct Answer Was: " + anime_questions_answers[qnum][5])
               self.Submit_button.configure(text="Submit")
               self.questions_setup()
 
class End:
 def __init__(self):
     background="OldLace"
     self.end_box= Toplevel(root)
     self.end_box.title("End Box")
 
     self.end_frame = Frame (self.end_box, width=1000, height=1000, bg=background)
     self.end_frame.grid()
 
     end_heading = label (self.end_frame, text="Well Done", font=("Tw Cen MT", 22, "bold"), bg=background, pady=15)
     end_heading.grid(row=0)
 
     exit_button = Button (self.end_frame, text="Exit", width=10, bg="Indianlime1", font=("Tw Cen MT", 12, "bold"), command=self.close_end)
     exit_button.grid(row=4, pady=20)
 
     self.quit= Button(self.quiz_frame, text="Quit", font=("Helvetica", "13", "bold"))
  
 def close_end(self):
       self.end_box.destroy()
       root.withdraw()
 
       self.quit= Button(self.quiz_fame, text="Quit", font=("Helvetica", "13", "bold"), bg="lime2", command=self.endscreen)
       self.quit.grid(row=7,column=3,sticky=3, padx=5, pady=5)
 
 def endscreen(self):
     root.window()
     name=name[0]
     file=open("LeaderBoard.txt","a")
     file.write(str(score))
     file.write(" - ")
     file.write(name+"\n")
     file.close()
 
     inputFile = open("LeaderBoard.txt", "r")
     lineList = inputFile.readlines()
     lineList.sort()
     top=[]
     top5=(lineList[-5:])
     for line in top5:
         point=line.split(" _ ")
         top.append((int(point[0]), point[1]))
     file.close()
     top.sort()
     top.reverse()
     return_string=""
     for i in range(len(top)):
           return_string +="{} - {}\n".format(top[i][1])
     print(return_string)
 
     open_endscrn=End()
     open_endscrn.listLabel.config(text=return_string)
 
     self.listLabel = Label(self.enf_frame, text="1st Place Avaliable", font=("Tw Cen MT",18), width=40, bg=background, padx=10, pady=10)
     self.listLabel.grid(column=0, row=2)
 
    
  
  
  
 def end_screen(self):
       root.withdraw()
       open_endscrn=End()
 
 
 
            
 
 
if __name__ == "__main__":
   root = Tk()
   root.title("Warzone")
 
   quiz_instance = GUIWindow(root) #instantiation, making an instance of the class Quiz
   root.mainloop()#so the frame doesnt dissapear
