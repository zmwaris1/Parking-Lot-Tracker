class ParkingLotTracker:

    def __init__(self, MAX_SIZE=40):
        self.slots = [i for i in range(1, MAX_SIZE+1)]
        self.vehicles = {}

    def printSlots(self):
        return self.slots
    
    def registerVehicle(self, id):
        if len(id) == 0:
            return 'Enter a valid Vehicle Id'
        
        if id not in self.vehicles:
            if len(self.slots) > 0:
                slot = self.slots.pop(0)
                return self._assignSpot(id, slot)
            else:
                return 'No parking space'
        return 'Vehicle already parked.'
    
    def _assignSpot(self, id, spot):
        self.vehicles[id] = spot
        return f'Spot for vehicle {id} is {spot}'
    
    def getDetails(self, id):
        if id in self.vehicles:
            spot = self.vehicles[id]
            if spot <= 20:
                level = 'A'
            else:
                level = 'B'
            d = {'level':level, 'spot':spot}
            return d
        else:
            return 'Vehicle not parked here.'
        
    def emptySpot(self, id):
        if id in self.vehicles:
            slot = self.vehicles.pop(id)
            self.slots.append(slot)
            self.slots.sort()
            return self.printSlots()
        return 'Vehicle Id is not present'
        
    
obj = ParkingLotTracker()


while True:
    user_input = input("Enter Vehicle Id or q to quit: ")
    if user_input.lower() == 'q':
        break
    second_input = input("Enter 'R' to register, 'D' to get details of parking, 'E' to empty parking spot: ")
    if second_input.upper() == 'R':
        print(obj.registerVehicle(user_input))
    elif second_input.upper() == 'D':
        print(obj.getDetails(user_input))
    elif second_input.upper() == 'E':
        print(obj.emptySpot(user_input))
    else:
        'Enter Valid Input.'

