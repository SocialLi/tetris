import random
import sys
import pygame
from block import *

ai_block = Block()

def update_screen(ai_settings, screen, buttons):
	screen.blit(ai_settings.background, (0, 0))
	pygame.draw.rect(screen, ai_settings.game_screen_bgcolor, ai_settings.game_screen_rect, ai_settings.game_border_width)
	show_button(ai_settings, screen, buttons)
	show_next_block(ai_settings, screen)
	draw_score(ai_settings, screen)
	draw_block1(screen)
	draw_lines(ai_settings, screen, buttons)
	draw_block2(screen)
	if ai_settings.pause == 1:
		move_down()

	pygame.display.flip()

# 绘制得分及其边框
def draw_score(ai_settings, screen):
	text = ai_settings.my_font.render("得分：{0}".format(ai_block.score), True, ai_settings.score_text_color)
	screen.blit(text, ai_settings.score_text_rect)
	pygame.draw.lines(screen, ai_settings.score_text_border_color, True, ai_settings.score_text_border, 4)


def show_next_block(ai_settings, screen):
	screen.blit(ai_settings.box_image, (1230, 150))
	i = 0
	for rec in ai_block.next_block.recs:
		next_rec = [rec[0] + 480, rec[1] + 80, 30, 30]
		pygame.draw.rect(screen, ai_block.next_color[i], next_rec)
		i += 1

def show_button(ai_settings, screen, buttons):
	# 重新开始
	screen.fill(buttons.restart_bg_color, buttons.restart_button)
	screen.blit(buttons.restart_image, buttons.restart_image_rect)
	pygame.draw.lines(screen, (buttons.color1, buttons.color2, buttons.color3), True, buttons.restart_border, 3)

	# 暂停音乐
	screen.fill(buttons.pause_bg_color, buttons.pause_button)
	if ai_settings.music_stats:
		screen.blit(buttons.pause_image, (419, 380))
	else:
		screen.blit(buttons.go_on_image, (419, 380))
	pygame.draw.lines(screen, (buttons.color1, buttons.color2, buttons.color3), True, buttons.pause_border, 3)

	# 最高分
	screen.blit(ai_settings.highest_score_image, (360, 217))
	pygame.draw.lines(screen, (buttons.color1, buttons.color2, buttons.color3), True, ai_settings.highest_score_border, 3)

	# 显示格子
	screen.fill(buttons.lines_button_bg_color, buttons.lines_button)
	if ai_settings.draw_line:
		screen.blit(buttons.lines_button_image2, (419, 450))
	else:
		screen.blit(buttons.lines_button_image1, (419, 450))
	pygame.draw.lines(screen, (buttons.color1, buttons.color2, buttons.color3), True, buttons.lines_border, 3)

	# 暂停游戏
	screen.fill(buttons.suspended_bg_color, buttons.suspended_button)
	if ai_settings.pause == 1:
		screen.blit(buttons.suspended_image1, (440, 520))
	else:
		screen.blit(buttons.suspended_image2, (440, 520))
	pygame.draw.lines(screen, (buttons.color1, buttons.color2, buttons.color3), True, (buttons.suspended_border), 3)

def change_color(buttons):
	if buttons.color3 == 255 and buttons.color2 == 0:
		if buttons.color1 < 255:
			buttons.color1 += 3
		else:
			self.buttons.color1 = 255
	elif buttons.color3 == 0 and buttons.color2 == 255:
		if buttons.color1 > 0:
			buttons.color1 -= 3
		else:
			buttons.color1 = 0
	# G
	if buttons.color1 == 255 and buttons.color3 == 0:
		if buttons.color2 < 255:
			buttons.color2 += 3
		else:
			buttons.color2 = 255
	elif buttons.color1 == 0 and buttons.color3 == 255:
		if buttons.color2 > 0:
			buttons.color2 -= 3
		else:
			buttons.color2 = 0
	# B
	if buttons.color1 == 0 and buttons.color2 == 255:
		if buttons.color3 < 255:
			buttons.color3 += 3
		else:
			buttons.color3 = 255
	elif buttons.color1 == 255 and buttons.color2 == 0:
		if buttons.color3 > 0:
			buttons.color3 -= 3
		else:
			buttons.color3 = 0


def check_events(ai_settings, buttons):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
			elif event.key == pygame.K_LEFT and ai_settings.pause == 1:
				transverse(1)
			elif event.key == pygame.K_RIGHT and ai_settings.pause == 1:
				transverse(2)
			elif event.key == pygame.K_UP and ai_settings.pause == 1:
				change()
			elif event.key == pygame.K_DOWN and ai_settings.pause == 1:
				fast_down()
			elif event.key == pygame.K_SPACE:
				ai_settings.pause *= -1 
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_mouse(mouse_x, mouse_y, ai_settings, buttons)


def move_down():
	for fixed_rect in ai_block.fixed_block:
		for x in ai_block.now_block.recs:
			next_x = [x[0], x[1] + 3, 30, 30]
			if pygame.rect.Rect(next_x).colliderect(fixed_rect):
				fix()
				return
	for x in ai_block.now_block.recs:
		x[1] += 3	
			

def draw_block1(screen):
	for rec in ai_block.accumulate_list:
		pygame.draw.rect(screen, rec[1], rec[0])
	

def draw_block2(screen):
	i = 0
	for rec in ai_block.now_block.recs:
		pygame.draw.rect(screen, ai_block.now_color[i], rec)
		i += 1



def fix():
	i = 0
	for rect in ai_block.now_block.recs:
		ai_block.fixed_block.append(rect)
		ai_block.accumulate_list.append([rect, ai_block.now_color[i]])
		i += 1
	lis = [int(ai_block.now_block.recs[0][1]), int(ai_block.now_block.recs[1][1]), int(ai_block.now_block.recs[2][1]), int(ai_block.now_block.recs[3][1])]
	li = []
	for y in lis:
		if y not in li:
			li.append(y)
	eliminate(li)
	ai_block.change_record = 0
	ai_block.creat_block()
	

def transverse(number):
	if number == 1:
		for x in ai_block.now_block.recs:
			for rec in ai_block.fixed_block:
				next_x = [x[0] - 30, x[1], 30, 30]
				if pygame.rect.Rect(next_x).colliderect(rec) or next_x[0] < 680:
					return
		for x in ai_block.now_block.recs:
				x[0] -= 30
	else:
		for x in ai_block.now_block.recs:
			for rec in ai_block.fixed_block:
				next_x = [x[0] + 30, x[1], 30, 30]
				if pygame.rect.Rect(next_x).colliderect(rec) or next_x[0] > 1100:
					return
		for x in ai_block.now_block.recs:
			x[0] += 30


def eliminate(lis):
	for y in lis:
		count = 0
		for rec in ai_block.accumulate_list:
			if int(rec[0][1]) == y:
				count += 1
		if count == 15:
			temp1 = []
			for rec in ai_block.accumulate_list:
				if int(rec[0][1]) != y:
					temp1.append(rec)
			ai_block.accumulate_list = temp1
			temp2 = []
			for rec in ai_block.fixed_block:
				if int(rec[1]) != y:
					temp2.append(rec)
			ai_block.fixed_block = temp2
			
			for rec in ai_block.accumulate_list:
				if int(rec[0][1]) < y:
					rec[0][1] += 30
			lis.append(y)
			ai_block.score += 10
			

def fast_down():
	down_lis = []
	for rec in ai_block.now_block.recs:
		if rec[0] not in down_lis:
			down_lis.append(rec[0])
	fixed_lis = []
	for rec in ai_block.fixed_block:
		if rec[0] in down_lis:
			fixed_lis.append(rec)
	fixed_lis.sort(key=lambda x: x[1])
	flag = 1
	while flag:
		for rec in fixed_lis:
			for x in ai_block.now_block.recs:
				next_x = [x[0], x[1] + 3, 30, 30]
				if pygame.rect.Rect(next_x).colliderect(rec):
					flag = 0
					break
			if not flag:
				break
		if flag:
			for x in ai_block.now_block.recs:
				x[1] += 3


def is_game_over(ai_settings):
	for rec in ai_block.accumulate_list:
		if rec[0][1] <= 150:
			ai_settings.game_active = False
			if ai_block.score > int(ai_settings.best_score):
				ai_settings.storage(ai_block.score)
			return


def over_word(ai_settings, screen):
	text1 = ai_settings.my_font.render("Game Over!", True, (63, 204, 101))
	text2 = ai_settings.my_font.render("最终得分：{0}".format(ai_block.score), True, (63, 204, 101))
	text1_rect = text1.get_rect()
	text2_rect = text2.get_rect()
	screen_rect = screen.get_rect()
	text2_rect.centerx = text1_rect.centerx = screen_rect.centerx - 40
	text1_rect.centery = screen_rect.centery - 25
	text2_rect.centery = screen_rect.centery + 25
	screen.blit(text1, text1_rect)
	screen.blit(text2, text2_rect)
	pygame.display.flip()


def check_mouse(mouse_x, mouse_y, ai_settings, buttons):
	if buttons.restart_button.collidepoint(mouse_x, mouse_y):
		ai_settings.__init__()
		ai_block.__init__()
	elif buttons.pause_button.collidepoint(mouse_x, mouse_y):
		if ai_settings.music_stats:
			pygame.mixer.music.pause()
			ai_settings.music_stats = False
		else:
			pygame.mixer.music.unpause()
			ai_settings.music_stats = True
	elif buttons.lines_button.collidepoint(mouse_x, mouse_y):
		if ai_settings.draw_line == False:
			ai_settings.draw_line = True
		else:
			ai_settings.draw_line = False
	elif buttons.suspended_button.collidepoint(mouse_x, mouse_y):
		ai_settings.pause *= -1

def draw_lines(ai_settings, screen, buttons):
	if ai_settings.draw_line:
		for x in range(14):
			pygame.draw.line(screen, (buttons.color1, buttons.color2, buttons.color3), (709 + x * 30, 150), (709 + x * 30, 900), 1)
		for y in range(24):
			pygame.draw.line(screen, (buttons.color1, buttons.color2, buttons.color3), (680, 180 + y * 30), (1129, 180 + y * 30), 1)


def change():
	if isinstance(ai_block.now_block, Tblock):
		if ai_block.change_record == 0:
			next_x = [ai_block.now_block.recs[1][0] + 30, ai_block.now_block.recs[1][1] + 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x).colliderect(rec):
					return
			ai_block.now_block.recs[1][0] += 30
			ai_block.now_block.recs[1][1] += 30
			ai_block.change_record = 1

		elif ai_block.change_record == 1:
			next_x = [ai_block.now_block.recs[0][0] - 30, ai_block.now_block.recs[0][1] + 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x).colliderect(rec) or next_x[0] > 1130:
					return
			ai_block.now_block.recs[0][0] -= 30
			ai_block.now_block.recs[0][1] += 30
			ai_block.change_record = 2

		elif ai_block.change_record == 2:
			next_x = [ai_block.now_block.recs[3][0] - 30, ai_block.now_block.recs[3][1] - 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x).colliderect(rec):
					return
			ai_block.now_block.recs[3][0] -= 30
			ai_block.now_block.recs[3][1] -= 30
			ai_block.change_record = 3

		else:
			next_x = [ai_block.now_block.recs[1][0] + 30, ai_block.now_block.recs[1][1] - 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x).colliderect(rec) or next_x[0] < 680:
					return
			ai_block.now_block.recs[0][0] += 30
			ai_block.now_block.recs[0][1] -= 30
			ai_block.now_block.recs[1][0] -= 30
			ai_block.now_block.recs[1][1] -= 30
			ai_block.now_block.recs[3][0] += 30
			ai_block.now_block.recs[3][1] += 30
			ai_block.change_record = 0

	elif isinstance(ai_block.now_block, Iblock):
		if ai_block.change_record == 0:
			next_x1 = [ai_block.now_block.recs[0][0] - 30, ai_block.now_block.recs[0][1] + 30, 30, 30]
			next_x2 = [ai_block.now_block.recs[2][0] + 30, ai_block.now_block.recs[2][1] - 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] + 60, ai_block.now_block.recs[3][1] - 60, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec) or next_x1[0] < 680 or next_x3[0] > 1100:
					return
			ai_block.now_block.recs[0][0] -= 30
			ai_block.now_block.recs[0][1] += 30
			ai_block.now_block.recs[2][0] += 30
			ai_block.now_block.recs[2][1] -= 30
			ai_block.now_block.recs[3][0] += 60
			ai_block.now_block.recs[3][1] -= 60
			ai_block.change_record = 1
		else:
			next_x1 = [ai_block.now_block.recs[0][0] + 30, ai_block.now_block.recs[0][1] - 30, 30, 30]
			next_x2 = [ai_block.now_block.recs[2][0] - 30, ai_block.now_block.recs[2][1] + 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] - 60, ai_block.now_block.recs[3][1] + 60, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec):
					return
			ai_block.now_block.recs[0][0] += 30
			ai_block.now_block.recs[0][1] -= 30
			ai_block.now_block.recs[2][0] -= 30
			ai_block.now_block.recs[2][1] += 30
			ai_block.now_block.recs[3][0] -= 60
			ai_block.now_block.recs[3][1] += 60
			ai_block.change_record = 0

	elif isinstance(ai_block.now_block, LLblock):
		if ai_block.change_record == 0:
			next_x1 = [ai_block.now_block.recs[0][0] + 60, ai_block.now_block.recs[0][1], 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] + 30, ai_block.now_block.recs[1][1] - 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] - 30, ai_block.now_block.recs[3][1] + 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec):
					return
			ai_block.now_block.recs[0][0] += 60
			ai_block.now_block.recs[1][0] += 30
			ai_block.now_block.recs[1][1] -= 30
			ai_block.now_block.recs[3][0] -= 30
			ai_block.now_block.recs[3][1] += 30
			ai_block.change_record = 1

		elif ai_block.change_record == 1:
			next_x1 = [ai_block.now_block.recs[0][0], ai_block.now_block.recs[0][1] + 60, 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] + 30, ai_block.now_block.recs[1][1] + 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] - 30, ai_block.now_block.recs[3][1] - 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec) or next_x3[0] < 680:
					return
			ai_block.now_block.recs[0][1] += 60
			ai_block.now_block.recs[1][0] += 30
			ai_block.now_block.recs[1][1] += 30
			ai_block.now_block.recs[3][0] -= 30
			ai_block.now_block.recs[3][1] -= 30
			ai_block.change_record = 2

		elif ai_block.change_record == 2:
			next_x1 = [ai_block.now_block.recs[0][0] - 60, ai_block.now_block.recs[0][1], 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] - 30, ai_block.now_block.recs[1][1] + 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] + 30, ai_block.now_block.recs[3][1] - 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec):
					return
			ai_block.now_block.recs[0][0] -= 60
			ai_block.now_block.recs[1][0] -= 30
			ai_block.now_block.recs[1][1] += 30
			ai_block.now_block.recs[3][0] += 30
			ai_block.now_block.recs[3][1] -= 30
			ai_block.change_record = 3

		else:
			next_x1 = [ai_block.now_block.recs[0][0], ai_block.now_block.recs[0][1] - 60, 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] - 30, ai_block.now_block.recs[1][1] - 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] + 30, ai_block.now_block.recs[3][1] + 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec) or next_x3[0] > 1100:
					return
			ai_block.now_block.recs[0][1] -= 60
			ai_block.now_block.recs[1][0] -= 30
			ai_block.now_block.recs[1][1] -= 30
			ai_block.now_block.recs[3][0] += 30
			ai_block.now_block.recs[3][1] += 30
			ai_block.change_record = 0

	elif isinstance(ai_block.now_block, LRblock):
		if ai_block.change_record == 0:
			next_x1 = [ai_block.now_block.recs[0][0], ai_block.now_block.recs[0][1] + 60, 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] - 30, ai_block.now_block.recs[1][1] + 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] + 30, ai_block.now_block.recs[3][1] - 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec):
					return
			ai_block.now_block.recs[0][1] += 60
			ai_block.now_block.recs[1][0] -= 30
			ai_block.now_block.recs[1][1] += 30
			ai_block.now_block.recs[3][0] += 30
			ai_block.now_block.recs[3][1] -= 30
			ai_block.change_record = 1

		elif ai_block.change_record == 1:
			next_x1 = [ai_block.now_block.recs[0][0] - 60, ai_block.now_block.recs[0][1], 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] - 30, ai_block.now_block.recs[1][1] - 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] + 30, ai_block.now_block.recs[3][1] + 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec) or next_x1[0] < 680:
					return
			ai_block.now_block.recs[0][0] -= 60
			ai_block.now_block.recs[1][0] -= 30
			ai_block.now_block.recs[1][1] -= 30
			ai_block.now_block.recs[3][0] += 30
			ai_block.now_block.recs[3][1] += 30
			ai_block.change_record = 2

		elif ai_block.change_record == 2:
			next_x1 = [ai_block.now_block.recs[0][0], ai_block.now_block.recs[0][1] - 60, 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] + 30, ai_block.now_block.recs[1][1] - 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] - 30, ai_block.now_block.recs[3][1] + 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec):
					return
			ai_block.now_block.recs[0][1] -= 60
			ai_block.now_block.recs[1][0] += 30
			ai_block.now_block.recs[1][1] -= 30
			ai_block.now_block.recs[3][0] -= 30
			ai_block.now_block.recs[3][1] += 30
			ai_block.change_record = 3

		else:
			next_x1 = [ai_block.now_block.recs[0][0] + 60, ai_block.now_block.recs[0][1], 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] + 30, ai_block.now_block.recs[1][1] + 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] - 30, ai_block.now_block.recs[3][1] - 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec) or next_x1[0] > 1100:
					return
			ai_block.now_block.recs[0][0] += 60
			ai_block.now_block.recs[1][0] += 30
			ai_block.now_block.recs[1][1] += 30
			ai_block.now_block.recs[3][0] -= 30
			ai_block.now_block.recs[3][1] -= 30
			ai_block.change_record = 0

	elif isinstance(ai_block.now_block, ZLblock):
		if ai_block.change_record == 0:
			next_x1 = [ai_block.now_block.recs[0][0], ai_block.now_block.recs[0][1] + 60, 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] + 30, ai_block.now_block.recs[1][1] + 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] + 30, ai_block.now_block.recs[3][1] - 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec):
					return
			ai_block.now_block.recs[0][1] += 60
			ai_block.now_block.recs[1][0] += 30
			ai_block.now_block.recs[1][1] += 30
			ai_block.now_block.recs[3][0] += 30
			ai_block.now_block.recs[3][1] -= 30
			ai_block.change_record = 1

		else:
			next_x1 = [ai_block.now_block.recs[0][0] - 60, ai_block.now_block.recs[0][1], 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] - 30, ai_block.now_block.recs[1][1] + 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] + 30, ai_block.now_block.recs[3][1] + 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec) or next_x1[0] < 680:
					return
			ai_block.now_block.recs[0][1] -= 60
			ai_block.now_block.recs[1][0] -= 30
			ai_block.now_block.recs[1][1] -= 30
			ai_block.now_block.recs[3][0] -= 30
			ai_block.now_block.recs[3][1] += 30
			ai_block.change_record = 0

	elif isinstance(ai_block.now_block, ZRblock):
		if ai_block.change_record == 0:
			next_x1 = [ai_block.now_block.recs[0][0] + 60, ai_block.now_block.recs[0][1], 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] + 30, ai_block.now_block.recs[1][1] + 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] - 30, ai_block.now_block.recs[3][1] + 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec):
					return
			ai_block.now_block.recs[0][0] += 60
			ai_block.now_block.recs[1][0] += 30
			ai_block.now_block.recs[1][1] += 30
			ai_block.now_block.recs[3][0] -= 30
			ai_block.now_block.recs[3][1] += 30
			ai_block.change_record = 1

		else:
			next_x1 = [ai_block.now_block.recs[0][0], ai_block.now_block.recs[0][1] + 60, 30, 30]
			next_x2 = [ai_block.now_block.recs[1][0] - 30, ai_block.now_block.recs[1][1] + 30, 30, 30]
			next_x3 = [ai_block.now_block.recs[3][0] - 30, ai_block.now_block.recs[3][1] - 30, 30, 30]
			for rec in ai_block.fixed_block:
				if pygame.rect.Rect(next_x1).colliderect(rec) or pygame.rect.Rect(next_x2).colliderect(rec) or pygame.rect.Rect(next_x3).colliderect(rec) or next_x3[0] < 680:
					return
			ai_block.now_block.recs[0][0] -= 60
			ai_block.now_block.recs[1][0] -= 30
			ai_block.now_block.recs[1][1] -= 30
			ai_block.now_block.recs[3][0] += 30
			ai_block.now_block.recs[3][1] -= 30
			ai_block.change_record = 0

