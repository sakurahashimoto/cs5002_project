from tkinter import W
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt


#a = step size
#x0 = starting point
#e = end
ITER_MAX = 1000

#takes four palameters
#deriv_f takes deriv functions
def gradient_descent(x0, a, e, deriv_f, f=None):
    i = 0
    xcurr = x0
    while i < ITER_MAX:
        #xnext = current place - a * deriv_f(xcurr)
        if f is None:
            xnext = xcurr - a * deriv_f(xcurr)
        else:
            xnext = xcurr - a * deriv_f(xcurr, f)
        if abs(xnext - xcurr) < e:
            #reach the bottom
            break
        xcurr = xnext
        #update iteration number
        i += 1
    print(f"i = {i}")
    return xcurr

#takes four palameters
#deriv_f takes deriv functions
def three_d_gradient_descent(x0, y0, a, e, deriv_f, f=None):
    i = 0
    xcurr = x0
    ycurr = y0
    while i < ITER_MAX:
        #deriv x = 'f(x0, y0)
         #deriv y = 'f(x0, y0)
        deriv_x, deriv_y = three_d_approx_deriv(xcurr, ycurr, f)
        xnext = xcurr - a * deriv_x
        ynext = ycurr - a * deriv_y
        if abs(xnext - xcurr) < e and abs(ynext - ycurr) < e:
            #reach the bottom
            break
        xcurr = xnext
        ycurr = ynext
        #update iteration number
        i += 1
    print(f"i = {i}")
    return xcurr, ycurr

#f1(x) = x^2
def f1(x):
    return x * x 

# 'f1(x) = 2x  
def deriv_f1(x):
    return 2 * x

# approximate derivative
def approx_deriv(x, function):
    h = 000000000000.1
    return (function(x + h) - function(x)) / h

# approximate derivative
def three_d_approx_deriv(x, y, function):
    #I set very small value of h
    h = 000000000000.1
    x1 = (function(x + h, y) - function(x, y)) / h
    y1 = (function(x, y + h) - function(x, y)) / h
    return (x1, y1)

#f2(x) = x^2 -2x + 3
def f2(x):
    return x**2 - 2 * x + 3


# 'f2(x) = 2x - 2
def deriv_f2(x):
    return 2 * x - 2

#f3(x) = sin(x) + cos(√2x), for 0 ≤ x ≤ 10
def f3(x):
    return np.sin(x) + np.cos(np.sqrt(2)*x)

# f′3(x) = cos(x) −√2 sin(√2x)
def deriv_f3(x):
    return np.cos(x) - np.sqrt(2) * np.sin(np.sqrt(2)*x)

#f4
def f4(x,y):
    return x**2 + y**2


#make a function that returns (x, y) for points 
def get_points(startx, endx, num_points, function):
    xs = []
    ys = []
    step_size = abs(endx - startx)/num_points 
    for x in np.arange(startx, endx, step_size):
        y = function(x)
        xs.append(x)
        ys.append(y)
    return (xs, ys)

#make a function that returns (x, y, z) for points 
def get_points(startx, endx, starty, endy, num_points):
    #xs is all of the number from startx and endx. And number of points in between
    xs = np.linspace(startx, endx, num_points)
    ys = np.linspace(starty, endy, num_points)
    #changing points into mesh grid
    X, Y = np.meshgrid(xs, ys)
    #for all x and y in a grid calculate z 
    Z = X ** 2 + Y ** 2
    return (X, Y, Z)

#opt_x is the minimum value of a function.(the bottom)
def plot_opt(opt_x_list, function, y_label, title):
    xs, ys = get_points(-10, 10, 100, function)
    sb.lineplot(x=xs, y=ys)
    opt_y_list = []
    for x in opt_x_list:
        opt_y_list.append(function(x))
    sb.scatterplot(x=opt_x_list, y=opt_y_list, s=100, color="red")
    plt.title(title)
    plt.xlabel('$x$')
    plt.ylabel(f'${y_label}$')
    plt.show()

#opt_x is the minimum value of a function.(the bottom)
def plot_opt(opt_x_list, opt_y_list, function, x_label, y_label, title):
    X, Y, Z = get_points(-10, 10, -10, 10, 100)
    opt_z_list = []
    for x in opt_x_list:
        for y in opt_y_list:
            opt_z_list.append(function(x,y))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.scatter(opt_x_list[0], opt_y_list[0], opt_z_list[0], color="red", s=100)
    plt.title(f"${title}$")
    plt.xlabel(f'${x_label}$')
    plt.ylabel(f'${y_label}$')
    plt.show()

    # sb.lineplot(x=xs, y=ys)
    # opt_z_list = []
    # for x in opt_x_list:
    #     for y in opt_y_list:
    #         opt_z_list.append(function(x, y))
    # X, Y = np.meshgrid(opt_x_list, opt_y_list)
    # sb.scatterplot(x=opt_x_list, y=opt_y_list, s=100, color="red")
    # plt.title(title)
    # plt.xlabel('$x$')
    # plt.ylabel(f'${y_label}$')
    # plt.show()

#2.1_3
# What is the output of the gradient algorithm for every value of α? A. see below
# Are you observing any variations in the output? If so, why do you think this is happening?
# If the step is too big (a=1) or too small (a=0.0001), the f1 and f2 give the wrong answers. 
# If it is too big then it steps so big it skips the bottom and jumps to the other side of 
# the mountain. It it is too small, the step is within the e value, then it is considered we 
# reached the bottom. 
#a=0.001 seems to show the aploximately the right results. i shows the number of loops meaning
#steps it took to compute. 
if __name__ == "__main__":
    # 2.1_1
    # plot_opt([gradient_descent(3.0, 0.1, 0.001, deriv_f1)], f1, "f(x) = x^2", "f1")
    # plot_opt([gradient_descent(3.0, 0.1, 0.001, deriv_f2)], f2, "f(x) = x^2 -2x + 3", "f2")

    # 2.1_2
    # for x0 in [3, -3]:
    #     print(f"x0 = {x0}, a=0.1, e=0.001:")
    #     print(f" f1 = {gradient_descent(x0, 0.1, 0.001, deriv_f1)}")
    #     print(f" f2 = {gradient_descent(x0, 0.1, 0.001, deriv_f2)}")
    #     print()

    # 2.1_3
    # for a in [1, 0.001, 0.0001]:
    #     print(f"x0 = 3, a={a}, e=0.001:")
    #     print(f" f1 = {gradient_descent(3, a, 0.001, deriv_f1)}")
    #     print(f" f2 = {gradient_descent(3, a, 0.001, deriv_f2)}")
    #     print()

    # 2.1_4
    #Yes I see variations in output showed at the terminal below. 
    #If the difference is too big between x0 and x1 then they do not take a step. 
    #If the diffence is smaller such as e=0.01 then it took 89 steps. 
    #If the difference is e=0.0001, the results for f1 and f2 are the most accurate of 
    #the three. Because the more you narrow the limit of the distance closer and more 
    #accurate points for the bottom of the mountain becomes. 
    # for e in [0.1, 0.01, 0.0001]:
    #     print(f"x0 = 3, a=0.1, e={e}:")
    #     print(f" f1 = {gradient_descent(3, 0.01, e, deriv_f1)}")
    #     print(f" f2 = {gradient_descent(3, 0.01, e, deriv_f2)}")
    #     print()

    # 2.2_1
    # plot_opt([gradient_descent(1, 0.1, 0.0001, deriv_f3)], f3, "f(x) = sin(x) + cos(√2x)", "f3")

    # 2.2_2
    # x0 = 1, a=0.1, e=0.0001:
    # i = 46
    # f3 = 2.708226412251601
    # x0 = 4, a=0.1, e=0.0001:
    #i = 60
    # f3 = 2.7247767591694703
    # x0 = 5, a=0.1, e=0.0001:
    # i = 36
    # f3 = 6.113192318985102
    # x0 = 7, a=0.1, e=0.0001:
    # i = 28
    # f3 = 6.124341228954422
    # result = []
    # for x0 in [1, 4, 5, 7]:
    #     result.append(gradient_descent(x0, 0.1, 0.001, deriv_f3))
    # print(result)
    # plot_opt(result, f3, "f(x) = sin(x) + cos(√2x)", "f3")

    # 3.1
    #we compare x1 (handcaliculated) and x2 (picked a random small value of h) 
    #the resutls shows 10, and 10.99999999998 respectively. Looks similar. 
    # x1 = deriv_f1(5) 
    # x2 = approx_deriv(5, f1)
    # print(x1, x2)
    
    #The results are 8 and 8.09999999 respectively. Looks similar. 
    # x3 = deriv_f2(5)
    # x4 = approx_deriv(5, f2)
    # print(x3, x4)

    # 3.2 
    # got 0.004642275147320177 for the original
    # print(gradient_descent(3, 0.1, 0.001, deriv_f1))
    # got -0.0452803536002245 for the approximate derivitve of f1
    # print(gradient_descent(3, 0.1, 0.001, approx_deriv, f1))
    # got 1.0048357032784585 for the original 
    # print(gradient_descent(3, 0.1, 0.001, deriv_f2))
    # got 0.9549565958604198 for the approximate derivitive of f2
    # print(gradient_descent(3, 0.1, 0.001, approx_deriv, f2))
    #The resutls are not the exactly the same, however, they are similar. 

    # 4.1
    # Implemented three_d_approx_deriv
    
    # 4.2
    # print(three_d_gradient_descent(3, 3, 0.1, 0.001, three_d_approx_deriv, f4))
    optx, opty = three_d_gradient_descent(3, 3, 0.1, 0.001, three_d_approx_deriv, f4)
    plot_opt([optx], [opty], f4, "x", "y", "f (x, y) = x^2 + y^2")
    