import pygame

class Buttons():

	def __init__(self):
		self.my_font = pygame.font.SysFont('simhei', 20, True, True)
		# 重新开始按钮
		self.restart_button = pygame.rect.Rect(400, 300, 130, 40)
		self.restart_bg_color = (150, 10, 200)
		self.restart_image = self.my_font.render("重新开始", True, (255, 255, 250))
		self.restart_image_rect = self.restart_image.get_rect()
		self.restart_image_rect.x = 417
		self.restart_image_rect.y = 310
		self.restart_border = [(398, 299), (530, 299), (530, 340),(398, 340)]
		self.color1 = 255
		self.color2 = 0
		self.color3 = 0

		# 暂停音乐按钮
		self.pause_button = pygame.rect.Rect(400, 370, 130, 40)
		self.pause_bg_color = (50, 100, 150)
		self.pause_image = self.my_font.render("暂停音乐", True, (255, 255, 250))
		self.go_on_image = self.my_font.render("继续音乐", True, (255, 255, 250))
		self.pause_border = [(398, 368), (530, 368), (530, 411),(398, 411)]

		# 画线按钮
		self.lines_button = pygame.rect.Rect(400, 440, 130, 40)
		self.lines_button_bg_color = (50, 100, 150)
		self.lines_button_image1 = self.my_font.render("显示格子", True, (255, 255, 250))
		self.lines_button_image2 = self.my_font.render("隐藏格子", True, (255, 255, 250))
		self.lines_border = [(398, 438), (530, 438), (530, 481),(398, 481)]

		# 暂停
		self.suspended_button = pygame.rect.Rect(420, 510, 90, 40)
		self.suspended_bg_color = (50, 100, 150)
		self.suspended_image1 = self.my_font.render("暂停", True, (255, 255, 250))
		self.suspended_image2 = self.my_font.render("继续", True, (255, 255, 250))
		self.suspended_border = [(418, 509), (511, 509), (511, 551),(418, 551)]

 