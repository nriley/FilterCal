import filter
import requests
import urlparse

__all__ = ('add_alarms_to_events_in_ics',)

def add_alarms_to_events_in_ics(url):
    parsed_url = urlparse.urlparse(url)

    # validate that URL is valid
    
    assert parsed_url.scheme.lower() == 'https'
    assert parsed_url.netloc.lower().endswith('new-innov.com')
    
    response = requests.get(url)
    assert response.headers['Content-Type'] == 'text/calendar'

    # XXX multiple matching strings (weekend rounds, too)
    return filter.add_alarms_to_events_matching(response.text,
                                                'Volume Back Up/ Home Call')

if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    sys.stdout.write(add_alarms_to_events_in_ics(url))
