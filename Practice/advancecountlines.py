"""
Program to count lines from user input text file with.
"""

__author__ = "Sachin Kharel"

def main():
    getfilename = input("Enter the file name: ")
    try:
        fhand = open("Practice/"+ getfilename)
    except:
        print("File cannot be opened or File not found: ", getfilename)
        quit()
    count = 0
    for line in fhand:
        count =count + 1
        print(count, line)
    print("\nLine count: ", count)
    

if __name__ == "__main__":
    main()
