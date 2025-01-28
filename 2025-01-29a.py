"""
@brief 2025 New Year's Day Demo
@version 1.0
@author Dinosaur_MC
@date 2025-01-29
@requires Python 3.8 or higher
"""

import turtle
import time
import math
from typing import Union

try:
    from pydantic import BaseModel
except ImportError:
    print("pydantic not found, installing...")
    import os

    # 安装pydantic模块
    os.system("pip install pydantic")
    from pydantic import BaseModel


# 设置屏幕
screen = turtle.Screen()
screen.setup(width=520, height=520)
screen.bgcolor("white")
screen.title("Python demo - 2025.01.29 by Dinosaur_MC")

# 创建画笔
pen = turtle.Turtle()
pen.speed(8)
pen.penup()


def cvrtX(x: float):
    return x - 240


def cvrtY(y: float):
    return 240 - y


# 坐标转换
def cvrtPos(x: float, y: float):
    return (cvrtX(x), cvrtY(y))


# 计算圆心角度
def calcA(direction: bool = True):
    x, y = pen.pos()
    if y != 0:
        k = -x / y
        a = math.atan(k) * 180 / math.pi
    else:
        a = 90
    return a + 180 if direction else a


# 设置画笔位置
def setPos(pos: tuple[float, float]):
    pen.goto(cvrtX(pos[0]), cvrtY(pos[1]))


# 绘制直线
def drawLine(dir: float, len: float):
    pen.setheading(dir)
    pen.forward(len)


# 绘制圆弧
def drawCircle(r: float, a: float, dir: bool = True):
    pen.setheading(calcA(dir))
    pen.circle(r, a)


class Line(BaseModel):
    direction: float
    length: float


class Circle(BaseModel):
    radius: float
    angle: float = 360
    direction: bool = True


class Pattern(BaseModel):
    pos: tuple[float, float] = None
    draws: list[Union[Line, Circle]]


# 绘制图案
def drawPattern(pattern: Pattern):
    if pattern.pos:
        setPos(pattern.pos)
    pen.pendown()
    pen.begin_fill()
    for draw in pattern.draws:
        if isinstance(draw, Line):
            drawLine(draw.direction, draw.length)
        elif isinstance(draw, Circle):
            drawCircle(draw.radius, draw.angle, draw.direction)
        else:
            raise ValueError("Invalid draw type")
    pen.end_fill()
    pen.penup()


# 绘制“福”字
def drawFu():
    pen.pensize(5)
    pen.color("red")

    r1 = 233.75
    r2 = 191.00

    patterns: list[Pattern] = [
        Pattern(
            pos=(68.10, 153.32),
            draws=[
                Line(direction=180, length=44.10),
                Circle(radius=r1, angle=-60.76),
                Line(direction=270, length=146.89),
                Line(direction=180, length=42.41),
                Line(direction=90, length=89.32),
                Circle(radius=r2, angle=39.72),
            ],
        ),
        Pattern(
            pos=(209.43, 170.67),
            draws=[
                Line(direction=180, length=190.43),
                Circle(radius=r1, angle=60.56),
                Line(direction=90, length=60.77),
                Circle(radius=r2, angle=-41.13, direction=False),
                Line(direction=0, length=40.83),
                Line(direction=270, length=209.01),
                Circle(radius=r1, angle=12.42, direction=False),
                Line(direction=90, length=235.01),
                Line(direction=0, length=32.39),
                Line(direction=270, length=250.01),
                Circle(radius=r1, angle=11.85, direction=False),
                Line(direction=90, length=300.55),
            ],
        ),
        Pattern(
            pos=(234.00, 48.00),
            draws=[
                Line(direction=90, length=41.58),
                Circle(radius=r1, angle=-49.20),
                Line(direction=180, length=59.00),
                Circle(radius=r2, angle=37.80),
            ],
        ),
        Pattern(
            pos=(240.00, 98.57),
            draws=[
                Line(direction=270, length=103.71),
                Line(direction=0, length=231.91),
                Circle(radius=r1, angle=28.09),
                Line(direction=180, length=186.00),
                Line(direction=-45.1, length=55.62),
                Line(direction=270, length=24.36),
                Line(direction=0, length=135.02),
                Circle(radius=r2, angle=9.81),
                Line(direction=180, length=121.02),
            ],
        ),
        Pattern(
            pos=(233.75, 228.50),
            draws=[
                Line(direction=270, length=243.66),
                Circle(radius=r1, angle=94.36, direction=False),
                Line(direction=180, length=240.15),
                Line(direction=-44.20, length=56.41),
                Line(direction=270, length=35.08),
                Line(direction=0, length=146.80),
                Circle(radius=r2, angle=10.79, direction=False),
                Line(direction=180, length=66.90),
                Line(direction=270, length=117.18),
                Circle(radius=r2, angle=17.49, direction=False),
                Line(direction=180, length=126.80),
                Line(direction=270, length=84.77),
                Circle(radius=r2, angle=15.19, direction=False),
                Line(direction=90, length=144.18),
                Line(direction=180, length=47.81),
            ],
        ),
        Pattern(
            pos=(322.00, 302.91),
            draws=[
                Line(direction=270, length=39.33),
                Line(direction=0, length=40.10),
                Line(direction=90, length=39.33),
                Line(direction=180, length=40.10),
            ],
        ),
    ]
    for pattern in patterns:
        drawPattern(pattern)


def writeText(text, x, y, fsize=40):
    pen.goto(x, y)
    pen.write(text, align="center", font=("华文中宋", fsize, "bold"))


def main():
    drawFu()
    screen.update()
    pen.hideturtle()
    time.sleep(1.5)
    pen.clear()

    pen.color("red")
    writeText("2025", 0, 128, 56)
    writeText("蛇年伊始,", 0, 48, 32)
    writeText("Python登场~", 0, 0, 32)
    writeText("新年快乐！", 26, -96)
    writeText("Happy Python Year", 0, -192, 32)
    screen.update()
    time.sleep(2.5)
    screen.bye()


if __name__ == "__main__":
    main()
