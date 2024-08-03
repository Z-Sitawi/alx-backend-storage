#!/usr/bin/env python3
"""  A function that inserts a new document
in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs
    :param mongo_collection: a pymongo collection object
    :param kwargs: document to be inserted
    :return: the new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
