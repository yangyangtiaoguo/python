import turtle
"""
import 引入外部库、 def 定义函数
"""
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        '''
        rad为正代表小蛇的左边，即在上方（圆心），angle旋转弧长
        circle圆形轨迹运动
        fd=forward直线轨迹运动
        '''
        turtle.pencolor("blue")
        turtle.circle(rad,angle)
        turtle.pencolor("red")
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.pencolor("blue")
    turtle.circle(60,180)
    turtle.fd(rad*2/3)

def main():
    """
    setup 启动图形窗口 启动窗口的宽度和高度，窗口左上角在屏幕中坐标的位置
    pensize()运动轨迹宽度
    pythonsize 像素
    seth初始运动方向
    """
    turtle.setup(1300,800,0,0)
    pythonsize = 10
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-70)
    drawSnake(40,80,5,pythonsize/2)

main()
    
