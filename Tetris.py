import pygame
import random
import cv2
import sys
import time
# 方塊的顏色



global rocket 
rocket  = 0
def target_tracking():
    time.sleep(3)
    tracker_type = "TLD"
    tracker = cv2.legacy.TrackerTLD_create()
    # Read video
    video = cv2.VideoCapture(0)
 
    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()
 
    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    
    # Define an initial bounding box
    bbox = (287, 23, 86, 320)
 
    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)
 
    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
    count = 0
    x = 0
    y = 0
    global rocket 
    while True:
        time.sleep(0.1)
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
        
        # Start timer
        timer = cv2.getTickCount()
 
        # Update tracker
        ok, bbox = tracker.update(frame)
 
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
 
        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        cv2.putText(frame, "direction : " , (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        if count == 0:
            x = int(bbox[0])
            y = int(bbox[1])

        if count == 30:
            # tmpx = x - int(bbox[0])
            # tmpy = y - int(bbox[1])
            tmpx1 = 0 + int(bbox[0])
            tmpy1 = 0 + int(bbox[1])
            tmpx2 = 600 - int(bbox[0])
            tmpy2 = 480 - int(bbox[1])
            winx = [0,0]
            winy = [0,0]
            if abs(tmpx1) < abs(tmpx2):
                winx[1] = abs(tmpx1)
            else :
                winx[0] = 1
                winx[1] = abs(tmpx2)
                
            if abs(tmpy1) < abs(tmpy2):
                winy[1]  = abs(tmpy1)
            else :
                winy[0] = 1
                winy[1]  = abs(tmpy2)
            
            if winx[1] > winy[1] and winx[0] == 0 :
                rocket = 3
                cv2.putText(frame, "direction : " + "left", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
                
            elif winx[1] > winy[1] and winx[0] == 1 :
                rocket = 4
                cv2.putText(frame, "direction : " + "right", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            if winy[1] > winx[1] and winy[0] == 0  :
                rocket  = 1
                cv2.putText(frame, "direction : " + "up", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            elif winy[1] > winx[1] and winy[0] == 1:
                rocket = 2
                cv2.putText(frame, "direction : " + "down", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
                
            # if abs(tmpx) > abs(tmpy) and tmpx > 0 and abs(tmpx) > 5 :
            
                # cv2.putText(frame, "direction : " + "right", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
                
            # if abs(tmpx) > abs(tmpy) and tmpx < 0 and abs(tmpx) > 5:
            
                # cv2.putText(frame, "direction : " + "left", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            # if abs(tmpy) > abs(tmpx) and tmpy > 0 and abs(tmpy) > 10:
            
                # cv2.putText(frame, "direction : " + "up", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            # if abs(tmpy) > abs(tmpx) and tmpy < 0 and abs(tmpy) > 10:
                # cv2.putText(frame, "direction : " + "down", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            count = 0
        count += 1
        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
    
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        
        cv2.putText(frame, "box : " + str(int(bbox[0]))+","+str(int(bbox[1]))+","+str(int(bbox[2]))+","+str(int(bbox[3])), (100,70), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        
        # Display result
        cv2.imshow("Tracking", frame)
        cv2.resizeWindow("Tracking", 600, 480);
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : 
            break



def main():
    # 0  1  2  3
    # 4  5  6  7
    # 8  9  10 11
    # 12 13 14 15
    colors = [
        (0, 0, 0),
        (120, 37, 179),
        (100, 179, 179),
        (80, 34, 22),
        (80, 134, 22),
        (180, 34, 22),
        (180, 34, 122),
    ]
    class Figure:
        figures = [
            [[1, 5, 9, 13], [4, 5, 6, 7]],
            [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
            [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
            [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
            [[1, 2, 6, 7], [1, 4, 5, 8]],
            [[1, 2, 4, 5], [2, 6, 7, 11]],
            [[1, 2, 5, 6]],
        ] # 每個方塊的圖案
        
        def __init__(self, x, y):
            self.x = x # 
            self.y = y
            self.type = random.randint(0, len(self.figures) - 1) # 方塊圖案
            self.color = random.randint(1, len(colors) - 1) # 方塊顏色
            self.rotation = 0 # 轉到第幾個
        
        def image(self):
            return self.figures[self.type][self.rotation]

        def rotate(self):
            self.rotation = (self.rotation + 1) % len(self.figures[self.type])

    class Tetris:
        level = 2
        score = 0
        state = "start"
        field = []
        height = 0
        width = 0
        x = 100
        y = 60
        zoom = 20
        figure = None

        def __init__(self, height, width):
            self.height = height
            self.width = width
            for i in range(height):
                new_line = []
                for j in range(width):
                    new_line.append(0)
                self.field.append(new_line)

        def new_figure(self):
            self.figure = Figure(3, 0)
        
        def intersects(self):
            intersection = False
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.figure.image():
                        if i + self.figure.y > self.height - 1 or \
                                j + self.figure.x > self.width - 1 or \
                                j + self.figure.x < 0 or \
                                self.field[i + self.figure.y][j + self.figure.x] > 0:
                            intersection = True
            return intersection
        
        def freeze(self):
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.figure.image():
                        self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
            self.break_lines()
            self.new_figure()
            if self.intersects():
                game.state = "gameover"

        def break_lines(self):
            lines = 0
            for i in range(1, self.height):
                zeros = 0
                for j in range(self.width):
                    if self.field[i][j] == 0:
                        zeros += 1
                if zeros == 0:
                    lines += 1
                    for i1 in range(i, 1, -1):
                        for j in range(self.width):
                            self.field[i1][j] = self.field[i1 - 1][j]
            self.score += lines ** 2

        def go_space(self):
            while not self.intersects():
                self.figure.y += 1
            self.figure.y -= 1
            self.freeze()

        def go_down(self):
            self.figure.y += 1
            if self.intersects():
                self.figure.y -= 1
                self.freeze()

        def go_side(self, dx):
            old_x = self.figure.x
            self.figure.x += dx
            if self.intersects():
                self.figure.x = old_x

        def rotate(self):
            old_rotation = self.figure.rotation
            self.figure.rotate()
            if self.intersects():
                self.figure.rotation = old_rotation

    pygame.init()

    # 定義一些颜色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

    size = (400, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Tetris")

    done = False
    counter = 0
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    pressing_down = False
    global rocket 
    while not done:
        if game.figure is None:
            game.new_figure()
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()
        
        for event in pygame.event.get():
           #@ time.sleep(1)
            if event.type == pygame.QUIT:
                done = True
            
            # if type(rocket) == int:
                # if rocket == 1:
                    #print("good1")
                    # game.rotate()
                # if rocket == 2:
                    #print("good2")
                    # pressing_down = True
                # if rocket == 3:
                    #print("good3")
                    # game.go_side(-1)
                #if rocket == 4:
                    #print("good4")
                    #game.go_side(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    game.go_side(-1)
                if event.key == pygame.K_RIGHT:
                    game.go_side(1)
                if event.key == pygame.K_SPACE:
                    game.go_space()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        screen.fill(WHITE)

        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, colors[game.field[i][j]],
                                    [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

        if game.figure is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.figure.image():
                        pygame.draw.rect(screen, colors[game.figure.color],
                                        [game.x + game.zoom * (j + game.figure.x) + 1,
                                        game.y + game.zoom * (i + game.figure.y) + 1,
                                        game.zoom - 2, game.zoom - 2])

        font = pygame.font.SysFont('Calibri', 25, True, False)
        font1 = pygame.font.SysFont('Calibri', 65, True, False)
        text = font.render("Score: " + str(game.score), True, BLACK)
        text_game_over = font1.render("Game Over :( ", True, (255, 0, 0))

        screen.blit(text, [0, 0])
        if game.state == "gameover":
            screen.blit(text_game_over, [10, 200])
            # done = True

        pygame.display.flip()
        clock.tick(fps/3)

    pygame.quit()



# pygame.init()

# # 定義一些颜色
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GRAY = (128, 128, 128)

# size = (400, 500)
# screen = pygame.display.set_mode(size)

# pygame.display.set_caption("Tetris")

# # 循环，直到使用者點擊關閉按鈕
# done = False
# clock = pygame.time.Clock()
# fps = 25
# game = Tetris(20, 10)
# counter = 0

# pressing_down = False

# while not done:
#     if game.figure is None:
#         game.new_figure()
#     counter += 1
#     if counter > 100000:
#         counter = 0

#     if counter % (fps // game.level // 2) == 0 or pressing_down:
#         if game.state == "start":
#             game.go_down()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 game.rotate()
#             if event.key == pygame.K_DOWN:
#                 pressing_down = True
#             if event.key == pygame.K_LEFT:
#                 game.go_side(-1)
#             if event.key == pygame.K_RIGHT:
#                 game.go_side(1)
#             if event.key == pygame.K_SPACE:
#                 game.go_space()
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_DOWN:
#                 pressing_down = False

#     screen.fill(WHITE)

#     for i in range(game.height):
#         for j in range(game.width):
#             pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
#             if game.field[i][j] > 0:
#                 pygame.draw.rect(screen, colors[game.field[i][j]],
#                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

#     if game.figure is not None:
#         for i in range(4):
#             for j in range(4):
#                 p = i * 4 + j
#                 if p in game.figure.image():
#                     pygame.draw.rect(screen, colors[game.figure.color],
#                                     [game.x + game.zoom * (j + game.figure.x) + 1,
#                                     game.y + game.zoom * (i + game.figure.y) + 1,
#                                     game.zoom - 2, game.zoom - 2])

#     font = pygame.font.SysFont('Calibri', 25, True, False)
#     font1 = pygame.font.SysFont('Calibri', 65, True, False)
#     text = font.render("Score: " + str(game.score), True, BLACK)
#     text_game_over = font1.render("Game Over :( ", True, (255, 0, 0))

#     screen.blit(text, [0, 0])
#     if game.state == "gameover":
#         screen.blit(text_game_over, [10, 200])
#         # done = True

#     pygame.display.flip()
#     clock.tick(fps)

# pygame.quit()


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        

        pass
