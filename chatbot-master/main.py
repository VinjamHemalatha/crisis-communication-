from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")

conversation = {
    'hello',
    'hi',
    'what is your name?',
    'My name is chatbox',
    'Can You Speak in English',
    'yes'
    'What is the new virus revolving all over the world?'
    'Corona Virus',
    'what is corona Virus?',
    'Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.',
    'what are the Symtoms of corona virus?',
    'Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.',
    'what are the preventive measures of corona?',
    'The best way to prevent and slow down transmission is be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face ',
    'how do this virus spread?',
    'The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette ',
    'how the infection is prevented',
    'To prevent infection and to slow transmission of COVID-19, do the following Wash your hands regularly with soap and water, or clean them with alcohol-based hand rub. Maintain at least 1 metre distance between you and people coughing or sneezing. Avoid touching your face. Cover your mouth and nose when coughing or sneezing. Stay home if you feel unwell. Refrain from smoking and other activities that weaken the lungs. Practice physical distancing by avoiding unnecessary travel and staying away from large groups of people. ',
    'what is the present situation of the world due to corona virus?',
    'The situation is getting worst and worst day by day.'
}

trainer = ListTrainer(bot)


trainer.train(conversation)

main = Tk()

main.geometry("500x650")

main.title("crisis communication chatbox")


def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=35, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()


textF = Entry(main, font=("Verdana", 10))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 15), command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()


main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()
