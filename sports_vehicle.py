from vehicle import Vehicle


class SportsVehicle(Vehicle):
    def __init__(self, model_no=None, car_type="Sports", engine_type="Oil", engine_power=None, tire_size=None,
                 turbo=None):
        super(SportsVehicle, self).__init__(model_no, car_type, engine_type, engine_power, tire_size)
        self.turbo = turbo

    def __str__(self):
        return ("Model Number : " + str(self.model_no) + "\nCar Type : " + str(
            self.car_type) + "\nEngine Type :  " + str(self.engine_type) +
                "\nEngine Power : " + str(self.engine_power) + " C.C." "\nTire Size : " + str(
                    self.tire_size) + " inch" + "\nTurbo : " + str(self.turbo))
