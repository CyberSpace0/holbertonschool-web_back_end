#!/usr/bin/env python3
"""List all databases in MongoDB."""

from pymongo import MongoClient

def list_all(mongo_collection) -> None:
    """List all databases available in the MongoDB server."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    databases = client.list_database_names()

    for database in databases:
        print(database)
