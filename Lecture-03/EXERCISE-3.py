hours_worked = int(input("Enter number of hours worked: ")) 
hourly_payrate = float(input("Enter the hourly pay tate: "))
if hours_worked <= 40:
    total_pay = hours_worked * hourly_payrate
else:
    overtime_hours = hours_worked - 40
    total_pay = (40 * hourly_payrate) + (overtime_hours * hourly_payrate * 1.5)
print("Total pay: $", total_pay)