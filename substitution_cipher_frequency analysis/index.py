from collections import Counter

ciphertext = """
lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi

bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt

wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb
"""


# Count only alphabetic characters
letters = [
    character
    for character in ciphertext.lower()
    if character.isalpha()
]

# Total number of letters
total_letters = len(letters)

# Count each letter
frequency = Counter(letters)

# Sort letters from most frequent to least frequent
sorted_frequency = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)
# Show the English frequency table
english_frequencies = {
    "A": 0.0817,
    "B": 0.0150,
    "C": 0.0278,
    "D": 0.0425,
    "E": 0.1270,
    "F": 0.0223,
    "G": 0.0202,
    "H": 0.0609,
    "I": 0.0697,
    "J": 0.0015,
    "K": 0.0077,
    "L": 0.0403,
    "M": 0.0241,
    "N": 0.0675,
    "O": 0.0751,
    "P": 0.0193,
    "Q": 0.0010,
    "R": 0.0599,
    "S": 0.0633,
    "T": 0.0906,
    "U": 0.0276,
    "V": 0.0098,
    "W": 0.0236,
    "X": 0.0015,
    "Y": 0.0197,
    "Z": 0.0007
}

# Function to show the English frequency table
def show_english_frequency_table():
    print("\nNormal English Letter Frequencies")
    print("---------------------------------")
    print("Letter | Frequency")
    print("------------------")

    sorted_english = sorted(
        english_frequencies.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for letter, frequency_value in sorted_english:
        print(f"  {letter}    |  {frequency_value:.4f}")

    print("---------------------------------")

# Function that displays the frequency table
def show_frequency_table():
    print("\nLetter | Count | Frequency")
    print("--------------------------")

    for letter, count in sorted_frequency:
        relative_frequency = count / total_letters

        print(
            f"  {letter}    |"
            f"  {count:<5} |"
            f"  {relative_frequency:.4f}"
        )

    print("--------------------------")
    print(f"Total letters: {total_letters}")


# Show the table when the program starts
show_frequency_table()


print("\nOriginal ciphertext:")
print(ciphertext)
print("-----------------------------------")


# Dictionary that stores the user's substitutions
substitutions = {}


while True:
    user_input = input(
    "Enter a ciphertext character to substitute "
    "(type 'quit' = exit, 'table' = ciphertext table, "
    "or 'english' = English frequency table): "
).lower()
    if user_input == "quit":
        break

    if user_input == "table":
        show_frequency_table()
        continue

    if user_input == "english":
        show_english_frequency_table()
        continue

    if len(user_input) != 1 or not user_input.isalpha():
        print("Please enter one letter, 'table', or 'quit'.")
        continue

    new_value = input(
        f"Enter the plaintext replacement for '{user_input}': "
    ).lower()

    if len(new_value) != 1 or not new_value.isalpha():
        print("Please enter only one replacement letter.")
        continue

    substitutions[user_input] = new_value

    decrypted_text = ""

    for character in ciphertext:
        if character.isalpha():
            decrypted_text += substitutions.get(character.lower(), "_")
        else:
            decrypted_text += character

    print("\nCurrent substitutions:")
    print("----------------------")

    for cipher_letter, plain_letter in substitutions.items():
        print(cipher_letter, "->", plain_letter)

    print("\nCurrent decrypted text:")
    print(decrypted_text)
    print("-----------------------------------")


# Create the final output
final_text = ""

for character in ciphertext:
    lowercase_character = character.lower()

    if lowercase_character in substitutions:
        final_text += substitutions[lowercase_character]

    elif character.isalpha():
        final_text += "_"

    else:
        final_text += character


print("\nFinal substitutions:")
print("--------------------")

for cipher_letter, plain_letter in substitutions.items():
    print(cipher_letter, "->", plain_letter)


print("\nFinal decrypted text:")
print(final_text)