from ast import Break
from bdb import Breakpoint
from email.mime import image
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor
from typing_extensions import Self
from click import command
import customtkinter
# import functions
from tkinter import filedialog
import random
from tkinter import ttk
from PIL import Image, ImageTk
import os
import webbrowser

PATH = os.path.dirname(os.path.realpath(__file__))

def save_pat_info():
    first_name_txt = str(first_name_entry.get())
    last_name_txt = str(last_name_entry.get())
    year_txt = int(yob_entry.get())
    age_txt = 2022-int(year_txt)
    email_patient_txt = str(email_entry.get())
    

    for i in range(5):
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = "1234567890"
        use_for = lower_case + upper_case + number 
        length_for_iD = 8
        iD = "".join(random.sample(use_for,length_for_iD))
        pat_un_id = iD


   
    

    if len(str(first_name_txt)) < 3:
        msg = messagebox.showerror(message="Please enter valid value in the entry boxes.")
        Breakpoint
    else:
        file = filedialog.asksaveasfile(initialdir="c://home//dev_ian//Desktop//Patients",
                                                defaultextension=".Doc",
                                                filetypes=[
                                                ("Document file",".Doc"),                                           # ("Excel file",".xlsx"),
                                                ("All files","*"),
                                                ("Excel",".xlsx"),
                                                ("Word Macro-Enabled Document",""),
                                                ("PDF",".pdf")
                                            ]
            )
        first_name_txt = str(first_name_entry.get())
        last_name_txt = str(last_name_entry.get())
        year_txt = int(yob_entry.get())
        age_txt = 2022-int(year_txt)
        patient_gender = str(pat_gender_entry.get())
        email_patient_txt = str(email_entry.get())
        pat_county_txt = str(pat_county_entry.get())
        # add_info_entry_txt = str(pat_add_info.get(1.0,END))
        
        file.write("PATIENT DETAILS\n")
        file.write(f"ID: {pat_un_id}\n")
        file.write( f'Name: {first_name_txt} {last_name_txt}\n'),
        file.write(f"Gender: {patient_gender}\n")
        file.write(f'Year of Birth: {year_txt}\n')
        file.write(f'Age : {age_txt}\n'),
        file.write(f'Email: {email_patient_txt}\n'),
        file.write(f"County: {pat_county_txt}\n")
        # file.write(f'Patient also showed signs  of : {add_info_entry_txt}')
        file.close()
        succ_reg_msg = messagebox.showinfo(title="Registration",
                                            message="Patient registered succesfully",
                                            )
    
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    yob_entry.delete(0,END)
    pat_email_entry.delete(0,END)
    pat_gender_entry.delete(0,END)
    pat_county_entry.delete(0,END)
def entry_clear():
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    yob_entry.delete(0,END)
    pat_email_entry.delete(0,END)
    pat_gender_entry.delete(0,END)
    pat_county_entry.delete(0,END)

def add_patient_record():
    first_name_entry.get(),last_name_entry.get(),
    email_entry.get(),
    pat_county_entry.get()

    

class view_patient(customtkinter.CTkToplevel):
    WIDTH = 800
    HEIGHT = 900


    def __init__(self,):
        super().__init__()
        customtkinter.set_appearance_mode("Dark") 
        self.title("Obtain Patient Sample")
        self.geometry(f"{view_patient.HEIGHT}x{view_patient.WIDTH}")
        self.pat_tree_view = ttk.Treeview(master=self)
        self.style = ttk.Style()
        self.style.configure("Treeview",
            background = "Silver",
            foreground = "Black",
            rowheight = 25,
            fieldbackground = "Silver",
            width=800,
            height=1200
        )

        self.pat_tree_view['columns'] = ('firstname','Lastname','Patient ID','Gender','Year of Birth','Patient Email','County')
        PATH = os.path.dirname(os.path.realpath(__file__))
        self.settings_image = self.load_image("/Icons/settings.png", 20)
        self.bell_image = self.load_image("/Icons/bell.png", 20)
        self.add_folder_image = self.load_image("/Icons/add-folder.png", 20)
        self.add_list_image = self.load_image("/Icons/add-folder.png", 20)
        self.add_user_image = self.load_image("/Icons/add-user.png", 20)
        self.chat_image = self.load_image("/Icons/chat.png", 20)
        self.home_image = self.load_image("/Icons/home.png", 20)


        self.button_1 = customtkinter.CTkButton(master=self, image=self.add_folder_image, text="Add ", height=32,
                                                compound="right",command=functions.open_database )

        self.button_1.grid(row=1, column=0, columnspan=1, padx=0, pady=(20, 10), sticky="ew")

        self.pat_tree_view.column("#0",width=0,stretch=NO)
        self.pat_tree_view.column("firstname",width=120,anchor=W)
        self.pat_tree_view.column("Lastname",width=120,anchor=W)
        self.pat_tree_view.column("Patient ID",width=120,anchor=W)
        self.pat_tree_view.column("Gender",width=120,anchor=W)
        self.pat_tree_view.column("Year of Birth",width=120,anchor=W)
        self.pat_tree_view.column("Patient Email",width=120,anchor=W)
        self.pat_tree_view.column("County",width=120,anchor=W)


        self.pat_tree_view.heading("firstname",text="Firstname",anchor=W)
        self.pat_tree_view.heading("Lastname",text="Lastname",anchor=W)
        self.pat_tree_view.heading("Patient ID",text="Patient ID",anchor=W)
        self.pat_tree_view.heading("Gender",text="Gender",anchor=W)
        self.pat_tree_view.heading("Year of Birth",text="Year of Birth",anchor=W)
        self.pat_tree_view.heading("Patient Email",text="Patient's Email",anchor=W)
        self.pat_tree_view.heading("County",text="County",anchor=W)

        global count
        count=0
        self.pat_tree_view.insert(parent='',index='end',iid=0,values=(first_name_entry.get(),
                                                                     last_name_entry.get(),
                                                                     'gyrugr7687',
                                                                    pat_gender_entry.get(),
                                                                     yob_entry.get(),
                                                                     email_entry.get(),
                                                                     pat_county_entry.get()
                                                                     ))
        count+=1
        self.pat_tree_view.grid(row=0,column=0)



        # self.button_1 = customtkinter.CTkButton(master=self, image=self.add_folder_image, text="Add Folder", height=32,
        #                                         compound="right", )
        # self.button_1.grid(row=1, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")

    def load_image(self, path, image_size):
        """ load rectangular image with path relative to PATH """
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))


app = customtkinter.CTk()
#     # settings_image = functions.load_image("/Icons/settings.png", 20)
#     bell_image = functions.load_image(,path="/Icons/bell.png",image_size = 20)
#     add_folder_image = functions.load_image(path="/Icons/add-folder.png",image_size = 20,)
#     add_list_image = functions.load_image(path="/Icons/add-folder.png",image_size = 20)
#     add_user_image = functions.load_image(path="/Icons/add-user.png",image_size=20)
#     chat_image = functions.load_image(path="/Icons/chat.png",image_size = 20)
#     home_image = functions.load_image(path="/Icons/home.png",image_size = 20)


app.title("Viral Scope")
WIDTH = 1200
HEIGHT = 1500
app.geometry(f'{1500}x{1200}')

app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

frame_left = customtkinter.CTkFrame(master=app,
                                                width=180,
                                                corner_radius=0)
frame_left.grid(row=0, column=0, sticky="nswe")

frame_centre = customtkinter.CTkFrame(master=app)
frame_centre.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

frame_centre.rowconfigure((0, 1, 2, 3), weight=1)
frame_centre.rowconfigure(7, weight=10)
frame_centre.columnconfigure((0, 1), weight=1)
frame_centre.columnconfigure(2, weight=0)
frame_info = customtkinter.CTkFrame(master=frame_centre)
# frame_info.grid(row=5, column=0, columnspan=2, rowspan=2, pady=5, padx=20, sticky="nsew")
# frame_info.rowconfigure(0, weight=1)
frame_info.columnconfigure(0, weight=1)
frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
frame_left.grid_rowconfigure(11, minsize=10)

view_sample_frame = customtkinter.CTkFrame(master=frame_centre,height=450)
view_sample_frame.grid(row=0, column=0, columnspan=2, rowspan=5, pady=10, padx=20, sticky="nsew")
view_sample_frame.grid_rowconfigure(0, minsize=10) 
# sample_image = PhotoImage(master = view_sample_frame,file="RBC.png")

# label_sample = customtkinter.CTkLabel (master = view_sample_frame,text="sample",image = sample_image)
# label_sample.grid(row=0,column=0)




frame_right = customtkinter.CTkFrame(master=app,
                                                width=350,
                                                corner_radius=0)
frame_right.grid(row=0, column=3, sticky="nswe")


# app.label_1 = customtkinter.CTkLabel(master=frame_left,
#                                                text="Sample Collection",
#                                                text_font=("Roboto Medium", -16),
#                                                )  # font name and size in px
# app.label_1.grid(row=1, column=0, pady=10, padx=10)


# app.label_1.grid(row=1, column=0, pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_left,
                                                 text="Obtain Sample",
                                                #  command = functions.Obtain_sample
                                                )
button_1.grid(row=2, column=0, pady=10, padx=20)

button_2 = customtkinter.CTkButton(master=frame_left,
                                                 text="View Patients",
                                                #  command=functions.open_database
                                                )
button_2.grid(row=3, column=0, pady=10, padx=20)

button_3 = customtkinter.CTkButton(master=frame_left,
                                    text="Run Diagnosis",
                                    )
button_3.grid(row=4, column=0, pady=10, padx=20)

# label_info_1 = customtkinter.CTkLabel(master=frame_info,
#                                             text="WELCOME TO VIRAL SCOPE\n" +
#                                                  "Discover a whole new way of diagnosis,\n" +
#                                                 " @viral_scope,\n",
#                                             height=100,
#                                             corner_radius=6,  # <- custom corner radius
#                                             fg_color=("white", "gray38"),  # <- custom tuple-color
#                                             justify=LEFT)
# label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

label_mode = customtkinter.CTkLabel(master=frame_left, text="Appearance Mode:")
label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

appearance_optionmenu = customtkinter.CTkOptionMenu(master=frame_left,
                                                    values=["Light", "Dark", "System"],
                                                    # command=functions.change_appearance_mode
                                                    )
appearance_optionmenu.grid(row=10, column=0, pady=10, padx=20, sticky="w")



app.radio_var = IntVar(value=0)

label_radio_group = customtkinter.CTkLabel(master=frame_right,
                                                        text="Patient Registration:")
label_radio_group.grid(row=0, column=0, columnspan=1, pady=5, padx=1, sticky="")

# slider_1 = customtkinter.CTkSlider(master=frame_centre,
#                                              from_=0,
#                                              to=1,
#                                              number_of_steps=3,
#                                             )
# slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

# slider_2 = customtkinter.CTkSlider(master=frame_centre,
#                                             )
# slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

# switch_1 = customtkinter.CTkSwitch(master=frame_centre,
#                                                 text="CTkSwitch")
# switch_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

# switch_2 = customtkinter.CTkSwitch(master=frame_centre,
#                                                 text="CTkSwitch")
# switch_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

# combobox_1 = customtkinter.CTkComboBox(master=frame_centre,
#                                                     values=["Input 1", "Input 2"])
# combobox_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

# check_box_1 = customtkinter.CTkCheckBox(master=frame_centre,
#                                                      text="Checkbox 1")
# check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

# check_box_2 = customtkinter.CTkCheckBox(master=frame_centre,
#                                                      text="CheckBox")
# check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

entry = customtkinter.CTkEntry(master=frame_centre,
                                            width=120,
                                            placeholder_text="Email Adress",
                                            )
entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")



        # set default values
appearance_optionmenu.set("Dark")
button_3.configure(state="disabled", text="Disabled ")


first_name_entry = StringVar()
last_name_entry = StringVar()
age_entry  = IntVar()
email_entry = StringVar()
pat_add_info = StringVar()
pat_gender_entry = StringVar()
pat_county = StringVar()




first_name_label = customtkinter.CTkLabel(master=frame_right,
                                        text="First name",
                                        )
first_name_label.grid(row=1,column=0,pady=8 )
first_name_entry = customtkinter.CTkEntry(master= frame_right,textvariable=first_name_entry,placeholder_text="firstname")
first_name_entry.grid(row=1,column=1,pady=8)
last_name_label = customtkinter.CTkLabel(master=frame_right,text="Last name")
last_name_label.grid(row = 2,column = 0,pady=8)
last_name_entry = customtkinter.CTkEntry(master = frame_right,placeholder_text="lastname",textvariable=last_name_entry)
last_name_entry.grid(row=2,column=1,pady=8)
pat_gender_label = customtkinter.CTkLabel(master = frame_right,text="Gender")
pat_gender_label.grid(row = 3,column = 0,pady=8)
pat_gender_entry = customtkinter.CTkEntry(master=frame_right,placeholder_text="Gender",textvariable=pat_gender_entry)
pat_gender_entry.grid(row = 3,column = 1,pady=8)
yob_label = customtkinter.CTkLabel(master = frame_right,text="Year of Birth")
yob_label.grid(row = 4,column=0,pady=8)
yob_entry = customtkinter.CTkEntry(master = frame_right,placeholder_text="YOB",textvariable=age_entry)
yob_entry.grid(row=4,column = 1,pady=8)
pat_email_label = customtkinter.CTkLabel(master = frame_right,text="Email")
pat_email_label.grid(row = 5,column = 0,pady=8)
pat_email_entry = customtkinter.CTkEntry(master=frame_right,placeholder_text="Email address",textvariable=email_entry)
pat_email_entry.grid(row = 5,column = 1,pady=8)
pat_county_label = customtkinter.CTkLabel(master = frame_right,text="County")
pat_county_label.grid(row=6,column = 0,pady=8)
pat_county_entry = customtkinter.CTkEntry(master = frame_right,placeholder_text="County of residence",textvariable = pat_county)
pat_county_entry.grid(row=6,column = 1,pady=8)
pat_add_info_label = customtkinter.CTkLabel(master=frame_right,text="Symptoms:")
pat_add_info_label.grid(row=7,column=0)
pat_add_info = customtkinter.CTkTextbox(master=frame_right,)
pat_add_info.grid(row=8,column=1,pady=8)
vertical_sb = customtkinter.CTkScrollbar(master=pat_add_info)
vertical_sb.grid(row=0,column=2,pady=8)








Reg_pat_button = customtkinter.CTkButton(master=frame_right,
                                                text="Register",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=save_pat_info
                                                )
Reg_pat_button.grid(row=9, column=0, columnspan=1, pady=20, padx=20, sticky="we")

clear_pat_det_button = customtkinter.CTkButton(master = frame_right,
                                            text="Clear",
                                            fg_color=None,border_width=2,
                                            command=entry_clear
                                            )
clear_pat_det_button.grid(row=9, column=1, columnspan=1, pady=20, padx=20, sticky="we")






mainloop()