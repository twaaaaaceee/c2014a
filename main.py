import random


class Student:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True

    def to_study(self):
            print("time to study")
            self.progress+=0.12
            self.gladness-=3
    def to_sleep(self):
            print("i will sleep")
            self.progress+=3
    def to_chill(self):
            print("Rest time")
            self.progress-=0.1
            self.gladness+=5
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
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")

    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
    live.cube=random.randint(1,3)
    if live.cube==1
         self.to.study()
    elif live_cube==2
            self.to.sleep()
    elif live_cube==3
        self.to.chill()
    self.end.of.day






