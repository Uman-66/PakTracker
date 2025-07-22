from modules.elec_calc import ElectricityCalc
from tkinter import *
from modules.inflation_calc import Inflate


def elctricity_calculte():
    window.withdraw()  # Hides it
    calc = ElectricityCalc()

def inflation_calculte():
    window.withdraw()  # Hides it
    calc = Inflate()

window = Tk()
window.title("PakTracker")
window.config(padx=20, pady=20)
logo = PhotoImage(file="assets/logo1.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
gen_logo = canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=2)

bill_button = Button(text="Bill Calculator", command=elctricity_calculte)
bill_button.grid(row=1, column=0)

inflat_button = Button(text="Inflation Calculator", command=inflation_calculte)
inflat_button.grid(row=1, column=1)

window.mainloop()


