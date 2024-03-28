import tkinter as tk
import sqlite3
from contextlib import closing
from tkinter import messagebox
from jogo_da_forca import Forca
from main import *

class Login(tk.Frame):

	def __init__(self, master=None):
		tk.Frame.__init__(self, master=None, bg='#2e2e2c', pady=25)

		self.bLog = tk.Button(self, font=("Helvetica", 12, "bold"), text="LOGIN", foreground='#fcca28', bg='#363636', padx=80, pady=10, command=self.loginn)
		self.bLog.pack(fill=tk.X, pady=5)
		self.bCreat = tk.Button(self, font=("Helvetica", 12, "bold"), text="REGISTER", foreground='#fcca28', bg='#363636', padx=80, pady=10, command=self.criar_login)
		self.bCreat.pack(fill=tk.X)

	def loginn(self):
		self.bLog.destroy()
		self.bCreat.destroy()

		self.userLog1 = tk.Label(self, font=("Helvetica", 12, "bold"), text='USER', foreground='#fcca28', bg='#2e2e2c', padx=80)
		self.userLog1.pack(fill=tk.X)
		self.userLog2 = tk.Entry(self, font=("Helvetica", 12), bg='#363636', foreground='white')
		self.userLog2.pack(fill=tk.X, pady=15)

		self.keyLog1 = tk.Label(self, font=("Helvetica", 12, "bold"), text='KEY', foreground='#fcca28', bg='#2e2e2c', padx=80)
		self.keyLog1.pack(fill=tk.X)
		self.keyLog2 = tk.Entry(self, show='*', font=("Helvetica", 12), bg='#363636', foreground='white')
		self.keyLog2.pack(fill=tk.X, pady=15)

		self.button1 = tk.Button(self, font=("Helvetica", 12, "bold"), text='LOGIN',foreground='#fcca28', bg='#2e2e2c', padx=80, command=self.loginButton)
		self.button1.pack(fill=tk.X, pady=8)

		self.voltarInicio = tk.Button(self, font=("Helvetica", 12, "bold"), text='VOLTAR', foreground='#fcca28', bg='#2e2e2c', padx=80, command=self.voltar_inicio)
		self.voltarInicio.pack(fill=tk.X)

	def criar_login(self):
		self.bLog.destroy()
		self.bCreat.destroy()

		self.user = tk.Label(self,  font=("Helvetica", 12, "bold"), text='USER', foreground='#fcca28', bg='#2e2e2c', padx=80)
		self.user.pack(fill=tk.X)
		self.user2 = tk.Entry(self, font=("Helvetica", 12), bg='#363636', foreground='white')
		self.user2.pack(fill=tk.X, pady=15)

		self.key = tk.Label(self, font=("Helvetica", 12, "bold"), text='KEY', foreground='#fcca28', bg='#2e2e2c', padx=80)
		self.key.pack(fill=tk.X)
		self.key1 = tk.Entry(self, show='*', font=("Helvetica", 12), bg='#363636', foreground='white')
		self.key1.pack(fill=tk.X, pady=15)

		self.button2 = tk.Button(self, font=("Helvetica", 12, "bold"), text='REGISTER', foreground='#fcca28', bg='#2e2e2c', padx=80, command=self.button_create)
		self.button2.pack(fill=tk.X, pady=8)

		self.voltarInicio2 = tk.Button(self, font=("Helvetica", 12, "bold"), text='VOLTAR', foreground='#fcca28', bg='#2e2e2c', padx=80, command=self.voltar_inicio2)
		self.voltarInicio2.pack(fill=tk.X)

	def loginButton(self):
		conexao = sqlite3.connect('../hangman-game/db/jogadores.db')
		cursor = conexao.cursor()
		cursor.execute('SELECT * from jogadores')
		resultado = cursor.fetchall()
		login_successful = False

		for dado in resultado:
			if self.userLog2.get() == dado[0] and self.keyLog2.get() == dado[1]:
				login_successful = True
				break
			
		if login_successful:
			self.userLog1.destroy()
			self.userLog2.destroy()
			self.keyLog1.destroy()
			self.keyLog2.destroy()
			self.button1.destroy()
			self.voltarInicio.destroy()
			self.iniciarBut = tk.Button(self, font=("Helvetica", 12, 'bold'), text='JOGAR', foreground='#fcca28', bg='#363636', padx=90, pady=10, command=self.playGame)
			self.iniciarBut.pack(fill=tk.X, pady=8)
			self.sair = tk.Button(self, font=("Helvetica", 12, 'bold'), text='SAIR', foreground='#fcca28', bg='#363636', padx=90, pady=10, command=self.voltar_inicio3)
			self.sair.pack(fill=tk.X)
		else:
			conexao.commit()
			messagebox.showinfo(title="Login Info", message="Login Invalído")
				
		conexao.commit()
		cursor.close()
		conexao.close()

	def button_create(self):
		conexao = sqlite3.connect('../hangman-game/db/jogadores.db')
		cursor = conexao.cursor()
		cursor.execute('SELECT * from jogadores')
		resultado = cursor.fetchall()
		try:

			if self.user2.get() not in resultado and self.user2.get() != None:
				cursor.execute('INSERT INTO jogadores VALUES (?,?,?)', (self.user2.get(), self.key1.get(), 0))
				messagebox.showinfo(title="Register Info", message="Criado Com Sucesso.")
				self.bLog.destroy()
				self.bCreat.destroy()
				self.user.destroy()
				self.user2.destroy()
				self.key.destroy()
				self.key1.destroy()
				self.button2.destroy()
				self.voltarInicio2.destroy()
				self.loginn()

		except:
			conexao.commit()
			messagebox.showinfo(title="Register Info", message="User Indisponível\nTente Novamente.")
			
		conexao.commit()
		cursor.close()
		conexao.close()

	def playGame(self):
		self.iniciarBut.destroy()

		self.img = tk.PhotoImage(file="../hangman-game/imgs/image1.png")
		self.img = self.img.subsample(4, 4)

		self.background = tk.Label(image=self.img, bd=0)
		self.background.place(x=0, y=0)
		self.background.image = self.img

		self.l = tk.Label(self).pack()
		self.master.app = Forca(self.l).pack(pady=2.5)


	def rank(self):
		pass

	def voltar_inicio(self):
		self.userLog1.destroy()
		self.userLog2.destroy()
		self.keyLog1.destroy()
		self.keyLog2.destroy()
		self.button1.destroy()
		self.voltarInicio.destroy()

		self.bLog = tk.Button(self, font=("Helvetica", 12, "bold"), text="LOGIN", foreground='#fcca28', bg='#363636', padx=80, pady=10, command=self.loginn)
		self.bLog.pack(fill=tk.X, pady=5)
		self.bCreat = tk.Button(self, font=("Helvetica", 12, "bold"), text="REGISTER", foreground='#fcca28', bg='#363636', padx=80, pady=10, command=self.criar_login)
		self.bCreat.pack(fill=tk.X)

	def voltar_inicio2(self):
		self.user.destroy()
		self.user2.destroy()
		self.key.destroy()
		self.key1.destroy()
		self.button2.destroy()
		self.voltarInicio2.destroy()

		self.bLog = tk.Button(self, font=("Helvetica", 12, "bold"), text="LOGIN", foreground='#fcca28', bg='#363636', padx=80, pady=10, command=self.loginn)
		self.bLog.pack(fill=tk.X, pady=5)
		self.bCreat = tk.Button(self, font=("Helvetica", 12, "bold"), text="REGISTER", foreground='#fcca28', bg='#363636', padx=80, pady=10, command=self.criar_login)
		self.bCreat.pack(fill=tk.X)

	def voltar_inicio3(self):
		self.iniciarBut.destroy()
		self.sair.destroy()
		
		self.bLog = tk.Button(self, font=("Helvetica", 12, "bold"), text="LOGIN", foreground='#fcca28', bg='#363636', padx=80, pady=10, command=self.loginn)
		self.bLog.pack(fill=tk.X, pady=5)
		self.bCreat = tk.Button(self, font=("Helvetica", 12, "bold"), text="REGISTER", foreground='#fcca28', bg='#363636', padx=80, pady=10, command=self.criar_login)
		self.bCreat.pack(fill=tk.X)

	def update_acertos(username, acertos):
		with sqlite3.connect('caminho_para_seu_banco_de_dados.db') as conexao:
			cursor = conexao.cursor()
			cursor.execute("UPDATE jogadores SET acertos = ? WHERE username = ?", (acertos, username))
			conexao.commit()