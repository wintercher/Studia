a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

def in_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

if is_a_triangle(a, b, c):
    print("True")
else:
    print("False")

#dobry kod
