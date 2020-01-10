from flask import Flask, render_template, request
import Eventbrite

app = Flask(__name__)

@app.route('/')
def getHomePage():
    return render_template('home.html')


@app.route('/createEvent', methods=['POST','GET'])
def createEvent():
    if request.method=='POST':
        event_name = request.form['event_name']
        event_start_utc = request.form['event_start_utc']
        event_end_utc = request.form['event_end_utc']
        event_currency = request.form['event_currency']
        response = Eventbrite.createEvent(event_name, event_start_utc, event_end_utc, event_currency)
        if response == 200:
            data = 'New Event Created!'
        else:
            data = 'Error creating event'
        return render_template('createEvent.html', data=data)
    else:
        return render_template('createEvent.html')


@app.route('/deleteEvent', methods=['POST','GET'])
def deleteEvent():
    if request.method=='POST':
        eventId = request.form['eventId']
        response_json = Eventbrite.deleteEvent(eventId)
        result = response_json['deleted']
        if(result == True):
            data = 'The Event has been deleted!'
        else:
            data = 'Event Id does not exist'
        return render_template('deleteEvent.html', data=data)
    else:
        return render_template('deleteEvent.html')


@app.route('/getEvents')
def getEvents():
    return render_template('getEvents.html')


@app.route('/listEvents',  methods=['POST','GET'])
def listOrganizationEvents():
    if request.method=='POST':
        data = Eventbrite.listOrganizationEvents()
        return render_template('listEvents.html', data=data )


if __name__ == '__main__':
    app.run()
    app.config["DEBUG"] = True

