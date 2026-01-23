class icantect:
    name = "hugahuga"
    score = {"eng":9,
             "mat":8,
             "his":10.1}
    def score_average(self):
        print(f"{self.name} score average is : {(self.score["eng"] + self.score["mat"] + self.score["his"])/3}")
    def show_rank(self):
        average = (self.score["eng"] + self.score["mat"] + self.score["his"])/3
        if average > 10:
            average = "?"
        elif average >= 9 and average < 10:
            average = "huyen thoai"
        elif average < 9 and average >= 8:
            average = "kim cuong"
        elif average >= 5 and average < 8:
            average = "vang"
        elif average < 5:
            average = "dong"
        print(f"{self.name} have rank is : {average}")
    def show_info(self):
        print(f"name : {self.name}")
        print(f"end : {self.score["eng"]}")
        print(f"mat : {self.score["mat"]}")
        print(f"his : {self.score["his"]}")
studen_info = icantect()
studen_info.score_average()
studen_info.show_info()
studen_info.show_rank()