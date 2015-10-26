def quick_sort(entry, first, last, comparisons=0):
    if first < last:
        pivot = partition(entry, first, last)

        comparisons += quick_sort(entry, first, pivot - 1, pivot - 1 - first - 1)
        comparisons += quick_sort(entry, pivot, last, last - pivot - 1)
        return pivot - 1 - first
    else:
        return 0


def partition(entry, first, last):
    pivot_value = entry[first]

    left = right = first + 1

    while right <= last:
        if entry[right] < pivot_value:
            entry[left], entry[right] = entry[right], entry[left]
            left += 1

        right += 1

    entry[first], entry[left - 1] = entry[left - 1], entry[first]

    return left


t1 = [int(line.rstrip('\n')) for line in open('./t1.txt')]
t2 = [int(line.rstrip('\n')) for line in open('./t2.txt')]
t3 = [int(line.rstrip('\n')) for line in open('./t3.txt')]
t4 = [int(line.rstrip('\n')) for line in open('./t4.txt')]

print(quick_sort(t1, 0, len(t1) - 1))  # 21
print(quick_sort(t2, 0, len(t2) - 1))  # 518
# print(quick_sort(t3, 0, len(t3) - 1)) # 8921
# print(quick_sort(t4, 0, len(t4) - 1))
