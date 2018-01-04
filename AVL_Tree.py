from Queue import Queue
class AVL_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1
      
     #balance        
    def _get_balance(self):
        if self.left is None and self.right is None:
          return 0
        elif self.left is None:
          return self.right.height
        elif self.right is None:
          return 0 - self.left.height
        else:
          return self.right.height - self.left.height
    
    #height for each node
    def _indiv_height(self):
      if self.right is None and self.left is None:
        self.height = 1
      elif self.left and self.right is None:
        self.height = self.left.height + 1 
      elif self.right and self.left is None: 
        self.height = self.right.height + 1  
      elif self.left.height >= self.right.height:
        self.height = self.left.height + 1        
      else:
        self.height = self.right.height + 1    
        
  def __balance(self, current):
    cur_balance = current._get_balance()
    if cur_balance < 2 and cur_balance > -2:
      return current
    if cur_balance == 2:
      r_balance = current.right._get_balance()
      if r_balance == 1 or r_balance == 0:
        return self._right_rotate(current)
      elif r_balance == -1:
        current.right = self._left_rotate(current.right)
        return self._right_rotate(current)
    if cur_balance == -2:
      l_balance = current.left._get_balance()
      if l_balance == -1 or l_balance == 0:
        return self._left_rotate(current)
      elif l_balance == 1:
        current.left = self._right_rotate(current.left)
        return self._left_rotate(current)

  def _right_rotate(self, node):
    n_left = node
    n_parent = node.right
    if node.right.left:
      n_left.right = node.right.left
    else:
      n_left.right = None
    n_parent.left = n_left
    n_left._indiv_height()
    n_parent._indiv_height()
    return n_parent

  def _left_rotate(self, node):
    n_right = node
    n_parent = node.left
    if node.left.right:
      n_right.left = node.left.right
    else:
      n_right.left = None
    n_parent.right = n_right
    n_right._indiv_height()
    n_parent._indiv_height()
    return n_parent

  #insert
  def _insert_recursion(self, node, val):
        if node:
            if node.value == val:
                raise ValueError
            elif node.value > val:
                if node.left:
                    node.left = self._insert_recursion(node.left, val)
                else:
                    node.left = self.__BST_Node(val)
            else:
                if node.right:                
                    node.right = self._insert_recursion(node.right, val)            
                else:
                    node.right = self.__BST_Node(val)
        else: 
            node = self.__BST_Node(val)
        node._indiv_height()
        return self.__balance(node)
    
  #height      
  def _height(self, node):
        if node.left and node.right:
            if self._height(node.left) >= self._height(node.right):
                return 1 + self._height(node.left)
            else:
                return 1 + self._height(node.right)
        elif node.left:
            return 1 + self._height(node.left)
        elif node.right:
            return 1 + self._height(node.right)
        else:
            return 1
    
  #remove_element
  def _remove_recursion(self, val, node):
    if node is None:
      raise ValueError
    if node.value == val:
      node = self._rem(node)
      if node is None:
        return node
    elif val < node.value:
     node.left = self._remove_recursion(val, node.left)
     node._indiv_height()    	
    elif val > node.value:
      node.right = self._remove_recursion(val, node.right)
      node._indiv_height()
    return self.__balance(node)
	
  def _rem(self, current):
    if current.left is None and current.right is None:
      return None 	
    elif current.left and current.right is None:
      return current.left      
    elif current.left is None and current.right:
      return current.right    	
    else:
        n_node = current.right
        while n_node.left:
          n_node = n_node.left
        current.value = n_node.value
        current.right = self._remove_recursion(current.value, current.right)
        return current
    
  #pre_order private
  def _pre_order_rec(self, node, ret):
      ret = ret + str(node.value) + ", "
      if node.left is not None:
          ret = self._pre_order_rec(node.left, ret)
      if node.right is not None:
          ret = self._pre_order_rec(node.right, ret)
      return ret
  def _pre_order(self):
    #base case
    if self.__root is None:
          return"[ ]"    
    else:
        po_string = "[ "
        po_string = self._pre_order_rec(self.__root, po_string)
        po_string = po_string[0:-2] + " ]"
        return po_string
    
  #in_order but in list form
  def __iol_rec(self, node):
      if node.left and node.right:
          return self.__iol_rec(node.left) + [node.value] + self.__iol_rec(node.right)
      elif node.left:
          return self.__iol_rec(node.left) + [node.value]
      elif node.right:
          return [node.value] + self.__iol_rec(node.right)
      else:
          return [node.value]
  
  #in_order private
  def _in_order_rec(self, node, ret):
    if node.left is None:
        ret += str(node.value) + ", "
    else:
        ret = self._in_order_rec(node.left, ret)
        ret += str(node.value) + ", "
    if node.right is not None:
        ret = self._in_order_rec(node.right, ret)
    return ret        
  def _in_order(self):
    #base case
    if self.__root is None:
        return "[ ]"
    else:
        io_string = "[ "
        io_string = self._in_order_rec(self.__root, io_string)
        io_string = io_string[0:-2] + " ]"
        return io_string
    
  #post_order private
  def _post_order_rec(self, node, ret):
      if node.left is not None:
          ret = self._post_order_rec(node.left, ret)
      if node.right is None:
          ret = ret + str(node.value) + ", "
      else:
          ret = self._post_order_rec(node.right, ret)
          ret = ret + str(node.value) + ", "
      return ret
  def _post_order(self):
    #base case
    if self.__root is None:
        return "[ ]"
    else:
        poo_string = "[ "
        poo_string = self._post_order_rec(self.__root, poo_string)
        poo_string = poo_string[0:-2] + " ]"
        return poo_string
        
      
  def __init__(self):
      self.__root = None
      self.__tr = 0
      
  def insert_element(self, val):
      self.__root = self._insert_recursion(self.__root, val)
      self.__tr = self._height(self.__root) 

  def remove_element(self, value):
      self.__root = self._remove_recursion(value, self.__root)
      if self.__root:
          self.__tr = self._height(self.__root)
          
  def to_list(self):
      in_order_l = list()
      if self.__root is None:
          return in_order_l
      elif self.__root.left is None and self.__root.right is None:
          in_order_l.append(self.__root.value)
      else:
          in_order_l += self.__iol_rec(self.__root)
      return in_order_l 
  
  def in_order(self):
    return self._in_order()
    
  def pre_order(self):
    return self._pre_order()

  def post_order(self):
    return self._post_order()
    
  def breadth_first(self):
     if self.__root is None:
         return "[ ]"
     ret = "[ "
     horizontal_tra = Queue()
     horizontal_tra.enqueue(self.__root)
     while len(horizontal_tra) != 0:
         pop = horizontal_tra.dequeue()
         if pop.left is not None and pop.right is not None:
             horizontal_tra.enqueue(pop.left)
             horizontal_tra.enqueue(pop.right)
             ret = ret + str(pop.value) + ", "
         elif pop.left:
            horizontal_tra.enqueue(pop.left)
            ret = ret + str(pop.value) + ", "
         elif pop.right:
            horizontal_tra.enqueue(pop.right)
            ret = ret + str(pop.value) + ", "
         elif not pop.right and not pop.left and len(horizontal_tra) == 0:
            ret = ret + str(pop.value) + " ]"
         elif not pop.right and not pop.left:
            ret = ret + str(pop.value) + ", "
     return ret
    
  def get_height(self):
      if self.__root:
          return self.__tr
      else:
          return 0
  
  def __str__(self):
    return self.in_order()
