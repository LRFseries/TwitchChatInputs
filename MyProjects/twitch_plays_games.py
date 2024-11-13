import pydirectinput, pyautogui, requests, socket, re, time

def switch(text):
    if text == "w":
        pydirectinput.keyDown('w')
        time.sleep(1)
        pydirectinput.keyUp('w')

    elif text == "wlong":
        pydirectinput.keyDown('w')
        time.sleep(3)
        pydirectinput.keyUp('w')

    elif text == "wshort":
        pydirectinput.keyDown('w')
        time.sleep(0.25)
        pydirectinput.keyUp('w')

    elif text == "a":
        pydirectinput.keyDown('a')
        time.sleep(1)
        pydirectinput.keyUp('a')

    elif text == "along":
        pydirectinput.keyDown('a')
        time.sleep(3)
        pydirectinput.keyUp('a')

    elif text == "ashort":
        pydirectinput.keyDown('a')
        time.sleep(0.25)
        pydirectinput.keyUp('a')

    elif text == "s":
        pydirectinput.keyDown('s')
        time.sleep(1)
        pydirectinput.keyUp('s')

    elif text == "slong":
        pydirectinput.keyDown('s')
        time.sleep(3)
        pydirectinput.keyUp('s')

    elif text == "sshort":
        pydirectinput.keyDown('s')
        time.sleep(0.25)
        pydirectinput.keyUp('s')

    elif text == "d":
        pydirectinput.keyDown('d')
        time.sleep(1)
        pydirectinput.keyUp('d')

    elif text == "dlong":
        pydirectinput.keyDown('d')
        time.sleep(3)
        pydirectinput.keyUp('d')

    elif text == "dshort":
        pydirectinput.keyDown('d')
        time.sleep(0.25)
        pydirectinput.keyUp('d')

    elif text == "sprint":
        pydirectinput.keyDown('shift')
        pydirectinput.keyDown('w')
        time.sleep(1)
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('shift')

    elif text == "sprintlong":
        pydirectinput.keyDown('shift')
        pydirectinput.keyDown('w')
        time.sleep(3)
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('shift')

    elif text == "marathon":
        pydirectinput.keyDown('shift')
        pydirectinput.keyDown('w')
        time.sleep(8)
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('shift')

    elif text == "click":
        pydirectinput.click()
        
    elif text == "rclick":
        pydirectinput.rightClick()
    
    elif text == "right":
        pydirectinput.move(1000, 0, relative=True)
    
    elif text == "smallright":
        pydirectinput.move(200, 0, relative=True)

    elif text == "90right":
        pydirectinput.move(2500, 0, relative=True)
    
    elif text == "invright":
        pydirectinput.move(72, 0, relative=True)

    elif text == "left":
        pydirectinput.move(-1000, 0, relative=True)

    elif text == "90left":
        pydirectinput.move(-2500, 0, relative=True)

    elif text == "smallleft":
        pydirectinput.move(-200, 0, relative=True)

    elif text == "invleft":
        pydirectinput.move(-72, 0, relative=True)

    elif text == "up":
        pydirectinput.move(0, -500, relative=True)

    elif text == "invup":
        pydirectinput.move(0, -50, relative=True)

    elif text == "down":
        pydirectinput.move(0, 500, relative=True)

    elif text == "invdown":
        pydirectinput.move(0, 50, relative=True)

    elif text == "jump":
        pydirectinput.press('space')
    
    elif text == "wjump":
        pydirectinput.keyDown('w')
        pydirectinput.keyDown('space')
        time.sleep(1.5)
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('space')

    elif text == "wcrouch":
        pydirectinput.keyDown('ctrl')
        pydirectinput.keyDown('w')
        time.sleep(1.5)
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('ctrl')

    elif text == "crouchjump":
        pydirectinput.keyDown('w')
        pydirectinput.keyDown('ctrl')
        pydirectinput.keyDown('space')
        time.sleep(1.5)
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('space')
        pydirectinput.keyUp('ctrl')

    elif text == "e":
        pydirectinput.press('e')

    elif text == "1":
        pydirectinput.press('1')

    elif text == "2":
        pydirectinput.press('2')

    elif text == "3":
        pydirectinput.press('3')

    elif text == "4":
        pydirectinput.press('4')

    elif text == "5":
        pydirectinput.press('5')

    elif text == "6":
        pydirectinput.press('6')

    elif text == "7":
        pydirectinput.press('7')

    elif text == "8":
        pydirectinput.press('8')

    elif text == "9":
        pydirectinput.press('9')

    elif text == "attack":
        pydirectinput.mouseDown()
        time.sleep(3.5)
        pydirectinput.mouseUp()

    elif text == "attacklong":
        pydirectinput.mouseDown()
        time.sleep(8)
        pydirectinput.mouseUp()

    elif text == "rclickhold":
        pydirectinput.mouseDown(button='right')
        time.sleep(2)
        pydirectinput.mouseUp(button='right')

    elif text == "q":
        pydirectinput.press('q')

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'chatreader'
token = 'oauth:9o92ln368d7nyhap052w8mct5phx1v'
channel = '#LRF_Series'

sock = socket.socket()
sock.connect((server,port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

sock.recv(2048).decode('utf-8')
sock.recv(2048).decode('utf-8')

while True: 
    message = sock.recv(2048).decode('utf-8')
    
    if message.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))


    elif len(message) > 0:
        text = re.search('PRIVMSG #.* :(.*)\r', message).group(1)
        print(repr(text))
        switch(text)
