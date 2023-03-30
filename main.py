from typing import List

def even_list(int_list: List[int]) -> List[int]:
    i = 0
    while i < len(int_list):
        if int_list[i] % 2 != 0:
            del int_list[i]
        else:
            i += 1
    return int_list
# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)
# Boilerplate code
if __name__ == "__main__":
    main()
