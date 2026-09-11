# some code was previously done on my leetcode account for practice, tried to mesh it with the assignment requirements
def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "none"
 
    # inequality to validate it's actually a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "none"
 
    # classify triangle
    triangle = None
    if a == b == c:
        triangle = "equilateral"
    elif a == b or a == c or b == c:
        triangle = "isosceles"
    else:
        triangle = "scalene"
 
    # right angle check
    sides = sorted([a, b, c])
    x, y, z = sides[0], sides[1], sides[2]
    if x**2 + y**2 == z**2:     # pythagoreom theorem for right angle
        triangle += " right"
    return triangle
 
 
def main():
    examples = [
        (3, 3, 3),      # equilateral
        (5, 5, 3),      # isosceles
        (3, 4, 5),      # scalene right
        (4, 5, 6),      # scalene
        (1, 2, 10),     # none
    ]

    # formatting for clearer output
    for a, b, c in examples:
        print(f"classify_triangle({a}, {b}, {c}) = {classify_triangle(a, b, c)}")
 
 
if __name__ == "__main__":
    main()