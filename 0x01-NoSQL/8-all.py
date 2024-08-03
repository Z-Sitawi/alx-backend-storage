#!/usr/bin/env python3
""" A function that lists all documents in a collection """


def list_all(mongo_collection):
    """
        lists all documents in a collection
    :param mongo_collection: is a pymongo collection object
    :return: A list of all documents
            or an empty list if no document in the collection
    """
    return mongo_collection.find()
