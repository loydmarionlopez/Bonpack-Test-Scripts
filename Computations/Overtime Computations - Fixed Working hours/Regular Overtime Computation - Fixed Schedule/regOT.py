def calculate_overtime(daily_rate, working_hours, reg_ot_hours, reg_ot_rate):
    # Calculate rate per hour
    
    fixed_working_hour = working_hours - 1
    
    rate_per_hour = daily_rate / fixed_working_hour
    
    print(f"Rate per Hour: {rate_per_hour}")
    
    
    # Calculate total for overtime
    overtime_total = rate_per_hour * reg_ot_hours * reg_ot_rate
    
    return overtime_total

daily_rate = 690
working_hours = 9
reg_ot_hours = 2
reg_ot_rate = 1.25

overtime_pay = calculate_overtime(daily_rate, working_hours, reg_ot_hours, reg_ot_rate)
print(f"Overtime Pay: {overtime_pay}")
