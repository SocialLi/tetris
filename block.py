import random
class Iblock():
	def __init__(self):
		self.recs = [
			[890, 150, 30, 30],
			[890, 180, 30, 30],
			[890, 210, 30, 30],
			[890, 240, 30, 30],
		]

class LLblock():
	def __init__(self):
		self.recs = [
			[860, 150, 30, 30],
			[860, 180, 30, 30],
			[890, 180, 30, 30],
			[920, 180, 30, 30],
		]

class LRblock():
	def __init__(self):
		self.recs = [
			[920, 150, 30, 30],
			[920, 180, 30, 30],
			[890, 180, 30, 30],
			[860, 180, 30, 30],
		]

class ZLblock():
	def __init__(self):
		self.recs = [
			[920, 150, 30, 30],
			[890, 150, 30, 30],
			[890, 180, 30, 30],
			[860, 180, 30, 30],
		]

class ZRblock():
	def __init__(self):
		self.recs = [
			[860, 150, 30, 30],
			[890, 150, 30, 30],
			[890, 180, 30, 30],
			[920, 180, 30, 30],
		]

class Tblock():
	def __init__(self):
		self.recs = [
			[890, 150, 30, 30],
			[860, 180, 30, 30],
			[890, 180, 30, 30],
			[920, 180, 30, 30],
		]

class Oblock():
	def __init__(self):
		self.recs = [
			[860, 150, 30, 30],
			[890, 150, 30, 30],
			[860, 180, 30, 30],
			[890, 180, 30, 30],
		]

class Block():
	def __init__(self):
		self.next_block = self.choice(random.randint(1, 7))
		self.next_color = [
						(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245)),
						(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245)),
						(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245)),
						(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245))
						]
		self.accumulate_list = []
		self.fixed_block = []
		self.change_record = 0
		self.score = 0
		self.creat_block()
		for x in range(15):
			self.fixed_block.append([680 + 30 * x, 900, 30, 30])

	def choice(self, number):
		if number == 1:
		    return Iblock()
		elif number == 2:
		    return LLblock()
		elif number == 3:
		    return LRblock()
		elif number == 4:
		    return ZLblock()
		elif number == 5:
		    return ZRblock()
		elif number == 6:
		    return Tblock()
		elif number == 7:
		    return Oblock()


    # 创建方块
	def creat_block(self):
		self.now_block = self.next_block
		self.next_block = self.choice(random.randint(1, 7))
		self.now_color = self.next_color
		self.next_color = [
						(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245)),
						(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245)),
						(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245)),
						(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245))
						]


