def bubble_sort(data):
    data_len = data.shape[0]
    for i in range(data_len - 1):
        for j in range(data_len - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield data


def selection_sort(data):
    data_len = data.shape[0]
    for i in range(data_len - 1):
        min_idx = i
        for j in range(i + 1, data_len):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        yield data


def insertion_sort(data):
    data_len = data.shape[0]
    for i in range(1, data_len):
        anchor = data[i]
        j = i - 1
        while j >= 0 and anchor < data[j]:
            data[j + 1] = data[j]
            j -= 1
            yield data
        data[j + 1] = anchor
        yield data


def shell_sort(data):
    data_len = data.shape[0]
    groups = data_len // 2
    while groups != 0:
        for group_idx in range(groups):
            # group insertion sort
            for i in range(group_idx + groups, data_len, groups):
                anchor = data[i]
                j = i - groups
                while j >= group_idx and anchor < data[j]:
                    data[j + groups] = data[j]
                    j -= groups
                    yield data
                data[j + groups] = anchor
                yield data
        groups //= 2


def merge_cost(data):
    data_len = data.shape[0]
    data_tmp = data.copy()
    interval = 1
    while interval < data_len:
        for start in range(0, data_len, interval * 2):
            low = start
            mid = min(start + interval, data_len)
            end = min(start + 2 * interval, data_len)
            point_left = low
            point_right = mid
            while point_left < mid and point_right < end:
                if data[point_left] < data[point_right]:
                    data_tmp[low] = data[point_left]
                    point_left += 1
                else:
                    data_tmp[low] = data[point_right]
                    point_right += 1
                low += 1

            while point_left < mid:
                data_tmp[low] = data[point_left]
                point_left += 1
                low += 1

            while point_right < end:
                data_tmp[low] = data[point_right]
                point_right += 1
                low += 1

        data = data_tmp.copy()
        interval *= 2

        yield data


def quick_sort(data):
    data_len = data.shape[0]
    range_stack = [range(0, data_len)]
    while range_stack:
        unsort_range = range_stack.pop()
        if len(unsort_range) <= 1:
            continue
        start, end = unsort_range[0], unsort_range[-1]
        left, right = start+1, end
        anchor = data[start]
        while left < right:
            while left < right and data[right] >= anchor:
                right -= 1
            while left < right and data[left] < anchor:
                left += 1
            data[left], data[right] = data[right], data[left]
        if data[left] < data[start]:
            data[left], data[start] = data[start], data[left]

        yield data
        range_stack.append(range(start, left))
        range_stack.append(range(left + 1, end + 1))


if __name__ == "__main__":
    import numpy as np

    data = np.array([0, 1, 2, -1, -5, -3, 5, 2, 7])
    res = quick_sort(data)
    print(data)
    for each in res:
        print(each)
