#!/usr/bin/env python3
""" Module has a function that returns all students sorted by average score """


def top_students(mongo_collection):
    """
    :param mongo_collection: A pymongo collection object
    :return: A list of all students sorted by average score
    """
    students_list = mongo_collection.find()
    new_std_list = []
    for std in students_list:
        obj = {}
        for k, v in std.items():
            obj.update({k: v})
        all_topics = obj['topics']
        score = 0
        for topic in all_topics:
            score += topic['score']

        obj.update({"averageScore": score / len(all_topics)})
        new_std_list.append(obj)

    return sorted(new_std_list, key=lambda x: x.get('averageScore', 0),
                  reverse=True)
