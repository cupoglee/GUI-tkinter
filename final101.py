import tkinter as tk
from tkinter import *
class GUI1(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("The Final GUI - SMRUTHI S KADAGADKAI")
        self.configure(bg='grey')
        self.geometry('1200x500')
        global img1
        self.resizable(2,2)
        image_path1 = "E:\\Smruthi\\RVCE BIS\\ELs\\PY-LAB\\rvcelogo.png"
        img1 = tk.PhotoImage(file=image_path1)
        img_label101 = tk.Label(self,image = img1)
        img_label101.configure(width=100, height=100)
        img_label101.pack(fill='both')
        label_go1 = tk.Label(self, text="Go, Change the world", font=('Calibri', 12, 'italic'))
        label_go1.pack(padx=(1030,3), pady=10 )

        label_rvce = tk.Label(self, text="Rashtreeya Vidyalaya College of Engineering", font=('Times New Roman', 24, 'bold'))
        label_rvce.pack()

        label_el = tk.Label(self, text="Experiential Learning Presentation", font=('Times New Roman', 19, 'italic'))
        label_el.pack()

        label_sub = tk.Label(self, text="Subject : Python (lab)", font=('Times New Roman', 16, 'bold'))
        label_sub.pack(padx=10, pady=10)

        label_teacher = tk.Label(self, text="Submitted to : Prashanth Sir, Chandrashekhar Sir", font=('Times New Roman', 16, 'bold'))
        label_teacher.pack(padx=(1, 700), pady=10)

        label_name = tk.Label(self, text="Submitted by : Smruthi S Kadagadkai", font=('Times New Roman', 16, 'bold'))
        label_name.pack(padx=(1, 800), pady=10)
        

        button_gui1 = tk.Button(self, text='Height of a basketball', height=2, font=('Comic Sans MS', 14), command=self.open_gui2)
        button_gui1.configure(bg='light blue', activebackground='yellow')
        button_gui1.pack( pady=10)

        button_gui2 = tk.Button(self, text='List Operations', height=2, font=('Comic Sans MS', 14), command=self.open_gui3)
        button_gui2.configure(bg='light blue', activebackground='yellow')
        button_gui2.pack( pady=10)

    def open_gui2(self):
        self.gui2 = GUI2()
        self.gui2.wm_geometry("1500x1500")
        self.gui2.wm_title("Height of a basketball")
        self.gui2.grab_set()
        self.gui2.focus_set()
        self.gui2.mainloop()

    def open_gui3(self):
        self.gui3 = GUI3()
        self.gui3.wm_geometry("1500x1500")
        self.gui3.wm_title("Set Operations")
        self.gui3.grab_set()
        self.gui3.focus_set()
        self.gui3.mainloop()

    

class GUI2(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Height of a basketball")
        global img
        self.geometry("1500x1500")
        self.configure(bg='light pink')
        self.title("Finding the height of the ball thrown by the basketball player")
        self.resizable(1,1)
        image_path = "E:\\Smruthi\\RVCE BIS\\ELs\\PY-LAB\\basketball.png"
        img = tk.PhotoImage(file=image_path)
        img_label = tk.Label(self,image = img)
        img_label.configure(width=100, height=300)
        img_label.pack(fill='both')  

        label = tk.Label(self, text="Height of Basketball", font=('Helvetica', 24, 'bold'))
        label.pack(padx=20, pady=20 )

   
        entry_labelv = tk.Label(self, text="Enter the velocity of the ball", font =('Times New Roman', 14, 'italic'))
        entry_labelv.pack(padx=20, pady=10)

        entry_velocity = tk.Entry(self)
        entry_velocity.pack()

 
        entry_labelh = tk.Label(self, text="Enter the height of the player", font =('Times New Roman', 14, 'italic'))
        entry_labelh.pack(padx=20, pady=10)

        entry_height = tk.Entry(self)
        entry_height.pack()

  
        
        result_label = tk.Label(self, text="The total height reached by the ball is", font=('Times New Roman', 14, 'bold'))
        result_label.pack(padx=10, pady=10)
  
    
        button1 = tk.Button(self, text='Tap to Run', height=2, font=('Comic Sans MS', 14), command=lambda: calculations())
        button1.configure(bg='light blue', activebackground='yellow')
        button1.pack( pady=10)
   
    
    
        def calculations():
            velocity = float(entry_velocity.get())
            heightplayer = float(entry_height.get())
            a = -16
            timecalc = -velocity/(2*a)
            heightcal= (a*(timecalc**2))+(velocity*timecalc)
            totalheight = heightplayer + heightcal
            result_label.config(text=totalheight)

class GUI3(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("List Operations")

        nums_list = [2, 3, 4, 5]

        
        self.geometry("1500x1500")
        self.configure(bg='orange')
        self.title("List Operations")
        self.resizable(1,1)
        global img2
        image_path2 = "E:\\Smruthi\\RVCE BIS\\ELs\\PY-LAB\\lisstt.png"
        img2 = tk.PhotoImage(file=image_path2)
        img_label2 = tk.Label(self,image = img2)
        img_label2.configure(width=800, height=50)
        img_label2.pack()  

        label_1 = tk.Label(self, text="List Operations", font=('Helvetica', 24, 'bold'))
        label_1.pack(padx=10, pady=10 )

   
        entry_labelbleh = tk.Label(self, text="nums_list = [2, 3, 4, 5]", font =('Times New Roman', 14, 'italic'))
        entry_labelbleh.pack(padx=10)

        entry_label_toadd = tk.Label(self, text="Enter the number you want to add", font=('Times New Roman', 14, 'bold'))
        entry_label_toadd.pack(padx=10, pady=10) 

        entry_toadd = tk.Entry(self)
        entry_toadd.pack()

        button_toadd = tk.Button(self, text='ADD!', height=1, font=('Comic Sans MS', 14), command=lambda: adding())
        button_toadd.configure(bg='light blue', activebackground='yellow')
        button_toadd.pack( pady=10)

        entry_label_toremove = tk.Label(self, text="Enter the position you want to remove", font=('Times New Roman', 14, 'bold'))
        entry_label_toremove.pack(padx=10, pady=10) 

        entry_toremove = tk.Entry(self)
        entry_toremove.pack()

        button_toremove = tk.Button(self, text='POP!', height=1, font=('Comic Sans MS', 14), command=lambda: removing())
        button_toremove.configure(bg='light blue', activebackground='yellow')
        button_toremove.pack( pady=10)

        entry_label_toinsertposition = tk.Label(self, text="Enter the position you want to insert", font=('Times New Roman', 14, 'bold'))
        entry_label_toinsertposition.pack(padx=10, pady=10) 
   
        entry_toinsertposition = tk.Entry(self)
        entry_toinsertposition.pack()

        entry_label_toinsertitem = tk.Label(self, text="Enter the element you want to insert", font=('Times New Roman', 14, 'bold'))
        entry_label_toinsertitem.pack(padx=10, pady=10) 

        entry_toinsertitem = tk.Entry(self)
        entry_toinsertitem.pack()

        button_toinsert = tk.Button(self, text='INSERT!', height=1, font=('Comic Sans MS', 14), command=lambda: inserting())
        button_toinsert.configure(bg='light blue', activebackground='yellow')
        button_toinsert.pack( pady=10)

        result_label_toremove = tk.Label(self, text="The updated list is:", font=('Times New Roman', 14, 'bold'))
        result_label_toremove.pack(padx=10, pady=10)

    
        def adding():
            adding_element = int(entry_toadd.get())
            nums_list.append(adding_element)
        
            result_label_toremove.config(text=nums_list)

        def removing():
            removing_element = int(entry_toremove.get())
            nums_list.pop(removing_element)
        
            result_label_toremove.config(text=nums_list)

        def inserting():
            removing_element = int(entry_toinsertitem.get())
            positional = int(entry_toinsertposition.get())
            nums_list.insert(positional, removing_element )
        
            result_label_toremove.config(text=nums_list)

if __name__ == "__main__":
    gui1 = GUI1()
    gui1.mainloop()

if __name__ == "__main__":
    gui2 = GUI1()
    gui1.mainloop()