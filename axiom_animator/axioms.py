
import math 
from fractions import Fraction
from typing import Callable, Union, Optional

#Setting Number as type that can be one of three
Number = Union[int, float, Fraction]
#Setting BinaryOp as a callable type with two args and number or possible Number or none return
BinaryOp = Callable[[Number, Number], Optional[Number]]
#Setting SetRue as a callable type with a single argument and single bool return
SetRule = Callable[[Number], bool]


 
# -- Set Memebership Function --
# These functions are pretty simple an check if a number is a whole number, integer, rational

def is_integer(num: Number) -> bool:
    return isinstance(num, int)

def is_whole_number(num: Number) -> bool:
    return isinstance(num, int) and num >=0

def is_rational(num: Number) -> bool: 
    return isinstance(num, (int, float, Fraction))

# -- Binary Operations -- 
# These functions are pretty simple as well, they just perform simple mathametical operations

def op_add(a: Number, b: Number) -> Number: 
    return a + b

def op_subtract(a: Number, b: Number) -> Number:
    return a - b

def op_multiply(a: Number, b: Number) -> Number:
    return a * b

def op_divide(a: Number, b: Number) -> Number | None:
    if b == 0:
        return None
    return a / b

# -- Axiom Checkers --

def is_closed(op: BinaryOp, a: Number, b: Number, rule: SetRule) -> bool: 
    try:
        result = op(a, b)
        return result is not None and rule(result)
    except Exception:
        return False
    
def is_commutative(op: BinaryOp, a: Number, b: Number) -> bool:
    try:
        return op(a, b) == op(b, a)
    except Exception:
        return False
    
def is_associative(op: BinaryOp, a: Number, b: Number, c: Number) -> bool:
    ab: Optional[Number] = op(a, b)
    bc: Optional[Number] = op(b, c)

    if ab is None or bc is None:
        return False
    left: Optional[Number] = op(ab, c)
    right: Optional[Number] = op(a, bc)

    return left == right if left is not None and right is not None else False

def has_identity(op: BinaryOp, identity: Number, a: Number) -> bool: 
    try: 
        return op(a, identity) == a and op(identity, a) == a
    except Exception:
        return False
    
def has_inverse(op: BinaryOp, identity: Number, a: Number, inverse: Number) -> bool:
    try: 
        return op(a, inverse) == identity and op(inverse, a) == identity
    except:
        return False