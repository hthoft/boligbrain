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
g = 0

total = []
types = []

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
        self.entryVar.trace_add("write", self.entryVarLockout)

        self.blockVar = customtkinter.StringVar()
        self.blockVar.set(value='01')

        self.floorVar = customtkinter.StringVar()
        self.floorVar.set(value='00')

        self.sequenceVar = customtkinter.StringVar()
        self.sequenceVar.set(value='01')

        self.amountVar = customtkinter.StringVar()
        self.amountVar.set(value=0)

        self.label_8 = customtkinter.CTkLabel(master=self, textvariable=self.amountVar,
                                              text_font=("Samsung Sharp Sans", -10))  # font name and size in px
        self.label_8.place(anchor='c', x=500, y=275, width=50)

        self.label_3 = customtkinter.CTkLabel(master=self, text="AMOUNT",
                                              text_font=("Samsung Sharp Sans", -10))  # font name and size in px
        self.label_3.place(anchor='c', x=270, y=275, width=50)

        self.label_3 = customtkinter.CTkLabel(master=self, text="BLOCK",
                                              text_font=("Samsung Sharp Sans", -10))  # font name and size in px
        self.label_3.place(anchor='c', x=505, y=275, width=50)

        self.label_4 = customtkinter.CTkLabel(master=self, text="FLOOR",
                                              text_font=("Samsung Sharp Sans", -10))  # font name and size in px
        self.label_4.place(anchor='c', x=560, y=275, width=50)

        self.label_5 = customtkinter.CTkLabel(master=self, text="NUMBER",
                                              text_font=("Samsung Sharp Sans", -10))  # font name and size in px
        self.label_5.place(anchor='c', x=615, y=275, width=50)

        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="Amount", textvariable=self.entryVar)
        self.entry.place(anchor='c', x=270, y=300, width=100)

        self.blockEntry = customtkinter.CTkEntry(master=self, placeholder_text="Amount", textvariable=self.blockVar)
        self.blockEntry.place(anchor='c', x=505, y=300, width=50)

        self.floorEntry = customtkinter.CTkEntry(master=self, placeholder_text="Amount", textvariable=self.floorVar)
        self.floorEntry.place(anchor='c', x=560, y=300, width=50)

        self.sequenceEntry = customtkinter.CTkEntry(master=self, placeholder_text="Amount", textvariable=self.sequenceVar)
        self.sequenceEntry.place(anchor='c', x=615, y=300, width=50)


        self.button_1 = customtkinter.CTkButton(master=self, text="Tilføj Modul", command=self.button_event)
        self.button_1.place(anchor='c', x=400, y=300)

        self.button_2 = customtkinter.CTkButton(master=self, text="Beregn Sekvens", command=self.button_event2, fg_color=("red"), hover_color=("darkred"))
        self.button_2.place(anchor='c', x=400, y=340)

        self.optionlist = customtkinter.StringVar()
        self.optionlist.trace_add("write", self.optionRetreive)
        self.options = []

        self.selector_2 = customtkinter.CTkComboBox(master=self, variable=self.optionlist, values=self.options)
        self.selector_2.place(anchor='c', x=270, y=340, width=100)

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


    def button_event(self):
        global h
        #print("Button pressed")

        moduleCode = []
        moduleCode.append(self.blockVar.get())
        moduleCode.append(self.floorVar.get())
        moduleCode.append(self.sequenceVar.get())

        try:
            integer_result = int(self.entryVar.get())
        except ValueError:
            None
        else:
            for g in range(integer_result):
                choices = ()
                for j in range(len(resolution)):
                    choices = choices + (int((d.get("stringVar"+str(j)).get())),)
                moduleTypes = choices
                choices = choices + ('m' + str(h),)
                choices = choices + (moduleCode,)
                print(choices)
                total.append(choices)

        if moduleTypes not in types:
            self.options.append("Type " + str(h))
            self.selector_2.configure(values=self.options)
            types.append(moduleTypes)
            h = h + 1

    def optionRetreive(self, var, index, mode):
        try:
            integer_result = int(self.optionlist.get()[5:])
        except ValueError:
            None
        else:
            options = types[integer_result]
            for j in range(len(resolution)):
                d.get("stringVar" + str(j)).set(options[j])

    def entryVarLockout(self, var, index, mode):
        try:
            integer_result = int(self.entryVar.get())
        except ValueError:
            #print("not a valid integer")
            self.blockEntry.configure(state=tkinter.DISABLED)
            self.floorEntry.configure(state=tkinter.DISABLED)
            self.sequenceEntry.configure(state=tkinter.DISABLED)
            self.blockVar.set('')
            self.floorVar.set('')
            self.sequenceVar.set('')
        else:
            if integer_result == 1:
                #print("unlocked")
                self.blockEntry.configure(state=tkinter.NORMAL)
                self.floorEntry.configure(state=tkinter.NORMAL)
                self.sequenceEntry.configure(state=tkinter.NORMAL)
                self.blockVar.set('01')
                self.floorVar.set('00')
                self.sequenceVar.set('01')
                ## UNLOCK VALUES FOR BLOK; FLOOR; ID
            else:
                #print("locked")
                self.blockEntry.configure(state=tkinter.DISABLED)
                self.floorEntry.configure(state=tkinter.DISABLED)
                self.sequenceEntry.configure(state=tkinter.DISABLED)
                self.blockVar.set('')
                self.floorVar.set('')
                self.sequenceVar.set('')

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
