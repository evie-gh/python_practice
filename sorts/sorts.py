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
    
    if len(list) <= 1:
        return
      
    comp = comparator if sort_order == SortOrder.ASCENDING else lambda x, y: comparator(x, y) * -1

    for _ in list:
        swap_performed = False
        for j in range(len(list) - 1):
            comparison = comp(list[j], list[j + 1])
            if comparison > 0:
                swap(list, j, j + 1)
                swap_performed = True
        if not swap_performed:
            return
        
def selection_sort(list, comparator = default_comparator, sort_order = SortOrder.ASCENDING):
    if sort_order not in SortOrder:
        raise ValueError("sort_order must be in " + list(SortOrder))
    
    if len(list) <= 1:
        return
    
    comp = comparator if sort_order == SortOrder.ASCENDING else lambda x, y: comparator(x, y) * -1
    
    for i in range(len(list)):
        lowest_index = i
        lowest_value = list[i]
        for j in range(i + 1, len(list)):
            comparison = comp(list[j], lowest_value)
            if comparison < 0:
                lowest_index = j
                lowest_value = list[j]
        if lowest_index != i:
            swap(list, i, lowest_index)

def insertion_sort(list, comparator = default_comparator, sort_order = SortOrder.ASCENDING):
    if sort_order not in SortOrder:
        raise ValueError("sort_order must be in " + list(SortOrder))
    
    if len(list) <= 1:
        return
    
    comp = comparator if sort_order == SortOrder.ASCENDING else lambda x, y: comparator(x, y) * -1

    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            comparison = comp(list[j], list[j - 1])
            if comparison < 0:
                swap(list, j, j - 1)
            else:
                break

def heap_sort(list, comparator = default_comparator, sort_order = SortOrder.ASCENDING):
    if sort_order not in SortOrder:
        raise ValueError("sort_order must be in " + list(SortOrder))
    
    if len(list) <= 1:
        return
    
    comp = comparator if sort_order == SortOrder.ASCENDING else lambda x, y: comparator(x, y) * -1

    #
    # build a heap in-place. 
    # an implicit complete binary tree data strure is formed by the following:
    # for a given node list[i], its children are found in list[2i + 1] and list[2i + 2].
    # its parent is in list[floor((i - 1) / 2)].
    #

    def left_child(index):
        return 2 * index + 1

    # sift a root node of a subheap down to re-establish the heap property
    def sift_down(start, end):
        i = start
        while left_child(i) < end:
            largest_child = left_child(i)
            if largest_child + 1 < end:
                comparison = comp(list[largest_child], list[largest_child + 1])
                if comparison < 0:
                    largest_child += 1

            comparison = comp(list[i], list[largest_child])
            if comparison < 0:
                swap(list, i, largest_child)
                i = largest_child
            else:
                return
    
    # construct the heap by sifting down each non-leaf node (stored in [0..floor(len(list)/2)]) bottom-up
    for i in range(int(len(list)/2) - 1, -1, -1):
        sift_down(i, len(list))
    
    # now that the heap is constructed, pop the minimum (moving from the heap into the sorted items at the end of the array) repeatedly
    for i in range(len(list) - 1, 0, -1):
        swap(list, 0, i)
        sift_down(0, i)
