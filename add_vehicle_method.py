from sports_vehicle import SportsVehicle
from normal_vehicle import NormalVehicle
from heavy_vehicle import HeavyVehicle


def valid_engine_power():
    while (True):
        try:
            engine_power = float(input("Power of engine(C.C.): "))
            print("")
            break
        except ValueError as ex:
            print("Invalid input. Please try again.")
            continue

    return engine_power


def valid_tire_size():
    while (True):
        try:
            tire_size = float(input("Size of tire (Inch) : "))
            print("")
            break;


        except ValueError as ex:
            print("Invalid input. Please try again.")
            continue
    return tire_size


def valid_weight():
    while (True):
        try:
            weight = float(input("Weight of the vehicle(kg): "))

            break
        except ValueError as ex:
            print("Invalid input. Please try again.")
            continue
    return weight


def add_vehicle(vehicle_list, visitor_count):
    model_no = input("Model number of car: ")
    print("")
    if model_no in vehicle_list:
        print("This model number already exists. Please try again.")
        return 0
    while (True):
        print("Type of car : ")
        print("1.Normal Vehicle \t 2.Sports Vehicle \t 3.Heavy Vehicle")
        print("(Type '1/2/3' to select)")

        car_option = input()
        print("")
        if (car_option == '1'):
            car_type = "Normal"
            while (True):
                print("Type of engine: ")
                print("1.Oil \t 2.Gas \t 3.Diesel")
                print("(Type '1/2/3' to select)")
                engine_option = input()
                print("")
                if (engine_option == '1'):
                    engine_type = "Oil"
                    break
                elif (engine_option == '2'):
                    engine_type = "Gas"
                    break
                elif (engine_option == '3'):
                    engine_type = "Diesel"
                    break
                else:
                    print("Invalid choice. Please try again.")
                    continue
            engine_power = valid_engine_power()
            tire_size = valid_tire_size()

            new_vehicle = NormalVehicle(model_no, car_type, engine_type, engine_power, tire_size)
            vehicle_list[str(model_no)] = new_vehicle
            break
        elif (car_option == '2'):

            visitor_count += 20
            car_type = "Sports"
            engine_type = "Oil"
            engine_power = valid_engine_power()
            tire_size = valid_tire_size()
            while (True):

                turbo_option = input("Has turbo? (Type 'y/n')")
                if (turbo_option == 'y'):
                    turbo = "Yes"
                    break
                elif (turbo_option == 'n'):
                    turbo = "No"
                    break
                else:
                    print("Invalid input.Please try again.")
                    continue

            new_vehicle = SportsVehicle(model_no, car_type, engine_type, engine_power, tire_size, turbo)
            vehicle_list[str(model_no)] = new_vehicle
            break
        elif (car_option == '3'):
            car_type = "Heavy"
            engine_type = "Diesel"
            engine_power = valid_engine_power()
            tire_size = valid_tire_size()
            weight = valid_weight()

            new_vehicle = HeavyVehicle(model_no, car_type, engine_type, engine_power, tire_size, weight)
            vehicle_list[str(model_no)] = new_vehicle
            break
        else:
            print("Invalid choice. Please try again.")
            continue
    print("\nVehicle model no. ", model_no, " is added.")
    return visitor_count
