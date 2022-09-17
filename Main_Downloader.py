import customtkinter
from tkinter import filedialog
from datetime import datetime
import time
# from re import S

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


def button_get():
    Schedule_full_date = entry.get()
    Schedule_date = Schedule_full_date.split(":")
    Schedule_hour = int(Schedule_date[0])
    Schedule_min = int(Schedule_date[1])
    # print(Schedule_hour,Schedule_min)
    # current Date Propertise

    current_date = datetime.now()
    # print(current_date)

    Current_month = int(current_date.strftime("%m"))
    Current_day = int(current_date.strftime("%d"))

    Current_hour = int(current_date.strftime("%H"))
    Current_min = int(current_date.strftime("%M"))
    Remain_time = (Schedule_hour-Current_hour)*60 + \
        (Schedule_min - Current_min)  # Remain time is in minutes

    print(f"your remain time is{Remain_time}")
    time.sleep(Remain_time*60)

    print("Remain_time look")
    return Remain_time

url_store_path_display = "gg"
def url_store_path():
    url_store_path_display = filedialog.askdirectory()
    return url_store_path_display

# print(Remain_time)

label = customtkinter.CTkLabel(master=app, text="Input download Location")
label.place(relx=0.05, rely=0.1)

entry = customtkinter.CTkEntry(master=app, placeholder_text="Input Time")
entry.pack(padx=20, pady=10)


button2 = customtkinter.CTkButton(
    master=app, text="Open Download folder", command=url_store_path).pack()
    

button = customtkinter.CTkButton(
    master=app, text="Start Scheduling (Downloading)", command=button_get).pack()

customtkinter.CTkLabel


app.mainloop()
print(url_store_path_display)                  
# Schedule Date Propertise
# Schedule_date = Schedule_full_date.split(":")
# Schedule_hour = Schedule_date[0]
# Schedule_min = Schedule_date[1]

# print(Schedule_full_date,Schedule_hour)