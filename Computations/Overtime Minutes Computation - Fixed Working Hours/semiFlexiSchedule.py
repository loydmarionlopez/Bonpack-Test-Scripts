from datetime import datetime

schedule_start = datetime.strptime("06:00 PM", "%I:%M %p")
schedule_end = datetime.strptime("06:00 AM", "%I:%M %p")
time_in = datetime.strptime("05:39 PM", "%I:%M %p")
time_out = datetime.strptime("10:03 PM", "%I:%M %p")

required_minutes = 12 * 60  # Replace 8 depends on your working hours

regular_work_minutes = int((schedule_end - schedule_start).total_seconds() / 60)
actual_work_minutes = int((time_out - time_in).total_seconds() / 60)
undertime_minutes = max(0, required_minutes - actual_work_minutes)

early_overtime_minutes = 0
if time_in < schedule_start:
    early_overtime_minutes = int((schedule_start - time_in).total_seconds() / 60)

late_overtime_minutes = 0
if time_out > schedule_end:
    late_overtime_minutes = int((time_out - schedule_end).total_seconds() / 60)

total_overtime_minutes = early_overtime_minutes + late_overtime_minutes

print("Early Overtime minutes:", early_overtime_minutes)
print("Late Overtime minutes:", late_overtime_minutes)
print("Total Overtime minutes:", total_overtime_minutes)
print("Undertime minutes:", undertime_minutes)