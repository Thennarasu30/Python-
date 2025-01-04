class ClassFile:
    # Create a class and function, and list out the items in the list
    def Subfields():
        List = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Subfields in AI are:")
        for field in List:
            print(field)

    # Create a function that checks whether the given number is Odd or Even
    def OddEven():
        Number = int(input("Enter the Number: "))
        if (Number % 2) == 0:
            print(Number, "is an Even Number")
        else:
            print(Number, "is an Odd Number")

    # Create a function that tells eligibility of marriage for male and female according to their age limit
    def Eligible():
        Male = "Male"
        Female = "Female"
        Gender = input("Your Gender: ")
        Age = int(input("Your Age: "))
        if (Gender == Male and Age >= 21) or (Gender == Female and Age >= 18):
            print("Eligible")
        else:
            print("Not eligible")

    # Calculate the percentage of your 10th mark
    def Percentage():
        Subject1 = int(input("Subject1: "))
        Subject2 = int(input("Subject2: "))
        Subject3 = int(input("Subject3: "))
        Subject4 = int(input("Subject4: "))
        Subject5 = int(input("Subject5: "))
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        print("Total:", Total)
        Percentage = Total / 5
        print("Percentage:", Percentage)

    # Print area and perimeter of triangle using class and functions
    def Triangle():
        Height = int(input("Height: "))
        Breadth = int(input("Breadth: "))
        AreaFormula = (Height * Breadth) / 2
        print("Area Formula = (Height * Breadth) / 2")
        print("Area of Triangle:", AreaFormula)
        Height1 = int(input("Height1: "))
        Height2 = int(input("Height2: "))
        Breadth = int(input("Breadth: "))
        print("Perimeter formula: Height1 + Height2 + Breadth")
        print("Perimeter of Triangle:", (Height1 + Height2 + Breadth))
