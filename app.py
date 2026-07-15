import os

def main():
    name = os.getenv("NAME", "DefaultUser")
    print(f"Hello {name}, GitHub Actions + Jenkins working 🚀")

if __name__ == "__main__":
    main()