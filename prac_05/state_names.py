"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state KeyError")
    state_code = input("Enter short state: ").upper()
try:
    print(f"{state_code}:{CODE_TO_NAME[state_code]}")
except:
    print("Empty choice")

for state in CODE_TO_NAME:
    print(f"{state:<3} is {CODE_TO_NAME[state]}")