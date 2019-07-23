import simplegui
import math

width = 600
height = 400
ball_pos = [width/2,height/2]
ball_vel = [-2,2]
pad1_pos = height/2
pad2_pos = height/2
pad1_vel = 0
pad2_vel = 0
pad_width = 20
pad_height = 40
ball_radious = 20
score1 =0
score2=0

def ball_init(right):
    global ball_pos, ball_vel
    ball_pos = [width/2, height/2]
    ball_radious = 20
    ball_vel = [2,-2]
def draw(canvas):
    global pad2_pos, pad1_pos,pad1_vel, pad2_vel,ball_pos,ball_vel,ball_radious,score1,score2
    canvas.draw_line([width/2,0],[width/2,400],2,"navy")
    canvas.draw_line([pad_width,0],[pad_width,400],2,"black")
    canvas.draw_line([width-pad_width,0],[width-pad_width,400],2,"black")
    
    if ball_pos[1] <= (ball_radious) or ball_pos[1] >= (height - ball_radious):
        ball_vel[1] = -ball_vel[1]


    if ball_pos[0] <= (pad_width + ball_radious):
        if ball_pos[1] > pad1_pos + pad_height or ball_pos[1] < pad1_pos - pad_height:
            score2 += 1
            ball_init(True)
        else:
            ball_vel[0] = -ball_vel[0]
        
    
    
    if ball_pos[0] >= (width - pad_width - ball_radious):
        if ball_pos[1] > pad2_pos + pad_height or ball_pos[1] < pad2_pos - pad_height:
            score1 += 1
            ball_init(True)
        else:
            
            #print pad2_pos + pad_height, pad2_pos - pad_height, pad2_pos, ball_pos[1]
            ball_vel[0] = -ball_vel[0]
                                        
    
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    pad2_pos = pad2_pos + pad2_vel
    pad1_pos = pad1_pos + pad1_vel
# draw paddle

    canvas.draw_polygon([[0,pad1_pos+pad_height],[0,pad1_pos-pad_height],[pad_width,pad1_pos-pad_height],[pad_width,pad1_pos+pad_height]],2,"green","blue")
    canvas.draw_polygon([[width-pad_width,pad2_pos+pad_height],[width-pad_width,pad2_pos-pad_height],[width,pad2_pos-pad_height],[width,pad2_pos+pad_height]],2,"green","blue")
    canvas.draw_circle([ball_pos[0],ball_pos[1]],ball_radious,3,"yellow","blue")
    canvas.draw_text(str(score1), (170, 50), 36, "Red")
    canvas.draw_text(str(score2), (400, 50), 36, "Red")
def keyd(key):
    global pad2_pos,pad2_vel,pad1_pos,pad1_vel
    k = key
    if k == simplegui.KEY_MAP["up"]:
        pad2_vel = -4        
        
    elif k == simplegui.KEY_MAP["down"]:
        pad2_vel = 4
        
    elif k == simplegui.KEY_MAP["w"]:
        pad1_vel = -4
    elif k == simplegui.KEY_MAP["s"]:
        pad1_vel = 4

    
def keyu(key):
    global pad2_pos,pad2_vel,pad1_pos,pad1_vel
    k = key
    if k == simplegui.KEY_MAP["up"]:
        pad2_vel = 0        
        
    elif k == simplegui.KEY_MAP["down"]:
        pad2_vel = 0
        
    elif k == simplegui.KEY_MAP["w"]:
        pad1_vel = 0
    elif k == simplegui.KEY_MAP["s"]:
        pad1_vel = 0

    


frame = simplegui.create_frame("Ping Pong",width,height,300)
frame.start()
frame.set_canvas_background("Aqua")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keyd)
frame.set_keyup_handler(keyu)
