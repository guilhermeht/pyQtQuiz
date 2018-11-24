from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
import sys

class Window(QWidget):
	windowHeight = 700
	windowsWidth = 600
	vPerguntas = []
	vRespostas = []

	def __init__(self):
		super().__init__()
		try:
			count = 0
			file = open("oi", "r")
			for line in file:
				line = line.rstrip('\n')
				if count % 5 == 0:
					self.vPerguntas.append(line)
				else:
					self.vRespostas.append(line)
				count+=1

			file.close()
		except:
			print("Could not open questions file")
			sys.exit()
		self.startUI()

	def startUI(self):
		# QToolTip.setFont(QFont('Cursive',10))
		# self.setToolTip('teste de widget')

		# Question
		self.question = QLineEdit(self)
		self.question.move(self.windowsWidth/2-250, 20)
		self.question.resize(475,200)
		self.question.setText(self.vPerguntas[0])
		
		# Creating Answer Buttons
		# Button1
		self.button1 = QPushButton(self.vRespostas[0], self)
		self.button1.resize(200,75)
		self.button1.move(50,250)
		self.button1.clicked.connect(self.botao_clicado)

		# Button2
		self.button2 = QPushButton(self.vRespostas[1], self)
		self.button2.resize(200, 75)
		self.button2.move(325,250)
		self.button2.clicked.connect(self.botao_clicado)


		# Button3
		self.button3 = QPushButton(self.vRespostas[2], self)
		self.button3.resize(200, 75)
		self.button3.move(50,350)
		self.button3.clicked.connect(self.botao_clicado)

		# Button4
		self.button4 = QPushButton(self.vRespostas[3], self)
		self.button4.resize(200, 75)
		self.button4.move(325,350)
		self.button4.clicked.connect(self.botao_clicado)

		# Timer
		self.timer = QProgressBar(self)
		#                      x, y, width, heigh
		self.timer.setGeometry(50, 475, 475, 20)

		# Criacao da Janela
		self.resize(self.windowsWidth, self.windowHeight)
		self.move(300, 300)
		self.setWindowTitle("Quiz Arquitetura")
		self.show()

	def botao_clicado(self):
		completed = 0
		value = 0.0
		while completed != 1:
			self.timer.setValue(value)
			value += 0.000001
			if value >= 101:
				completed = 1

if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = Window()
	sys.exit(app.exec_())