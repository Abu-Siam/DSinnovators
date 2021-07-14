class Vehicle:
    def __init__(self, model_no=None, car_type=None, engine_type=None, engine_power=None, tire_size=None):
        # self.car_type = car_type
        self.car_type = car_type
        self.model_no = model_no
        self.engine_type = engine_type
        self.engine_power = engine_power
        self.tire_size = tire_size

    def set_model_no(self, model_no):
        self.model_no = model_no

    def get_model_no(self):
        return self.model_no

    def set_engine_type(self, engine_type):
        self.engine_type = engine_type

    def get_engine_type(self):
        return self.engine_type

    def set_engine_power(self, engine_power):
        self.engine_power = engine_power

    def get_engine_power(self):
        return self.engine_power

    def set_tire_size(self, tire_size):
        self.tire_size = tire_size

    def get_tire_size(self):
        return self.tire_size
