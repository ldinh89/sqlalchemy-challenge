import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import os
import sys
print(os.path.dirname(__file__))

root_project_path = os.path.join(os.path.dirname(__file__))
sys.path.insert(0, root_project_path)

hawaii_path = os.path.join(root_project_path, "hawaii.sqlite")



engine = create_engine("sqlite:///"+hawaii_path)


Base = automap_base()
Base.prepare(engine, reflect = True)

print(Base.classes.keys())
Measurement = Base.classes.measurement
Station = Base.classes.station


app = Flask(__name__)


@app.route("/")
def Welcome():
    """List all available API routes."""
    return(
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start<br/>" 
        f"/api/v1.0/<start/end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date)

    session.close()
    precip_date = []
    for row in results:
        prep_dict = {}
        prep_dict["date"] = row.date
        prep_dict["tobs"] = row.tobs
        precip_date.append(prep_dict)
        return jsonify(precip_date)



@app.route("/api/v1.0/stations")
def staion():
    session = Session(engine)

    results = session.query(Station.name).all()

    staion_list = list(np.ravel(results))
    return jsonify(staion_list)

if __name__ == "__main__":
    app.run(debug=True)