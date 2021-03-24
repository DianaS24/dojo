fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
p1 = 0
p2 = 0

def move_player(value):
    global p1, p2

    if value == "w" or value == "W":
        p1 = 0
    if value == "s" or value == "S":
        p1 = 1
    if value == "d" or value == "D":
        p2 = p2 + 1
    if value == "a" or value == "A":
        p2 = p2 - 1

    if p2 > 5: p2 = 0
    if p2 < 0: p2 = 5

    return fighters[p1][p2]


print("Street Fighter 2")
print("-------------------")
print("Choose your player:")
print()
for x1 in range(len(fighters)):
    for x2 in range(len(fighters[x1])):
        print("[" + fighters[x1][x2] + "]")
    print()
print()

print("Press the w (up), s (down), a (left), d (right) keys to select or press the e key to exit: ")

key = ""
while key != "e":
    key = raw_input()
    print(move_player(key))
