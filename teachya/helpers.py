import json
from sqlalchemy import create_engine

def get_db_engine():
    with open('config.json') as json_data_file:
        config = json.load(json_data_file)
    print(config)
    return create_engine(
        'mysql://{user}:{password}@{host}:{port}/{db}'.format(**(config['mysql']))
    )
