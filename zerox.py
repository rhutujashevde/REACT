from gpiozero import Button, LEDBoard
import time
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

button1 = Button(14)
button2 = Button(15)
button3 = Button(18)
button4 = Button(23)
button5 = Button(24)
leds = LEDBoard(17,27,22,10,9)

engine = create_engine('sqlite:///mcqs.sqlite')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Mcqs(Base):
    __tablename__ = 'Mcqs'

    id = Column(Integer, primary_key = True)
    question = Column(String(250), nullable = False)
    a = Column(String(250), nullable = False)
    b = Column(String(250), nullable = False)
    c = Column(String(250), nullable = False)
    d = Column(String(250), nullable = False)
    answer = Column(String(1), nullable = False)
    answer_name = Column(String(250), nullable = False)

leds.on()
print("welcome")
time.sleep(2)
leds.off()
ans = "no"
while True:
    if button1.is_pressed:
        ans = "yes"
        mcqid = random.randint(1,5)
        mcq = session.query(Mcqs).filter_by(id=mcqid).first()
        print(mcq.question)
        print("a.",mcq.a)
        print("b.",mcq.b)
        print("c.",mcq.c)
        print("d.",mcq.d)
        time.sleep(1)
    if ans == "yes":
        if button2.is_pressed:
            ans = "a"
            time.sleep(1)
        elif button3.is_pressed:
            ans = "b"
            time.sleep(1)
        elif button4.is_pressed:
            ans = "c"
            time.sleep(1)
        elif button5.is_pressed:
            ans = "d"
            time.sleep(1)
    if ans != "yes" and ans != "no": 
        if ans == mcq.answer:
            print("Yay!! Correct Answer!!")
            ans = "no"
        else:
        	ans = "no"
            print("Wrong Answer!!The correct answer is",mcq.answer+".",mcq.answer_name)	

Base.metadata.create_all(engine)

