#Author：Jehu Xue
# -*- coding:utf-8 -*-
import time
import blockchain

# 测试上一个哈希值
blockchain = blockchain.Blockchain()
last_block = {'block_number': 1, 'nonce': 0, 'previous_hash': 0, 'timestamp': 1547603975.9364002, 'transactions': []}


previous_hash = blockchain.hash(last_block)
print(previous_hash)

# 测试monggodb数据库
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["BlockChain1"]
# mycol = mydb["sites"]

# dblist = myclient.database_names() #python2
# mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
# x = mycol.insert_one(mydict)
# dblist = myclient.list_database_names()
# if "test" in dblist:
#     print("数据库已存在！")
#     print(x)
# else:
#     print("数据库不存在！")

# last = mycol.find().sort([("timestamp", -1)]).limit(1)
# # last_block = last[0]
# print(last)

# result = mycol.find({},{'_id':0}).sort([("timestamp",-1)])
# # r = result[0]
# # print(r)
#
# for x in result:
#   print(x)






