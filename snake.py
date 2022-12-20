from turtle import Turtle 


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]
    
  def add_part(self, position):
    name = Turtle('square')
    name.color('white')
    name.up()
    name.goto(position)
    self.segments.append(name)

  def get_snake_parts(self):
    return self.segments

  def create_snake(self):
    for position in STARTING_POSITIONS: 
      # segment_name = 'segment'+'_'+str(index+1)
      self.add_part(position)

  def move_up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def move_down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def move_left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
  
  def move_right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)

  # def add_one_to_snake(self):
  #   self.add_part('_', self.segments[-1].xcor(), self.segments[-1].ycor(), self.segments)

  def move(self):
    for segment in range(len(self.segments)-1, 0, -1):
        if segment > 0:
          new_position = self.segments[segment - 1].position()
          self.segments[segment].goto(new_position)
      
    self.head.forward(MOVE_DISTANCE)


