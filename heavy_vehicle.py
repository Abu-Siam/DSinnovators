from vehicle import Vehicle


class HeavyVehicle(Vehicle):
    def __init__(self, model_no=None, car_type="Heavy", engine_type="Diesel", engine_power=None, tire_size=None,
                 weight="None"):
        super(HeavyVehicle, self).__init__(model_no, car_type, engine_type, engine_power, tire_size)
        self.weight = weight

    def __str__(self):
        return ("Model Number : " + str(self.model_no) + "\nCar Type : " + str(
            self.car_type) + "\nEngine Type :  " + str(self.engine_type) +
                "\nEngine Power : " + str(self.engine_power) + " C.C." "\nTire Size : " + str(
                    self.tire_size) + " inch" + "\nWeight : " + str(self.weight) + " kg")
