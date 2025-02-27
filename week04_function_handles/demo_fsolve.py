"""Practice understanding of function handles.

Use scipy.optimize.fsolve to find the closest root of a function.
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc


def eval_quadratic(x, a, b, c):
    """Evaluate f(x) = a*x^2 + b*x + c."""
    y = a*x**2 + b*x + c
    return y


def plot_quadratic(a, b, c, xplot=np.linspace(-5, 5, 301)):
    """Plot a quadratic function."""
    fig, ax = plt.subplots(figsize=(6, 3))  # initialize figure
    yplot = eval_quadratic(xplot, a, b, c)  # define y-values to plot
    ax.plot(xplot, yplot)  # plot the quadratic function
    ax.plot(xplot, np.zeros_like(xplot), '--', c='0.3', zorder=0)  # plot a zero-line
    ax.set(xlim=xplot[[0, -1]], xlabel='x', ylabel='y')  # add labels
    ax.grid()  # add a grid
    fig.tight_layout()  # rescale axes in figure to look nice
    return fig, ax


if __name__ == '__main__':
    # define constants for parabola coefficients and initial guess
    A, B, C = 1, 1, -12
    X0 = [-5, 4]

    # plot the parabola and initial guess as an x
    fig, ax = plot_quadratic(A, B, C)
    ax.scatter(X0, [0,0], color='black', marker='x', label='Initial guesses')

    # call fsolve to find the closest root, add to plot as red circle
    x0_actually = sc.optimize.fsolve(func=eval_quadratic, x0=X0, args=(A,B,C))
    ax.scatter(x0_actually, [0,0], color='red', marker='o', facecolors='none', label='Roots')
    ax.legend()

    plt.show()
