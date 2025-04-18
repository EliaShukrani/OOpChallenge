
from Pet import Pet

print("Creating pet: Max")
max_pet = Pet("Max")

print(f"{max_pet.name} is eating...")
max_pet.eat()

print(f"{max_pet.name} is playing...")
max_pet.play()

print(f"{max_pet.name} is sleeping...")
max_pet.sleep()


max_pet.train("roll over")
max_pet.train("play dead")


max_pet.get_status()
