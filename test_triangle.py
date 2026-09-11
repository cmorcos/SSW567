from triangle import classify_triangle

def test_equilateral():
    assert classify_triangle(3, 3, 3) == "equilateral"
 
def test_big_equilateral():
    assert classify_triangle(1000, 1000, 1000) == "equilateral"

def test_isosceles1():
    assert classify_triangle(5, 5, 3) == "isosceles"
 
 
def test_isosceles2():
    assert classify_triangle(3, 5, 5) == "isosceles"
 
 
def test_isosceles3():
    assert classify_triangle(5, 3, 5) == "isosceles"

def test_scalene1():
    assert classify_triangle(4, 5, 6) == "scalene"
 
 
def test_scalene_right():
    assert classify_triangle(3, 4, 5) == "scalene right"
    assert classify_triangle(5, 3, 4) == "scalene right"
    assert classify_triangle(4, 5, 3) == "scalene right"
    assert classify_triangle(5, 12, 13) == "scalene right"

def test_zero():
    assert classify_triangle(0, 3, 3) == "none"
 
 
def test_negative():
    assert classify_triangle(-3, 4, 5) == "none"
 
 
def test_incorrect_triangle_inequality():
    assert classify_triangle(1, 2, 10) == "none"
 
 
def test_nontriangle():
    # 1 + 2 == 3, a straight line, not a real triangle
    assert classify_triangle(1, 2, 3) == "none"
 
 
def test_triangle_inequality_middle_side_large():
    assert classify_triangle(1, 10, 1) == "none"

def test_scalene():
    assert classify_triangle(2.5, 3.5, 4.5) == "scalene"