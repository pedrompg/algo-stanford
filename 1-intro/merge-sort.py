def merge_sort(list_to_order):
    l = len(list_to_order)

    if l <= 1:
        return list_to_order

    middle = l // 2
    ll = merge_sort(list_to_order[middle:])
    rl = merge_sort(list_to_order[:middle])

    l3 = []
    i = j = 0
    while i < len(ll) and j < len(rl):
        if ll[i] <= rl[j]:
            l3.append(ll[i])
            i += 1
        else:
            l3.append(rl[j])
            j += 1

    while i < len(ll):
        l3.append(ll[i])
        i += 1
    while j < len(rl):
        l3.append(rl[j])
        j += 1

    return l3

print(merge_sort([5, 4, 1, 8, 7, 2, 6]))
