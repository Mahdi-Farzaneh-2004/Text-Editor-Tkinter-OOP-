from tkinter import font, ttk, filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
os.chdir("photo")

class Text_Editor:
    def __init__(self, master, title="Text Editor"):
        self.master = master
        self.master.title(title)
        self.master.geometry("1300x800")
        self.style=ttk.Style(self.master)
        #---menu--------------------------
        self.menu_main=tk.Menu(master)
        master.configure(menu=self.menu_main)
        
        self.File_menu=tk.Menu(self.menu_main, tearoff=0)

        self.menu_main.add_cascade(label="File", menu=self.File_menu)

        self.File_menu.add_command(label="Open", command=self.File_open)

        self.File_menu.add_command(label="Save", command=self.save)

        self.File_menu.add_command(label="Save as", command=self.save_as)
        #----Top section------------------
        self.frame_top=tk.Frame(master, bg="#E8E8E8", border=10)
        self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, ipady=60)

        self.new_button=ttk.Button(self.frame_top, padding=(19, 25, 19, 25), command=self.new ,style="My2.TButton")
        self.new_button.place(relx=0.003, rely=0.005)

        self.save_button=ttk.Button(self.frame_top, padding=(20, 0, 20, 0), command=self.save,style="My2.TButton")
        self.save_button.place(relx=0.003, rely=0.8)

        #---sepatator--
        sepatator=[145, 800, 420, 650, 975]

        for s in sepatator:
            line=ttk.Separator(self.frame_top, orient="vertical")
            line.place(x=s, relheight=1)

        self.Label_color=tk.LabelFrame(self.frame_top, bg="#E8E8E8", text="Color", font=("Segoe UI", 9))
        self.Label_color.place(x=158, y=-5, width=250, height=100)

        self.color1=["black.png", "white.png", "red.png", "yellow.png", "darkgreen.png", "darkred.png"]

        self.color2=["pink.png", "green.png", "orange.png", "purple.png", "gray.png", "blue.png"]

        self.row1 = tk.Frame(self.Label_color, bg="#E8E8E8")
        self.row1.pack(side=tk.TOP, pady=2)

        self.row2 = tk.Frame(self.Label_color, bg="#E8E8E8")
        self.row2.pack(side=tk.TOP, pady=2)

        for x in self.color1:
            self.image=Image.open(x)
            self.image=self.image.resize((20, 20), Image.Resampling.BOX)
            self.image_tk=ImageTk.PhotoImage(self.image)
            self.image_button=ttk.Button(self.row1, image=self.image_tk, text=x)
            self.image_button.image=self.image_tk
            self.image_button.pack(side=tk.LEFT, padx=3)
            self.image_button.bind("<Button-1>", lambda event:self.color(event))

        for y in self.color2:
            self.image=Image.open(y)
            self.image=self.image.resize((20, 20), Image.Resampling.BOX)
            self.image_tk=ImageTk.PhotoImage(self.image)
            self.image_button=ttk.Button(self.row2, image=self.image_tk, text=y)
            self.image_button.image=self.image_tk
            self.image_button.pack(side=tk.LEFT, padx=3)
            self.image_button.bind("<Button-1>", lambda event:self.color(event))

        self.selected_item_font_name = tk.StringVar()
        self.selected_item_font_size= tk.StringVar()

        self.font_list=list(font.families())

        self.number_font=[]
        for n in range(101):
            self.number_font.append(n)

        self.Label_frame_font = tk.LabelFrame(self.frame_top, background="#E8E8E8", text="Font", font=("Segoe UI", 9))
        self.Label_frame_font.place(x=435, y=-5, width=200, height=100)

        self.combobox_font_name=ttk.Combobox(self.Label_frame_font, textvariable=self.selected_item_font_name, width=20, value=self.font_list)
        self.combobox_font_name.pack(pady=5)

        self.combobox_font_size=ttk.Combobox(self.Label_frame_font, width=5, value=self.number_font, textvariable=self.selected_item_font_size)
        self.combobox_font_size.pack(side=tk.LEFT, padx=15)

        B=["B", "I"]
        for v in B:
            self.Button=ttk.Button(self.Label_frame_font, text=v, width=3, padding=(2,2))
            self.Button.pack(side=tk.LEFT, padx=3)
            self.Button.bind("<Button-1>", self.font)

        self.combobox_font_name.set("Arial")
        self.combobox_font_size.set(10)

        self.combobox_font_name.bind("<<ComboboxSelected>>", self.font)
 
        self.combobox_font_size.bind("<<ComboboxSelected>>", self.font)

        self.Label_background=tk.LabelFrame(self.frame_top, bg="#E8E8E8", text="Background Color", font=("Segoe UI", 9))
        self.Label_background.place(x=665,y=-5)

        self.background_color1=["black.png", "gray.png", "blue.png"]

        self.background_color2=["green.png", "orange.png", "pink.png"]

        self.Frame1=tk.Frame(self.Label_background, bg="#E8E8E8")
        self.Frame1.pack(side=tk.TOP, pady=4)

        self.Frame2=tk.Frame(self.Label_background, bg="#E8E8E8")
        self.Frame2.pack(side=tk.TOP, pady=4)

        for s in self.background_color1:
            self.image=Image.open(s)
            self.image=self.image.resize((20, 20), Image.Resampling.BOX)
            self.image_tk=ImageTk.PhotoImage(self.image)
            self.image_button=ttk.Button(self.Frame1, image=self.image_tk, text=s)
            self.image_button.image=self.image_tk
            self.image_button.pack(side=tk.LEFT, padx=5)
            self.image_button.bind("<Button-1>", lambda event:self.Background_color(event))

        for f in self.background_color2:
            self.image=Image.open(f)
            self.image=self.image.resize((20, 20), Image.Resampling.BOX)
            self.image_tk=ImageTk.PhotoImage(self.image)
            self.image_button=ttk.Button(self.Frame2, image=self.image_tk, text=f)
            self.image_button.image=self.image_tk
            self.image_button.pack(side=tk.LEFT, padx=5)
            self.image_button.bind("<Button-1>", lambda event:self.Background_color(event))

        self.paragraph=tk.LabelFrame(self.master, bg="#E8E8E8")
        self.paragraph.place(x=825, y=5)

        list_number={f"1.\n2.\n3.":self.number1, f"1:\n2:\n3:":self.number2, f"1=\n2=\n3=":self.number3}
        for x, m in list_number.items():
            self.button=ttk.Button(self.paragraph, text=x, command=m, width=4, style="My1.TButton")
            self.button.pack(side=tk.LEFT, pady=5, padx=5)
            self.style.configure("My1.TButton1",font=("Segoe UI", 7))

        self.Label_language=tk.LabelFrame(self.frame_top, bg="#E8E8E8", text="Language", font=("Segoe UI", 9))
        self.Label_language.place(x=990, y=-5)

        lan={"Fa":self.Language_fa , "En":self.Language_en}
        for ln, df in lan.items():
            self.Button_fa=ttk.Button(self.Label_language, text=ln, width=5, command=df)
            self.Button_fa.pack(side=tk.LEFT, padx=4, pady=7)

        #--- Text-------------------------
        self.txt=tk.Text(master, fg="red", font=("Arial", 10), bg="white")
        self.txt.place(x=0, y=125, relwidth=0.99, relheight=1)

        self.txt.bind("<Return>", lambda event:self.Line(event))
        self.txt.bind("<Button-1>", lambda event:self.Line(event))
        self.txt.bind("<KeyRelease>", lambda event:self.Line(event))

        self.txt.focus_set()

        self.set=set()

        self.num_set=set()

        self.scrollbar=ttk.Scrollbar(self.master, command=self.txt.yview, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.txt.configure(yscrollcommand=self.scrollbar.set)
        #---bottom-----
        frame_bottom=tk.Frame(self.master, bg="#E8E8E8")
        frame_bottom.pack(side=tk.BOTTOM, fill=tk.X, ipady=10, ipadx=100)

        self.label_bottom=tk.Label(frame_bottom ,bg="#E8E8E8")
        self.label_bottom.place(x=20, y=-1)

        self.Language_en()
        self.master.update()

    def Line(self, event):
        current_index = self.txt.index("insert")
        line_number, text = current_index.split('.')
        self.label_bottom.configure(text=f"Line: {line_number}    Index: {text}")

    def number1(self):
        if not self.num_set:
            self.num_set.add("Return")
        else:
            self.num_set.clear()
        self.txt.bind("<Return>", lambda event: f(event))
        self.num=1
        def f(event):
            if self.num_set:
                self.txt.insert(tk.END, f"{self.num}.")
                self.num+=1
            else:
                return

    def number2(self):
        if not self.num_set:
            self.num_set.add("Return")
        else:
            self.num_set.clear()
        self.txt.bind("<Return>", lambda event: f(event))
        self.num=1
        def f(event):
            if self.num_set:
                self.txt.insert(tk.END, f"{self.num}:")
                self.num+=1
            else:
                return
    def number3(self):
        if not self.num_set:
            self.num_set.add("Return")
        else:
            self.num_set.clear()
        self.txt.bind("<Return>", lambda event: f(event))
        self.num=1
        def f(event):
            if self.num_set:
                self.txt.insert(tk.END, f"{self.num}=")
                self.num+=1
            else:
                return

    def Language_fa(self):
        self.style.configure("My.TButton",font=("Segoe UI", 9))

        self.menu_main.entryconfig(1, label="فايل", font=("Segoe UI", 9))
        self.File_menu.entryconfig(0, label="بازکردن", font=("Segoe UI", 9))
        self.File_menu.entryconfig(1, label="ذخيره", font=("Segoe UI", 9))
        self.File_menu.entryconfig(2, label="ذخيره در", font=("Segoe UI", 9))

        self.new_button.configure(text="جديد",style="My.TButton")

        self.save_button.configure(text="ذخيره",style="My.TButton")

        self.Label_color.configure(text="رنگ", font=("Segoe UI", 9))

        self.Label_frame_font.configure(text="فونت", font=("Segoe UI", 9))

        self.Label_background.configure(text="رنگ پس زمينه", font=("Segoe UI", 9))

        self.Label_language.configure(text="زبان", font=("Segoe UI", 9))

        self.paragraph.configure(text="متن", font=("Segoe UI", 9))
        
    def Language_en(self):
        self.style.configure("My.TButton",font=("Segoe UI", 9))

        self.menu_main.entryconfig(1, label="File", font=("Segoe UI", 9))
        self.File_menu.entryconfig(0, label="Open", font=("Segoe UI", 9))
        self.File_menu.entryconfig(1, label="Save", font=("Segoe UI", 9))
        self.File_menu.entryconfig(2, label="Save as", font=("Segoe UI", 9))

        self.new_button.configure(text="New",style="My.TButton")

        self.save_button.configure(text="Save",style="My.TButton")

        self.Label_color.configure(text="Color", font=("Segoe UI", 9))

        self.Label_frame_font.configure(text="Font", font=("Segoe UI", 9))

        self.Label_background.configure(text="Background Color", font=("Segoe UI", 9))

        self.Label_language.configure(text="Language", font=("Segoe UI", 9))

        self.paragraph.configure(text="Paragraph", font=("Segoe UI", 9))
        
    def Background_color(self, event):
        text = event.widget["text"]
        l, k, j=text.partition(".")
        self.txt.configure(bg=l)

    def color(self, event):
        btn_text = event.widget["text"]
        a, b, c=btn_text.partition(".")
        self.txt.configure(fg=a)

    def new(self):
        global path
        path=filedialog.askdirectory(title="New", initialdir="C:/Users/Mahdi/Desktop")
        l=list(os.listdir(path))
        count=1
        for v in l:
            if v[0:8]=="New Text":
                count+=1
        if count==1:
            path = os.path.join(path,"New Text 1.txt")  
        else:
            path = os.path.join(path,f"New Text {count}.txt")

        self.master.title(path)
                
        with open(path ,"w" ,encoding="utf-8") as f:
            f.write("Hello")
        with open(path, "r", encoding="utf-8") as f:
            reader=f.read()
            self.txt.delete("1.0", tk.END)
            self.txt.insert(tk.END, reader)
    
    def font(self, event):
        clk=event.widget["text"]
        selected_item_font_size_get=int(self.selected_item_font_size.get())
        selected_item_font_name_get=self.selected_item_font_name.get()
        if clk == "B":
            if "bold" in self.set:
                self.set.remove("bold")
            else:
                self.set.add("bold")

        if clk == "I":
            if "italic" in self.set:
                self.set.remove("italic")
            else:
                self.set.add("italic")
                
        list_=[selected_item_font_name_get, selected_item_font_size_get]+list(self.set)
            
        list_t=tuple(list_)
        self.txt.configure(font=list_t)

    def bold_itali(self, name):
        p=self.selected_item_font_size.get()
        o=self.selected_item_font_name.get()
        font_c=(o, p)+tuple(name)
        self.txt.configure(font=font_c)

    def File_open(self):
        global file_path_open
        file_path_open=filedialog.askopenfilename(title="Open", initialdir="c:/Desktop", filetype=(("Text File","*.txt"),("All File","*.*")))
        if file_path_open:
            self.master.title(file_path_open)
            with open(file_path_open,"r",encoding="utf-8") as f:
                content = f.read()
                self.txt.delete(1.0 ,tk.END)
                self.txt.insert(tk.END, content)
                
    def save_as(self):
        file_path_save_as=filedialog.asksaveasfilename(title="Save as", defaultextension=".txt", initialdir="c:/Desktop", filetype=(("Text File","*.txt"),("All File","*.*")))
        if file_path_save_as:
            self.master.title(file_path_save_as)
            with open(file_path_save_as, "w", encoding="utf-8") as f:
                f.write(self.txt.get("1.0", "end"))
                
    def save(self):
        with open(path ,"w", encoding="utf-8") as f:
            f.write(self.txt.get("1.0", "end"))

if __name__=="__main__":
    root = tk.Tk()
    icon_image = Image.open("n.jpg")
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon_photo)
    text = Text_Editor(root)
    root.mainloop()
