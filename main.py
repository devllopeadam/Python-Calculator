import tkinter as tk


window = tk.Tk()
window.title("Calculator")
window.geometry("350x500")
window.resizable(False, False)
window.iconbitmap("./icon.ico")
window.configure(background="#3a4452")


def makeButton(value):
    return tk.Button(
        buttons,
        text=value,
        background="#4d5765",
        fg="white",
        font="Arial 16",
        borderwidth=0,
        command=lambda: showIt(value),
    )


def makeOperator(value):
    return tk.Button(
        buttons,
        text=value,
        background="#4d5765",
        fg="#33ffd8",
        font="Arial 16",
        borderwidth=0,
        command=lambda: showIt(value),
    )


def makeGrid(element, rowValue, columnValue):
    element.grid(row=rowValue, column=columnValue, padx=10, pady=10, sticky="news")


def clearEntry():
    entryValue.set("")


def deleteOneCharacter():
    stringValue = entryValue.get()
    entryValue.set(stringValue[0:-1])


def showIt(charachter):
    eResult.insert("end", charachter)


def calculate():
    cal = eval(entryValue.get())
    entryValue.set(cal)


# Entry
entryValue = tk.StringVar()
eResult = tk.Entry(
    window,
    width=350,
    font=("Arial", 20, "bold"),
    bg="#3a4452",
    borderwidth=0,
    fg="white",
    textvariable=entryValue,
)
eResult.pack(ipady=5, padx=10, pady=10)

# Entry Frame
buttons = tk.Frame(width=350, height=500, background="#3a4452")
buttons.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
buttons.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
buttons.pack(fill="both", padx=10, pady=20, expand=True)


# Clear Button
clearBtn = tk.Button(
    buttons,
    text="AC",
    background="#ffa500",
    fg="white",
    font=2,
    borderwidth=0,
    command=clearEntry,
)
clearBtn.grid(row=0, column=0, sticky="nesw", padx=10, pady=10)
# Delete one character Button
deBtn = tk.Button(
    buttons,
    text="DE",
    background="#4d5765",
    fg="white",
    font=2,
    borderwidth=0,
    command=deleteOneCharacter,
)
deBtn.grid(row=0, column=1, sticky="nesw", padx=10, pady=10)
# Dot Button
dotBtn = makeOperator(".")
dotBtn.grid(row=0, column=2, padx=10, pady=10, sticky="news")
# Operators Buttons
divisionBtn = makeOperator("/")
multi = makeOperator("*")
mince = makeOperator("-")
plus = makeOperator("+")
divisionBtn.grid(row=0, column=3, padx=10, pady=10, sticky="news")
# Create Numbers Buttons

one = makeButton(1)
two = makeButton(2)
three = makeButton(3)
foor = makeButton(4)
five = makeButton(5)
six = makeButton(6)
seven = makeButton(7)
eigth = makeButton(8)
nine = makeButton(9)
zero = makeButton(0)

dubleZero = makeButton("00")
###########################
#########The Result########
###########################

equalBtn = tk.Button(
    buttons,
    text="=",
    background="#4d5765",
    fg="#33ffd8",
    font=3,
    borderwidth=0,
    command=lambda: calculate(),
)
equalBtn.grid(row=4, column=2, columnspan=2, padx=10, pady=10, sticky="news")


numberButtons = [
    seven,
    eigth,
    nine,
    multi,
    foor,
    five,
    six,
    mince,
    one,
    two,
    three,
    plus,
    zero,
    dubleZero,
    equalBtn,
]

makeGrid(numberButtons[0], 1, 0)
makeGrid(numberButtons[1], 1, 1)
makeGrid(numberButtons[2], 1, 2)
makeGrid(numberButtons[3], 1, 3)
makeGrid(numberButtons[4], 2, 0)
makeGrid(numberButtons[5], 2, 1)
makeGrid(numberButtons[6], 2, 2)
makeGrid(numberButtons[7], 2, 3)
makeGrid(numberButtons[8], 3, 0)
makeGrid(numberButtons[9], 3, 1)
makeGrid(numberButtons[10], 3, 2)
makeGrid(numberButtons[11], 3, 3)
makeGrid(numberButtons[12], 4, 0)
makeGrid(numberButtons[13], 4, 1)


window.mainloop()
