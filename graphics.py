import matplotlib.pyplot as plt

"""
this class is used for 2 vars
"""


def graphics_use_for_2_vars(a, b):
    mode = input('select the mode of the graphics. '
                 'between'
                 '1 = black'
                 '0 = white')

    if mode == '1':
        plt.style.use('dark_background')
    elif mode == '0':
        pass
    type_graphic = input('input the mode for the grap'
                         '1: graphics inverse'
                         '2: graphics dispers'
                         '3: ')
    if type_graphic == '1':
        fig = plt.figure()
        axes = fig.add_axes([0.1, 0.1, 0.5, 0.9])
        axes2 = fig.add_axes([0.5, 0.55, 0.5, 0.9])
        axes.plot(a, b, 'b')
        axes2.plot(b, a, 'r')
        axes2.set_facecolor('gray')

    if type_graphic == '2':
        plt.scatter(a, b)
    if type_graphic == '3':
        plt.bar(a, b)
    plt.tight_layout()
    plt.show()
