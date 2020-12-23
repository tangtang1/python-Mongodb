
from pymongo import MongoClient
import pandas as pd
Connect_URL=""

class Mongo(object):
    def __init__(self):
        self.dbconn = MongoClient(Connect_URL)
    def __enter__(self):
        return self.dbconn
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.dbconn.close()

#查询数据库函数
def query_collect(collection):
    with Mongo() as MO:
        result = MO[collection]
        #example
        data=result.find({}, {'key':'value'})
        return data

data=query_collect('')
df=pd.DataFrame(data)
