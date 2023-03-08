from app import inc
from app import get_age
from app import deinc

#test fonction 1
def test_answer1():
    assert inc(1) == 2

#test fonction 2
def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "2002/09/11".split(""))   
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 25 
    
#tset fonction 3
def test_answer2():
    assert deinc(3) == 2