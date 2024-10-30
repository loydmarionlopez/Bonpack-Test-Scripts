def calculate_overtime(daily_rate, working_hours, reg_ot_hours, reg_ot_rate):
    # Calculate rate per hour
    
    
    rate_per_hour = daily_rate / working_hours
    
    print(f"Rate per Hour: {rate_per_hour}")
    
    overtime_total = rate_per_hour * reg_ot_hours * reg_ot_rate
    
    return overtime_total

daily_rate = 645
working_hours = 9
reg_ot_hours = 2
reg_ot_rate = 1.25

overtime_pay = calculate_overtime(daily_rate, working_hours, reg_ot_hours, reg_ot_rate)
print(f"Overtime Pay: {overtime_pay}")
