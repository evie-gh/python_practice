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
    
    def test_empty_single(self):
        for test_list in [[], [-387]]:
            for func in sorting_algorithms.values():
                list_copy = test_list.copy()
                func(list_copy)
                self.assertListEqual(test_list, list_copy)

                list_copy = test_list.copy()
                func(list_copy, sort_order=sorts.SortOrder.DESCENDING)
                self.assertListEqual(test_list, list_copy)

    def test_sorting(self):
        for test_list in [[-967153, 180291, 250110, -842723, -3701, -612791, 43993, -181828, 51011, -932719],
                           [81497, 836583, 536516, 894021, -744399, -943861, -900306, -679152, 591792, 748742],
                           [-202762, 212425, 458334, -522110, -16120, -902054, 194856, -705583, -975078, -231770],
                           [537882, 106327, -969394, -970028, -628415, -469152, 874998, 602016, -13642, 142053, -672324, 176585, 524556, 411173, 226438, -814207, -758328, -269396, 758683, -346637, 982485, 336673, -789908, 336895, 719382, -982120, 281233, 767464, 121961, 895145, 784854, 607146, 470868, -175230, -602783, 721081, 563912, -973268, -713882, -638066, -237577, 884272, 974477, 523431, -660390, 750220, 419840, -293960, 684515, 716476, 30490, -468599, 941430, 966037, 765302, -840941, -41393, 730398, 305591, 292857, 174911, -238487, 644796, 490125, -920638, -850486, 121758, 427218, -538489, 486189, -147310, -915622, 455439, 994182, 759865, 296754, -198477, 906701, 695123, -138270, -554559, 945902, 194742, 870587, 390195, -314450, -733717, 572109, 331323, 519645, -548263, 393727, -613340, -102897, -281751, 245079, -776500, -759912, 793850, 296949],
                           [-476606, -521133, 408305],
                           ['abc', 'zdf', 'a', 'aaaa', '0x45']]:
            for func in sorting_algorithms.values():
                list_copy = test_list.copy()
                list_sorted = sorted(test_list)
                func(list_copy)
                self.assertListEqual(list_copy, list_sorted)

                list_copy = test_list.copy()
                list_sorted = sorted(test_list, reverse = True)
                func(list_copy, sort_order=sorts.SortOrder.DESCENDING)
                self.assertListEqual(list_copy, list_sorted)

if __name__ == '__main__':
    unittest.main()
