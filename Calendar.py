# imports
from icalendar import Calendar
from datetime import datetime
from pathlib import Path
import os
import pytz

urlpatterns = [
    path('', views.Calendar, name='Calendar'),
    path('Calendar/', views.EventListView.as_view(), name='Calendar'),
]
# init the calendar
cal = Calendar()

# Some properties are required to be compliant
cal.add('prodid', '-//My calendar product//example.com//')
cal.add('version', '2.0')
# Add subcomponents
event = Event()
event.add('name', 'Awesome Meeting')
event.add('description', 'Define the roadmap of our awesome project')
event.add('dtstart', datetime(2022, 1, 25, 8, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2022, 1, 25, 10, 0, 0, tzinfo=pytz.utc))

return date



