import random
import string

def randomPassGenerator(length):
    x = string.ascii_letters + string.digits + string.punctuation + string.hexdigits
    password = ''.join(random.choice(x)for t in range (length))
    return password
def main():
    while True:

        length = int(input("Enter Desired Digit or Length of Password: "))
        passW = randomPassGenerator(length)
        print(f'Your password is : {passW}')

if __name__ == '__main__':
    main()


