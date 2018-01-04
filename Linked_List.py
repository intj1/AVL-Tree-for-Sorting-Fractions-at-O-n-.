class Linked_List(object):

    class __Node(object):
        def __init__(self, val, right = None, left = None):
            self.val = val
            self.next = right
            self.prev = left

    def __init__(self):
        self._size = 0
        self._header = Linked_List.__Node(None)
        self._header.prev = None
        self._trailer = Linked_List.__Node(None)
        self._trailer.next = None
            
    def append_element(self, val):
        newest = Linked_List.__Node(val)
        if self._size == 0:
            self._header.next = newest
            self._trailer.prev = newest
            newest.next = self._trailer
            newest.prev = self._header
        else:
            newest.prev = self._trailer.prev
            self._trailer.prev.next = newest
            self._trailer.prev = newest
            newest.next = self._trailer
        self._size += 1

    def insert_element_at(self, val, index):
        if index >= self._size or index < 0:
            raise IndexError
        newest = Linked_List.__Node(val)
        #finding item at index - 1
        if index <= len(self)//2:
            current = self._header
            for i in range(0,index):
                current = current.next
        else:
            current = self._trailer
            for i in range(0,len(self)-index+1):
                current = current.prev
        newest.next = current.next
        current.next.prev = newest
        newest.prev = current
        current.next = newest      
        self._size += 1

    def get_element_at(self, index):
        if index >= self._size or index < 0:
            raise IndexError
        #finding item at index
        if index < len(self)//2:
            current = self._header
            for i in range(0,index+1):
                current = current.next
        else:
            current = self._trailer
            for i in range(0,len(self)-index):
                current = current.prev
        return current.val

    def remove_element_at(self, index):
        if index >= self._size or index < 0:
            raise IndexError
        #getting item at index-1
        if index < len(self)//2:
            current = self._header
            for i in range(0,index):
                current = current.next
        else:
            current = self._trailer
            for i in range(0,len(self)-index+1):
                current = current.prev
        value = current.next
        current.next.next.prev = current
        current.next = current.next.next
        self._size -= 1
        return value.val

    def rotate_left(self):
        if self._size <= 1:
            return
        zero = self._header.next
        one = zero.next
        last = self._trailer.prev
        self._header.next = one
        one.prev = self._header
        self._trailer.prev = zero
        zero.next = self._trailer
        last.next = zero
        zero.prev = last

    def __len__(self):
        return self._size

    def __str__(self):
        if self._size < 1:
            return "[ ]"
        ret = "[ "
        for x in self:
            ret = ret + str(x) + ", "
        ret = ret[0:len(ret)-2]
        ret = ret + " ]"
        return ret

    def __iter__(self):
        self.__iter_index = 0
        self._curr_item = self._header.next
        return self

    def __next__(self):
        if self.__iter_index == self._size:
            raise StopIteration
        self.__iter_index += 1
        to_return = self._curr_item
        self._curr_item = self._curr_item.next
        return to_return.val
