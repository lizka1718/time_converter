def add_time(start, duration, start_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    

    if period == 'PM':
        start_hour += 12

    duration_hour, duration_minute = map(int, duration.split(':'))

    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + end_minute // 60
    end_minute %= 60


    days_passed = end_hour // 24
    end_hour %= 24

    if end_hour < 12:
        new_period = 'AM'
    else:
        new_period = 'PM'

    if end_hour % 12 != 0:
        end_hour = end_hour
    else:
        end_hour = 12
    
    if end_hour > 12:
        end_hour -= 12

    new_time = f"{end_hour}:{end_minute:02d} {new_period}"

    if start_day:
        day_index = days_of_week.index(start_day.capitalize())
        new_day_index = (day_index + days_passed) % 7
        new_time += f", {days_of_week[new_day_index]}"

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} later) "
    
    return new_time

print(add_time('11:43 PM', '24:20', 'tueSday'))

