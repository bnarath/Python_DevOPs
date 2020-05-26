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
            print(list(range(user_input*loop, user_input*(loop+1))))
            loop+=1 #First time done
            try:
                yes_or_no = input("Want to continue? 'y' or 'n' ").lower()
                ['y', 'n'].index(yes_or_no)
            except ValueError:
                print("Strictly enter 'y' or 'n' ")
            except:
                print("Something went wrong")
            else:
                if yes_or_no == 'n':
                    done = True




