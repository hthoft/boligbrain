import tkinter
import tkinter.messagebox
import customtkinter
import random
import time

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

resolution = ['Const.', 'Dry', 'Wet', 'Interior', 'Facade', "Tech"]
hardness = 5

d = {}
o = []
h = 0
g = 0

total = []
types = []

class App(customtkinter.CTk):

    WIDTH = 800
    HEIGHT = 800

    def __init__(self):
        super().__init__()

        self.title("BM Modul Sekvens Selektion")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        self.label_9 = customtkinter.CTkLabel(master=self, text="MODULES",
                                              text_font=("Samsung Sharp Sans", -20))  # font name and size in px
        self.label_9.place(anchor='c', x=245, y=390, width=100)

        self.label_9 = customtkinter.CTkLabel(master=self, text="PRODUCTION SEQUENCE",
                                              text_font=("Samsung Sharp Sans", -20))  # font name and size in px
        self.label_9.place(anchor='c', x=555, y=390, width=250)

        self.orderField = customtkinter.CTkTextbox(master=self, state='disabled')
        self.orderField.place(anchor='nw', x=100, y=410, width=290, height=350)

        self.sequenceField = customtkinter.CTkTextbox(master=self, state='disabled')
        self.sequenceField.place(anchor='nw', x=410, y=410, width=290, height=350)

        self.label_1 = customtkinter.CTkLabel(master=self, text="BM Byggeindustri", text_font=("Samsung Sharp Sans", -30))  # font name and size in px
        self.label_1.place(anchor='c', x=400, y=100)

        self.label_2 = customtkinter.CTkLabel(master=self, text="PSG - Add difficulties in fields:", text_font=("Samsung Sharp Sans", -15))  # font name and size in px
        self.label_2.place(anchor='c', x=400, y=140)

        self.entryVar = customtkinter.StringVar()
        self.entryVar.set(value=1)
        self.entryVar.trace_add("write", self.entryVarLockout)

        self.blockVar = customtkinter.StringVar()
        self.blockVar.set(value='01')

        self.floorVar = customtkinter.StringVar()
        self.floorVar.set(value='00')

        self.sequenceVar = customtkinter.StringVar()
        self.sequenceVar.set(value='1')

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

        self.selector_1 = customtkinter.StringVar()
        self.selector_1.trace_add('write', self.selectorLockout1)

        self.selector_2 = customtkinter.StringVar()
        self.selector_2.trace_add('write', self.selectorLockout2)

        self.switch_1 = customtkinter.CTkSwitch(master=self, text="Contains First Module", onvalue=True, offvalue=False,
                                                variable=self.selector_1)
        self.switch_1.place(anchor='w', x=40, y=300)

        self.switch_2 = customtkinter.CTkSwitch(master=self, text="Contains Final Module", onvalue=1, offvalue=0,
                                                variable=self.selector_2)
        self.switch_2.place(anchor='w', x=40, y=340)

        self.button_1 = customtkinter.CTkButton(master=self, text="Add Module", command=self.button_event)
        self.button_1.place(anchor='c', x=400, y=300)

        self.button_2 = customtkinter.CTkButton(master=self, text="Calculate Sequence", command=self.button_event2, fg_color=("red"), hover_color=("darkred"))
        self.button_2.place(anchor='c', x=400, y=340)

        self.optionlist = customtkinter.StringVar()
        self.optionlist.trace_add("write", self.optionRetreive)
        self.options = []

        self.selector_3 = customtkinter.CTkComboBox(master=self, variable=self.optionlist, values=self.options)
        self.selector_3.place(anchor='c', x=270, y=340, width=100)



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

        try:
            integer_result = int(self.entryVar.get())
        except ValueError:
            None
        else:
            for g in range(integer_result):
                moduleCode = []
                moduleCode.append(self.blockVar.get())
                moduleCode.append(self.floorVar.get())
                moduleCode.append(self.sequenceVar.get())

                choices = ()
                for j in range(len(resolution)):
                    #choices = choices + (int((d.get("stringVar"+str(j)).get())),)
                    choices = choices + (random.randint(1,5),)
                moduleTypes = choices

                if self.selector_1.get() == '1':
                    choices = choices + ('End',)
                elif self.selector_2.get() == '1':
                    choices = choices + ('First',)
                else:
                    choices = choices + ('',)

                self.orderField.configure(state='normal')
                self.orderField.insert(tkinter.END, str(choices[:len(resolution)]) + '  ->  ' + str(moduleCode) + '  : ' + str(round((sum(choices[:len(resolution)])/(hardness*len(resolution)))*100)) + '% ''\n')
                self.orderField.configure(state='disabled')

                choices = choices + ('m' + str(h),)
                choices = choices + (moduleCode,)
                print(choices)
                total.append(choices)
                self.sequenceVar.set(int(self.sequenceVar.get())+1)

        if moduleTypes not in types:
            self.options.append("Type " + str(h))
            self.selector_3.configure(values=self.options)
            types.append(moduleTypes)
            h = h + 1

    def selectorLockout1(self, var, index, mode):
        if self.selector_2.get() == '1':
            self.switch_2.deselect()

    def selectorLockout2(self, var, index, mode):
        if self.selector_1.get() == '1':
            self.switch_1.deselect()

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
            #self.blockVar.set('')
            #self.floorVar.set('')
            #self.sequenceVar.set('')
        else:
            #print("unlocked")
            self.blockEntry.configure(state=tkinter.NORMAL)
            self.floorEntry.configure(state=tkinter.NORMAL)
            self.sequenceEntry.configure(state=tkinter.NORMAL)


    def on_closing(self, event=0):
        self.destroy()

    def singleListReducer(self, lst, featuresLength):
        """
        Takes a single list and reduces it dimensions. This function is meant to be used
        in conjuction with the function below called "tupleDimensionReducer".
        """
        reducedList = []
        for i in range(featuresLength - 1):
            appender = float(lst[i] * 2 / 3) + float(lst[i + 1] * 1 / 3)
            reducedList.append(appender)
        return reducedList

    # print(singleListReducer(lstt, featureLength))

    def tupleDimensionReducer(self, tupleInput, featuresLength):
        """
        This function takes a tuple and reduces its dimensionality by 1.
        It does this by taking a "weighted average" between 2 dimensions and then adding them together.
        The first element in the tuple weights 2/3 while the second element weights 1/3.
        That pattern will continue trickling down until the last dimension has been reached.
        """

        # First we change the tuples into variables of type list. This makes us able to edit elements in them.
        for i in range(len(tupleInput)):
            tupleInput[i] = list(tupleInput[i])

        for i in range(len(tupleInput)):
            tupleInput[i] = self.singleListReducer(tupleInput[i], featuresLength)
        for i in range(len(tupleInput)):
            tupleInput[i] = tuple(tupleInput[i])
        return tupleInput

    def sequencerBM(self, propertyList):
        """
        This function takes a list of tuples, sorts them
        and then arranges them to alternate between lowest and highest.
        This ensures that BM avoids putting two complex modules right after each other.
        """
        listSorted = sorted(propertyList)

        endList = []
        for i in range(len(listSorted)):
            if "End" in listSorted[i]:
                endList.append(listSorted[i])
                listSorted.pop(i)
                break

        listRevSorted = []

        # The following code sorts the list of tuples alternating with the smallest value and then the higest value,
        # starting from the lowest value.
        for i in range(len(listSorted)):
            if (i % 2) == 0:
                # listRevSorted.append(2)
                listRevSorted.append(listSorted[-1])
                listSorted.pop(-1)
            elif (i % 2) == 1:
                # listRevSorted.append(1)
                listRevSorted.append(listSorted[0])
                listSorted.pop(0)
        for i in range(len(endList)):
            listRevSorted.append(endList[i])

        return listRevSorted

    def button_event2(self):
        results = [(1,1,5,4,2,"m1","End"),(4,1,5,4,2,"m2"),(4,1,5,4,2,"m2"),(4,1,5,4,2,"m2"),(2,4,4,4,2,"m3"),(2,4,4,4,2,"m3"),(2,4,4,4,2,"m3"),(2,4,4,4,2,"m3"),(2,4,4,4,2,"m3"),(2,4,4,4,2,"m3")]
        results = self.sequencerBM(total)
        for i in range(len(results)):
            self.sequenceField.configure(state='normal')
            self.sequenceField.insert(tkinter.END, str(results[i][:len(resolution)]) + '  ->  ' + str(results[i][8]) + '  : ' + str(round((sum(results[i][:len(resolution)])/(hardness*len(resolution)))*100)) + '% ' '\n')
            self.sequenceField.configure(state='disabled')
            print(results[i])


if __name__ == "__main__":
    app = App()
    app.mainloop()
