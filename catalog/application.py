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


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return "The current session state is %s" % login_session['state']


@app.route('/category/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[i.serialize for i in categories])


@app.route('/category/<int:category_id>/categoryItem/JSON')
def categoryItemJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(CategoryItem).filter_by(
        category_id=category_id).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


@app.route('/category/<int:category_id>/categoryItem/<int:categoryItem_id>/JSON')
def menuItemJSON(category_id, categoryItem_id):
    Category_Item = session.query(CategoryItem).filter_by(id=categoryItem_id).one()
    return jsonify(Category_Item=Category_Item.serialize)


@app.route('/')
@app.route('/category/')
def showCategories():
    """Show all categories"""
    categories = session.query(Category).order_by(asc(Category.name))
    return render_template('categories.html', categories=categories)


@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    """Create new category"""
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')


@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    """Edit new category"""
    editedCategory = session.query(
        Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            return redirect(url_for('showCategories'))
    else:
        return render_template(
            'editCategory.html', category=editedCategory)


@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    """Delete a category"""
    categoryToDelete = session.query(
        Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        session.commit()
        return redirect(
            url_for('showCategories', category_id=category_id))
    else:
        return render_template(
            'deleteCategory.html', category=categoryToDelete)


@app.route('/category/<int:category_id>')
@app.route('/category/<int:category_id>/categoryItem/')
def showCategoryItem(category_id):
    """Show a category item"""
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(CategoryItem).filter_by(
        category_id=category_id).all()
    return render_template('categoryItems.html', items=items, category=category)


@app.route('/category/<int:category_id>/categoryItem/new/', methods=['GET', 'POST'])
def newCategoryItem(category_id):
    """Create a category item"""
    if request.method == 'POST':
        newItem = CategoryItem(name=request.form['name'], description=request.form[
                           'description'], category_id=category_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('showCategoryItem', category_id=category_id))
    else:
        return render_template('newCategoryItem.html', category_id=category_id)


@app.route('/category/<int:category_id>/categoryItem/<int:categoryItem_id>/edit', methods=['GET', 'POST'])
def editCategoryItem(category_id, categoryItem_id):
    """Edit a category item"""
    editedItem = session.query(CategoryItem).filter_by(id=categoryItem_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showCategoryItem', category_id=category_id))
    else:

        return render_template(
            'editCategoryItem.html', category_id=category_id, categoryItem_id=categoryItem_id, item=editedItem)


@app.route('/category/<int:category_id>/categoryItem/<int:categoryItem_id>/delete', methods=['GET', 'POST'])
def deleteCategoryItem(category_id, categoryItem_id):
    """Delete a category item"""
    itemToDelete = session.query(CategoryItem).filter_by(id=categoryItem_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showCategoryItem', category_id=category_id))
    else:
        return render_template('deleteCategoryItem.html', item=itemToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
