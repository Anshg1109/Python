def circle(radius):
    area = 3.14 * radius*radius
    print("Area of circle is : ",area)

def rectangle(height,width):
    area = height*width
    print("Area of Rectangle is : ",area)

def square(side):  
    area = side * side  
    print("Area of Square:", area)

def cylinder(height , radius):
    area = 2*3.14*radius*height + 2*3.14*radius*radius
    print("Area of cylinder: ",area)


while True:  
    print("\nMAIN MENU")  
    
    print("1. Calculate Area")  
    print("2. Exit")  
    choice1 = int(input("Enter the Choice:"))  
  
    
    if choice1 == 1:  
        print("\nCALCULATE AREA")  
        print("1. Circle")  
        print("2. Rectangle")  
        print("3. Square")  
        print("4. Cylinder")  
        print("5. Exit")
        choice3 = int(input("Enter the Choice:"))  
  
        if choice3 == 1:  
            radius = int(input("Enter Radius of Circle:"))  
            circle(radius)  
              
        elif choice3 == 2:  
            height = int(input("Enter Height of Rectangle:"))  
            width = int(input("Enter Width of Rectangle:"))  
            rectangle(height, width)  
              
        elif choice3 == 3:  
            side = int(input("Enter Side of Square:"))  
            square(side)  
        
        elif choice3 == 4:
            radius = int(input("Enter Radius of Cylinder:"))  
            height = int(input("Enter Height of Cylinder:"))
            cylinder(height,radius)
  
        elif choice3 == 5:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  
      
    elif choice1 == 2:  
        break  
      
    else:  
        print("Oops! Incorrect Choice.")

