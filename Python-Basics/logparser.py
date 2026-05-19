
with open("auth.log", "r") as f:
    for line in f:
        if "FAILED" in line:
            print(line.strip())



