"""subject reader programming"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display it"""
    data = get_data()
    print(data)
    display_subject(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
        # print("----------")
    input_file.close()
    return data


def display_subject(data):
    """display subject data"""
    for subject_data in data:
        print("{} is taught by  {:13} and has {:4} students".format(*subject_data))  # version 1
        # print(f"{subject_data[0]} is taught by {subject_data[1]} and has {subject_data[2]} students")   version 2

main()
