import filter

import requests

def add_alarms_to_events_in_ics(url):
    response = requests.get(url)
    return filter.add_alarms_to_events_matching(response.text,
                                                'Volume Back Up/ Home Call')

if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    sys.stdout.write(add_alarms_to_events_in_ics(url))

# XXX if error, redirect to the original URL
