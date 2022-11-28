import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

resolution = ['Const.', 'Dry', 'Wet', 'Interior', 'Facade']
hardness = 5

d = {}
o = []
h = 0

total = []

class App(customtkinter.CTk):

    WIDTH = 800
    HEIGHT = 500

    def __init__(self):
        super().__init__()

        self.title("BM Modul Sekvens Selektion")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        self.label_1 = customtkinter.CTkLabel(master=self, text="BM Byggeindustri", text_font=("Samsung Sharp Sans", -30))  # font name and size in px
        self.label_1.place(anchor='c', x=400, y=100)

        self.label_2 = customtkinter.CTkLabel(master=self, text="PSG - Indtast sværhedsgrader i felterne:", text_font=("Samsung Sharp Sans", -15))  # font name and size in px
        self.label_2.place(anchor='c', x=400, y=140)

        self.entryVar = customtkinter.StringVar()
        self.entryVar.set(value=1)

        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="Amount", textvariable=self.entryVar)
        self.entry.place(anchor='c', x=270, y=300, width=100)

        self.button_1 = customtkinter.CTkButton(master=self, text="Tilføj Modul", command=self.button_event)
        self.button_1.place(anchor='c', x=400, y=300)

        self.button_2 = customtkinter.CTkButton(master=self, text="Beregn Sekvens", command=self.button_event2, fg_color=("red"), hover_color=("darkred"))
        self.button_2.place(anchor='c', x=400, y=340)

        self.selector_1 = customtkinter.StringVar()
        self.selector_1.trace_add('write', self.my_callback_1)

        self.selector_2 = customtkinter.StringVar()
        self.selector_2.trace_add('write', self.my_callback_2)

        self.switch_1 = customtkinter.CTkSwitch(master=self, text="Contains First Module", onvalue=True, offvalue=False, variable=self.selector_1)
        self.switch_1.place(anchor='w', x=500, y=300)

        self.switch_2 = customtkinter.CTkSwitch(master=self, text="Contains Final Module", onvalue=1, offvalue=0, variable=self.selector_2)
        self.switch_2.place(anchor='w', x=500, y=340)

        for k in range(hardness):
            o.append(str(k+1))

        for i in range(len(resolution)):
            var = "hardness" + str(i)
            d["stringVar{0}".format(i)] = customtkinter.StringVar(self, 1, var)

        locals().update(d)
        for i in range(len(resolution)):

            self.selector = customtkinter.CTkComboBox(master=self, variable=d.get("stringVar"+ str(i)), values=o)

            # Calculate the optimal position for the dropdown...
            center = App.WIDTH/2
            width = 50
            iPos = (center/2)+(width/2) + ((575-225)/(len(resolution)-1))*i

            self.selector.place(anchor='c', x=iPos, y=230, width=50)

            self.label = customtkinter.CTkLabel(master=self, text=resolution[i], text_font=("Samsung Sharp Sans", -14))
            self.label.place(anchor='c', x=iPos, y=200, width=60)


    def my_callback_1(self, var, index, mode):
        print(self.selector_1.get())

    def my_callback_2(self, var, index, mode):
        print(self.selector_2.get())

    def button_event(self):
        global h
        print("Button pressed")

        try:
            integer_result = int(self.entryVar.get())
        except ValueError:
            print("not a valid integer")
        else:
            for g in range(integer_result):
                choices = ()
                for j in range(len(resolution)):
                    choices = choices + (int((d.get("stringVar"+str(j)).get())),)
                if self.selector_1.get() == '1':
                    print("HELLO")
                    choices = choices + ('End',)

                if self.selector_2.get() == '1':
                    print("HELLO")
                    choices = choices + ('First',)
                choices = choices + ('m' + str(h),)
                print(choices)
                total.append(choices)
        h = h + 1

    def on_closing(self, event=0):
        self.destroy()

    def sequencerBM(self, propertyList):
        """
        This function takes a list of tuples, sorts them
        and then arranges them to alternate between lowest and highest.
        This ensures that BM avoids putting two complex modules right after each other.
        """
        listSorted = sorted(propertyList)

        listRevSorted = []

        # The following code sorts the list of tuples alternating with the smallest value and then the higest value,
        # starting from the lowest value.
        rev = True
        for i in range(len(listSorted)):
            if (i % 2) == 0:
                # listRevSorted.append(2)
                listRevSorted.append(listSorted[-1])
                listSorted.pop(-1)
            elif (i % 2) == 1:
                # listRevSorted.append(1)
                listRevSorted.append(listSorted[0])
                listSorted.pop(0)
        return listRevSorted

    def button_event2(self):
        print(total)
        print(self.sequencerBM(total))

if __name__ == "__main__":
    app = App()
    app.mainloop()
