class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.reverse_list_of_list = self.list_of_lists.reverse()
        self.next_element = iter([])
        return self

    def __next__(self):
        try:
            next_item = next(self.next_element)
        except StopIteration:
            if len(self.list_of_lists) == 0:
                raise StopIteration

            try:
                self.next_element = iter(self.list_of_lists.pop())
            except:
                pass

            next_item = next(self.next_element)
        return next_item

list_of_lists = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]

for item in FlatIterator([['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]):
    print(item)

new_list = FlatIterator(list_of_lists)
print(f"\n{list(new_list)}\n")


def test_1():
    list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),\
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        print(flat_iterator_item == check_item)


if __name__ == "__main__":
    test_1()











