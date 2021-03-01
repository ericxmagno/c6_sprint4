from time import sleep
import random1

def delay(seconds):
    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)

def main():
    for i in range(5):
        print(i)
        delay(random1.get_random_number())
        
if __name__ == "__main__":
    main()