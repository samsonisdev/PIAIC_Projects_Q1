
def access(list1, index):
    try:
        return list1[index]
    except IndexError as ind:
        return "Can't Access", ind

def modify(list1, index, new_val):
    try:
        list1[index] = new_val
        return list1
    except IndexError as ind:
        return "Can't Modify", ind

def slice_list(list1, start_index, end_index):
    try:
        return list1[start_index:end_index]
    except IndexError as ind:
        return "Can't Slice", ind

def list_game():

    my_list = ["Shamoon", 19, "PIAIC", "Shahmir", 20, "FHGS", "Sohaib", 19, "PIAIC"]

    print("---LIST GAME---")
    print('''-Press A to access an element
-Press M to modify an element
-Press S to slice the list''')
    option = input("Option: ")
    print("Provided List: ", my_list)

    if option == "A" or option == "a":
        index = int(input("Enter index to access element: "))
        print("Provided index: ", index)
        print(f"Element at {index}th index: ", access(my_list, index))
    elif option == "M" or option == "m":
        index = int(input("Enter index to modify element: "))
        new_val = input("Enter new value: ")
        print("Modified List: ", modify(my_list, index, new_val))
    elif option == "S" or option == "s":
        start_index = int(input("Enter start index: "))
        end_index = int(input("Enter end index: "))
        print("Sliced List: ", slice_list(my_list, start_index, end_index))
    else:
        print("Invalid Option!")

list_game()