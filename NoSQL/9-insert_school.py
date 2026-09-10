#!/usr/bin/env python3
"""Insert a new school into the specified MongoDB collection."""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """Insert a new document into the specified MongoDB collection."""
    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
