while True:
    y = input("Do you continue the program"
              "please enter y/n: ")
    # print(input_program)

    if y == "y":
        # 1 for Python Basic Program
        print("Enter 1 for Python Basic Program")
        input_program = int(input("Enter your Choice: "))
        if input_program == 1:
            print("-----------------------------------------------------------------")
            print("1st Level Program please select what you want to see\n"
                  "1. Hello World\n"
                  "2. End statement use\n"
                  "3. C:\\darshit\\python Video\\ Fy\\ Newfolderprint f,n small\n"
                  "4. Arithmetic Operations\n"
                  "5. String Slicing")

            sub_basic_program = int(input("(Basic Python Program)Enter your Choice: "))

            # ---------------------------------------------------------------------------------------
            # 4. Writing Our First Python Program _ Python Tutorials For Absolute Beginners In Hindi
            # ---------------------------------------------------------------------------------------

            if sub_basic_program == 1:
                print("Hello World")

            elif sub_basic_program == 2:
                print("Hello World")
                print("Hello Developers")
                print("\n difference\n")
                print("Hello World", end=", ")
                print("Hello Developers")

            elif sub_basic_program == 3:
                print("C:\\darshit\\python Video\\fy\\new folder")

            # ---------------------------------------------------------------------------------------
            # 5. Using Python As A Calculator _ Python Tutorials For Absolute Beginners In Hindi
            # 6. Comments, Escape Sequences & Print Statement_ Python Tutorials For Absolute Beginners In Hindi
            # 7. Variables, Datatypes and Typecasting _ Python Tutorials For Absolute Beginners In Hindi
            # ---------------------------------------------------------------------------------------
            elif sub_basic_program == 4:
                while True:
                    try:
                        art_yn = int(input("To Arithmetic Continue Operation  1/0: "))

                        if art_yn == 1:

                            num1 = int(input("Enter Value Num1: "))
                            num2 = int(input("Enter Value Num2: "))
                            print("Enter 1 for addition         ( + )")
                            print("Enter 2 for Subtraction      ( - )")
                            print("Enter 3 for Multiplication   ( * )")
                            print("Enter 4 for Division         ( / )")
                            print("Enter 5 for Modulus          ( % )")
                            print("Enter 6 for Exponentiation   ( ** )")
                            print("Enter 7 for Floor Division   ( // )")
                            a_opretion = int(input("Enter your Choice: "))

                            if a_opretion == 1:
                                print("Two Number Addition is :", num1 + num2)

                            elif a_opretion == 2:
                                print("Two Number Subtraction is :", num1 - num2)

                            elif a_opretion == 3:
                                print("Two Number Multiplication is :", num1 * num2)

                            elif a_opretion == 4:
                                print("Two Number Division is :", num1 / num2)

                            elif a_opretion == 5:
                                print("Two Number Modulus is :", num1 % num2)

                            elif a_opretion == 6:
                                print("Two Number Exponentiation is :", num1 ** num2)

                            elif a_opretion == 7:
                                print("Two Number Floor Division is :", num1 // num2)
                            else:
                                break

                        else:
                            break
                    except Exception as e:
                        print("Please Enter Valid Input 1 or 0", "Error: (", e, " )")

            # ---------------------------------------------------------------------------------------
            # 8. String Slicing And Other Functions In Python _ Python Tutorials For Absolute Beginners In Hindi
            # ---------------------------------------------------------------------------------------
            elif sub_basic_program == 5:
                string_slic = str(input("Enter your String: "))

                while True:
                    try:
                        sli = input("Do you continue the Slicing\n"
                                    "please enter y/n: ")
                        if sli == "y":
                            print("\n---Select One---\n"
                                  "1. normal Slicing\n"
                                  "2. char skip\n")

                            sli_typ = int(input("Enter your Choice: "))
                            if sli_typ == 1:
                                f = input("Enter Slicing start point: ")
                                lt = input("Enter Slicing End point: ")
                                if f == "" and lt == "":
                                    print(string_slic[:])

                                elif f == "":
                                    lt = int(lt)
                                    print(string_slic[:lt])

                                elif lt == "":
                                    f = int(f)
                                    print(string_slic[f:])

                                else:
                                    f = int(f)
                                    lt = int(lt)
                                    print(string_slic[f:lt])

                            elif sli_typ == 2:
                                s_f = input("Enter Slicing start point: ")
                                s_lt = input("Enter Slicing End point: ")
                                skp = input("Enter (How many step to jump): ")

                                if s_f == "" and s_lt == "" and skp == "":
                                    # s_f = 0
                                    # s_lt = 0
                                    # skp = 0
                                    print(string_slic[::])

                                elif s_f == "" and s_lt == "":
                                    skp = int(skp)
                                    print(string_slic[::skp])

                                elif s_f == "" and skp == "":
                                    s_lt = int(s_lt)
                                    print(string_slic[:s_lt:])

                                elif s_lt == "" and skp == "":
                                    s_f = int(s_f)
                                    print(string_slic[s_f::])

                                elif s_f == "":
                                    s_lt = int(s_lt)
                                    skp = int(skp)
                                    print(string_slic[:s_lt:skp])

                                elif s_lt == "":
                                    s_f = int(s_f)
                                    skp = int(skp)
                                    print(string_slic[s_f::skp])

                                elif skp == "":
                                    s_f = int(s_f)
                                    s_lt = int(s_lt)
                                    print(string_slic[s_f:s_lt:])

                                else:
                                    print(string_slic[s_f:s_lt:skp])
                                    break

                            else:
                                break

                        else:
                            print("Thank you Using for Slicing program ")
                            break

                    except Exception as e:
                        print(e)

            elif sub_basic_program == 6:
                print("6")

            elif sub_basic_program == 7:
                print("7")
            elif sub_basic_program == 8:
                print("8")
        elif input_program == 2:
            print("2nd Program")

    else:
        print("Thank You for use and learn My program")
        break
