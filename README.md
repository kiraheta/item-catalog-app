# Item Catalog App

# Overview
A RESTful web application using the Python framework Flask that provides a variety of sports categories, category items and a user registration & third-party OAuth authentication system. Registered users have the ability to post, edit and delete their own items.

This project satisfies a project requirement for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

# Enviroment Setup

### Install the virtual machine

1. Download & install  [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

2. Download & install [Vagrant](https://www.vagrantup.com/downloads.html)

 Check if Vagrant is successfully installed by running on terminal.

  ```vagrant --version```

  If you see the version number, then you're good.

### Download VM configuration

1. Download or Clone the repository

 ```git clone https://github.com/kiraheta/item-catalog-app.git```

2. ```cd``` into directory **item-catalog-app/catalog**.

### Running the VM
1. Inside the subdirectory, run the command
```vagrant up```. Doing so will download & install the Linux OS.

2. Once ```vagrant up``` is completed and your shell prompt returns, run ```vagrant ssh``` to log into newly installed Linux OS.

3. Lastly, run ```cd /vagrant```

### Setup the Database
1. Run ```python database_setup.py``` to initialize the database

2. Run ```python lotsofitems.py``` to populate the database with categories and category items.

## Running the Item Catalog App

1. Run ```python application.py``` to run the Flask web server.

2. Visit ```http://localhost:8000 ``` to view the item catalog app. You should be able to view, add, edit, and delete catalog items and categories.
