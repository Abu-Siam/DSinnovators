def remove_vehicle(vehicle_list):
    model_no = input("Please enter the model number of car you want to remove: ")

    try:
        del vehicle_list[str(model_no)]
        print("Vehicle model no. ", model_no, " is removed.")
    except KeyError as ex:
        print("invalid model")
