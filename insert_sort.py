# -*- coding: utf-8 -*-

lists = [49, 38, 65, 97, 76, 13, 27, 49, 55, 04]
'''''插入排序—————直接插入排序(Straight Insertion Sort)'''


def insert_sort(lists):
    for i in range(1, len(lists)):
        j = i-1
        key = lists[i]
        while j >= 0:
            if key < lists[j]:
                lists[j+1] = lists[j]
                lists[j] = key
                print lists
            j -= 1
    return lists


insert_sort(lists)

