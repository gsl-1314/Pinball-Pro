from tkinter import *
import random
import time
class Ball:
  def __init__(self, canvas, paddle, color):
    self.canvas = canvas
    self.paddle = paddle
    self.id = canvas.create_oval(60, 60, 120, 120, fill=color)
    self.canvas.move(self.id, 245, 100)
    startx = [-3, -2, -1, 1, 2, 3]
    random.shuffle(startx)
    self.x = startx[0]
    self.y = -3
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = self.canvas.winfo_width()
    self.hit_bottom = False
    self.countHit=0
  def draw(self):
    self.canvas.move(self.id, self.x, self.y)
    pos = self.canvas.coords(self.id)#top-left bottom-right
    if (pos[1] <= 0 or self.hit_paddle(pos) == True):
      self.y = -self.y
    if (pos[0] <= 0 or pos[2] >= self.canvas_width):
      self.x = -self.x
    if (pos[3] >= self.canvas_height):
      self.hit_bottom = True
  def hit_paddle(self, pos):
    paddle_pos = self.canvas.coords(self.paddle.id)
    if (pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]):
      if (pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]):
        self.countHit=self.countHit+1
        return True
    return False
class Paddle:
  def __init__(self, canvas, color):
    self.canvas = canvas
    self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
    self.x = 0
    self.canvas.move(self.id, 200, 300)
    self.canvas_width = self.canvas.winfo_width()
    self.canvas.bind_all("<Key-Left>", self.turn_left)
    self.canvas.bind_all("<Key-Right>", self.turn_right)
  def draw(self):
    pos = self.canvas.coords(self.id)
    if (pos[0] + self.x >= 0 and pos[2] + self.x <= self.canvas_width):
      self.canvas.move(self.id, self.x, 0)
    #self.x = 0
  def turn_left(self, event):
    self.x = -4
  def turn_right(self, event):
    self.x = 4
class GameOver:
  def __init__(self, canvas, color):
    self.canvas=canvas
    self.id=canvas.create_rectangle(0,0,100,50,fill=color)
    self.x=(self.canvas.winfo_width()-100)/2
    self.y=(self.canvas.winfo_height()-50)/2
    self.canvas.move(self.id,self.x,self.y)
    self.canvas_width=self.canvas.winfo_width
    self.canvas.create_text(self.x+50,self.y+20,fill="white",font="宋体",text="游戏结束")
	
tk = Tk()
strCount=StringVar()
strOver=StringVar()
tk.title("Game")
tk.resizable(0, 0)#not resizable
tk.wm_attributes("-topmost", 1)#at top
lblCount=Label(tk,bg='white',textvariable=strCount,fg='red')
lblCount.pack()
#lblOver=Label(tk,bg='black',width=30,height=5,font=24,fg='white',textvariable=strOver)
canvas = Canvas(tk, width = 500, height = 500, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()#init
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
while 1:
  if (ball.hit_bottom == False):
   ball.draw()
   paddle.draw()
   strCount.set(f'次数:{ball.countHit}')
   tk.update_idletasks()
   tk.update()
   time.sleep(0.01)
  else:
   #strOver.set('游戏结束')
   #lblOver.pack()
   GameOver(canvas,'black')
   tk.update_idletasks()
   tk.update()
   time.sleep(3)
   break