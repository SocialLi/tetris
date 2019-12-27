import pygame
from settings import Settings
import game_function as gf
from block import *
from button import Buttons

def run_game():
	pygame.init()
	pygame.mixer.init()
	file = 'BGM.mp3'
	track = pygame.mixer.music.load(file)
	pygame.mixer.music.play(loops=50)

	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), ai_settings.display_style, 32)
	buttons = Buttons()
	pygame.display.set_caption("俄罗斯方块")


	while True:
		gf.check_events(ai_settings, buttons)
		gf.is_game_over(ai_settings)
		gf.change_color(buttons)
		if not ai_settings.game_active:
			gf.over_word(ai_settings, screen)
		if ai_settings.game_active:
			gf.update_screen(ai_settings, screen, buttons)
	


run_game()
