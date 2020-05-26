loop = 0
done = False
while not done:
    try:
        user_input = int(input("How many numbers?"))
    except ValueError:
        print("Enter an integer, please")
    except:
        print("Something went wrong")
    else:
        while not done:
            for no in range(user_input*loop, user_input*(loop+1)):
                print(no, end='\t')
            print('\n')
            loop+=1 #First time done
            entered_y_or_no = False
            while not entered_y_or_no:
                try:
                    yes_or_no = input("Want to continue? 'y' or 'n' ").lower()
                    ['y', 'n'].index(yes_or_no)
                except ValueError:
                    print("Strictly enter 'y' or 'n' ")
                except:
                    print("Something went wrong")
                else:
                    entered_y_or_no = True
                    if yes_or_no == 'n':
                        done = True




