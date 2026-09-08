#!/usr/bin/env python3
"""Provide a helper function for calculating pagination index ranges."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes for a given pagination page."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)