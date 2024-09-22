# Import the dependencies.
import datetime as dt
import numpy as np


#################################################
# Database Setup
#################################################
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    return(
        f"Welcome to the Hawaii Climate Analysis API<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in MMDDYYYY format.</p>"
    )

@app.route("/api/v1.0/precipitaion")
def precipitation():
    prev_year=dt.date(2017, 8, 23) - dt.timedelta(days=365)

    precipitation = session.query(Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    
    session.close()
    precip = { date: prcp for date, prcp in precipitation}

    return jsonify(precip)

if __name__ == "__main__":
    app.run(debug=True)

# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
