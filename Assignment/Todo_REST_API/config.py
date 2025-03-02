import os
class Config(object):
    SECRET_KEY = '7d9a849a65fb3f95ca2f61b71848542b5cf52135599fd591392dc72b076ba2b5'
    file_path = os.path.abspath(os.getcwd())+"\db.sqlite"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False