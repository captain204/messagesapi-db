import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
#SQLALCHEMY_DATABASE_URI ="postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="root", DB_PASS="", DB_ADDR="127.0.0.1", DB_NAME="messages")
SQLALCHEMY_DATABASE_URI ="postgresql:///messages"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


#psql --username=nuru --dbname=messages --command="\dt"
#postgres=# \c messages
#sudo -u postgres psql open postgress terminal
#\l list all tables
#psql \c  connect * Switch to messages table
