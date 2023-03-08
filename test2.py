from app import inc
from app import get_age
from app import deinc

#test fonction 1
def test_answer1():
    assert inc(2) == 3

#test fonction 2
def test_get_age():
    
    assert get_age(1,5) == 6
    
#tset fonction 3
def test_answer2():
    assert deinc(17) == 16