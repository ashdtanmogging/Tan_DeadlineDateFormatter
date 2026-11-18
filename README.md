# Event Deadline Formatter (Version 2)

## Description
A date-formatting tool designed to help classmates clearly read activity deadlines by converting numeric dates into full calendar dates with weekdays.

## How to Run
1. Ensure Python 3 is installed on your computer.
2. Run the file in your terminal: `python event_deadline_v2.py`
3. Enter the event title and numeric year, month, and day.

## What Changed in Version 2
- **Date Object Integration:** Imported Python's `datetime` module (`date`) to validate and process calendar dates.
- **Readable Date Output:** Used `.strftime("%B")` to display the full month name and `.strftime("%A")` to automatically determine the day of the week.
- **Text Formatting:** Added `.strip()` and `.upper()` to make the event title stand out cleanly.
