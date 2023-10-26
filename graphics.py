import matplotlib.pyplot as plt

"""
this class is used for 2 vars
"""


def graphics_use_for_var_one_var(a):
    type_graphic_1_var = input("""input the mode for the grap: 
                         1: bar 
                         2: histograma
                         type graphic: """)

    if type_graphic_1_var == '1':
        plt.bar(a)
    if type_graphic_1_var == '2':
        plt.hist(a)
    plt.tight_layout()
    plt.show()


def graphics_use_for_vars(a, b):
    mode = input("""select the mode of the graphics, between.
                 1 = black
                 0 = white
                 mode: """)

    if mode == '1':
        plt.style.use('dark_background')
    elif mode == '0':
        pass
    type_graphic_2_var = input("""input the mode for the grap:
                                1: graphics inverse
                                2: graphics dispers
                                type grapjic: """)
    if type_graphic_2_var == '1':
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

        ax1.set_title('relations  x - y')
        ax1.plot(a, b, 'b')
        ax2.set_title('relation y - x')
        ax2.plot(b, a, 'r')
        ax2.set_facecolor('gray')
    if type_graphic_2_var == '2':
        plt.scatter(a, b)
    plt.tight_layout()
    plt.show()
