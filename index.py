while True:
    a = int(input("1. Add subject\n2. Change subject Info\n3. Overall Calculation\n4. Quit\nOption: "))
    if a == 1:
        import createSubject
        createSubject
    elif a == 2:
        import changeSubInfo
        changeSubInfo
    elif a == 3:
        import overallCal
        overallCal
    elif a == 4:
        print("Thank you")
        break