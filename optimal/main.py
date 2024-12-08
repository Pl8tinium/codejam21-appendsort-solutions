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

# Modified append_sort function to take input parameters
def append_sort(elements):
    total_appends = 0
    for i in range(1, len(elements)):
        appends_needed = 0
        while elements[i] <= elements[i - 1]:
            elements[i] *= 10
            appends_needed += 1

        if appends_needed > 1 and (elements[i] // 10) + (10 ** (appends_needed - 1) - 1) > elements[i - 1]:
            elements[i] = elements[i - 1] + 1
            appends_needed -= 1
        total_appends += appends_needed

    return total_appends

# Main execution
if __name__ == "__main__":
    num_cases, test_cases = parse_input("optimal/input.in")
    
    for case_num in range(num_cases):
        _, elements = test_cases[case_num]
        result = append_sort(elements)
        print(f'Case #{case_num + 1}: {result}')
