class BinaryHeap:
    heap = list() 


    def __init__(self, *args):
        elems = list(args);
        for element in elems:
            self.add_elem(element)
    
    

    def add_elem(self, elem):
        self.heap.append(elem) 
        pos = len(self.heap);
        while (pos > 1) and (self.heap[pos-1] > self.heap[(pos // 2) - 1]): # добавленый элемент больше предка => поднимаем элемент по дереву 
            self.heap[pos-1], self.heap[(pos // 2) - 1] = self.heap[(pos // 2) - 1], self.heap[pos - 1]            
            pos = pos // 2


    def get_sorted(self):
        sorted_list = list()
        while len(self.heap) > 0:
            sorted_list.append(self.heap[0])
            self.del_first()
        return sorted_list


    def del_first(self):
        pos = 1;
        while (pos * 2 < len(self.heap)): 
            if (len(self.heap) > pos * 2 - 1) and (self.heap[pos * 2 - 1] < self.heap[pos * 2]): # 2 дочерних и правый больше => поднимаем правый.
                self.heap[pos - 1] = self.heap[pos * 2]
                pos = pos * 2 + 1
            else:
                self.heap[pos - 1] =  self.heap[pos * 2 - 1] # поднимаем левый
                pos = pos * 2
        self.heap.pop(pos-1) 


    def show_heap(self):
        return self.heap;


new_heap = BinaryHeap(1, 3, 5, 6, 2, 1, 445, 12, 10.5, 7, 6)
print(new_heap.get_sorted())    