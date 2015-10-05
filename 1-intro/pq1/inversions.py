def merge_and_count_split(left, right, count):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
            count += len(left)

    result.extend(left if left else right)

    return result, count


def sort_and_count_inversions(entry, count=0):
    l = len(entry)

    if l <= 1:
        return entry, 0

    middle = l // 2
    left, count_left = sort_and_count_inversions(entry[:middle], count)
    right, count_right = sort_and_count_inversions(entry[middle:], count)
    return merge_and_count_split(left, right, count_left + count_right)

t1 = [int(line.rstrip('\n')) for line in open('t1.txt')]
t2 = [int(line.rstrip('\n')) for line in open('t2.txt')]
t3 = [int(line.rstrip('\n')) for line in open('t3.txt')]
t4 = [int(line.rstrip('\n')) for line in open('t4.txt')]

print(sort_and_count_inversions(t1)[1])
print(sort_and_count_inversions(t2)[1])
print(sort_and_count_inversions(t3)[1])
print(sort_and_count_inversions(t4)[1])