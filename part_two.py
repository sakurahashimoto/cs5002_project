import numpy as np
from functools import partial
import seaborn as sb
import matplotlib.pyplot as plt
import part_one


# 1.1
def load_data(filename):
    """
    Load the data into two arrays
    Args:
        filename: string representing the name of the file
            containing the data (x,y)
    Return:
        array containing the values of x
        array containing the values of y
    """
    data = np.loadtxt(filename)
    return data[:, 0], data[:, 1]


def plot(a, b, x, y, x_label, y_label, title):
    # get y values using found a and b
    line_y = a * x + b
    sb.lineplot(x=x, y=line_y)
    sb.scatterplot(x=x, y=y, s=100, color="red")
    plt.title(f"${title}$")
    plt.xlabel(f"{x_label}")
    plt.ylabel(f"{y_label}")
    plt.show()


def scale(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    std_x = np.std(x)
    std_y = np.std(y)
    scaled_x = (x - x_mean) / std_x
    scaled_y = (y - y_mean) / std_y
    return scaled_x,scaled_y


def main():
    x, y = load_data("data_chol_dias_pressure.txt")
    x,y = scale(x, y)
    # 1.3
    # 0.4 is starting a. 50 is starting b. 0.000001 is step size. 0.1 is stopping limit.
    opt_a, opt_b = part_one.three_d_gradient_descent(
        0.3, 50, 0.001, 0.001, part_one.three_d_approx_deriv, partial(g, x=x, y=y)
    )
    print(opt_a, opt_b)
    plot(
        opt_a,
        opt_b,
        x,
        y,
        "Total Cholesterol Level (mmol/L)",
        "Diastolic Blood Pressure (mm Hg)",
        "y = a^*x + b^*",
    )


# 1.2
def g(a, b, x, y):
    result = 0
    # loop over all x and y pairs and sum up the result for g
    for i in range(0, len(x)):
        calculation = ((a * x[i] + b) - y[i]) ** 2
        result += calculation
    return result


if __name__ == "__main__":
    main()
