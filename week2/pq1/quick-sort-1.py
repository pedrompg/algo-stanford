def quick_sort(entry, first, last):
    if first < last:
        pivot = partition(entry, first, last)

        quick_sort(entry, first, pivot - 1)
        quick_sort(entry, pivot + 1, last)

    return entry


def partition(entry, first, last):
    pivot_value = entry[first]

    left = right = first + 1

    while right <= last:
        if entry[right] < pivot_value:
            entry[left], entry[right] = entry[right], entry[left]
            left += 1

        right += 1

    entry[first], entry[left - 1] = entry[left - 1], entry[first]

    return left - 1


t1 = [int(line.rstrip('\n')) for line in open('./t1.txt')]
t2 = [int(line.rstrip('\n')) for line in open('./t2.txt')]
t3 = [int(line.rstrip('\n')) for line in open('./t3.txt')]
t4 = [int(line.rstrip('\n')) for line in open('./t4.txt')]

print(quick_sort(t1, 0, len(t1) - 1))  # 25
# print(quick_sort(t2, 0, len(t2) - 1))  # 615
# print(quick_sort(t3, 0, len(t3) - 1)) # 10297
# print(quick_sort(t4, 0, len(t4) - 1))
