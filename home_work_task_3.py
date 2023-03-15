class FlatIteration:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.sub_list_for_iter = []
        self.current_iter = iter(list_of_list)
        return self

    def __next__(self):
        while True:
            try:
                self.next_item = next(self.current_iter)
            except StopIteration:
                if not self.sub_list_for_iter:
                    print("цикл закончен")
                    raise StopIteration
                else:
                    self.current_iter = self.sub_list_for_iter.pop()
                    continue
            if isinstance(self.next_item, (list, tuple)):
                self.sub_list_for_iter.append(self.current_iter)
                self.current_iter = iter(self.next_item)
            else:
                return self.next_item


list_of_list = [
                ['a', [2, 4, [[[['a', 'b']]]]], 'b', 'c'],
                ['d', 'e', (0, (5, [[[["o", "o"]]]], 55), 6, 5), 'f', 'h', False],
                [1, 2, None]
                ]

new_list = FlatIteration(list_of_list)
print(f"\n{list(new_list)}\n")

def test_2():

    list_of_lists_1 = [
                    ['a', [2, 4, [[[['a', 'b']]]]], 'b', 'c'],
                    ['d', 'e', (0, (5, [[[["o", "o"]]]], 55), 6, 5), 'f', 'h', False],
                    [1, 2, None]
                    ]

    for flat_iterator_item, check_item in\
            zip(FlatIteration(list_of_lists_1),\
                ['a', 2, 4, 'a', 'b', 'b', 'c', 'd', 'e', 0, 5, 'o', 'o', 55, 6, 5, 'f', 'h', False, 1, 2, None]):

        print(flat_iterator_item == check_item)


if __name__ == "__main__":
    test_2()












