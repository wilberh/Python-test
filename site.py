# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# Python assignment - by Wilber H.

import json
import urllib.request
import time
import hashlib
from flask import Flask, render_template, request, redirect, url_for, session


# create the application object
app = Flask(__name__)

# Each function is a "view" (request handler). Use decorators to route URLs to views
@app.route('/home')
def home_page():
    # render a static template

    url = "http://octopart.com/api/v3/parts/search"

    # NOTE: Use your API key here (https://octopart.com/api/register)
    url += "?apikey=6af0e556" 

    args = [
    ('ad','adi'),
    ('start', 0),
    ('limit', 10)
    ]

    url += '&' + urllib.parse.urlencode(args)

    data = urllib.request.urlopen(url).read()
    search_response = json.loads(data)
    template_data = []
    temp = dict()

    # print number of hits
    print(search_response['hits'])

    # print results
    for result in search_response['results']:
        part = result['item']
        temp['brand-name'] = part['brand']['name']
        temp['part'] = part['mpn']
        template_data.append(temp)

    return render_template('home.html', template_data=template_data)

@app.route('/')
def index():
    # redirects to /home
    return redirect(url_for('home_page'))



if __name__ == '__main__':
    # The server will reload itself everytime there's a code change
    app.debug = True
    
    # Runs local server with the app and listens on all public IP addresses
    app.run(host = '0.0.0.0', port = 5000)  
        