while True:
    a = int(input("1. Add subject\n2. Change subject Info\n3. Subject Calculation\n4. Overall Calculation\n5. Quit\nOption: "))
    if a == 1:
        import createSubject
        createSubject
    elif a == 2:
        import changeSubInfo
        changeSubInfo
    elif a == 5:
        print("Thank you")
        break