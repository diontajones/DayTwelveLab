class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print('Starting engine...')
        self.engine_on = True

    def make_noise(self):
        print('Beep beep!')


class Truck(Vehicle):
    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
        self.cargo = False

    def load_cargo(self):
        print('Loading the truck bed...')
        self.cargo = True


class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        Vehicle.__init__(self, make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print('Vroom vroom!')

print('Hello')
print('Welcome to DJ Bikes & Trucks!')

bike1 = Motorcycle('Harley', 0, 50000, 300)
bike2 = Motorcycle('Ducati', 1000, 50000, 250)
bike3 = Motorcycle('Honda', 20000, 50000, 240)

truck1 = Truck('Toyota', 1000, 30000)
truck2 = Truck('Ford', 200000, 5000)
truck3 = Truck('Chevy', 50000, 20000)

bikes = [bike1, bike2, bike3]
trucks = [truck1, truck2, truck3]
vehicles_to_compare = []


while True:
    selection = input('Would you like to use bikes or trucks? (b or t) ')
    if selection == 'b':
        for index, bike in enumerate(bikes):
            print(f'{index + 1}: {bike.make}: with {bike.miles} miles and a top speed of {bike.top_speed} costs {bike.price}')
        while True:
            compare_choice = input('Would you like to compare one of these vehicles? (y or n) ')
            if compare_choice == 'y':
                compare_number = input('Enter the number of the vehicle you want to compare: ')
                if compare_number == '1':
                    print(f'{bike1.make} added!')
                    vehicles_to_compare.append(bike1)
                if compare_number == '2':
                    print(f'{bike2.make} added!')
                    vehicles_to_compare.append(bike2)
                if compare_number == '3':
                    print(f'{bike3.make} added!')
                    vehicles_to_compare.append(bike3)
            elif compare_choice == 'n':
                leave1 = input('Would you like to leave? (y or n) ')
                if leave1 == 'y':
                    print('Goodbye!')
                    break
                if leave1 == 'n':
                    continue
            else:
                print('Please select y or n!')
        while True:
            x = input('Would you like to compare your vehicle now? (y or n) ')
            if x == 'n':
                continue
            elif x == 'y':
                for vehicle in vehicles_to_compare:
                    print(f'{vehicle.make}: with {vehicle.miles} miles cost ${vehicle.price}')
                    vehicle.make_noise()
                break
            else:
                print('Please select y or n!')
    elif selection == 't':
        for index, truck in enumerate(trucks):
            print(f'{index + 1}: {truck.make}: with {truck.miles} miles costs {truck.price}')
        while True:
            compare_choice = input('Would you like to compare one of these vehicles? (y or n) ')
            if compare_choice == 'y':
                compare_number = input('Enter the number of the vehicle you want to compare: ')
                if compare_number == '1':
                    print(f'{truck1.make} added!')
                    vehicles_to_compare.append(truck1)
                if compare_number == '2':
                    print(f'{truck2.make} added!')
                    vehicles_to_compare.append(truck2)
                if compare_number == '3':
                    print(f'{truck3.make} added!')
                    vehicles_to_compare.append(truck3)
            elif compare_choice == 'n':
                leave2 = input('Would you like to leave? (y or n) ')
                if leave2 == 'y':
                    print('Goodbye!')
                    break
                if leave2 == 'n':
                    continue
            else:
                print('Please select y or n!')
        while True:
            x = input('Would you like to compare your vehicle now? (y or n) ')
            if x == 'n':
                continue
            elif x == 'y':
                for vehicle in vehicles_to_compare:
                    print(f'{vehicle.make}: with {vehicle.miles} miles cost ${vehicle.price}')
                    vehicle.make_noise()
                break
            else:
                print('Please select y or n!')
    else:
        print('Invalid Option')
        continue















