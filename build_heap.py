# python3
# Nikita Smirnovs 221RDB433
import threading





class MinHeap:
    def swap_operation(self,iter,smallest_num,elem):
        self.swaps.append((iter, smallest_num))
        self.array[iter], self.array[smallest_num] = self.array[smallest_num], self.array[iter]
        self.heap_iter(smallest_num, elem)

    def __init__(self, array):
        self.array = array
        self.swaps = []
        self.build_heap()

    def build_heap(self):
        elem = len(self.array)
        for i in range(n // 2 - 1, -1, -1):
            self.heap_iter(i, elem)

    def heap_iter(self, iter, elem):
        smallest_num = iter
        left_leaf = 2 * iter + 1
        right_leaf = 2 * iter + 2
        smallest_num = self.left_leaf_condition(left_leaf, elem,smallest_num)
        smallest_num = self.right_leaf_condition(right_leaf,elem,smallest_num)
        self.check_smallest_value(smallest_num,iter,elem)

    def print_swaps(self):
        print(len(self.swaps))
        for x in self.swaps:
            print(*x)

    def left_leaf_condition(self,left_leaf, elem, smallest_num):
        if left_leaf < elem and self.array[left_leaf] < self.array[smallest_num]:
            return left_leaf
        return smallest_num

    def right_leaf_condition(self,right_leaf,elem,smallest_num):
        if right_leaf < elem and self.array[right_leaf] < self.array[smallest_num]:
            return right_leaf
        return smallest_num
        
    def check_smallest_value(self,smallest_num,iter, elem):
        if smallest_num != iter:
            self.swap_operation(iter,smallest_num,elem)



class Node:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self) -> str:
        return f"{self.value}"

    
def check_answer(filename, swaps_func):
    with open("tests/" + filename + ".a", "r") as file:
        n = int(file.readline())
        array = file.readlines()
    print(array)

    fil = [list(map(int,element[:-2].strip().split(" "))) for element in array ]
    # print(fil)
    return swaps_func == fil


def open_file(filename):
    with open("tests/" + filename, "r") as file:
        n = int(file.readline())
        array = list(map(int, file.readline().split()))

    return n, array



if __name__ == "__main__":
    command = input("command: ").strip().upper()


    match command:

        case "I":
            n = int(input("swaps count: "))
            array = list(map(int, input().split()))

        case "F":
            name = input("file name: ")

            assert not name.endswith(".a")

            n, array = open_file(name)



    assert len(array) == n

    min_heap = MinHeap(array)
    min_heap.print_swaps()

    try:
        check_answer(name,min_heap.swaps)
    except Exception:
        pass