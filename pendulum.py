import pygame
import math

class Pendulum:
	def __init__(self, x, y, radius, friction):
		self.origin = pygame.Vector2(x, y)
		self.postion = pygame.Vector2(0, 0)
		
		self.radius = radius
		
		self.rads = math.radians(45)
		
		self.gravity = 10
		self.friction = friction
		
		self.angular_velocity = 0.0
		self.angular_acceleration = 0.0
		
	
	def update(self):
		self.angular_acceleration = -1 * self.gravity * math.sin(self.rads) / self.radius
		self.angular_velocity += self.angular_acceleration
		self.rads += math.radians(self.angular_velocity)
		self.rads *= self.friction
		
		self.position = pygame.Vector2(
			self.radius * math.sin(self.rads),
			self.radius * math.cos(self.rads))
		self.position += self.origin
	
	def draw(self, surface):
		pygame.draw.line(surface, 'white', self.origin, self.position, 2)
		pygame.draw.circle(surface, 'white', self.position, 20)