import pgzrun


def main():
    TITLE = "Paranoid"
    WIDTH = 800
    HEIGHT = 500
    
    paddle = Actor("paddleblue.png")
    paddle.x = 120
    paddle.y = 420

    ball = Actor("ballblue.png")
    ball.x = 30
    ball.y = 300
    
    pgzrun.go()



if __name__ == '__main__':
    main()