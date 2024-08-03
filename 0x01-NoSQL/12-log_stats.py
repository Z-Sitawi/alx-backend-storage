#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx
nbr_docs_in_nginx = nginx_collection.count_documents({})
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
# Prints
print(f'{nbr_docs_in_nginx} logs')
print('Methods:')
for method in methods:
    print(f'\tmethod {method}: {nginx_collection.count_documents({"method": method})}')
print(f'{nginx_collection.count_documents({"method": "GET", "path": "/status"})} status check')
