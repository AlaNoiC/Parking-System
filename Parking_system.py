class ParkingSlot:
    def __init__(self, full_capacity):
        self.full_capacity = full_capacity
        self.no = self.full_capacity
        self.slot_dict = {f'A{i}': False for i in range(1, self.no + 1)}

    def get_available_slot(self):
        new_slot = {k: v for k, v in self.slot_dict.items() if v == False}
        return list(new_slot.keys())

    def insert_car(self, enter_slot_insert):
        if enter_slot_insert in self.slot_dict:
            if self.slot_dict[enter_slot_insert]:
                print("Already Parked")
            else:
                self.slot_dict[enter_slot_insert] = True
                print(f"Slot {enter_slot_insert} selected!!")
        else:
            print("Invalid slot ! Please enter a code from the list given !!!")

    def remove_car(self, enter_slot_remove):
        if enter_slot_remove in self.slot_dict:
            if not self.slot_dict[enter_slot_remove]:
                print("empty slot no car to remove!!")
            else:
                self.slot_dict[enter_slot_remove] = False
                print(f"Slot {enter_slot_remove} removed!!")
        else:
            print("Invalid slot ! Please enter a code from the list given !!!")

full_capacity = int(input("Enter the capacity of the ParkingSlot:"))
test = ParkingSlot(full_capacity)
print(test.get_available_slot())

enter_slot_remove = f"A{int(input('A')or'1')}"
test.remove_car(enter_slot_remove)