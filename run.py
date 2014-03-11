class Run:
	def __init__(self):
		try:
			import gameP
			game = gameP.Game()
		except:
			import gameC
			game = gameC.Game()

run = Run()
