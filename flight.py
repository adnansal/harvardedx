class Flight:

    counter=1
    def __init__(self,origin,destination,duration):
        #Keep track of the flight
        self.id=Flight.counter
        Flight.counter+=1

        #Keep track of passengers.
        self.passengers=[]

        # Details of the flight
        self.origin=origin
        self.destination=destination
        self.duration=duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight origin: {self.destination}")
        print(f"Flight origin: {self.duration}")
        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def delay(self,amount):
        self.duration+=amount

    def add_passanger(self,p):
        self.passengers.append(p)
        p.flight_id=self.id

class Passenger:
    def __init__(self,name):
        self.name=name

def main():
    f1=Flight(origin="New York",destination="Bihar",duration=540)
    f1.delay(25)
    

    #create passenger
    alice=Passenger("Alice")
    bob=Passenger("Bob")

    f1.add_passanger(alice)
    f1.add_passanger(bob)
    f1.print_info()
    f2=Flight(origin="Orlando",destination="Hyderabad",duration=340)
    f2.print_info()




if __name__=="__main__":
    main()