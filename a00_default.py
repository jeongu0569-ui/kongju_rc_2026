class Add_test :
    def __add__(self,value):
        return value



def main():
    a = Add_test()
    b = Add_test()


    string = "this fomat: {2:d} {1:5d} {0:05f}".format(-10.1263, -20, -30)

    print(string)



if __name__ == "__main__":
    main()
