def parse_input(filename):
    with open(filename, 'r') as f:
        # Read number of test cases
        num_cases = int(f.readline().strip())
        test_cases = []
        
        # Process each test case
        for _ in range(num_cases):
            # Read N (number of elements)
            num_elements = int(f.readline().strip())
            # Read and parse list of integers
            elements = list(map(int, f.readline().strip().split()))
            test_cases.append((num_elements, elements))
            
    return num_cases, test_cases

def custom_counter():
    length = 1
    while True:
        for i in range(0, 10 ** length):
            yield str(i).zfill(length)
        length += 1

def append_sort(elements):
    highest_cur_nr = elements[0]
    appended_total = 0

    for i in range(1, len(elements)):
        if elements[i] <= highest_cur_nr:
            tested_element = elements[i]
            counter = custom_counter()
            cur_appended_nr = next(counter)
            while tested_element <= highest_cur_nr:
                tested_element = int(str(elements[i]) + cur_appended_nr)
                cur_appended_nr = next(counter)

            appended_total += len(cur_appended_nr)
            highest_cur_nr = tested_element
        else:
            highest_cur_nr = elements[i]

    return appended_total

# Main execution
if __name__ == "__main__":
    num_cases, test_cases = parse_input("rudimentary/input.in")
    
    for case_num in range(num_cases):
        _, elements = test_cases[case_num]
        result = append_sort(elements)
        print(f'Case #{case_num + 1}: {result}')



