#+------------------------------------
# Project: Dinner Jia Sa
#  - Solution to your dinner frustration
# Author: Joycelyn Chen
#+------------------------------------


# Init fridge
# food storage file:
# store food entries in a json file with the following schema
# {main: {}, protein: {}, veggie: {}}
# within each category stored the food detail: {food: quantity, unit} 



import json


fridge_location = "fridge.json"


def fridge_empty():
    try:
        with open(fridge_location, 'r') as f:
            content = json.load(f)
            return content == {}
                
    except FileNotFoundError:
        return True


def fridge_status():
    if fridge_empty():
        return "empty"
    return "not empty"


def init_fridge():
    fridge_content = {"main": {}, "protein": {}, "veggie": {}}
    add_more = True
    while(add_more):
        category = input("Enter category (main/protein/veggie): ")
        food_name = input("Enter food name: ")
        quantity = int(input("Enter quantity: "))
        unit = input("Enter unit: ")
        fridge_content[category][food_name] = {"quantity": quantity, "unit": unit}
        
        add_more = input("Wanna add more? Y/N").upper() == "Y"

    with open(fridge_location, 'w') as f:
        json.dump(fridge_content, f)


def ready4dinner():
    # check if the user is ready to execute the following program, type 1 to continue, others to end
    ready = int(input("Are you ready for dinner? type number 1) YESSSS 2) Nah\n"))
    if ready == 1:
        return True
    else:
        print("Then why are you even here. Bye.")
        return False


def query_main():
    # pull the 'main' key from the fridge, then display them on screen, have user input one main course they want, then return as a string
    with open(fridge_location, 'r') as f:
        fridge_content = json.load(f)
    main_options = list(fridge_content["main"].keys())
    print("Choose a main course:")
    for i, option in enumerate(main_options):
        print(f"{i+1}. {option}")
    choice = int(input("Enter the number of your choice: "))
    return main_options[choice-1]


def query_protein():
    with open(fridge_location, 'r') as f:
        fridge_content = json.load(f)
    protein_options = list(fridge_content["protein"].keys())
    print("Choose protein(s):")
    for i, option in enumerate(protein_options):
        print(f"{i+1}. {option}")
    choices = input("Enter the numbers of your choices, separated by comma: ")
    choices = [protein_options[int(i)-1] for i in choices.split(",")]
    return choices


def query_veggie():
    # pull the 'veggie' key from the fridge, then display them on screen, have user choose whatever they want, separate each input with comma
    with open(fridge_location, 'r') as f:
        fridge_content = json.load(f)
    veggie_options = list(fridge_content["veggie"].keys())
    print("Choose veggie(s):")
    for i, option in enumerate(veggie_options):
        print(f"{i+1}. {option}")
    choices = input("Enter the numbers of your choices, separated by comma: ")
    choices = [veggie_options[int(i)-1] for i in choices.split(",")]
    return choices


if __name__ == "__main__":
    # init fridge if not already existed
    if fridge_status() == 'empty':
        init_fridge()
    
    if ready4dinner():
        main = query_main()
        protein = query_protein()
        veggie = query_veggie()
        print(f"Your dinner choice: {main} with {', '.join(protein)} and {', '.join(veggie)}")
    else:
        print("Goodbye!")