import matplotlib.pyplot as plt

"""
this class is used for 2 vars
"""


def graphics_use_for_2_vars(a, b):
    mode = input("""select the mode of the graphics, between.
                 1 = black
                 0 = white
                 mode: """)

    if mode == '1':
        plt.style.use('dark_background')
    elif mode == '0':
        pass
    type_graphic = input("""input the mode for the grap:
                         1: graphics inverse
                         2: graphics dispers
                         3: bar 
                         4: histograma
                         type graphic: """)
    if type_graphic == '1':
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

        ax1.set_title('relations  x - y')
        ax1.plot(a, b, 'b')
        ax2.set_title('relation y - x')
        ax2.plot(b, a, 'r')
        ax2.set_facecolor('gray')

    if type_graphic == '2':
        plt.scatter(a, b)
    if type_graphic == '3':
        plt.bar(a, b)
    if type_graphic == '4':
        plt.hist(a, b)
    plt.tight_layout()
    plt.show()
