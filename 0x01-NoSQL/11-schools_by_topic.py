#!/usr/bin/env python3
"""
A function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """

    :param mongo_collection: pymongo collection object
    :param topic: (string) will be topic searched
    :return: the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
