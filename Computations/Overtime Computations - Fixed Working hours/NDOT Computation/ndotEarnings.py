def calculate_overtime(daily_rate, working_hours, ndot_hours, ndot_rate):
    
    fixed_working_hours = working_hours - 1
    # Calculate rate per hour
    rate_per_hour = daily_rate / fixed_working_hours
    
    print(f"Rate per Hour: {rate_per_hour}")
    # Calculate total for overtime
    overtime_total = rate_per_hour * ndot_hours * ndot_rate
    
    return overtime_total

daily_rate = 645
working_hours = 9
ndot_hours = 2
ndot_rate = 1.25

overtime_pay = calculate_overtime(daily_rate, working_hours, ndot_hours, ndot_rate)
print(f"Overtime Pay: {overtime_pay}")
