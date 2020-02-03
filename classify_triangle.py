"""

Testing Triangle Classification
@eltonaloys

"""

def classify_triangle(a,b,c):
    """ Classifying the triangles with properties of the triangle """
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            return "Equilateral Triangle"
        elif a == b or b == c or a == c:
            return "Isoceles Triangle"
        elif a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b:
            return "Right Triangle"
        elif a != b or b != c or a != c:
            return "Scalene Triangle"
    else:
        return "Invalid Triangle"
    


def main():
    """ Taking a valid input for the sides of a triangle """
    try:
        a,b,c = input("Enter the sides of an triangle\n").split()
        a,b,c = int(a), int(b), int(c)
    except ValueError:
        print("The Given Input is an Invalid Integer")
    print(classify_triangle(a,b,c)) 

main()