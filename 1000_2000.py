#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: November 2019
# This program prints the number 1000-2000


def main():
    # this function prints the number 1000-2000

    # process & output
    for counter in range(1000, 2001):
        print(str(counter) + " ", end="")
        if (counter % 5 == 4):
            print("")


if __name__ == "__main__":
    main()
