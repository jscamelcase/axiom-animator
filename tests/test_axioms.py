
from fractions import Fraction 
from axiom_animator.axioms import (
    op_add,
    op_subtract,
    op_multiply,
    op_divide,
    is_closed,
    is_commutative,
    is_associative,
    has_identity,
    has_inverse, 
    is_integer, 
    is_rational,  
)

# -- CLOSURE TESTS -- #

#assert is a built-in keyword that lets you check that something is true during your progam's execution 

def test_addition_closure_rational():
    assert is_closed(op_add, 2, 3, is_rational)
    assert is_closed(op_add, 1.5, 2.5, is_rational)
    assert is_closed(op_add, Fraction(1, 2), Fraction(3, 4), is_rational)

def test_multiplecation_closure_integer():
    assert is_closed(op_multiply, 2, 3, is_integer)
    assert not is_closed(op_multiply, 2.5, 2, is_integer)

# -- COMMUTATIVITY --
def test_additon_commutativity():
    assert is_commutative(op_add, 2, 5)

def test_multiplication_commutativity():
    assert is_commutative(op_multiply, 4, 3)

# -- ASSOCIATIVITY --

def test_addition_associativity():
    assert is_associative(op_add, 1, 2, 3)

def test_multiplication_associativity():
    assert is_associative(op_multiply, 2, 3 ,4)

# -- IDENTITY ELEMENT --

def test_addition_identity():
    assert has_identity(op_add, 0, 7)

def test_multiplication_identity():
    assert has_identity(op_multiply, 1, 5)

# --INVERSE ELEMENT --
def test_additive_inverse():
    assert has_inverse(op_add, 0, 7, -7)
    assert has_inverse(op_add, 0, -3.5, 3.5)

def test_multiplicative_inverse(): 
    assert has_inverse(op_multiply, 1, 4, 0.25)
    assert has_inverse(op_multiply, 1, Fraction(1, 3), 3)