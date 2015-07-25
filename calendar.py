// Calendar
import calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
result = cal.formatmonth(2015,1)
print result

//HTML calendar
htmlCal = calendar.HTMLCalendar(calendar.SUNDAY)
result1 = htmlCal.formatmonth(2015,1)
print result1
