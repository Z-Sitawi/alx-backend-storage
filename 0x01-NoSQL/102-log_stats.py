#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def get_top_ips(collection, limit=10):
    """
    Get the top IP addresses with the highest occurrence in the collection.

    :param collection: The MongoDB collection to query.
    :param limit: Number of top IPs to return.
    :return: List of tuples (IP, count) sorted by count in descending order.
    """
    pipeline = [
        # Group by IP address and count occurrences
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        # Sort by count in descending order
        {'$sort': {'count': -1}},
        # Limit to the top `limit` IPs
        {'$limit': limit}
    ]

    # Execute the aggregation pipeline
    results = list(collection.aggregate(pipeline))

    # Format the results for display
    return [(result['_id'], result['count']) for result in results]


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    nbr_docs_in_nginx = nginx_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Prints
    print(f'{nbr_docs_in_nginx} logs')
    print('Methods:')
    for method in methods:
        print(f'\tmethod {method}: '
              f'{nginx_collection.count_documents({"method": method})}')

    obj = {"method": "GET", "path": "/status"}
    print(f'{nginx_collection.count_documents(obj)} status check')

    # Get top 10 IPs
    top_ips = get_top_ips(nginx_collection, limit=10)
    print('IPs:')
    for ip, count in top_ips:
        print(f'\t{ip}: {count}')
