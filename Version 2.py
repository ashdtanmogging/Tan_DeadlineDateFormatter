from datetime import date

event_title = input("Enter event title: ").strip()
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = date(year, month, day)

formatted_title = event_title.upper()
month_name = event_date.strftime("%B")      # Full month name (e.g., June)
weekday_name = event_date.strftime("%A")    # Full weekday name (e.g., Wednesday)
readable_date = f"{month_name} {event_date.day}, {event_date.year}"

print("\nFormatted Output:")
print("Event:", formatted_title)
print("Date:", readable_date)
print("Year:", event_date.year)
print("Month:", month_name)
print("Day:", event_date.day)
print("Weekday:", weekday_name)
