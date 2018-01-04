import unittest
from AVL_Tree import AVL_Tree

class AVL_Test(unittest.TestCase):

  def setUp(self):
    self.__string_bst = AVL_Tree()
    
  def test_empty(self):
      self.assertEqual('[ ]', str(self.__string_bst), 'Empty Tree(in_order) should be printed "[ ]"')
      self.assertEqual('[ ]', self.__string_bst.pre_order(), 'Empty Tree(pre_order) should be printed "[ ]"')
      self.assertEqual('[ ]', self.__string_bst.post_order(), 'Empty Tree(post_order) should be printed "[ ]"')
      self.assertEqual('[ ]', self.__string_bst.breadth_first(), 'Empty Tree(breadth_first) should be printed "[ ]"')
      
  def test_value_error(self):
      with self.assertRaises(ValueError):
          self.__string_bst.remove_element(1)
      self.assertEqual('[ ]', str(self.__string_bst), 'Should raise ValueError')

  def test_height_empty_tree_then_insert_then_remove(self):
      self.assertEqual(0, self.__string_bst.get_height(), 'Empty tree should have height of 0')
      self.__string_bst.insert_element(1)
      self.assertEqual(1, self.__string_bst.get_height(), 'Height should be 1 now')
      self.__string_bst.remove_element(1)
      self.assertEqual(0, self.__string_bst.get_height(), 'Empty tree should have height of 0')
    
  def test_string_outputs_right_trees(self):
      for i in range(1, 10):
          self.__string_bst.insert_element(i)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]', str(self.__string_bst), 'in_order format fails')
      self.assertEqual('[ 4, 2, 1, 3, 6, 5, 8, 7, 9 ]', self.__string_bst.pre_order(), 'pre_order format fails')
      self.assertEqual('[ 4, 2, 6, 1, 3, 5, 8, 7, 9 ]', self.__string_bst.breadth_first(), 'breadth_first format fails')
      self.assertEqual('[ 1, 3, 2, 5, 7, 9, 8, 6, 4 ]', self.__string_bst.post_order(), 'post_order format fails')
      
  def test_string_outputs_left_trees(self):
      for i in range (9, 0, -1):
          self.__string_bst.insert_element(i)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]', str(self.__string_bst), 'in_order format fails')
      self.assertEqual('[ 6, 4, 2, 1, 3, 5, 8, 7, 9 ]', self.__string_bst.pre_order(), 'pre_order format fails')
      self.assertEqual('[ 6, 4, 8, 2, 5, 7, 9, 1, 3 ]', self.__string_bst.breadth_first(), 'breadth_first format fails')
      self.assertEqual('[ 1, 3, 2, 5, 4, 7, 9, 8, 6 ]', self.__string_bst.post_order(), 'post_order format fails')
  
  def test_remove_leaf_node(self):
      self.__string_bst.insert_element(26)
      self.__string_bst.insert_element(19)
      self.__string_bst.insert_element(29)
      self.__string_bst.insert_element(13)
      self.__string_bst.insert_element(22)
      self.__string_bst.insert_element(31)
      self.assertEqual('[ 13, 19, 22, 26, 29, 31 ]', str(self.__string_bst), 'in_order before removal format fails')
      self.__string_bst.remove_element(13)
      self.assertEqual('[ 19, 22, 26, 29, 31 ]', str(self.__string_bst), 'in_order after removal format fails')
      self.assertEqual('[ 26, 19, 22, 29, 31 ]', self.__string_bst.pre_order(), 'pre_order after removal format fails')
      self.assertEqual('[ 26, 19, 29, 22, 31 ]', self.__string_bst.breadth_first(), 'breadth_first after removal format fails')
      self.assertEqual('[ 22, 19, 31, 29, 26 ]', self.__string_bst.post_order(), 'post_order after removal format fails')
  
  def test_remove_node_with_one_child(self):
      self.__string_bst.insert_element(26)
      self.__string_bst.insert_element(19)
      self.__string_bst.insert_element(29)
      self.__string_bst.insert_element(13)
      self.__string_bst.insert_element(22)
      self.__string_bst.insert_element(31)
      self.assertEqual('[ 13, 19, 22, 26, 29, 31 ]', str(self.__string_bst), 'in_order before removal format fails')
      self.__string_bst.remove_element(29)
      self.assertEqual('[ 13, 19, 22, 26, 31 ]', str(self.__string_bst), 'in_order after removal format fails')
      self.assertEqual('[ 26, 19, 13, 22, 31 ]', self.__string_bst.pre_order(), 'pre_order after removal format fails')
      self.assertEqual('[ 26, 19, 31, 13, 22 ]', self.__string_bst.breadth_first(), 'breadth_first after removal format fails')
      self.assertEqual('[ 13, 22, 19, 31, 26 ]', self.__string_bst.post_order(), 'post_order after removal format fails')  
      
  def test_remove_leaf_nodes_test_height(self):
      self.__string_bst.insert_element(26)
      self.__string_bst.insert_element(19)
      self.__string_bst.insert_element(29)
      self.__string_bst.insert_element(13)
      self.__string_bst.insert_element(22)
      self.__string_bst.insert_element(31)
      self.assertEqual(3, self.__string_bst.get_height(), 'Height should be 3')
      self.__string_bst.remove_element(13)
      self.__string_bst.remove_element(22)
      self.__string_bst.remove_element(31)
      self.assertEqual(2, self.__string_bst.get_height(), 'Height should be 2')
 
  def test_remove_node_with_one_child_test_height(self):
      self.__string_bst.insert_element(26)
      self.__string_bst.insert_element(19)
      self.__string_bst.insert_element(29)
      self.__string_bst.insert_element(13)
      self.__string_bst.insert_element(22)
      self.__string_bst.insert_element(31)
      self.assertEqual(3, self.__string_bst.get_height(), 'Height should be 3')
      self.__string_bst.remove_element(29)
      self.assertEqual(3, self.__string_bst.get_height(), 'Height should be 3')
      
  def test_a_very_complicated_tree(self):
      self.__string_bst.insert_element(17)
      self.__string_bst.insert_element(-6)
      self.__string_bst.insert_element(12) 
      self.__string_bst.insert_element(14)
      self.__string_bst.insert_element(26)
      self.__string_bst.insert_element(-2)
      self.__string_bst.insert_element(0)
      self.__string_bst.insert_element(18)
      self.__string_bst.insert_element(-3)
      self.__string_bst.insert_element(20)
      self.__string_bst.insert_element(19)
      #remove for rotation
      self.__string_bst.remove_element(12)
      self.__string_bst.remove_element(17)
      #insert for rotation
      self.__string_bst.insert_element(-5)
      self.__string_bst.insert_element(-4)
      self.assertEqual('[ 14, -3, 20, -5, -2, 18, 26, -6, -4, 0, 19 ]', self.__string_bst.breadth_first(), 'breadth_first fails')
      self.assertEqual('[ -6, -5, -4, -3, -2, 0, 14, 18, 19, 20, 26 ]', str(self.__string_bst), 'in_order fails')
      self.assertEqual('[ 14, -3, -5, -6, -4, -2, 0, 20, 18, 19, 26 ]', self.__string_bst.pre_order(), 'pre_order fails')
      self.assertEqual('[ -6, -4, -5, 0, -2, -3, 19, 18, 26, 20, 14 ]', self.__string_bst.post_order(), 'post_order fails')
      
  #height tests
  def test_height_right(self):
      for i in range(1, 10):
          self.__string_bst.insert_element(i)
      self.assertEqual(4, self.__string_bst.get_height(), 'Height should be 4')
      
  def test_height_left(self):
      for i in range(9, 0, -1):
          self.__string_bst.insert_element(i)
      self.assertEqual(4, self.__string_bst.get_height(), 'Height should be 4')
      
  def test_string_formats_and_removal_and_height(self):
      for i in range(1, 10):
          if i%2 == 1:
              self.__string_bst.insert_element(i)
      for i in range(1, 10):
          if i%2 == 0:
              self.__string_bst.insert_element(i)
      self.assertEqual(4, self.__string_bst.get_height(), 'Height should be 4')
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]', str(self.__string_bst), 'in_order format fails')
      self.assertEqual('[ 3, 1, 2, 7, 5, 4, 6, 9, 8 ]', self.__string_bst.pre_order(), 'pre_order format fails')
      self.assertEqual('[ 3, 1, 7, 2, 5, 9, 4, 6, 8 ]', self.__string_bst.breadth_first(), 'breadth_first format fails')
      self.assertEqual('[ 2, 1, 4, 6, 5, 8, 9, 7, 3 ]', self.__string_bst.post_order(), 'post_order format fails')
      self.__string_bst.remove_element(4)
      self.assertEqual(4, self.__string_bst.get_height(), 'Height should still be 4')
      
  def test_insert_value_already_in_tree(self):
      for i in range(1, 10):
          if i%2 == 1:
              self.__string_bst.insert_element(i)
      for i in range(1, 10):
          if i%2 == 0:
              self.__string_bst.insert_element(i)
      self.__string_bst.insert_element(26)
      self.__string_bst.insert_element(19)
      self.__string_bst.insert_element(29)
      self.__string_bst.insert_element(13)
      self.__string_bst.insert_element(22)
      self.__string_bst.insert_element(31)
      with self.assertRaises(ValueError):
          self.__string_bst.insert_element(13)
          
  def test_remove_value_not_in_tree(self):
      for i in range(1, 10):
          if i%2 == 1:
              self.__string_bst.insert_element(i)
      for i in range(1, 10):
          if i%2 == 0:
              self.__string_bst.insert_element(i)
      self.__string_bst.insert_element(26)
      self.__string_bst.insert_element(19)
      self.__string_bst.insert_element(29)
      self.__string_bst.insert_element(13)
      self.__string_bst.insert_element(22)
      self.__string_bst.insert_element(31)
      with self.assertRaises(ValueError):
          self.__string_bst.remove_element(12)

  def test_remove_node_two_children_and_height(self):
      self.__string_bst.insert_element(20)
      self.__string_bst.insert_element(19)
      self.__string_bst.insert_element(50)
      self.__string_bst.insert_element(6)
      self.__string_bst.insert_element(19.5)
      self.__string_bst.insert_element(27)
      self.__string_bst.insert_element(1693)
      self.assertEqual('[ 6, 19, 19.5, 20, 27, 50, 1693 ]', str(self.__string_bst), 'in_order before removal format fails')
      self.assertEqual('[ 20, 19, 6, 19.5, 50, 27, 1693 ]', self.__string_bst.pre_order(), 'pre_order before removal format fails')
      self.assertEqual('[ 20, 19, 50, 6, 19.5, 27, 1693 ]', self.__string_bst.breadth_first(), 'breadth_first before removal format fails')
      self.assertEqual('[ 6, 19.5, 19, 27, 1693, 50, 20 ]', self.__string_bst.post_order(), 'post_order before removal format fails')
      self.assertEqual(3, self.__string_bst.get_height(), 'Height should be 3')
      self.__string_bst.remove_element(20)
      self.assertEqual('[ 6, 19, 19.5, 27, 50, 1693 ]', str(self.__string_bst), 'in_order after removal format fails')
      self.assertEqual('[ 27, 19, 6, 19.5, 50, 1693 ]', self.__string_bst.pre_order(), 'pre_order after removal format fails')
      self.assertEqual('[ 27, 19, 50, 6, 19.5, 1693 ]', self.__string_bst.breadth_first(), 'breadth_first after removal format fails')
      self.assertEqual('[ 6, 19.5, 19, 1693, 50, 27 ]', self.__string_bst.post_order(), 'post_order after format fails')
      self.assertEqual(3, self.__string_bst.get_height(), 'Height after removal of root should be 3')
      
if __name__ == '__main__':
  unittest.main()
