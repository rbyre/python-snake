from turtle import Turtle
import pickle
import os



FONT = ("Courier", 24, "normal")
highscorefile = './highscore.txt'

class Scoreboard(Turtle):
  def __init__(self):
    self.score = 0
    self.highscore = 0
    super().__init__()
    self.up()
    self.speed("fastest")
    self.hideturtle()
    self.color("white")
    self.goto(-290, 270)
    self.write_score()
    self.fetch_high_score()

  def add_one_point(self):
      self.score += 1
      self.write_score()
    
  def write_score(self):
      self.clear()
      self.goto(-290, 270)
      self.write(f"Score: {self.score}", align='left', font=FONT)
      self.goto(270, 270)
      self.write(f"Highscore: {self.highscore}", align='right', font=FONT)
      
      

  def reset(self):
    if self.score > self.highscore:
      self.highscore = self.score
      data = self.highscore
      file = open('highscore.txt', 'wb')
      pickle.dump(data, file)
      file.close()
    self.score = 0
  
  def fetch_high_score(self):
    isExist = os.path.exists(highscorefile)
    if isExist:
      file = open('highscore.txt', 'rb')
      data = pickle.load(file)
      self.highscore = data
      file.close()


  # def game_over(self):
  #   self.goto(0, 0)
  #   self.write("Game Over!", align=ALIGNMENT, font=FONT)