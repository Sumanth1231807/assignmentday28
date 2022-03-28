def surface_area_prism(l,h,b):
    surface = 2*((l*b) + (l*h) + (b*h))
    return surface

def volume_prism(l,b,h):
    volume=l*b*h
    return volume

def diagonol_prism(l,b,h):
    diagonal = ((l * l) + (b * b )+ (h * h))
    sqrt = diagonal ** 0.5
    return sqrt

if __name__=="__main__":
    l=int(input("Enter the Length : "))
    b=int(input("Enter the Breath : "))
    h=int(input("Enter the Height : "))
    surface=surface_area_prism(l,h,b)
    print(surface)
    volume=volume_prism(l,b,h)
    print(volume)
    diagonal=diagonol_prism(l,b,h)
    print(diagonal)