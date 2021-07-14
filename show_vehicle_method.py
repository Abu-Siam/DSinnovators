def show_vehicle_list(vehicle_list):
    id = 1
    for value in vehicle_list.values():
        print("------------------------------------------")
        print("VEHICLE NO. #", id)
        id += 1
        print(value)
