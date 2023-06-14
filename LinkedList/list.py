class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        if type(next) == type(self) or next is None:
            self.__next = next
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data =  data
    
class Stack:    
    top = None
    last = None
            
    def push(self, obj):
        if self.last != None:
            self.last.next = obj
            self.last = obj
        else:
            self.last = obj
            self.top = obj
            
    def pop(self):
        if self.top == None:
            return None
        pointer = self.top
        if self.top.next == None:
            self.top = None
            self.last = None
            return pointer

        pointer = self.top
        while pointer.next != self.last:
            pointer =  pointer.next
        pointer.next = None    
        self.last = pointer

    def reverse(self):
        
        pass        
        
    def get_data(self):    
        l = []
        pointer = self.top
        while pointer != None:
            l.append(pointer.data)
            pointer =  pointer.next
        return l 