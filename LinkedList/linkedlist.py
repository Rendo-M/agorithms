class Point:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_pointer(self, next_point):
        self.next = next_point        

    def get_pointer(self):
        return self.next

    def get_data(self):
        return self.data        

    def set_data(self, data):
        self.data = data


class LinkedList:
    first = None
    last = None

    def put_last(self, obj):
        if self.last != None:
            self.last.next = obj
            self.last = obj
        else:
            self.last = obj
            self.first = obj

    def put_first(self, obj):
        if self.first != None:
            obj.next = self.first 
            self.first = obj
        else:            
            self.last = obj
            self.first = obj


    def remove_first(self):
        obj = self.first
        if self.first != None:
            self.first = obj.next        
        return obj

    def remove_last(self):
        if self.last == None:
            return None
        obj = self.last
        if self.first.next == None:
            self.first = None
            self.last = None
            return obj
        pointer = self.first
        while pointer.next != self.last:
            pointer =  pointer.next
        pointer.next = None    
        self.last = pointer
        return obj

    def reverse(self):
        obj = self.remove_first() 
        new_last = obj
        new_first = obj
        if obj is None:
            return self

        while obj.next != None:
            obj = self.remove_first()
            new_last.next = obj
            new_last = obj    


