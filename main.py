from typing import List

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    sum=0
    i = 0
    j = 0
    while i < len(even_int_list):
        if even_int_list[i] % 2 != 0:
            del even_int_list[i]
        else:
            i += 1
    while j < len(even_int_list):
        sum+= even_int_list[j]*even_int_list[j]
        j+=1
    return sum
# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    output = sum_of_squares_of_even(even_int_list)
    print(output)
    # Boilerplate code
if __name__ == "__main__":
    main()
