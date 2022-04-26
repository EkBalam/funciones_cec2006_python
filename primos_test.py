import pytest
import primos as pr

def test_es_divisible_true():    
    assert pr.es_divisible(15, 5) == True

def test_es_divisible_false():    
    assert pr.es_divisible(15, 6) == False

def test_es_primo_true():    
    assert pr.es_primo(17) == True
    
def test_es_primo_false():    
    assert pr.es_primo(221) == False

def test_i_esimo_primo():
    assert pr.i_esimo_primo(20) == 71
    
def test_primeros_primos():
    assert pr.primeros_primos(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
def test_primos_hasta():
    assert pr.primos_hasta(19) == [2, 3, 5, 7, 11, 13, 17, 19]
