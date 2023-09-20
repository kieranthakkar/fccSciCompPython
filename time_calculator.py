def add_time(start: str, duration: str, day: str = None) -> str:
    twelveTime, AMorPM = start.split(" ")
    twelveHours, startMinutes = twelveTime.split(":")

    if AMorPM == "PM":
        militaryStartHours = int(twelveHours) + 12
        # militaryTime define
        pass
    else:
        militaryStartHours = int(twelveHours)

    # Prepare duration input.  1 string -> 2 integers (hours + minutes)
    addHours, addMinutes = duration.split(":")
    addHours, addMinutes = int(addHours), int(addMinutes)

    # Addition
    militaryNewHours: int = militaryStartHours + addHours
    overflowMinutes = int(startMinutes) + addMinutes
    if overflowMinutes >= 60:
        newMinutes = overflowMinutes - 60
        militaryNewHours += 1
    else:
        newMinutes: int = overflowMinutes

    # Convert newMinutes to string, so we can make it like 4:01 or 12:00 instead of 4:1 or 12:0
    finalMinutes: str = str(newMinutes)
    if len(finalMinutes) < 2:
        finalMinutes = "0" + finalMinutes

    # Over 24 hours?
    days = militaryNewHours // 24
    if days == 1:
        militaryNewHours -= 24
        addon = " (next day)"
    elif days > 1:
        militaryNewHours -= 24*days
        addon = f" ({days} days later)"
    else:
        addon = None

    # AM or PM check on the new time
    if militaryNewHours == 12:
        newAMorPM = "PM"
        finalHours: str = str(militaryNewHours)
    elif militaryNewHours > 12:
        newAMorPM = "PM"
        finalHours: str = str(militaryNewHours - 12)
    elif militaryNewHours == 0:
        finalHours: str = "12"
        newAMorPM = "AM"
    else:
        newAMorPM = "AM"
        finalHours: str = str(militaryNewHours)

    # Day of the week finder
    week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if day is not None :
        if addon is not None:
            for i in range(len(week)):
                if week[i] == day.capitalize():
                    newDayIterable = i + days
                    newDayIterable %= 7
                    addon = ", " + week[newDayIterable] + addon
        else:
            addon = ", " + day

    finalTime = f"{finalHours}:{finalMinutes}"

    if addon is None:
        new_time = finalTime + " " + newAMorPM
    else:
        new_time = finalTime + " " + newAMorPM + addon

    return new_time