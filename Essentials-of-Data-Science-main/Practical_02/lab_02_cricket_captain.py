# Practical 02 - Lab Assignment 2
# Choose captain of cricket team using dictionary

team = {}

print("Enter name and height of 11 cricket players")

for i in range(1, 12):
    name = input(f"Player {i} name: ")
    height = float(input(f"Player {i} height in cm: "))
    team[name] = height

captain = max(team, key=team.get)

print("\nCricket Team")
for player, height in team.items():
    print(player, ":", height, "cm")

print("\nCaptain of the team:", captain)
print("Height:", team[captain], "cm")
