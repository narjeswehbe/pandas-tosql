

import  mysql.connector
import  numpy as np
import pandas as pd
import sqlalchemy
from mysql.connector import Error

from DatabaseInfo import DatabaseInfo


def createFrame():
    np.random.seed(0)
    number_of_samples = 10
    frame = pd.DataFrame({
        'feature1': np.random.random(number_of_samples),
        'feature2': np.random.random(number_of_samples),
        'class': np.random.binomial(2, 0.1, size=number_of_samples),
    }, columns=['feature1', 'feature2', 'class'])

    print(frame)
    return frame

def FrameToSql(DatabaseInfo , frame):

    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.
                                                   format(DatabaseInfo.username, DatabaseInfo.password,
                                                          DatabaseInfo.host, DatabaseInfo.port ,  DatabaseInfo.databasename))
    frame.to_sql(con=database_connection, name='table_name_for_df', if_exists='replace')



if __name__ == '__main__':
   d = DatabaseInfo("root" , "12345678" , "localhost" , 3309 , "pandas")
   FrameToSql(d , createFrame())


