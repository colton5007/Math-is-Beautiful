from flask import Flask
from flask import request
from flask import redirect
from flask import Response
from latex2sympy.process_latex import process_sympy
from sympy import *
import numpy as np
from PIL import Image
from math import *
from threading import Thread

app = Flask(__name__)

tabs = list()
expr_r = None
expr_g = None
expr_b = None

HEIGHT = 1024
WIDTH = 1024


@app.route('/', methods=['Get', 'Post'])
def start():
    global expr_r
    global expr_g
    global expr_b
    global max_r, max_b, max_g
    if request.method == "GET":
        return open("static/one-time.html").read()
    else:
        latex_r = request.form["r"]
        latex_g = request.form["g"]
        latex_b = request.form["b"]

        max_r = int(request.form["max_r"])
        max_g = int(request.form["max_g"])
        max_b = int(request.form["max_b"])
        print max_r
        print max_g
        print max_b

        expr_r = process_sympy(latex_r).simplify()
        expr_g = process_sympy(latex_g).simplify()
        expr_b = process_sympy(latex_b).simplify()
        draw_image()
        return open("static/one-time.html").read()


@app.route("/img")
def image():
    return open("temp.png", "rb").read()


@app.route('/static/mathquill.css', methods=['Get'])
def mcss():
    return Response(open("static/mathquill.css").read(), mimetype="text/css")


@app.route('/static/mathquill.js', methods=['Get'])
def mjs():
    return open("static/mathquill.js").read()


def max_e(s):
    temp = s[0]
    for i in s:
        if i > temp:
            temp = i
    return temp


def min_e(s):
    temp = s[0]
    for i in s:
        if i < temp:
            temp = i
    return temp


def scale(maximum, setie):
    temp = list()
    min_set = min_e(setie)
    print "Minimum: " + str(min_set)
    spread = abs(max_e(setie) - min_set)
    print "Spread: " + str(spread)
    print "Maximum: " + str(maximum)
    try:
        multiplier = float(maximum)/spread
        print "Multiplier: " + str(multiplier)
    except Exception as e:
        print(e)
        multiplier = 0
    for s in setie:
        temp.append(int((s-min_set) * multiplier))
    return temp


def draw_image():
    red = list()
    green = list()
    blue = list()
    pic_array = list()
    x, y, right = symbols("x y right")
    left = lambda p : p
    r = lambdify([x, y, right], expr_r, [{"left": left}, "math"])
    g = lambdify([x, y, right], expr_g, [{"left": left}, "math"])
    b = lambdify([x, y, right], expr_b, [{"left": left}, "math"])
    for i in range(HEIGHT):
        for j in range(WIDTH):
            try:
                red.append(r(x=i, y=j, right=1))
            except Exception as e:
                print e
                red.append(0)

            try:
                green.append(g(x=i, y=j, right=1))
            except Exception as e:
                print e
                green.append(0)

            try:
                blue.append(b(x=i, y=j, right=1))
            except Exception as e:
                print e
                blue.append(0)

    red = scale(max_r, red)
    green = scale(max_g, green)
    blue = scale(max_b, blue)
    for i in range(HEIGHT * WIDTH):
        pic_array.append((red[i], green[i], blue[i]))

    pixels = np.array(pic_array, dtype=np.uint8).reshape((WIDTH, HEIGHT, 3))
    img = Image.fromarray(pixels)
    img.save("temp.png")


