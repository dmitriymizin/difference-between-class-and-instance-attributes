

class Building:
    total = 0

    def __init__(self):
        for i in range(1, 41):
            Building.total += 1
            print(f'building_house {i}, total {Building.total}')

building_house = Building()



