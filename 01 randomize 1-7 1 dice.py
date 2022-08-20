import numpy as np


def random_int_1_7_dice():
    """
    With assuming dice is not only 6 side, i make this with 7 side dice with numpy
    :return: int 1-7
    """
    return np.random.randint(1, 7, 1)[0]


def random_int_1_7_dice_v2():
    """
    with Assuming dice is only 6 side with a same probabilistic every side.
    :return: int 1-7
    """

    return int(np.round(6 * np.random.uniform(0, 1))) + 1


if __name__ == '__main__':
    print("vesion 1 >>>>",random_int_1_7_dice())
    print("vesion 2 >>>>", random_int_1_7_dice_v2())
