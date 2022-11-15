# custom_action.py
import argparse
import json


def plant():
    print("Starting the documenting of a tree plant")
    tree = {}
    print("Is it a just planted tree? Y or n")
    planted_tree = input()
    while planted_tree == "Y" or planted_tree == "y":
        print("First, what's the tree species")
        species = input()
        print("Whats the date dd/mm/yyyy")
        date = input()
        print("Amount:")
        amount = input()
        print("What is the id of the plant")
        id = input()
        print("What is width of the tree in cm?")
        width = input()
        print("And how long in cm?")
        height = input()
        print("Where are they planted?")
        s_coord = input("Latitude: ")
        e_coord = input("Longitude: ")
        tree["species"] = species
        tree["date"] = date
        tree["amount"] = amount
        tree["id"] = id
        tree["width"] = width
        tree["heigth"] = height
        tree["coords"] = (s_coord, e_coord)
        print("Is this correct? Y or n")
        print(tree)
        is_correct = input()
        if (is_correct == "y"):
            tree["updates"] = []
            flag_new = True
            return tree, flag_new

    if planted_tree == "n":
        print("What is the id of the plant")
        id = input()
        print("Whats the date dd/mm/yyyy")
        date = input()
        print("What is width of the tree in cm?")
        width = input()
        print("And how long in cm?")
        height = input()
        flag_old = False
        tree["id"] = id
        tree["width"] = width
        tree["heigth"] = height
        tree["date"] = date
        print("Is this correct? Y or n")
        print(tree)
        is_correct = input()
        if (is_correct == "y"):
            return tree, flag_old

    return


def main():
    parser = argparse.ArgumentParser(
        prog='TreePlanters',
        description='This program helps you keep track of your trees!',
    )

    # positional argument
    parser.add_argument('-p', '--plant', action="store_true",
                        help='Begin documenting a plant')  # -p flag for starting the documenting of a tree plant

    args = parser.parse_args()  # parsing of the arguments

    if (args.plant):
        tree_entry, flag = plant()  # if -p flag is true, execute plant function

        if flag:
            with open('data.json', 'r+') as file:
                file_data = json.load(file)
                file_data["trees"].append(tree_entry)
                file.seek(0)
                json.dump(file_data, file, indent=4)
        else:
            print("trying to update old tree entry")
            with open('data.json', 'r+') as file:
                file_data = json.load(file)
                for entry in file_data['trees']:
                    if (entry['id'] == tree_entry['id']):
                        print("trying to append")
                        jsonEntry = entry.copy()
                        jsonEntry["updates"].append(
                            {tree_entry['date'], tree_entry['width'],
                             tree_entry['heigth']})
                        entry.pop()

            with open('data.json', 'w') as file:
                file_data = json.load(file)
                file_data["trees"].append(jsonEntry)
                file.seek(0)
                json.dump(file_data, file, indent=4)


main()
