def CountSort(A):
    list_ = [0] * 101
    for i in A:
        list_[i] += 1
    return list_

print(CountSort([2, 5, 1]))
