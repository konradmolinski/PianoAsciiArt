from itertools import cycle

key_types = [
    [
        "_____",
        "|  | ",
        "|  | ",
        "|  | ",
        "|  | ",
        "|   |",
        "|   |",
        "|___|",
    ],
    [
        "_____",
        " |  |",
        " |  |",
        " |  |",
        " |  |",
        "|   |",
        "|   |",
        "|___|",
    ],
    [
        "_____",
        " | | ",
        " | | ",
        " | | ",
        " | | ",
        "|   |",
        "|   |",
        "|___|",
    ]
]

def show_white_keys(number_of_keys):
    keyboard_order = "RMLRMML"
    number_of_keys = list(range(number_of_keys))

    if len(number_of_keys) > 52 or len(number_of_keys) < 1:
        print("Number of keys to print cannot be bigger then 52 and must be at least 1.")
        return None

    for key in key_types[0]:
        current_line = key_types[0].index(key)
        zip_list = zip(number_of_keys, cycle(keyboard_order)) if len(number_of_keys) > len(keyboard_order) \
            else zip(number_of_keys, keyboard_order)

        for y in zip_list:
            if y[1] == "R":
                print(key_types[0][current_line], end="")
            elif y[1] == "L":
                print(key_types[1][current_line], end="")
            elif y[1] == "M":
                print(key_types[2][current_line], end="")
            else:
                print("wrong input value for keyboard order")
                break
        print("\r")








