import types


def flat_generator(list_of_lists):
    for i in list_of_lists:
        if isinstance(i, (list, tuple)):
            for j in flat_generator(i):
                yield j
        else:
            yield i

list_of_lists = [
                 ['a', (1, [[[0, "r"]]], 2), 'c'],
                 ['d', [[['g']]], 'e', [1, 2, [1, ['a', ['a']], 2, None]], 'f', False], [1]
                ]

print(list(flat_generator(list_of_lists)))


def test_4():
    list_of_lists = [
                        ['a',(1, [[[0, "r"]]], 2), 'c'],
                        ['d', [[['g']]], 'e', [1, 2, [1, ['a', ['a']], 2, None]], 'f', False], [1]
                    ]

    for flat_iterator_item, check_item in \
            zip(flat_generator(list_of_lists), ['a', 1, 0, 'r', 2, 'c', 'd', 'g', 'e', 1, 2, 1, 'a', 'a', 2, None, 'f', False, 1]):

        print(flat_iterator_item == check_item)
    print("*" * 50)
    print(isinstance(flat_generator(list_of_lists), types.GeneratorType))

if __name__ == "__main__":
    test_4()