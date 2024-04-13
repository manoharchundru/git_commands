from modules import dirlister

if __name__ == "__main__":
    files = dirlister.run()
    print("Files in directory:", files)
