import keyword


class A_test:
    def __repr__(self):
        return "A_test 객체이다"


def main():
    print("hello, world")
    print(keyword.kwlist)

    print("this is", "python", "class!", sep="_", end="\n")

    print(A_test)


if __name__ == "__main__":
    main()


