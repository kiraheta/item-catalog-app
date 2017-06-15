#!/usr/bin/env python3

"""
This program is a web application that provides a list of items within a
variety of categories and allows Authenticated users to post, edit, and delete
their own items.

@author: Kenny Iraheta
@Date: 2017-06-14
"""

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash


from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


# Connect to Database and create database session
engine = create_engine('sqlite:///categoryitems.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
