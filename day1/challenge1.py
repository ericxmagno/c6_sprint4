from time import sleep
import random

def delay(seconds):
    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)

def main():
    for i in range(5):
        print(i)
        delay(2)
        
if __name__ == "__main__":
    main()