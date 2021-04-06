#!/usr/bin/python3

x = 0
while True:
    try:
        filename = input("Which file to open?:")
        with open(filename, "r") as fh:
            file_data = fh.read()
    except FileNotFoundError:
        print(f'Sorry, {filename} is not found!')
    else:
        print(file_data)
        x=0
        break
    finally:
        x += 1
        if x == 3:
            print('Wrog filename 3 tims.\nCheck name and Return.')
            break