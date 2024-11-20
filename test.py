# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# 九九乘法表
def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i * j}", end='\t')
        print()


# Fibonacci数列
def fibonacci(n):
    a, b = 0, 1
    result = []
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == '__main__':
    # 快速排序
    print("快速排序:")
    array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(array)
    print(sorted_array)

    # 九九乘法表
    print("\n九九乘法表:")
    print_multiplication_table()

    # Fibonacci数列
    print("\nFibonacci数列:")
    fib_sequence = fibonacci(9)
    print(fib_sequence)
