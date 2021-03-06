"""Test all methods dealing with user endpoints
"""
import unittest
import json
import os

import sys  # fix import errors
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.ride_one = {"driver" : "John Doe" , "start_loc" : "Nairobi" , "end_loc" : "Thika",
            "departure_time" : "1800HRS" , "date" : "13/6/2018" , "route" : "Thika Super Highway" , "cost" : "400"}
        self.ride_two = {"driver" : "Jane Doe" , "start_loc" : "Nairobi", "end_loc" : "Syokimau",
            "departure_time" : "0900HRS", "date" : "14/6/2018" , "route" : "Mombas Road" , "cost" : "200"}
        self.request = { "pickup_loc" : "Roysambu"}
    '''
    GIVEN a user
    WHEN they view rides
    THEN test that all rides are returned
    '''
    def test_rides(self):
        response = self.app.get('/api/v1/rides', data = json.dumps(self.ride_two) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
    
    '''
    GIVEN a user
    WHEN they view a single ride
    THEN test that the ride is returned
    '''
    def test_ride(self):
        response = self.app.get('/api/v1/rides/1', data = json.dumps(self.ride_two) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
    
    '''
    GIVEN a user
    WHEN they want to request a ride
    THEN test that they can send a request
    '''
    def test_ride_request(self):
        response = self.app.post('/api/v1/rides/1/requests', data = json.dumps(self.request) , content_type = 'application/json')
        self.assertEqual(response.status_code, 201)