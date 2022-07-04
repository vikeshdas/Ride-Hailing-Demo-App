"""
    backend api for find cab,sortest distance from source to destination and source to cab distance 
"""

from flask import Flask,request,json
from flask_cors import CORS
import json
from json import JSONEncoder

import numpy

from cab_service import Cab


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

@app.route("/map", methods=['GET','POST'])
def map():
    """
        generate graph matrix and traffic matrix,with diagonal cell zeor represent ith node is not connected to ith node,if (i,j)th cell in matrix is zeor means ith node is not connected to jth node

        return:
            two matrix graph and traffic
    """
    graph,traffic=cabobj.map()
    all_data={'graph':graph,'traffic':traffic}
    encodedNumpyData = json.dumps(all_data, cls=NumpyArrayEncoder)
    return encodedNumpyData

@app.route("/find-driver", methods=['POST'])
def find_driver():
    """
        find the driver near source node,find path node from source to destination,sourceto destination distance and source to cab distance
        return:
            object,with driver accepted ride or not,source to cab,source 
            to destinaiton distance
    """
    source=request.form.get("source", type=int)
    destination=request.form.get("destination", type=int)

    accept,source_to_cab,source_to_destination,Path,trafic=cabobj.find_cab(source,destination)
    accept=float(accept)
    source_to_cab=float(source_to_cab)
    source_to_destination=float(source_to_destination)
    all_data={'accep':accept,'source_to_cab':source_to_cab,'srctodes':source_to_destination,'path':Path,'traffic':trafic}
    
    encodedNumpyData = json.dumps(all_data, cls=NumpyArrayEncoder) 
    return encodedNumpyData 


if __name__ == '__main__':
    cabobj=Cab()
    app.run(debug=True)
