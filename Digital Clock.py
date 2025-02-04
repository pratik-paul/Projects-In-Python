from tkinter import *
import time
import calendar

class DigitalClock:
    def __init__(self):
        self.clk = Tk()
        self.clk.title("Pratik's Digital Clock")
        self.clk.geometry("1350x700+0+0")
        self.clk.config(bg="#0C1E28")

        self.lb_hr = Label(self.clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#087587", fg="black")
        self.lb_hr.place(relx=0.25, rely=0.3, width=150, height=150)

        self.lb_hr_text = Label(self.clk, text="HOUR", font=("Times 20 bold", 20, 'bold'), bg="#087587", fg="white")
        self.lb_hr_text.place(relx=0.25, rely=0.45, width=150, height=50)

        self.lb_mn = Label(self.clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#008EA4", fg="black")
        self.lb_mn.place(relx=0.4, rely=0.3, width=150, height=150)

        self.lb_mn_text = Label(self.clk, text="MINUTE", font=("Times 20 bold", 20, 'bold'), bg="#008EA4", fg="white")
        self.lb_mn_text.place(relx=0.4, rely=0.45, width=150, height=50)

        self.lb_sc = Label(self.clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#06B4BB", fg="black")
        self.lb_sc.place(relx=0.55, rely=0.3, width=150, height=150)

        self.lb_sc_text = Label(self.clk, text="SECOND", font=("Times 20 bold", 20, 'bold'), bg="#06B4BB", fg="white")
        self.lb_sc_text.place(relx=0.55, rely=0.45, width=150, height=50)

        self.lb_dn = Label(self.clk, text="AM", font=("Times 20 bold", 70, 'bold'), bg="#9F0646", fg="black")
        self.lb_dn.place(relx=0.7, rely=0.3, width=150, height=150)

        self.lb_dn_text = Label(self.clk, text="NOON", font=("Times 20 bold", 20, 'bold'), bg="#9F0646", fg="white")
        self.lb_dn_text.place(relx=0.7, rely=0.45, width=150, height=50)

        self.lb_date = Label(self.clk, text="DATE", font=("Times 20 bold", 30, 'bold'), bg="#0C1E28", fg="white")
        self.lb_date.place(relx=0.4, rely=0.6, width=200, height=50)

        self.lb_day = Label(self.clk, text="DAY", font=("Times 20 bold", 30, 'bold'), bg="#0C1E28", fg="white")
        self.lb_day.place(relx=0.4, rely=0.7, width=200, height=50)

        self.update_time()
        self.update_date()

    def update_time(self):
        hr = str(time.strftime("%H"))
        mn = str(time.strftime("%M"))
        sc = str(time.strftime("%S"))
        if int(hr) > 12 and int(mn) > 0:
            self.lb_dn.config(text="PM")
        if int(hr) > 12:
            hr = str(int(int(hr) - 12))

        self.lb_hr.config(text=hr)
        self.lb_mn.config(text=mn)
        self.lb_sc.config(text=sc)

        self.lb_hr.after(200, self.update_time)

    def update_date(self):
        date = time.strftime("%d-%m-%Y")
        day = calendar.day_name[time.localtime().tm_wday]
        self.lb_date.config(text=date)
        self.lb_day.config(text=day)

        self.lb_date.after(1000, self.update_date)

    def run(self):
        self.clk.mainloop()

if __name__ == "__main__":
    clock = DigitalClock()
    clock.run()