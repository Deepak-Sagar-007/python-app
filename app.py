import os

def main():
    name = os.getenv("NAME", "DefaultUser")
    print(f"Hello {name}, how are you ")

if __name__ == "__main__":
    main()