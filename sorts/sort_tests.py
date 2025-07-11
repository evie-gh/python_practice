# sorting algorithm unit tests

import unittest
import sorts

sorting_algorithms = {
    "bubblesort" : sorts.bubble_sort,
    "insertionsort" : sorts.insertion_sort
}

class TestSortAlgorithms(unittest.TestCase):
    def test_nop(self):
        presorted_list_ascending = [-23, -4, 0, 0, 1, 4, 100, 1000003]
        self.assertListEqual(presorted_list_ascending, sorted(presorted_list_ascending))

        presorted_list_descending = [234234, 3888, 100, 3, 3, 0, -13944]
        self.assertListEqual(presorted_list_descending, sorted(presorted_list_descending, reverse = True))

        for func in sorting_algorithms.values():
            list_copy = presorted_list_ascending.copy()
            func(list_copy)
            self.assertListEqual(presorted_list_ascending, list_copy)

            list_copy = presorted_list_descending.copy()
            func(list_copy, sort_order=sorts.SortOrder.DESCENDING)
            self.assertListEqual(presorted_list_descending, list_copy)


if __name__ == '__main__':
    unittest.main()
