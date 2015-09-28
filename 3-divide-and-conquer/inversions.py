def merge_and_count_split(left_list, right_list):
    final_list = []
    count = 0
    i = j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            final_list.append(left_list[i])
            i += 1
        else:
            final_list.append(right_list[j])
            j += 1
            count += len(left_list[i:])

    while i < len(left_list):
        final_list.append(left_list[i])
        i += 1
    while j < len(right_list):
        final_list.append(right_list[j])
        j += 1

    return final_list, count


def sort_and_count_inversions(entry, count=0):
    l = len(entry)

    if l <= 1:
        return entry, 0

    middle = l // 2
    left, count_left = sort_and_count_inversions(entry[:middle], count)
    right, count_right = sort_and_count_inversions(entry[middle:], count)
    split, count_split = merge_and_count_split(left, right)
    return split, count_left + count_right + count_split


print(sort_and_count_inversions(([10, 2, 3, 22, 33, 7, 4, 1, 2])))
