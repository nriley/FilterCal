from flask import Flask, abort, redirect, request
from fetch import add_alarms_to_events_in_ics
app = Flask(__name__)

@app.route('/nical/filter')
def filtercal():
    ics_url = request.args.get('ics_url')
    if not ics_url:
        abort(500)

    # return useful errors

    # XXX if error, redirect to the original URL
    
    # XXX have a 'test' option
    # XXX caching with E-Tag, If-Modified-Since

    return (add_alarms_to_events_in_ics(ics_url), 200,
            {'Content-Type': 'text/calendar'})
    
# return redirect(ics_url)
