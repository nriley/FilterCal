from datetime import timedelta
from icalendar import Calendar, Alarm

__all__ = ('add_alarms_to_events_matching',)

def add_alarms_to_events_matching(ics, summary_substr,
                                  offset=timedelta(minutes=-30)):
    calendar = Calendar.from_ical(ics)
    alarm = Alarm()
    alarm.add('ACTION', 'DISPLAY')
    alarm.add('TRIGGER', offset)

    for event in calendar.walk(name='VEVENT'):
        if summary_substr in event['summary']:
            event.add_component(alarm)

    return calendar.to_ical()

if __name__ == '__main__':
    import sys
    ics = file(sys.argv[1]).read()
    ics = add_alarms_to_events_matching(ics, 'Volume Back Up/ Home Call')
    file('output.ics', 'w').write(ics)
