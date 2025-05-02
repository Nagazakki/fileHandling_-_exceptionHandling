filename = input("Enter the filename to read: ")

try: 
    with open(filename, 'r', encoding = 'utf-8') as file:
        content = file.read()
        print("\nFile contains the following: ")
        print(content)

except FileNotFoundError: 
    print(f"That file don't exist buddy.")

