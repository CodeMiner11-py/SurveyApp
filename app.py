# import tkinter module. This will be used for graphical interface.
from tkinter import *
# we will import everything from tkinter
import pickle
# this will be used for serialization
# create a Tk instance
page1 = Tk()
page1.title("My Survey App")
# now we will test if any results have been put in yet
try:
    # try to open answers file
    storage = open("s_answers.me", "rb")
    first_time = False # if it passes it is not the first time
except:
    first_time = True # else it is first time
if not first_time:
    s_list = pickle.load(storage) # if not we will deserialize the list
    storage.close()
else:
    s_list = list() # if not create an empty list.
def __repr__(self):
    return """
This is a SurveyData class instance.
This is an object to store and make changes to a list.
That list holds dictionaries containing results.
"""
# create a __repr__ function to return stuff about this object
def values(mydict):
    try:
        return list(mydict.values())
    except:
        return False
    # function to return values of a dict

    
# create a class to store our list.
class SurveyData:
    def __init__(self, list_id):
        self.id = list_id
        # set self.id to given list
        self.state = 'take/show'
        self.avgs = [None, None, None, None, None, None]
    def add(self, health, wellness, treatment, money, condition, simplification):
        # create func to add data to list
        add_dict = {}
        works = True # so far it works
        # add given values to dict
        # try to see if it works
        try:
            health = int(health)
        except:
            works = False
        try:
            wellness = int(wellness)
        except:
            works = False
        try:
            treatment = int(treatment)
        except:
            works = False
        try:
            money = int(money)
        except:
            works = False
        try:
            condition = int(condition)
        except:
            works = False
        try:
            simplification = int(simplification)
        except:
            works = False
        if works:
            for i in [health, wellness, treatment, money, condition, simplification]:
                if i > 100:
                    works = False
        if works: # if works
            add_dict["Health"] = int(health)
            add_dict["Wellness"] = int(wellness)
            add_dict["Treatment"] = int(treatment)
            add_dict["Money"] = int(money)
            add_dict["How Things Are Going"] = int(condition)
            add_dict["Earth Ratings"] = int(simplification)
            self.add_dict = add_dict
            # append dict to list
            self.id.append(add_dict)
        return works
    def compile_percent(self):
        # set average values to in-the-middle right now
        (h_avg, w_avg, t_avg, m_avg, c_avg, s_avg) = (0, 0, 0, 0, 0, 0)
        counter = 0 # 0 surveys so far
        for survey in self.id:
            counter += 1 # add 1 survey
            sv = values(survey) # these are values
            h_avg += sv[0] # add all the values
            w_avg += sv[1]
            t_avg += sv[2]
            m_avg += sv[3]
            c_avg += sv[4]
            s_avg += sv[5]
        try:
            h_avg /= counter # when done divide by num of surveys to get avg
            w_avg /= counter
            t_avg /= counter
            m_avg /= counter
            c_avg /= counter
            s_avg /= counter
        except:
            (h_avg, w_avg, t_avg, m_avg, c_avg, s_avg) = (0, 0, 0, 0, 0, 0)
        avg_list = [h_avg, w_avg, t_avg, m_avg, c_avg, s_avg]
        self.avgs = avg_list
        return self.avgs
    def take(self, nextfunc):
        def press():
            if SURVEYWORKS:
                warninglabel.pack(pady=10)
                warninglabel.destroy()
                h = hEntry.get()
                w = wEntry.get()
                t = tEntry.get()
                m = mEntry.get()
                c = cEntry.get()
                s = sEntry.get()
                self.add(h, w, t, m, c, s)
                surveypage.destroy()
                nextfunc()
            else:
                warninglabel.pack(pady=10)
                warninglabel.config(fg='#F00')
        def check_text():
            global entry, counter, SURVEYWORKS
            h = hEntry.get()
            w = wEntry.get()
            t = tEntry.get()
            m = mEntry.get()
            c = cEntry.get()
            s = sEntry.get()
            entries = [h, w, t, m, c, s]
            counter = 0
            for entry in entries:
                works = True
                try:
                    entry = int(entry)
                    works = True
                except:
                    works = False
                if entry == '':
                    works = None
                if not entry == '' and works:
                    if int(entry) > 100 or int(entry) < 0:
                        works = False
                if works == False:
                    if counter == 0:
                        hlabel.config(fg='#F00')
                    elif counter == 1:
                        wlabel.config(fg='#F00')
                    elif counter == 2:
                        tlabel.config(fg='#F00')
                    elif counter == 3:
                        mlabel.config(fg='#F00')
                    elif counter == 4:
                        clabel.config(fg='#F00')
                    else:
                        slabel.config(fg='#F00')
                elif works == True:
                    if counter == 0:
                        hlabel.config(fg='#0F0')
                    elif counter == 1:
                        wlabel.config(fg='#0F0')
                    elif counter == 2:
                        tlabel.config(fg='#0F0')
                    elif counter == 3:
                        mlabel.config(fg='#0F0')
                    elif counter == 4:
                        clabel.config(fg='#0F0')
                    else:
                        slabel.config(fg='#0F0')
                else:
                    if counter == 0:
                        hlabel.config(fg='#FFF')
                    elif counter == 1:
                        wlabel.config(fg='#FFF')
                    elif counter == 2:
                        tlabel.config(fg='#FFF')
                    elif counter == 3:
                        mlabel.config(fg='#FFF')
                    elif counter == 4:
                        clabel.config(fg='#FFF')
                    else:
                        slabel.config(fg='#FFF')
                counter += 1
            SURVEYWORKS = works
            surveypage.after(50, check_text)
        surveypage = Tk()
        surveypage.title("Taking the Survey")
        t1label = Label(surveypage, text="Answer the questions with a number from 1 to 100.\nMake sure all questions are green.")
        t1label.pack()
        
        label = Label(surveypage, text="_______________________________________________________")
        label.pack()
        hlabel = Label(surveypage, text="Do you like your state of health?")
        hlabel.pack(pady=15)
        hEntry = Entry(surveypage, width=10)
        hEntry.pack()
        
        wlabel = Label(surveypage, text="Are you happy?")
        wlabel.pack(pady=15)
        wEntry = Entry(surveypage, width=10)
        wEntry.pack()
        
        tlabel = Label(surveypage, text="Do you like how people treat you?")
        tlabel.pack(pady=15)
        tEntry = Entry(surveypage, width=10)
        tEntry.pack()
        
        mlabel = Label(surveypage, text="Do you have a decent amount of money?")
        mlabel.pack(pady=15)
        mEntry = Entry(surveypage, width=10)
        mEntry.pack()
        
        clabel = Label(surveypage, text="Do you like how things are going for you?")
        clabel.pack(pady=15)
        cEntry = Entry(surveypage, width=10)
        cEntry.pack()
        
        slabel = Label(surveypage, text="Are you happy about the Earth?")
        slabel.pack(pady=15)
        sEntry = Entry(surveypage, width=10)
        sEntry.pack()
        
        warninglabel = Label(surveypage, text='Please fix white/red entries.')

        # finishing button
        fButton = Button(surveypage, text="Finish Survey", command=press)
        fButton.pack(pady=20)

        check_text()

    def showresults(self, nextfunc):
        self.compile_percent()
        def press(): # if done button pressed
            repage.destroy()
            nextfunc()

        repage = Tk()
        repage.title("Result Averages") # create Tk

        line1 = Label(repage, text="____________________________________")
        # creates a line atop the page
        line1.pack()

        labels = [] # create labels and texts
        t0 = 'Average for Health: '
        t1 = 'Average for Wellness: '
        t2 = 'Average for Treatment: '
        t3 = 'Average for Money: '
        t4 = 'Average for How Things are Going: ' 
        t5 = 'Average for Earth Ratings: '
        t0 = t0 + str(int(self.avgs[0])) + '%'
        t1 = t1 + str(int(self.avgs[1])) + '%'
        t2 = t2 + str(int(self.avgs[2])) + '%'
        t3 = t3 + str(int(self.avgs[3])) + '%'
        t4 = t4 + str(int(self.avgs[4])) + '%'
        t5 = t5 +  str(int(self.avgs[5])) + '%'
        
        # now each text is complete
        texts = [t0, t1, t2, t3, t4, t5]
        for i in list(range(0, 6, 1)):
            l = Label(repage, text=texts[i])
            l.config(anchor='w', padx=0)
            l.pack(pady=15)
            labels.append(l)


        fButton = Button(repage, text="Done", command=press)
        fButton.pack()
        
        line2 = Label(repage, text="____________________________________")
        # creates a line below the page
        line2.pack(pady=15)
        
# set our __repr__ function to SurveyData __repr__
SurveyData.__repr__ = __repr__
survey = SurveyData(s_list)
survey.compile_percent()
def results():
    page1.withdraw()
    survey.showresults(page1.deiconify)
    
def savefinish():
    newwrite = open('s_answers.eshaan', 'wb')
    serial_code = pickle.dumps(s_list)
    newwrite.write(serial_code)
    page1.destroy()
    print('Thank you for using Eshaan\'s Survey App')
    print('Your data was saved to the file. When you open the app again, your data will be there.')

def finishreset():
    import os
    if os.path.exists("s_answers.eshaan"):
      os.remove("s_answers.eshaan")
    page1.destroy()
    print('Thank you for using Eshaan\'s Survey App')
    print('Your data was lost. Restart the app to create new data.')
    
def take():
    page1.withdraw()
    survey.take(page1.deiconify)
# buttons for survey mainpage
take_survey = Button(page1, text="Take Survey!", command=take)
show_results = Button(page1, text="Show Results", command=results)
save = Button(page1, text="Save and Finish", command=savefinish)
quitter = Button(page1, text='Finish and Reset', command=finishreset)
mylabel = Label(page1, text="Welcome to Eshaan's Survey App!")
mylabel.pack(pady=10)
line = Label(page1, text="______________________________________")
line.pack(pady=0)
take_survey.pack(pady=15)
show_results.pack(pady=15)
save.pack(pady=15)
quitter.pack(pady=15)
