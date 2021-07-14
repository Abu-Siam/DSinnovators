import add_vehicle_method as add_v
import remove_vehicle_method as rmv_v
import show_vehicle_method as shw_v

if __name__ == '__main__':
    print("***************************************************")
    print("DSINNOVATORS VEHICLE SHOWROOM COMMAND LINE SYSTEM")
    print("By- Abu Siam ")
    print("***************************************************")
    print("Press Ctrl + F2 (For PyCharm) / Ctrl + c  to exit the program.")
    vehicle_list = {}
    visitor_count = current_visitor = 30

    while (True):
        print("------------------------------------------")
        print("Select Operation:")
        print("1.Add Vehicle")
        print("2.Remove Vehicle")
        print("3.Show Vehicles")
        print("4.Show current visitor number")
        print("(Type '1/2/3/4' to select)")
        print("------------------------------------------")
        op_input = input("Option: ")
        print()
        if (op_input == '1'):
            visitor_count = add_v.add_vehicle(vehicle_list, visitor_count)
        elif (op_input == '2'):
            if (len(vehicle_list) == 0):
                print("Sorry there is no vehicle available currently in the showroom. Please add one.")
            rmv_v.remove_vehicle(vehicle_list)
        elif (op_input == '3'):
            if (len(vehicle_list) == 0):
                print("Sorry there is no vehicle available currently in the showroom. Please add one.")
            shw_v.show_vehicle_list(vehicle_list)
        elif (op_input == '4'):
            print("Total number of visitors are: ", int(visitor_count),".")
        else:
            print("Invalid option. Please try again.")

    # print(vehicle_list)
    # v.set_model_no(30)
# print(v)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
