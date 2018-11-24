from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
from random import randint
import time
import sys

class Window(QWidget):
	windowHeight = 700
	windowsWidth = 600
	vPerguntas = []
	vRespostas = []
	totalPerguntas = 0
	indiceRespostas = [0,1,2,3]

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
		self.totalPerguntas = len(self.vPerguntas)
		self.startUI()

	def startUI(self):
		# Getting Questions and Answer Index from random number
		self.numeroPergunta = randint(0,self.totalPerguntas-1)

		self.button1_index = (self.numeroPergunta*4) + self.indiceRespostas.pop(randint(0,len(self.indiceRespostas)-1))
		self.button2_index = (self.numeroPergunta*4) + self.indiceRespostas.pop(randint(0,len(self.indiceRespostas)-1)) 		
		self.button3_index = (self.numeroPergunta*4) + self.indiceRespostas.pop(randint(0,len(self.indiceRespostas)-1))
		self.button4_index = (self.numeroPergunta*4) + self.indiceRespostas.pop(randint(0,len(self.indiceRespostas)-1))
		
		# Question
		self.question = QLineEdit(self)
		self.question.move(self.windowsWidth/2-250, 20)
		self.question.resize(475,200)
		self.question.setText(self.vPerguntas[self.numeroPergunta])

		# Creating Answer Buttons
		# Button1
		print(self.button1_index)
		self.button1 = QPushButton(self.vRespostas[ self.button1_index ], self)
		self.button1.resize(200,75)
		self.button1.move(50,250)
		self.button1.clicked.connect(self.botao1_clicado)

		# Button2
		print(self.button2_index)
		self.button2 = QPushButton(self.vRespostas[ self.button2_index ], self)
		self.button2.resize(200, 75)
		self.button2.move(325,250)
		self.button2.clicked.connect(self.botao2_clicado)


		# Button3
		print(self.button3_index)
		self.button3 = QPushButton(self.vRespostas[ self.button3_index ], self)
		self.button3.resize(200, 75)
		self.button3.move(50,350)
		self.button3.clicked.connect(self.botao3_clicado)

		# Button4
		print(self.button4_index)
		self.button4 = QPushButton(self.vRespostas[ self.button4_index ], self)
		self.button4.resize(200, 75)
		self.button4.move(325,350)
		self.button4.clicked.connect(self.botao4_clicado)

		# Timer
		self.timer = QProgressBar(self)
		#                      x, y, width, heigh
		self.timer.setGeometry(50, 475, 475, 20)

		# Criacao da Janela
		self.resize(self.windowsWidth, self.windowHeight)
		self.move(300, 300)
		self.setWindowTitle("Quiz Arquitetura")
		self.show()


	def botao1_clicado(self):
		self.botao_clicado = self.button1_index
		self.checar_resposta()

	def botao2_clicado(self):
		self.botao_clicado = self.button2_index
		self.checar_resposta()

	def botao3_clicado(self):
		self.botao_clicado = self.button3_index
		self.checar_resposta()

	def botao4_clicado(self):
		self.botao_clicado = self.button4_index
		self.checar_resposta()

	def checar_resposta(self):
		print("Botao clicado "+str(self.botao_clicado))
		if((self.numeroPergunta*4)-self.botao_clicado == 0):
			self.question.setText("RESPOSTA CORRETA!")
		else:
			self.question.setText("RESPOSTA ERRADA! A resposta correta eh: "+self.vRespostas[self.numeroPergunta*4])
		app.processEvents() # Atualiza a tela com os novos textos
		time.sleep(2.2)
		self.mudar_pergunta()

	def mudar_pergunta(self):
		self.question.setText("Pergunta2")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = Window()
	sys.exit(app.exec_())