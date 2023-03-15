'''importer ...'''
import app


def test_pyanswer1():
    '''test fonction 1'''
    assert app.inc(1) == 2
def test_pyaddition():
    '''test fonction 2'''
    assert app.addition(2, 1) == 3
    assert app.addition(6, 1) == 7
def test_pyanswer2():
    '''tset fonction 3'''
    assert app.deinc(3) == 2
