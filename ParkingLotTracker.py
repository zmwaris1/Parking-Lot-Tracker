class ParkingLotTracker:
    def __init__(self, MAX_SIZE=40):
        """Constructor method to initialize the parking spots based on MAX_SIZE and a dictionary to add parked vehicles."""
        self.slots = [i for i in range(1, MAX_SIZE + 1)]
        self.vehicles = {}

    def printSlots(self):
        """Prints the empty slots that could be used for parking."""
        return self.slots

    def registerVehicle(self, id):
        """Registers vehicle id to initiate parking"""
        if len(id) == 0:
            return "Enter a valid Vehicle Id"

        if id not in self.vehicles:
            if len(self.slots) > 0:
                slot = self.slots.pop(0)
                return self._assignSpot(id, slot)
            else:
                return "No parking space"
        return "Vehicle already parked."

    def _assignSpot(self, id, spot):
        """Assigns a parking spot when vehicle is registered."""
        self.vehicles[id] = spot
        return f"Spot for vehicle {id} is {spot}"

    def getDetails(self, id):
        """Extract the details of the vehicle parked in the parking lot."""
        if id in self.vehicles:
            spot = self.vehicles[id]
            if spot <= 20:
                level = "A"
            else:
                level = "B"
            d = {"level": level, "spot": spot}
            return d
        else:
            return "Vehicle not parked here."

    def emptySpot(self, id):
        """Remove the vehicle from parking lot and display the remaining parking spots."""
        if id in self.vehicles:
            slot = self.vehicles.pop(id)
            self.slots.append(slot)
            self.slots.sort()
            return self.printSlots()
        return "Vehicle Id is not present"


obj = ParkingLotTracker()


while True:
    user_input = input("Enter Vehicle Id or q to quit: ")
    if user_input.lower() == "q":
        break
    second_input = input(
        "Enter 'R' to register, 'D' to get details of parking, 'E' to empty parking spot: "
    )
    if second_input.upper() == "R":
        print(obj.registerVehicle(user_input))
    elif second_input.upper() == "D":
        print(obj.getDetails(user_input))
    elif second_input.upper() == "E":
        print(obj.emptySpot(user_input))
    else:
        "Enter Valid Input."
