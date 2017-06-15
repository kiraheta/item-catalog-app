#!/usr/bin/env python3

"""
This program is a web application that provides a list of items within a
variety of categories and allows authenticated users to post, edit, and delete
their own items.

@author: Kenny Iraheta
@Date: 2017-06-14
"""

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash


from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem, User

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


@app.route('/')
@app.route('/category/')
def showCategories():
    """Show all categories"""
    categories = session.query(Category).order_by(asc(Category.name))
    return "Hello World!"


@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    """Create new category"""
    return "Create new category"


@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    """Edit new category"""
    return "Edit category"


# Delete a category
@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    """Delete a category"""
    return "Delete a category"


@app.route('/category/<int:category_id>/<int:categoryItem_id>')
def showCategoryItem(category_id,categoryItem_id):
    """Show a category item"""
    return "Show a category item"


@app.route('/category/<int:category_id>/new/', methods=['GET', 'POST'])
def newCategoryItem(category_id):
    """Create a category item"""
    return "Create a category item"


@app.route('/category/<int:category_id>/<int:categoryItem_id>/edit', methods=['GET', 'POST'])
def editCategoryItem(category_id, categoryItem_id):
    """Edit a category item"""
    return "Edit a category item"


@app.route('/category/<int:category_id>/<int:categoryItem_id>/delete', methods=['GET', 'POST'])
def deleteCategoryItem(category_id, categoryItem_id):
    """Delete a category item"""
    return "Delete a category item"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
