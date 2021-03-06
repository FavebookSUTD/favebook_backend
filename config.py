import os

DEFAULT_MONGO_URL = "mongodb://aoo-user:aoopass123@13.229.209.52:27017/50043db?authSource=admin"
DEFAULT_MYSQL_URL = "mysql+pymysql://aoo-user:aoopass123@52.221.216.110/50043db"

class Config(object):
    """
    Common configurations
    """
    JWT_SECRET_KEY = "thisisnottherealsecretkeydumbass"
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = "refresh"

    # Number of seconds it takes for expiry. 24 hours.
    # JWT_ACCESS_TOKEN_EXPIRES = 86400
    JWT_ACCESS_TOKEN_EXPIRES = 864000


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    MONGO_URI = "mongodb://localhost:27017/50043db"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://favebook_admin:password@localhost/50043db'
    API_KEY = "AIzaSyA68wWrXPVtGdVy4APQRZGJTHE_mo8b_Pk"


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = True

    MONGO_HOST = os.getenv("MONGO_URL", None)
    if MONGO_HOST:
        MONGO_URI = f"mongodb://faveadmin:password@{MONGO_HOST}:27017/50043db"

    else:
        MONGO_URI = DEFAULT_MONGO_URL

    MYSQL_HOST = os.getenv("MYSQL_URL", None)
    if MYSQL_HOST:
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://faveadmin:password@{MYSQL_HOST}/50043db"

    else:
        SQLALCHEMY_DATABASE_URI = DEFAULT_MYSQL_URL

    API_KEY = "AIzaSyA68wWrXPVtGdVy4APQRZGJTHE_mo8b_Pk"





app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}