'''
Dự Án Cuối Khóa HP3
Google Translator 
'''
#Tạo thư viện cho các lệnh 
from tkinter import *
import googletrans                                        #pip install googletrans
from tkinter import ttk
from PIL import ImageTk, Image
from googletrans import Translator

#Tạo cửa sổ
class ggd:
    def __init__(self):
        self.gd=Tk()
        self.gd.title("Google Translator") #Đặt tên cho cửa sổ
        self.gd.geometry("900x400")        #Đặt kích thước cho cửa sổ
        self.gd.config(bg="#F0F0F0")       #Đặt màu nền cho cửa sổ
        self.gd.iconbitmap("logo.ico")     #Tạo logo

        #menu
        self.frame_menu=Frame(self.gd)
        self.frame_menu.pack()
        self.frame_menu.configure(bg="white")
        self.frame_menu.place(x=0,y=0,width=900,height=400)
        #tạo các nút
        self.btn_start=Button(self.frame_menu,text="Start",fg="blue",
                              font=("Arial",28,'bold'),command=self.start)
        self.btn_start.place(x=50,y=150)

        self.btn_instruct=Button(self.frame_menu,text="Instruction",fg="black",
                                 font=("Arial",28,'bold'),command=self.instruct)
        self.btn_instruct.place(x=335,y=150)

        self.btn_quit=Button(self.frame_menu,text="Quit",fg="red",
                             font=("Arial",28,'bold'),command=self.gd.destroy)
        self.btn_quit.place(x=750,y=150)
        #tạo khung
        self.frame_hd=Frame(self.gd)
        self.frame_hd.configure(bg="white")
        self.frame_hd.place(x=0,y=0,width=900,height=400)
        self.frame_hd.place_forget()

        self.frame_st=Frame(self.gd)
        self.frame_st.configure(bg="white")
        self.frame_st.place(x=0,y=0,width=900,height=400)
        self.frame_st.place_forget()
        
        self.gd.mainloop()

    #Khai báo hàm
    #start
    def start(self):   
        self.frame_menu.place_forget()
        self.frame_st.place(x=0,y=0,width=900,height=400)
        #Tạo vùng gõ văn bản
        #Text 1
        f=Frame(self.frame_st,bg="#262626",bd=5)
        f.place(x=50,y=150,width=360,height=160)

        self.text1=Text(f,font=("Arial",15),bg="white",relief=GROOVE,wrap=WORD)
        self.text1.place(x=-2.5,y=-2.5,width=355,height=155)

        scrollbar1=Scrollbar(f)
        scrollbar1.pack(side="right",fill="y")
        scrollbar1.configure(command=self.text1.yview)
        self.text1.configure(yscrollcommand=scrollbar1.set)
        #Text 2
        f2=Frame(self.frame_st,bg="#262626",bd=5)
        f2.place(x=490,y=150,width=360,height=160)

        self.text2=Text(f2,font=("Arial",15),bg="white",relief=GROOVE,wrap=WORD)
        self.text2.place(x=-2.5,y=-2.5,width=355,height=155)

        scrollbar2=Scrollbar(f2)
        scrollbar2.pack(side="right",fill="y")
        scrollbar2.configure(command=self.text2.yview)
        self.text2.configure(yscrollcommand=scrollbar2.set)

        #Thêm ảnh
        self.path='mt.png'
        self.img=Image.open(self.path)
        self.img=self.img.resize((40,25))
        self.img=ImageTk.PhotoImage(self.img)
        self.label_img=Label(self.frame_st,image=self.img)
        self.label_img.place(x=430,y=120)

       #Thêm ngôn ngữ
        language=googletrans.LANGUAGES
        languageV=list(language.values())
        language.keys()

        #cb 1
        self.c1=ttk.Combobox(self.frame_st,values=languageV,font="Robot 14", state="r")
        self.c1.place(x=100,y=122)
        self.c1.set("English")
        #cb 2
        self.c2=ttk.Combobox(self.frame_st,values=languageV,font="Robot 14", state="r")
        self.c2.place(x=540,y=122)
        self.c2.set("Vietnamese")
        
        #Tạo nút bấm
        #Translate button (Nút dịch)
        translate=Button(self.frame_st,text_="Translate",font=("Arial",10),activebackground="white",cursor="hand2",
                         bd=1,width=8,height=2,bg="#262626",fg="white",command=self.translate_now)
        translate.place(x=414,y=215)
        #clear button (nút xóa tất cả)
        self.c=Button(self.frame_st, text="X",bg="white",font=('Arial',10),fg="black", command=self.clear)
        self.c.place(x=350,y=127,width=20,height=20)
        #nút back (Nút quay lại menu)
        self.btn_back=Button(self.frame_st,text="Back",fg="black",font=("Arial",10,'bold'),command=self.back)
        self.btn_back.place(x=10,y=370)

    def translate_now(self):
        self.text_=self.text1.get(1.0,END)
        self.t1=Translator()
        self.trans_text=self.t1.translate(self.text_,src=self.c1.get(),dest=self.c2.get())
        self.trans_text=self.trans_text.text

        self.text2.delete(1.0,END)
        self.text2.insert(END,self.trans_text)
    def clear(self):
        self.text1.delete(1.0,END)
        self.text2.delete(1.0,END)

    #Khai báo hàm

    #Hướng dẫn
    def instruct(self):
        self.frame_menu.place_forget()
        self.frame_hd.place(x=0,y=0,width=900,height=400)
        #nội dung
        self.lb_instruct=Label(self.frame_hd,text="Hướng dẫn",fg="black",bg="white",font=("Arial",20,'bold'))
        self.lb_instruct.place(x=350,y=-60,width=200,height=200)

        self.lb_instruct=Label(self.frame_hd ,text="1.Bấm nút Translate để dịch",
                               fg="black",bg="white",font=("Arial",13))
        self.lb_instruct.place(x=0,y=100,width=250,height=30)

        self.lb_instruct=Label(self.frame_hd ,text="2.Bấm dấu X để xóa ",
                               fg="black",bg="white",font=("Arial",13))
        self.lb_instruct.place(x=0,y=125,width=200,height=30)

        self.lb_instruct=Label(self.frame_hd ,text="3.Bấm dấu mũi tên chỉa xuống để chọn ngôn ngữ ",
                               fg="black",bg="white",font=("Arial",13))
        self.lb_instruct.place(x=0,y=150,width=411,height=30)
        
        self.lb_instruct=Label(self.frame_hd ,text="4.Bấm nút back để quay lại menu ",
                               fg="black",bg="white",font=("Arial",13))
        self.lb_instruct.place(x=0,y=175,width=293,height=30)
        
        #nút back (Nút quay lại menu)
        self.btn_back=Button(self.frame_hd,text="Back",fg="black",font=("Arial",10,'bold'),command=self.back)
        self.btn_back.place(x=10,y=370)

    #back
    def back(self):
        self.frame_st.place_forget()
        self.frame_hd.place_forget()
        self.frame_menu.place(x=0,y=0,width=900,height=400)



    


    

ggd()

# # # Hello, my name's Thinh
