import datetime

weekdays = { 'Monday':0,'Tuesday':1,'Wednesday':2,
             'Thursday':3,'Friday':4,'Saturday':5,
             'Sunday':6 }

months = { 'January':1,'February':2,'March':3,'April':4,
           'May':5,'June':6,'July':7,'August':8,'September':9,
           'October':10,'November':11,'December':12 }

def main():
   date_format = "%B %d, %Y"
   year = int(input("Please enter the year: "))
   holidays = {
      "New Year's Day": datetime.date(year,months['January'],get_adjusted_date(year, months['January'], 1)).strftime(date_format),
      "Birthday of Martin Luther King Jr.": datetime.date(year,months['January'],get_nth_weekday_of_month(year,months['January'],'Monday',3)).strftime(date_format),
      "Washington's Birthday": datetime.date(year,months['February'],get_nth_weekday_of_month(year,months['February'],'Monday',3)).strftime(date_format),
      "Memorial Day": datetime.date(year,months['May'],get_last_weekday_of_month(year,months['May'],'Monday')).strftime(date_format),
      "Juneteenth National Independence Day": datetime.date(year,months['June'],get_adjusted_date(year,months['June'],19)).strftime(date_format),
      "Independence Day": datetime.date(year,months['July'],get_adjusted_date(year,months['July'],4)).strftime(date_format),
      "Labor Day": datetime.date(year,months['September'],get_nth_weekday_of_month(year,months['September'],'Monday',1)).strftime(date_format),
      "Columbus Day": datetime.date(year,months['October'],get_nth_weekday_of_month(year,months['October'],'Monday',2)).strftime(date_format),
      "Veterans Day": datetime.date(year,months['November'],get_adjusted_date(year,months['November'],11)).strftime(date_format),
      "Thanksgiving": datetime.date(year,months['November'],get_nth_weekday_of_month(year,months['November'],'Thursday',4)).strftime(date_format),
      "Christmas Day": datetime.date(year,months['December'],get_adjusted_date(year,months['December'],25)).strftime(date_format)
   }
   for key, value in holidays.items():
      print(f"{key} falls on {value}")
   
def get_nth_weekday_of_month(year, month, weekday, nth):
   if nth < 1 or nth > 5:
      raise Exception(f"{nth} is an invalid 'nth' day of the month")
   if weekday not in weekdays:
      raise Exception(f"{weekday} is an invalid weekday")
   weekday_count = 0
   first_day = datetime.date(year, month, 1)
   for day in range(1, 32):
      current_date = datetime.date(year, month, day)
      if current_date.weekday() == weekdays[weekday]:
         weekday_count += 1
         if weekday_count == nth:
            return day
   raise Exception(f"There is no {nth} {weekday} in {month} {year}")

def get_last_weekday_of_month(year, month, weekday):
   if weekday not in weekdays:
      raise Exception("{weekday} is an invalid weekday")
   last_day = datetime.date(year, month, 1)
   last_day = last_day.replace(day=28)
   while last_day.month == month:
      last_day += datetime.timedelta(days=1)

   while last_day.weekday() != weekdays[weekday]:
      last_day -= datetime.timedelta(days=1)
   return last_day.day

def get_adjusted_date(year, month, day):
   input_date = datetime.date(year, month, day)
   if input_date.weekday() == weekdays['Saturday']:
      adjusted_date = input_date - datetime.timedelta(days=1)
   elif input_date.weekday() == weekdays['Sunday']:
      adjusted_date = input_date + datetime.timedelta(days=1)
   else:
      adjusted_date = input_date
   return adjusted_date.day
if __name__ == '__main__':
   main()
