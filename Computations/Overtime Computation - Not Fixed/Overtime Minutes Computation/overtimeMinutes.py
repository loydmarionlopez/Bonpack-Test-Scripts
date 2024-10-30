from datetime import datetime

# Employee's schedule
start_time = "07:30 AM" # Replace the Start time
end_time = "04:30 PM" # Replace the End time


time_in = "04:42 AM" # Replace the Time In
time_out = "05:04 PM" # Replace the Time Out

fmt = "%I:%M %p"
schedule_start = datetime.strptime(start_time, fmt)
schedule_end = datetime.strptime(end_time, fmt)
actual_in = datetime.strptime(time_in, fmt)
actual_out = datetime.strptime(time_out, fmt)


early_in_minutes = (schedule_start - actual_in).seconds // 60 if actual_in < schedule_start else 0
late_out_minutes = (actual_out - schedule_end).seconds // 60 if actual_out > schedule_end else 0


total_overtime_minutes = early_in_minutes + late_out_minutes
total_overtime_minutes

# Open this link for Reference:   https://prnt.sc/4Awg0REQGI46 