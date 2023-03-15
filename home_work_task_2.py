def flat_generator(list_of_lists):
    for sub_list in list_of_lists:
        for element in sub_list:
            yield element

list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]

x = flat_generator(list_of_lists_1)
print(list(x))


def test_2():
    list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
    for flat_iterator_item, check_item in\
            zip(flat_generator(list_of_lists_1), ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):

        print(flat_iterator_item == check_item)

if __name__ == "__main__":
    test_2()
