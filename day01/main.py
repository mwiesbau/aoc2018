

def load_file(filename):

    file_handle = open(filename, 'r')
    lines = file_handle.readlines()
    
    return lines


if __name__ == "__main__":
    lines = load_file('input.txt')
 
    freq_set = set()
    total = 0

    
    while True:
        for line in lines:
            total += int(line.strip())
            if total in freq_set:
                print("First Repeating frequency is: {}".format(total))
                exit(0)
            else:
                freq_set.add(total)
        print("The total is: {}".format(total))
