def extract_dob(file):
    # Creating a list to store all the Date of Births
    dobs = []
    with open(file) as f:
        for line in f:
            fields = line.strip().split("\t")  # Split each field in a line using "\t"
            # Extracting Date of Birth alone
            dob = fields[4]
            if dob == "PAN Number":  # Skipping the first line
                continue
            dobs.append(dob)
    return dobs


print(extract_dob("customers.txt"))