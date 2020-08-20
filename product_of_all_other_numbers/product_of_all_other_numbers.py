'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    products = []
    for i in range(0, len(arr)):
        if len(arr) == 2:
            products.append(int(arr[1]))
            products.append(int(arr[0]))
            break
        if len(arr) > 2 and i == 0:
            right = arr[i + 1]
            right_products = 0
            for i in range(right, len(arr)):
                right_products += arr[i]
            products.append(int(right_products))
        if len(arr) > 2 and i != 0:
            right_products = 0
            left_products = 0
            for i in range(0, i):
                left_products += arr[i]
            right = arr[i + 1]
            for i in range(right, len(arr)):
                right_products += arr[i]
            total = left_products * right_products
            products.append(int(total))

    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
