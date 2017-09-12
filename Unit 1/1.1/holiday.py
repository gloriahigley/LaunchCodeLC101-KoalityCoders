print("STUDIO 1")

days = dict([(0,"Sunday"), (1,"Monday"), (2,"Tuesday"),(3,"Wednesday"), (4,"Thursday"), (5,"Friday"),
             (6,"Saturday")])
holiday=int(input("On what number day will you leave? "))
stay_length=int(input("And for how long will you be going? "))
total_duration=holiday+stay_length
if total_duration > 6:
    day=total_duration%7
    print("\nou will be leaving on a " + days[day] + ".")
else:
    print("\nYou will be leaving on a " + days[total_duration] + ".")
exit=raw_input("\nPress any key to exit the program.")
