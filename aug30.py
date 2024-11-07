'''day = "Tuesday"

match day:
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a weekday.")'''

point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On the Y-axis at {y}")
    case (x, 0):
        print(f"On the X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")