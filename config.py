import os


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:123456@localhost/pitches'



config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
