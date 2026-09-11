from triangle import classify_triangle

def test_equilateral():
    assert classify_triangle(3, 3, 3) == "equilateral"
 
def test_big_equilateral():
    assert classify_triangle(1000, 1000, 1000) == "equilateral"