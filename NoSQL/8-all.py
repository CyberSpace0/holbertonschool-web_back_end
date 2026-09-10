#!/usr/bin/env python3
"""List all databases in MongoDB."""

from pymongo import MongoClient

def list_all(mongo_collection) -> None:
    """List all documents in the specified MongoDB collection."""
    return mongo_collection.find()
