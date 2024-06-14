import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', '/path/to/apache/logs')
    LOG_FILE_PATTERN = os.getenv('LOG_FILE_PATTERN', 'access_log*')
