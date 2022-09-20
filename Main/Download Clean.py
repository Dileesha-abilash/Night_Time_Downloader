from tkinter import filedialog
from tkinter import *
from datetime import datetime
import wget
import notifypy
import time


# Link and Path storing Var(s)

Download_store_path_display = "path of Download"
Link_store_path_display = "path of Link"


# Button click Functions

def Clock_date_fun ():
        
    Clock_h = time.strftime("%H")
    Clock_m = time.strftime("%M")
    Clock_s = time.strftime("%S")
    Clock_label.config(text=f"{Clock_h}:{Clock_m}:{Clock_s}")
    Clock_label.after(1000,Clock_date_fun)
 



def button_Download():
    global Remain_time
    global Schedule_full_date
    Schedule_full_date = entry.get()
    Schedule_date = Schedule_full_date.split(":")
    Schedule_hour = int(Schedule_date[0])
    Schedule_min = int(Schedule_date[1])

    current_date = datetime.now()
    app.destroy()

    Current_month = int(current_date.strftime("%m"))
    Current_day = int(current_date.strftime("%d"))

    Current_hour = int(current_date.strftime("%H"))
    Current_min = int(current_date.strftime("%M"))
    click()
    if chosied == 0:
        Remain_time = (Schedule_hour-Current_hour)*60 + \
            (Schedule_min - Current_min)  # Remain time is in minutes
    else:
        Remain_time = (24-Current_hour + Schedule_hour)*60 + \
            (Schedule_min - Current_min)  # Remain time is in minutes
    return Remain_time


def Download_store_path():
    global Download_store_path_display
    Download_store_path_display = filedialog.askdirectory()


def button_Link():
    global Link_store_path_display
    Link_store_path_display = filedialog.askopenfilename(
        filetypes=[("Link Files", ".txt")])


# Starting Of GUI
    # Main Window
app = Tk()
# canvas main

## -------- Clock Dynamically update
app.after(0,Clock_date_fun)
 ## ============================

Main_canvas = Canvas(app, width=720, height=512, bd=0, highlightthickness=0)
Main_canvas.pack(fill="both", expand=False)

bg = PhotoImage(file="bg_final.png")

##      --------------------------- Clock ----------------------
Clock_label = Label(app)

Clock_label.pack()

Main_canvas.create_window(325, 190,window=Clock_label,anchor="nw")

#                   ----------------------- 
Main_canvas.create_image(0, 0, image=bg, anchor="nw",)
Main_canvas.create_text(
    350, 235, text="Enter the Schedule Time (HH:MM)- 24hour ", fill="white")


Main_canvas.create_text(290, 200, text="Time Now",fill="white",font=("hevatica",10) )


whichday = IntVar()


def click():
    global chosied
    chosied = whichday.get()


check_day = Checkbutton(app, text="Tommarow", variable=whichday)

Main_canvas.create_window(350, 300, window=check_day)




app.title("Nite Down")
app.iconbitmap('1.ico')
app.geometry("720x512")


label = Label(master=app, text="Input download Location")
entry = Entry(app, width=44)

button2 = Button(master=app, text="Open Download folder",
                 command=Download_store_path,)
button3 = Button(master=app, text="Open Link file", command=button_Link)
button = Button(master=app, text="Start Scheduling (Downloading)",
                command=button_Download)

Main_canvas.create_window(235, 331, window=button3, anchor="nw")
Main_canvas.create_window(378, 331, window=button2, anchor="nw")
Main_canvas.create_window(270, 385, window=button, anchor="nw")
Main_canvas.create_window(230, 256, window=entry, anchor="nw")


app.mainloop()


open_file = open(f"{Link_store_path_display}")
read_file = open_file.read()

Links_one_by_one = read_file.split()


new = Tk()  # Timer Window

new.title("Nite Down")
new.iconbitmap('1.ico')

## Nortification

notification = notifypy.Notify()
notification.title = "We Scheduled Download"
notification.icon = "1.ico"
notification.message = f"We are Sucessfully Scheduled Your Task to {Schedule_full_date}.Dont Close the Pop-up Window😁"
notification.application_name = "Nite Down"
notification.send()

# Auto Executing Function

def Sleep_and_downlaod():
    for i, j in enumerate(Links_one_by_one):
        wget.download(f"{Links_one_by_one[i]}",
              f"{Download_store_path_display}")
    nortification2 = notifypy.Notify()
    nortification2.title = "Your Download Completed"
    nortification2.icon = "1.ico"
    nortification2.message = "We are Sucessfully Downloaded Your Files 👌 .Enjoy😊"
    nortification2.application_name = "Nite Down"
    nortification2.send()
    new.destroy()


new.after(Remain_time*60000, Sleep_and_downlaod)
# new.destroy(Remain_time + 1000 )
# new.after(0,Clock_Remain_fun)


new.geometry("720x512")
TimerCanvas = Canvas(new, width=720, height=512, bd=0, highlightthickness=0)
bg_new = PhotoImage(file="finl_maz_1.png")
TimerCanvas.create_image(0, 0, image=bg_new, anchor="nw",)
TimerCanvas.pack(fill="both", expand=False)

# TimerCanvas.create_window(325, 190,window=Clock_label,anchor="nw")

# messagebox.OKCANCEL("HEllo")
# nWE_LABELE = Label("hacker")
# nWE_LABELE.pack()
# new.destroy()
new.mainloop()
