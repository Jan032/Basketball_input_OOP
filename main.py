class BasketballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


print("Enter some Basketball player's data!")

first_name = input("First name: ")
last_name = input("Last name: ")
height_cm = input("Enter the height of the player (in cm): ")
weight_kg = input("Enter the weight of the player (in kg): ")
points = input("Enter player's points this season: ")
rebounds = input("Enter player's rebounds: ")
assists = input("player's assists: ")

new_player = BasketballPlayer(first_name=first_name,
                              last_name=last_name,
                              height_cm=int(height_cm),
                              weight_kg=int(weight_kg),
                              points=int(points),
                              rebounds=int(rebounds),
                              assists=int(assists))

with open("players.json", "w") as basketball_file:
    basketball_file.write(str(new_player.__dict__))

print("player info added successfully!")
print(f"player's data: {first_name} {last_name}, "
      f"height: {height_cm}cm, weight: {weight_kg}kg, "
      f"points(avg): {points}, rebounds(avg): {rebounds},"
      f" assists: {assists}")
