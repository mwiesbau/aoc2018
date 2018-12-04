

def load_file(filename):

    package_ids = []

    file_handle = open(filename, 'r')
    allLines = file_handle.readlines()

    for line in allLines:
        package_ids.append(line.strip())

    return package_ids


def parse_package(package):


    character_dict = {}
    three_count = 0
    two_count = 0


    for character in package:
        if character not in character_dict.keys():
            character_dict[character] = 1
        else:
            character_dict[character] += 1


    for character in character_dict.keys():
        if character_dict[character] == 3:
            three_count = 1
        if character_dict[character] == 2:
            two_count = 1

    return two_count, three_count

def parse_packages(package_ids):
    '''
    Parses all packages and returns a dict with word occurrences
    :param package_ids:
    :return:
    '''

    total_two_counts = 0
    total_three_counts = 0

    for package in package_ids:
        two_counts, three_counts = parse_package(package)
        total_two_counts += two_counts
        total_three_counts += three_counts


    return total_two_counts, total_three_counts


def radix_sort(package_ids):

    # iterate over columns from back to front
    for i in range(25, -1, -1):

        box = {}

        for package in package_ids:
            char_id = ord(package[i])

            # ADD PACKAGE TO THE BOX ACCORDING TO THE LETTER
            if not char_id in box.keys():
                box[char_id] = [package]
            else:
                box[char_id].append(package)

        sorted_keys = sorted(box.keys())
        new_list = []
        for key in sorted_keys:
            new_list += box[key]

    return new_list



def compare(packages):



    '''
    for i in range(1, len(packages)):
        mismatches = 0
        for j in range(0, 25):
            if packages[i-1][j] != packages[i][j]:
                mismatches += 1
        print(mismatches)
        if mismatches == 1:
            print(packages[i])
    '''
    mismatch_index = -1

    for i in range(0, len(packages)):
        for j in range(i, len(packages)):
            mismatch = 0
            for k in range(0,26):
                if packages[i][k] != packages[j][k]:
                    mismatch += 1
                    if mismatch == 1:
                        mismatch_index = k
            if mismatch == 1:
                print("mismatch at index: {}".format(mismatch_index))
                print("Package 1: {}({}){}".format(packages[i][:mismatch_index],
                                                               packages[i][mismatch_index],
                                                               packages[i][mismatch_index+1:]))
                print("Package 2: {}({}){}".format(packages[j][:mismatch_index],
                                                   packages[j][mismatch_index],
                                                   packages[j][mismatch_index + 1:]))





if __name__ == "__main__":
    package_ids = load_file('input.txt')
    two_counts, three_counts = parse_packages(package_ids)
    print("The result is: {}".format(two_counts*three_counts))


    sorted_list = radix_sort(package_ids)

    compare(package_ids)