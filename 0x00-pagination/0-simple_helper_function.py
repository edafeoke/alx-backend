#!/usr/bin/env python3
'''
0-simple_helper_function module
'''


def index_range(page: int, page_size: int) -> tuple:
    '''
    a function named index_range that takes two integer
    arguments page and page_size
    '''
    idx_tuple = page_size * (page - 1), page * page_size
    return idx_tuple
