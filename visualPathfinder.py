import pygame

pygame.init()

win = pygame.display.set_mode((1210, 760))
pygame.display.set_caption('Visual Pathfinder')
font = pygame.font.Font('freesansbold.ttf', 15)  # Font for buttons
font2 = pygame.font.Font('freesansbold.ttf', 15)  # Font for path
font3 = pygame.font.Font('freesansbold.ttf', 70)
squares = []
blocks = []
showPath = True
run = True
passedBoxes = []


for _ in range(1, 511):
    squares.append('')

start_pos_x = 10
start_pos_y = 10

def PutSquaresOnScreen():
    global start_pos_x, start_pos_y
    pygame.draw.rect(win, (0,0,0), (0,0,1100,690)) # Background
    start_pos_x = 10
    start_pos_y = 10
    for x in range(1,511):
        squares[x-1] = pygame.draw.rect(win, (192,192,192), (start_pos_x,start_pos_y,30,30))
        start_pos_x += 40
        if x % 30 == 0:
            start_pos_y += 40 
            start_pos_x = 10
PutSquaresOnScreen()

def HideButtonClick():
    global hideButton, hideButton_background
    hideButton_background = pygame.draw.rect(win, (200, 200, 200), (250, 695, 150, 50))
    if showPath:
        hideButton = font.render('Hide the Path', True, (0, 0, 0))
    else:
        hideButton = font.render('Show the Path', True, (0, 0, 0))
    win.blit(hideButton, (275, 713))
HideButtonClick()

def CaptureScreen():
    image = pygame.Surface((1210,690))
    image.blit(win,(0,0),((0,0),(1210,690)))
    pygame.image.save(image,'visualPathfinderCapture.png')

# Set up the reset button
resetButton_background = pygame.draw.rect(win, (200, 200, 200), (450, 695, 150, 50))
resetButton = font.render('Reset (R)', True, (0, 0, 0))
win.blit(resetButton, (490, 713))

# Set up the start button
startButton_background = pygame.draw.rect(win, (200, 200, 200), (650, 695, 150, 50))
startButton = font.render('Start (Space)', True, (0, 0, 0))
win.blit(startButton, (675, 713))

# Set up the start button
imageButton_background = pygame.draw.rect(win, (200, 200, 200), (850, 695, 150, 50))
imageButton = font.render('Save as PNG', True, (0, 0, 0))
win.blit(imageButton, (875, 713))

def GetPositionOfSquare(index):
    x_pos = 10 + (index%30) * 40     # x value in pixels
    y_pos = 10 + (index//30) * 40       # y value in pixels
    AddSymbol(x_pos,y_pos,index)


def CheckCollision(pos):
    num = 0
    for a in squares:
        if a.collidepoint(pos):
            GetPositionOfSquare(num)
        num += 1     
    return False


def RemoveSymbolFromGrid(symbol):
    if symbol == 'Start':
        try:  # If the user adds the symbol for the first time try function will be passed
            pygame.draw.rect(win, (192,192,192), (old_start_pos_x,old_start_pos_y,30,30))
            pygame.display.update()
        except:
            pass
    if symbol == 'End':
        try:
            pygame.draw.rect(win, (192,192,192), (old_end_pos_x,old_end_pos_y,30,30))
            pygame.display.update()
        except:
            pass


   
def AddSymbol(x_pos,y_pos,place):
    global start_x, start_y, end_x, end_y, old_start_pos_x, old_start_pos_y,old_end_pos_x,old_end_pos_y
    if button_clicked == 1:   # Left Click - Start Point
        RemoveSymbolFromGrid('Start')
        pygame.draw.rect(win, (0,0,250), (x_pos,y_pos,30,30))
        start_x = (place%30) + 1   # x value as an index 
        start_y = (place//30) + 1  # y value as an index
        old_start_pos_x = x_pos   # Stores the values so that if the user adds a new start point, old one will be deleted
        old_start_pos_y = y_pos
    elif button_clicked == 3:  # Right Click - Endpoint
        RemoveSymbolFromGrid('End')
        pygame.draw.rect(win, (250,0,0), (x_pos,y_pos,30,30))
        end_x = (place%30) + 1    # x value as an index 
        end_y = (place//30) + 1   # y value as an index
        old_end_pos_x = x_pos   # Stores the values so that if the user adds a new start point, old one will be deleted
        old_end_pos_y = y_pos
    elif button_clicked == 2:   # Middle button click - Blocks
        if [(place//30) + 1,(place%30) + 1] in blocks:
            pygame.draw.rect(win, (192,192,192), (x_pos,y_pos,30,30))
            blocks.remove([(place//30) + 1,(place%30) + 1])
        else:
            blocks.append([(place//30) + 1,(place%30) + 1])
            pygame.draw.rect(win, (178,40,162), (x_pos,y_pos,30,30))

def CheckAvailable(movement):
    line_checked = start_y
    element_checked = start_x
    for x in movement:
        if x == 'D':
            line_checked += 1
        elif x == 'U':
            line_checked -= 1
        elif x == 'L':
            element_checked -= 1
        elif x == 'R':
            element_checked += 1
    if 0 < line_checked < 18 and 0 < element_checked < 31:
        if not [line_checked,element_checked] in blocks:
            return True
        return False

def ReachedEnd(movement):
    line_checked = start_y
    element_checked = start_x
    for x in movement:
        if x == 'D':
            line_checked += 1
        elif x == 'U':
            line_checked -= 1
        elif x == 'L':
            element_checked -= 1
        elif x == 'R':
            element_checked += 1
    if [element_checked, line_checked] == [end_x, end_y]:
        return True

def ChangeBlockColors(movement,mode):
    line_checked = start_y
    element_checked = start_x
    count = 1
    for x in movement:
        if x == 'D':
            line_checked += 1
        elif x == 'U':
            line_checked -= 1
        elif x == 'L':
            element_checked -= 1
        elif x == 'R':
            element_checked += 1
        x_value = 10 + ((element_checked-1)*40)
        y_value = 10 + ((line_checked-1)*40)
        if mode == 'Final': 
            pygame.draw.rect(win, (0,230,0), (x_value,y_value,30,30))  #This line makes boxes green
            # Below lines add numbers to the boxes
            count_Text = font2.render(str(count), True, (0, 0, 0))
            win.blit(count_Text, (x_value+10, y_value+10))
            count += 1
        else:
            if showPath:
                pygame.draw.rect(win,(0,0,250),(-30 + start_x *40 ,-30 + start_y *40,30,30))        
                pygame.draw.rect(win, (230,230,0), (x_value,y_value,30,30))

    if mode == 'Final':  
        pygame.draw.rect(win, (0,230,0), (-30 + start_x *40,-30 + start_y *40,30,30))        
        pygame.draw.rect(win,(250,0,0),(x_value,y_value,30,30))
        pygame.draw.rect(win,(0,0,250),(-30 + start_x *40 ,-30 + start_y *40,30,30)) 
        
    pygame.display.update()


def CheckIfPassed(movement):
    line_checked = start_y
    element_checked = start_x
    for x in movement:
        if x == 'D':
            line_checked += 1
        elif x == 'U':
            line_checked -= 1
        elif x == 'L':
            element_checked -= 1
        elif x == 'R':
            element_checked += 1
    if [line_checked,element_checked] in passedBoxes:
        return True
    else:
        passedBoxes.append([line_checked,element_checked])
    return False


def StartPathFinding():
    moves = ['']
    while not ReachedEnd(moves[-1]):
        path = moves.pop(0)
        for x in ['D','U','L','R']:
            if CheckAvailable(path+x):
                if not CheckIfPassed(path+x):
                    moves.append(path+x)
                    ChangeBlockColors(moves[-1], 'Test')
                    if ReachedEnd(moves[-1]): # In some cases, the loop doesn't catch move[-1], so this if statement solves the problem 
                        passedBoxes = []
                        ChangeBlockColors(moves[-1], 'Final')
                        break

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_clicked = event.button
            position = pygame.mouse.get_pos()
            if CheckCollision(position) != False:
                CheckCollision(position)
            if hideButton_background.collidepoint(position):
                showPath = not showPath
                HideButtonClick()
            if resetButton_background.collidepoint(position):
                PutSquaresOnScreen()
                start_x = 0
                start_y = 0
                end_x = 0
                end_y = 0
                blocks = []
                passedBoxes = []
            if startButton_background.collidepoint(position):
                try: # To prevent crashing when the user didnt add both end and start points
                    StartPathFinding()
                except:
                    pass
            if imageButton_background.collidepoint(position):
                CaptureScreen()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            try:   # To prevent crashing when the user didnt add both end and start points
                StartPathFinding()
            except:
                pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            PutSquaresOnScreen()
            start_x = 0
            start_y = 0
            end_x = 0
            end_y = 0
            blocks = []
            passedBoxes = []
        pygame.display.update()

pygame.quit()
