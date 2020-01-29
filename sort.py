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
        while anchor < data[j] and j >= 0:
            data[j + 1] = data[j]
            j -= 1
            yield data
        data[j + 1] = anchor
        yield data


def shell_sort(data):
    raise NotImplementedError


def merge_cost(data):
    raise NotImplementedError


def quick_sort(data):
    raise NotImplementedError


if __name__ == "__main__":
    import numpy as np

    data = np.array([0, 1, 2, -1, -5, -3, 5, 2, 7])
    res = bubble_sort(data)
    print(data)
    for each in res:
        print(each)
