import script

print("import __name__ is set to: {}". format(__name__))

if __name__ == "__main__":
    print("import ran directly")
else:
    print("script ran through an import")
