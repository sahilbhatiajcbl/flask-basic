from flask import Flask
from flask_pymongo import PyMongo
from datetime import datetime
import json
    
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/jcbldb'
mongo = PyMongo(app)


@app.route('/add_order')
def add_order():
    orders = mongo.db.dashboard
    new_order = {
        'orderID': 'FEB2023002',
        'escID': 'FEB2023002ESC002',
        'status': 'OPEN',
        'priority': 'MEDIUM',
        'escSRC': 'Inbound calling',
        'custName': 'John Doe',
        'custMob': '555-1234',
        'escTYPE1': 'Cancel Request',
        'escTYPE2': 'Delay in Dispatch',
        'escTYPE3': 'Delay from procurement',
        'closingINF1': '',
        'closingINF2': '',
        'followUpTime': datetime(2023, 2, 14, 10, 30, 45),
        'createdAt': datetime.now(),
        'updatedAt': None
    }
    orders.insert_one(new_order)
    return 'Order added successfully'

@app.route("/get_dashboard")
def get_dashboard():
    dashboard = mongo.db.dashboard
    dashboardData = dashboard.find()
    res = {}
    for x in dashboardData:
        res.update(x)

    print(res)
    
    jsonres = json.dumps(res)

    print(jsonres)
    
    return jsonres