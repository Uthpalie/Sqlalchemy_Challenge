# Import the dependencies.

#%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`

Base = automap_base()

# Use the Base class to reflect the database tables

Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`

Station = Base.classes.station
Measurement = Base.classes.measurement

# Create a session

session = Session(engine)

#################################################
# Flask Setup
#################################################

from flask import Flask, jsonify

prcp_12months = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date < '2017-08-23', Measurement.date > '2016-08-22').\
    order_by(Measurement.date).all()
prcp_12months

prcp_dict = {date: prcp for date, prcp in prcp_12months}


station_counts = session.query(Measurement.station, func.count(Measurement.prcp)).\
    group_by(Measurement.station).all()

stations_dict = {station: prcp for station, prcp in station_counts}

temp_12months = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date < '2017-08-23', Measurement.date > '2016-08-22').\
    filter(Measurement.station == 'USC00519281').\
    order_by(Measurement.date).all()

temp_12months_dict = {date: tobs for date, tobs in temp_12months}


app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def welcome():
    return (
        f"Welcome to my homepage.<br/><br/>"
        f"This is the list of all available routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(prcp_dict)


@app.route("/api/v1.0/stations")
def stations():
    return jsonify(stations_dict)

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(temp_12months_dict)


if __name__=="__main__":
    app.run(debug=True)




