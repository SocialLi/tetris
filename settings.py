import pygame
filename = 'highest_score.txt'

class Settings():

	def __init__(self):
		self.screen_width = 1920
		self.screen_height = 980
		self.screen_bg_color = (230, 230, 230)
		self.display_style = pygame.FULLSCREEN
		self.background = pygame.image.load('images/bg4.jpg')

		self.game_border_width = 3
		self.game_screen_width = 15 * 30
		self.game_screen_height = 25 * 30
		self.game_screen_rect = (678, 148, self.game_screen_width + self.game_border_width * 2 - 2, self.game_screen_height + self.game_border_width * 2 - 2)
		self.game_screen_bgcolor = (50, 10, 200)


		# 下一个方块出现的框
		self.box_image = pygame.image.load('images/box.png')
		self.my_font = pygame.font.SysFont('kaiti', 30, True, True)

		# 得分及其边框
		self.score_text_color = (66, 77, 237)
		self.score_text_rect = (1330, 440)
		self.score_text_border = [(1310, 430), (1490, 430), (1490, 480), (1310, 480)]
		self.score_text_border_color = (200, 250, 0)

		
		
		self.pause_box = pygame.rect.Rect(610, 420, 110, 30)

		self.game_active = True
		self.pause = 1
		self.music_stats = True
		self.draw_line = False
		self.best_score = self.read_hightest_score()

		# 最高分
		self.my_font2 = pygame.font.SysFont('simhei', 35, True, True)
		self.highest_score_image = self.my_font2.render("最高分：{0}".format(self.best_score), True, (63, 65, 204))
		self.highest_score_border = [(338, 198), (576, 198), (576, 271),(338, 271)]

	def read_hightest_score(self):
		with open(filename) as f_obj:
			score = f_obj.read().strip()
		return score

	def storage(self, number):
		with open(filename, 'w') as f_obj:
			f_obj.write(str(number))







	

