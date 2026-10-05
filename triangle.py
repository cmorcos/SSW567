# some code was previously done on my leetcode account for practice
"""triangle classification program"""
def classify_triangle(a, b, c):
    """classify triangle based on side lengths"""
    if a <= 0 or b <= 0 or c <= 0:  # check if it's actually a triangle
        return "none"
    if a + b <= c or a + c <= b or b + c <= a:  # check if it's actually a triangle
        return "none"
    if a == b == c:
        triangle = "equilateral"
    elif a == b or a == c or b == c:
        triangle = "isosceles"
    else:
        triangle = "scalene"

    sides = sorted([a, b, c])   # right angle check
    x, y, z = sides[0], sides[1], sides[2]

    if x**2 + y**2 == z**2:
        triangle += " right"

    return triangle


def main():
    """example triangle classifications"""
    examples = [
        (3, 3, 3),
        (5, 5, 3),
        (3, 4, 5),
        (4, 5, 6),
        (1, 2, 10),
    ]

    for a, b, c in examples:
        result = classify_triangle(a, b, c)
        print(f"classify_triangle({a}, {b}, {c}) = {result}")


if __name__ == "__main__":
    main()
