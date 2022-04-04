#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program calculates if the grandchild can date~~


def main():
    # this function calculates if the grandchild can date w/ And & try catch

    # input
    age_Number_string = input("What is your Age? : ")

    # process & output
    try:
        age_Number = int(age_Number_string)

        if age_Number >= 25 and age_Number <= 40:
            print("You are acceptable for my grand child")
        else:
            print("You are Not acceptable for my grand child")

    except Exception:
        print("Not a valid Age")
    print("\nDone.")


if __name__ == "__main__":
    main()
