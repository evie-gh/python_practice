# sorting algorithm implementations

from enum import Enum

class SortOrder(Enum):
    ASCENDING = 0
    DESCENDING = 1

def default_comparator(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def swap(list, index0, index1):
    swap = list[index0]
    list[index0] = list[index1]
    list[index1] = swap

def bubble_sort(list, comparator = default_comparator, sort_order = SortOrder.ASCENDING):
    if sort_order not in SortOrder:
        raise ValueError("sort_order must be in " + list(SortOrder))

    for _ in list:
        swap_performed = False
        for j in range(len(list) - 1):
            comparison = comparator(list[j], list[j + 1])
            if sort_order == SortOrder.DESCENDING:
                comparison *= -1
            if comparison > 0:
                swap(list, j, j + 1)
                swap_performed = True
        if not swap_performed:
            return
        
def insertion_sort(list, comparator = default_comparator, sort_order = SortOrder.ASCENDING):
    if sort_order not in SortOrder:
        raise ValueError("sort_order must be in " + list(SortOrder))
    
    for i in range(len(list)):
        lowest_index = i
        lowest_value = list[i]
        for j in range(i + 1, len(list)):
            comparison = comparator(list[j], lowest_value)
            if sort_order == SortOrder.DESCENDING:
                comparison *= -1
            if comparison < 0:
                lowest_index = j
                lowest_value = list[j]
        if lowest_index != i:
            swap(list, i, lowest_index)

