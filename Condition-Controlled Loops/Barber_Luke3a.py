print('Triangle Validity')


keepgoing = 'yes'
while keepgoing == 'yes':
    #input point 1
    print()
    invalid_input = True
    while invalid_input == True:
        pt1x = float(input('Enter the X position of point 1: '))
        if pt1x <0:
            invalid_input = True
            print('Enter a non-negative number')
        elif pt1x >=0:
            invalid_input = False
         
    invalid_input = True
    while invalid_input == True:
        pt1y = float(input('Enter the Y position of point 1: '))
        if pt1y <0:
            invalid_input = True
            print('Enter a positive number or 0')
        elif pt1y >=0:
            invalid_input = False
    print()

    #input point 2
    invalid_input = True
    while invalid_input == True:
        pt2x = float(input('Enter the X position of point 2: '))
        if pt2x <0:
            invalid_input = True
            print('Enter a non-negative number')
        elif pt2x >=0:
            invalid_input = False
    
    invalid_input = True
    while invalid_input == True:
        pt2y = float(input('Enter the Y position of point 2: '))
        if pt2y <0:
            invalid_input = True
            print('Enter a positive number or 0')
        elif pt2y >=0:
            invalid_input = False
    print()
    #input point 3
    invalid_input = True
    while invalid_input == True:
        pt3x = float(input('Enter the X position of point 3: '))
        if pt3x <0:
            invalid_input = True
            print('Enter a non-negative number')
        elif pt3x >=0:
            invalid_input = False
            
    invalid_input = True
    while invalid_input == True:
        pt3y = float(input('Enter the Y position of point 2: '))
        if pt3y <0:
            invalid_input = True
            print('Enter a positive number or 0')
        elif pt3y >=0:
            invalid_input = False
    print()


    #distance computation
    side1 = ((pt1x - pt2x)**2 + (pt1y - pt2y)**2)**0.5
    side2 = ((pt2x - pt3x)**2 + (pt2y - pt3y)**2)**0.5
    side3 = ((pt3x - pt1x)**2 + (pt3y - pt1y)**2)**0.5

    print('Here are the lengths of each side of the triangle.')
    print('Side 1:',"{:.2f}".format(side1))
    print('Side 2:',"{:.2f}".format(side2))
    print('Side 3:',"{:.2f}".format(side3))
    print()

    formside1 = "{:.2f}".format(side1)
    formside2 = "{:.2f}".format(side2)
    formside3 = "{:.2f}".format(side3)

    #validity check
    if side1+side2 > side3:
        if side2+side3 > side1:
            if side3+side1 > side2:
                print('This is a valid triangle.')
                invalid_tri = False
    else:
        print('This is not a valid triangle')
        invalid_tri = True

    #triangle type
    if invalid_tri == False:
        if  formside1 == formside2 == formside3:
            print('It is equilateral.')
        elif formside1 == formside2 or formside2 == formside3 or formside3 == formside1:
            print('It is iscoceles.')
        elif formside1 != formside2 != formside3:
            print('It is scalene.')

    #keep going?
    print()
    keepgoing = input('Would you like to test another triangle? (yes/no): ')

if keepgoing == 'no':
    print('THE END')











