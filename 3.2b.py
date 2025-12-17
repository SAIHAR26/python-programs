import numpy as np

arr = np.array([[10, 25, 5],
                [7, 15, 30],
                [4, 5, 6]])

print(arr)

print("max value:", np.max(arr))
print("min value:", np.min(arr))
print("index of max:", np.argmax(arr))
print("index of min:", np.argmin(arr))

# Indices row-wise and column-wise
max_indices_rows = np.argmax(arr, axis=1)
min_indices_rows = np.argmin(arr, axis=1)

max_indices_cols = np.argmax(arr, axis=0)
min_indices_cols = np.argmin(arr, axis=0)

print("max indices along rows:", max_indices_rows)
print("min indices along rows:", min_indices_rows)
print("max indices along columns:", max_indices_cols)
print("min indices along columns:", min_indices_cols)

