def BinSer(list, l, h, n):
    list.sort()
    if l < h:
        mid = int(l + (h - l) / 2)
        if list[mid] == n:
            return mid
        elif n < list[mid]:
            h = mid - 1
            BinSer(list, l, h, n)
        elif n > list[mid]:
            l = mid + 1
            BinSer(list, l, h, n)
    else:
        return -1