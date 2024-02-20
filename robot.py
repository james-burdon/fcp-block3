import math
class Robot:
	
	def __init__(self, initial_x_position, initial_y_position, initial_x_velocity, initial_y_velocity):
		self.x = initial_x_position
		self.y = initial_y_position
		self.velocity_x = initial_x_velocity
		self.velocity_y = initial_y_velocity
	
	def move(self):
		self.x += self.velocity_x
		self.y += self.velocity_y

	def accelerate(self,x_acceleration,y_acceleration):
		self.velocity_x+=x_acceleration
		self.velocity_y+=y_acceleration

robot1 = Robot(0, 0, 1, 0)
robot2 = Robot(0, 1, 1, 0)
robot3 = Robot(1, 1, 1, 0)
robot1.accelerate(4,4)
print(robot1.velocity_x,robot1.velocity_y)
