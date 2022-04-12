def add_time(start, dur, weekday=0):
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    # Express start in terms of minutes since start of that day
    h = int(start[:start.find(":")])
    m = int(start[start.find(":")+1:start.find(" ")])
    pm = bool("PM" in start)
    start_time = h*60+m+int(pm)*12*60
    # Express duration in minutes
    dur_h = int(dur[:dur.find(":")])
    dur_m = int(dur[dur.find(":")+1:])
    dur_time = dur_h*60+dur_m
    # Add duration
    final_time = start_time+dur_time
    # Passes days, pm, hour and minute calculated
    days_passed = final_time//1440
    final_time = final_time%1440
    final_pm = bool(final_time>=720)
    final_h = final_time//60-int(final_pm)*12
    final_m = final_time%60
    # Construct string
    final_str = str(final_h)+":"
    if final_m<10:
        final_str += "0"
    final_str += str(final_m)
    if final_pm:
        final_str += " PM"
    else:
        final_str += " AM"
    if weekday:
        final_str += ", "+str(weekdays[(weekdays.index(weekday.lower())+days_passed)%7]).capitalize()
    if days_passed==1:
        final_str += " (next day)"
    elif days_passed>1:
        final_str += f" ({days_passed} days later)"
    return final_str

start = "11:43 PM"
dur = "24:20"
weekday = "tueSday"
print(add_time(start, dur, weekday))
