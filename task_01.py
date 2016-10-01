#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_party_stats(families, table_size=6):
    tables = 0
    guests = 0
    for obj in families:
        guests += len(obj)
        tables += -(-len(obj) // table_size)
    
    return guests, tables
