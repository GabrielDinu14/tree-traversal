import pytest
from main import tree

class TestFind(object):
    def test_find1(self):
        assert tree._find(2, tree.getRoot()).data == 2

    def test_find2(self):
        assert tree._find(4, tree.getRoot()).data == 4