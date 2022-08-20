
"""SELECTION_SORT
   input: unsorted list
   output: sorted list
   Implements selection sort with integral swap
"""

def selection_sort(a):
    for i in range(len(a) - 1):  # loop - iterate through the unsorted list from start to the penultimate element.

        minimum = i  # Assignment - Set minimum to i.

        for j in range(i + 1, len(a)):  # inner loop - iterate through unsorted list from the current
            #   ith + 1 element to the last element.

            if a[j] < a[minimum]:  # if 1st element value is less than the element to the right (2nd).

                minimum = j  # Reassignment - Set minimum to j.

        a[i], a[minimum] = a[minimum], a[i]  # swap - set 1st element to be the value of the 2nd and set the
        # 2nd element to be the value of the 1st.

    return a  # when the loop completes, return the sorted list.

print(selection_sort([11, 22, 14, 67, 2, 9]))
