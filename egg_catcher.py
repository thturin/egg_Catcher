"""
Project No. EGG CATCHER
3 events happening concurrently
1. create new egg at the top of the screen
2. move all the eggs mon the screen down a bit and then check to see if any of them have hit the bottom
3. check if the catcher caught an egg
"""
from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font
#only importing the modules that we are going to use


#INITIAL SETUP AND BACKGROUND DRAWING
canvas_width = 800
canvas_height = 400
root = Tk() #create a Tkinter window object
c = Canvas(root, width=canvas_width, height=canvas_height, background='deep sky blue')
c.create_rectangle(-5,canvas_height- 100, canvas_width+5,canvas_height+5,fill='sea green', width=0) #create_rectangle(x1,y1,x2,y2) <-top left and bottom right corner
c.create_oval(-80,-80,120,120,fill='orange', width=0) # same as rectangle
c.pack() #draw the main window and all of its contents

#SETUP THE EGGS
color_cycle = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan'])
egg_width = 45
egg_height = 55
egg_score = 10 #score 10 points for catching an egg
egg_speed = 500
egg_interval = 4000 #a new egg appears every 4 seconds
difficulty_factor = 0.95 #after every catch, the speed increases

#SETUP THE CATCHER
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width /2
catcher_start_y = canvas_height - catcher_height -20
print('The canvas height is ({},{})'.format(catcher_start_x,catcher_start_y))
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height
catcher = c.create_arc(catcher_start_x,catcher_start_y,catcher_start_x2,catcher_start_y2, start=200, extent=140,style='arc',outline=catcher_color,width=3) #extent is 140 degrees

#SCORE AND LIVES COUNTERS
game_font = font.nametofont('TkFixedFont')
game_font.config(size=18)

score = 0
score_text = c.create_text(10,10,anchor='nw',font=game_font,fill='darkblue', text='Score: {}'.format(score))
lives_remaining = 3
lives_text = c.create_text(canvas_width-10,10,anchor='ne',font=game_font, fill='darkblue', text='Lives {}'.format(lives_remaining))

#CREATE THE EGGS

c.mainloop()
