import pygame,sys
import numpy as np

pygame.init()

#CONSTANTS USED
wd = 300
ht = wd
size = wd//3
bg = (28,170,156)
line = (23,145,135)
ocolor = (255,255,255)
xcolor = (206,64,44)
rad = size//3
lwidth = 10
owidth = wd//60
xwidth = wd//30
gap = size//4

root = pygame.display.set_mode((ht,wd))
pygame.display.set_caption('TIC TAC TOE')
root.fill(bg)

board = np.zeros((3,3))#(rows,columns)

#FUNCTIONS USED
def text():
	txt = pygame.font.SysFont('Consolas',15)
	msg = txt.render('Press "r" to restart',True,xcolor,bg)
	box = msg.get_rect(bottomright = (wd,wd))
	root.blit(msg,box)

def diswinner(pl):
	if pl == 1:
		txt = pygame.font.SysFont('Consolas',30)
		msg = txt.render('O won!!',True,xcolor,ocolor)
		box = msg.get_rect(topleft = (0,0))
		root.blit(msg,box)
	elif pl == 2:
		txt = pygame.font.SysFont('Consolas',30)
		msg = txt.render('X won!!',True,xcolor,ocolor)
		box = msg.get_rect(topleft =(0,0))
		root.blit(msg,box)

def dline():
	#horizontal lines
	pygame.draw.line(root,line,(0,size),(wd,size),lwidth)
	pygame.draw.line(root,line,(0,2*size),(wd,2*size),lwidth)
	#vertical lines
	pygame.draw.line(root,line,(size,0),(size,wd),lwidth)
	pygame.draw.line(root,line,(2*size,0),(2*size,wd),lwidth)

def drawxo():
	for row in range(3):
		for col in range(3):
			if board[row][col]==1:
				pygame.draw.circle(root,ocolor,(int(col*size+size//2),int(row*size+size//2)),rad,owidth)
			elif board[row][col] == 2:
				pygame.draw.line(root,xcolor,(col*size+gap,row*size+size-gap),(col*size+size-gap,row*size+gap),xwidth)
				pygame.draw.line(root,xcolor,(col*size+gap,row*size+gap),(col*size+size-gap,row*size+size-gap),xwidth)

def msq(r,c,pl):
	board[r][c] = pl

def avail(r,c):
	return board[r][c]==0

def isfull():
	for row in range(3):
		for col in range(3):
			if board[row][col] == 0:
				return False
	return True

def checkwin(pl):
	#for vertical
	for col in range(3):
		if board[0][col] == pl and board[1][col] == pl and board[2][col] == pl:
			d_v_line(col,pl)
			return True
	#for horizontal
	for row in range(3):
		if board[row][0] == pl and board[row][1] == pl and board[row][2] == pl:
			d_h_line(row,pl)
			return True
	#for ascending diagonal
	if board[2][0] ==pl and board[1][1] ==pl and board[0][2] == pl:
		d_ad_line(pl)
		return True
	#for descending diagonal
	if board[0][0] ==pl and board[1][1] ==pl and board[2][2] == pl:
		d_dd_line(pl)
		return True
	return False

def d_v_line(col,pl):
	pX = col*size+size//2
	if pl == 1:
		color = ocolor
	elif pl ==2:
		color = xcolor
	pygame.draw.line(root,color,(pX,15),(pX,ht-15),15)

def d_h_line(row,pl):
	pY = row*size+size//2
	if pl == 1:
		color = ocolor
	elif pl ==2:
		color = xcolor
	pygame.draw.line(root,color,(15,pY),(wd-15,pY),15)

def d_ad_line(pl):
	if pl == 1:
		color = ocolor
	elif pl ==2:
		color = xcolor
	pygame.draw.line(root,color,(15,ht-15),(wd-15,15),15)

def d_dd_line(pl):
	if pl == 1:
		color = ocolor
	elif pl ==2:
		color = xcolor
	pygame.draw.line(root,color,(15,15),(wd-15,ht-15),15)

def restart():
	root.fill(bg)
	dline()
	text()
	player = 1
	for row in range(3):
		for col in range(3):
			board[row][col] =0

dline()

player = 1
game_over = False
text()
#MAINLOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

        	xval = event.pos[0] #x
        	yval = event.pos[1] #y

        	crow = int(yval//size)
        	ccol = int(xval//size)

        	if avail(crow,ccol):
        		if player == 1:
        			msq(crow,ccol,1)
        			if checkwin(player):
        				game_over =True
        				diswinner(player)
        			player = 2
        		elif player ==2:
        			msq(crow,ccol,2)
        			if checkwin(player):
        				game_over =True
        				diswinner(player)
        			player = 1
        		drawxo()
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_r:
        		restart()
        		game_over = False
    pygame.display.update()