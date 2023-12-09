import random


class Student:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.money=100
        self.alive=True


    def to_working(self):
        print("time go to job")
        self.progress+=0.5
        self.gladness-=1.5
        self.money+=50
    def to_study(self):
            print("time to study")
            self.progress+=0.12
            self.gladness-=3
            self.money-=10
    def to_sleep(self):
            print("i will sleep")
            self.progress+=3
            self.gladness+=2
            self.money+=0
    def to_chill(self):
            print("Rest time")
            self.progress-=0.1
            self.gladness+=5
            self.money-=50
    def is_alive(self):
        if self.progress<=0.5:
            print("Cast out")
            self.alive=False
        elif self.gladness>=0:
            print("Depresion . .")
            self.alive=False
        elif self.progress>5:
            print("Passed externaly")
            self.alive=False
        elif self.money>=0:
            print("will be kicked from the house")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")

    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live.cube=random.randint(1,3)
        if live.cube==1:
            self.to.study()
        elif live_cube==2:
            self.to.sleep()
        elif live_cube==3:
            self.to.chill()
        elif live_cube==4:
            self.to.working()
        self.end_of_day()
        self.is_alive()
nick=Student(name="Nick")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)







