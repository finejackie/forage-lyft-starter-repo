from tire.tire import Tire

class OctoprimeTires(Tire):
    def __init__(self, wear_array):
        self.wear_array = wear_array

    def needs_service(self) -> bool:
        return sum(self.wear_array) >= 3
