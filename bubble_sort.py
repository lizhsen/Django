# -*- coding: utf-8 -*-

lists = [49, 38, 65, 97, 76, 13, 27, 49]


def bubble_sort(lists):
    count = len(lists)
    for i in range(count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
                print lists
    return lists


bubble_sort(lists)