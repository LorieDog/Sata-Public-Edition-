print("Hi my name is Sata (Version 0.31, Main Special Edition.), What command would you like to insert?")
print("calculator) 31123")
print("timer) 209135")
print("statistics) 192012019")
number = int(input())
match number:
    case 31123:
        import math
        print("hello! im some sort of calculator!! please type one of the numbers to start")
        print("1) +")
        print("2) -")
        print("3) *")
        print("4) /")
        print("5) ^x")
        print("6) √")
        print("7) count to...")
        number = int(input())
        match number:
            case 1:
                print("please insert an X")
                X = int(input())
                print("please insert an Y")
                Y = int(input())
                print("the number of the Addition is:", X+Y,"!")
            case 2:
                print("please insert an X")
                X = int(input())
                print("please insert an Y")
                Y = int(input())
                print("the number of the Subtraction is:", X-Y,"!")
            case 3:
                print("please insert an X")
                X = int(input())
                print("please insert an Y")
                Y = int(input())
                print("the number of the Multiplication is:", X*Y,"!")
            case 4:
                print("please insert an X")
                X = int(input())
                print("please insert an Y")
                Y = int(input())
                if X == 0 or Y == 0:
                    print("Error! Zero number!!")
                elif X != 0 and Y != 0:
                    print("the number of the Division is:", X/Y,"!")
            case 5:
                print("please insert an X")
                X = int(input())
                print("please insert an Y")
                Y = int(input())
                Z = pow(X, Y)
                if X == 0 or Y == 0:
                    print("Error! Zero number!!")
                elif X != 0 and Y != 0:
                    print("the number of the Power is:", Z,"!")
            case 6:
                print("please insert an X")
                X = int(input())
                Y = math.sqrt(X)
                if X == 0 or X < 0:
                    print("Error! Zero/negative number!!")
                elif X != 0 and X > 0:
                    print(Y)
            case 7:
                print("please insert an X")
                X = int(input())
                print("please insert an Y")
                Y = int(input())
                print("please insert an Z")
                Z = int(input())
                for X in range(X,Y):
                    if X%Z == 0:
                        print(X)
    case 209135:
        import time
        print("The time is:")
        print(time.ctime())
    case 192012019:
        import statistics
        print("hello! im some sort of calculator for stats!! please type one of the numbers to start")
        print("1) Average (with only 4 inputs)")
        number = int(input())
        match number:
            case 1:
                print("please insert an A")
                A = int(input())
                print("please insert an B")
                B = int(input())
                print("please insert an C")
                C = int(input())
                print("please insert an D")
                D = int(input())
                print(statistics.mean([A, B, C, D]))
import time
time.sleep(1.5) 
print("Oh well i've finished my job")
time.sleep(1.5) 
print("Do you want to exit? (Y/N)")
Exit = input()
if Exit.upper() == 'Y' or 'y':
    exit()