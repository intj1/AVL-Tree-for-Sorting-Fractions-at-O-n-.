from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__size = 0
    self.__front = 0
    
  def __str__(self):
    if self.__size == 0:
        return "[ ]"
    old = self.__contents
    walk_backward = self.__front
    ret = "[ "
    for x in range(self.__size):
        ret = ret + str(old[walk_backward]) + ", "
        walk_backward = (walk_backward + 1) % len(old)
    ret = ret[0:len(ret)-2]
    ret = ret + " ]"
    return ret

    
  def __len__(self):
    return self.__size 

  def __grow(self):
    old = self.__contents
    walk_front = self.__front
    self.__capacity *= 2
    self.__contents = ([None] * self.__capacity)
    for i in range(self.__size):
        self.__contents[i] = old[walk_front]
        walk_front = (walk_front + 1) % len(old)
    self.__front = 0
        
  def push_front(self, val):
    if self.__size == self.__capacity:
        self.__grow()
    self.__front = (self.__front - 1) % len(self.__contents)
    self.__contents[self.__front] = val
    self.__size += 1
    
  def pop_front(self):
    if self.__size == 0:
        raise IndexError
    pop = self.__contents[self.__front]
    self.__contents[self.__front] = None
    self.__front = (self.__front + 1) % len(self.__contents)
    self.__size -=1
    return pop
    
  def peek_front(self):
    if self.__size == 0:
        return False
    return self.__contents[self.__front]
    
  def push_back(self, val):
    if self.__size == self.__capacity:
        self.__grow() 
    self.__contents[ (self.__front + self.__size) % len(self.__contents)] = val
    self.__size += 1
    
  def pop_back(self):
    if self.__size == 0:
        raise IndexError
    pop = self.__contents[(self.__front + self.__size - 1) % len(self.__contents)]
    self.__contents[(self.__front + self.__size - 1) % len(self.__contents)] = None
    self.__size -=1 
    return pop

  def peek_back(self):
    if self.__size == 0:
        return False
    return self.__contents[(self.__front + self.__size - 1) % len(self.__contents)]

