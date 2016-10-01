#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""THis module counts guests and number of tables needed"""


def get_party_stats(families, table_size=6):
    """choose number of tables based on guests and maximum table size

    Args:
        families (list): number of families and guests per family
        table_size (int): maximum number of guests per table

    Returns:
        guests (int): total number of guests
        tables (int): number of tables based on contraints

    Examples:
        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)

        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']], 2)
        (6, 4)
    """

    tables = 0
    guests = 0
    for obj in families:
        guests += len(obj)
        tables += -(-len(obj) // table_size)
    
    return guests, tables
