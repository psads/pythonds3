'''
Testing the Binary Tree module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import sys, os
sys.path.insert(0, os.path.abspath('../..'))

import pytest
from pythonds3.trees.binary_tree import BinaryTree


class TestBinaryTreeMethods:
    
    @pytest.fixture(scope = 'function', autouse = True)
    def setup_class(cls):
        '''Setting up'''
        cls.tree = BinaryTree('A')

    def test_get_root_val(self):
        '''Testing get_root_val() method'''
        assert self.tree.get_root_val() == 'A'

    def test_is_leaf(self):
        '''Testing is_leaf() method'''
        assert self.tree.is_leaf()

    def test_insert_left(self):
        '''Testing insert_left() method'''
        assert self.tree.height() == 0
        self.tree.insert_left('B')
        assert self.tree.height() == 1

    def test_insert_right(self):
        '''Testing insert_right() method'''
        assert self.tree.height() == 0
        self.tree.insert_right('C')
        assert self.tree.height() == 1

    def test_get_child_left(self):
        '''Testing get_child_left() method'''
        self.tree.insert_left('B')
        assert self.tree.get_child_left().get_root_val() == 'B'

    def test_get_child_right(self):
        '''Testing get_child_right() method'''
        self.tree.insert_right('C')
        assert self.tree.get_child_right().get_root_val() == 'C'

    def test_height(self):
        '''Testing height() method'''
        assert self.tree.height() == 0
        self.tree.insert_left('B')
        assert self.tree.height() == 1
        self.tree.insert_right('C')
        assert self.tree.height() == 1
        self.tree.get_child_left().insert_left('D')
        assert self.tree.height() == 2

    def test_size(self):
        '''Testing count_nodes() method'''
        assert self.tree.size() == 1
        assert len(self.tree) == 1
        self.tree.insert_left('B')
        assert self.tree.size() == 2
        self.tree.insert_right('C')
        assert self.tree.size() == 3
        self.tree.get_child_left().insert_left('D')
        assert self.tree.size() == 4
        assert len(self.tree) == 4

    def test_preorder(self, capsys):
        '''Testing preorder() method'''
        self.tree.insert_left('B')
        self.tree.insert_right('C')
        self.tree.get_child_left().insert_left('D')
        self.tree.get_child_left().insert_right('E')
        self.tree.get_child_right().insert_left('F')
        self.tree.get_child_right().insert_right('G')

        self.tree.preorder()
        out, err = capsys.readouterr()
        assert out.strip() == 'A B D E C F G'

    def test_inorder(self, capsys):
        '''Testing inorder() method'''
        self.tree.insert_left('B')
        self.tree.insert_right('C')
        self.tree.get_child_left().insert_left('D')
        self.tree.get_child_left().insert_right('E')
        self.tree.get_child_right().insert_left('F')
        self.tree.get_child_right().insert_right('G')

        self.tree.inorder()
        out, err = capsys.readouterr()
        assert out.strip() == 'D B E A F C G'

    def test_postorder(self, capsys):
        '''Testing postorder() method'''
        self.tree.insert_left('B')
        self.tree.insert_right('C')
        self.tree.get_child_left().insert_left('D')
        self.tree.get_child_left().insert_right('E')
        self.tree.get_child_right().insert_left('F')
        self.tree.get_child_right().insert_right('G')

        self.tree.postorder()
        out, err = capsys.readouterr()
        assert out.strip() == 'D E B F G C A'

    def test_print_exp(self, capsys):
        '''Testing print_exp() method'''
        self.tree = BinaryTree('*')
        self.tree.insert_left('+')
        left_subtree = self.tree.get_child_left()
        left_subtree.insert_left(1)
        left_subtree.insert_right(5)
        self.tree.insert_right(7)

        self.tree.print_exp()
        out, err = capsys.readouterr()
        assert out.strip() == '( ( 1 + 5 ) * 7 )'

    def test_postorder_eval(self):
        '''Testing postorder_eval() method'''
        self.tree = BinaryTree('*')
        self.tree.insert_left('+')
        left_subtree = self.tree.get_child_left()
        left_subtree.insert_left(1)
        left_subtree.insert_right(5)
        self.tree.insert_right(7)

        assert self.tree.postorder_eval() == 42

if __name__ == '__main__':
    pytest.main(['test_binary_tree.py'])
