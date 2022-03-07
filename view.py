from flask import Flask, abort, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from src import controller
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db= SQLAlchemy(app)
database_engine =  create_engine('sqlite:///app/database.db')

from src.models import ticket
from src import db_connector as dbc

db_c = dbc.DB_Connector()


@app.route('/')
def index():
	return '<h1>Hello, World!</h1>'

@app.route('/create_tickets.html', methods = ['GET', 'POST'])
def create_tickets():
	if request.method == 'GET':
		return render_template('create_tickets.html')
	
	if request.method == 'POST':
		title = request.form['Title']
		description = request.form['Description']
		status = request.form['Status']
		severity_level = request.form['SeverityLevel']
		id = request.form['ID']
		location = request.form['Location']
		building = request.form['Building']
		unit = request.form['Unit#']
		contact = request.form['Contact']
		additonalNotes = request.form['AdditionalNotes']
		return redirect('view_tickets.html')



@app.route('/view_tickets.html')
def view_tickets():
	ticket_list = [ticket.Ticket(title="Faucet Leak",
	description="Faucet is broken and leaking water", 
	status="Completed",
	severity_level="MILD",
	id="2",
	location="Bathroom", 
	building="Argenta Hall", 
	unit="23A", 
	contact="student@nevada.unr.edu", 
	additionalNotes="N/A"),]

	return render_template('view_tickets.html', tickets=ticket_list)


if __name__ == '__main__':
    app.run()