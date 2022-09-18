import customtkinter
from tkinter import Toplevel, filedialog
from tkinter import *
from datetime import datetime
import time
import wget
# from re import S
Download_store_path_display = "path of Download"
Link_store_path_display = "path of Link"
# current_date = datetime.now()
# print(current_date)

# Schedule_date = []
# Schedule_full_date = ""

# disable below
# print(Current_month, Current_day, Current_hour, Current_min)
# print(Current_month,Current_day,Current_hour)


# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()


def button_Download():
    global Remain_time

    Schedule_full_date = entry.get()
    Schedule_date = Schedule_full_date.split(":")
    Schedule_hour = int(Schedule_date[0])
    Schedule_min = int(Schedule_date[1])
    # print(Schedule_hour,Schedule_min)
    # current Date Propertise

    current_date = datetime.now()
    # print(current_date)
    app.destroy()

    Current_month = int(current_date.strftime("%m"))
    Current_day = int(current_date.strftime("%d"))

    Current_hour = int(current_date.strftime("%H"))
    Current_min = int(current_date.strftime("%M"))
    
    Remain_time = (Schedule_hour-Current_hour)*60 + \
        (Schedule_min - Current_min)  # Remain time is in minutes
    # new = Toplevel()

    print(f"your remain time is {Remain_time} minitues")
    # time.sleep(Remain_time*60)
    # print(Download_store_path_display)
    print("end of the button click")

    return Remain_time


# Download_store_path_display = "gg"


def Download_store_path():
    global Download_store_path_display
    Download_store_path_display = filedialog.askdirectory()

def button_Link():
    global Link_store_path_display
    Link_store_path_display = filedialog.askopenfilename()
        

# print(Remain_time)
# x = Download_store_path_display
# print(x)
# Basic Ui Settings


app.title("Schedule Downloader")
app.iconbitmap('D:\Python_projects\photo1.ico')
app.geometry("720x512")

label = customtkinter.CTkLabel(master=app, text="Input download Location")
label.place(relx=0.05, rely=0.1)

entry = customtkinter.CTkEntry(master=app, placeholder_text="Input Time")
entry.pack(padx=20, pady=10)


button2 = customtkinter.CTkButton(
    master=app, text="Open Download folder", command=Download_store_path).pack()


button3 = customtkinter.CTkButton(
    master=app, text="Open Link file", command=button_Link).pack()

button = customtkinter.CTkButton(
    master=app, text="Start Scheduling (Downloading)", command=button_Download).pack()
    

customtkinter.CTkLabel


app.mainloop()

print(Download_store_path_display)

wget.download("",f"{Download_store_path_display}")



## after Death of first window


open_file = open(f"{Link_store_path_display}")
read_file = open_file.read()

Links_one_by_one = read_file.split()




new = customtkinter.CTk()

new.title("Schedule Downloader")
new.iconbitmap('D:\Python_projects\photo1.ico')
for i in Link_store_path_display:
    wget.download(f"{Link_store_path_display[i]}",f"{Download_store_path_display}")

new.geometry("720x512")


new.mainloop()

# Schedule Date Propertise
# Schedule_date = Schedule_full_date.split(":")
# Schedule_hour = Schedule_date[0]
# Schedule_min = Schedule_date[1]

# print(Schedule_full_date,Schedule_hour)





## need to do

    # Sleep  eka use karaddi yata code okkoma wada karan nathi hinda new Conform download Window ekak
    # hadanna onee
    #Ui eka haddanna one
    # Exe convert Wen na Documentation eka kiyawanna onee

