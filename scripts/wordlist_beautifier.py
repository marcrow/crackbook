import re

# Script use to generate alternatives to wordlist and clean the input.
# It is pretty usefulll when you have a wordlist of more than 100 words
# With sometimes _ - and number at the end 


def process_wordlist(input_file, output_file, exclude_file=None):
    """
    Generates a new wordlist by applying the specified transformations.

    :param input_file: Path to the input file used as the source wordlist.
    :param output_file: Output path for the generated wordlist.
    :param exclude_file: Path to the file with banned words (one by line).
    """
    # Loads words to exclude
    exclude_words = set()
    if exclude_file:
        with open(exclude_file, "r") as ef:
            exclude_words = {line.strip().lower() for line in ef if line.strip()}

    processed_words = set()

    skip_copy=False

    with open(input_file, "r") as infile:
        for line in infile:
            word = line.strip()
            if not word:
                continue

            word = word.lower()

            if word in exclude_words:
                continue


            # Remove space 
            word_no_spaces = word.rstrip()
            word = word_no_spaces

            # Removes digits at the end of words to avoid conflicts with rules 
            word_no_digits = re.sub(r"\d{1,2}$", "", word)
            word = word_no_digits

            #  Removes special chars at the end of words to avoid conflicts with rules 
            trimmed_word = re.sub(r"[!@#$%^&*()+=.]+$", "", word)
            word=trimmed_word
            

            # Create variation without _ - . or space in the word 
            no_special_chars = re.sub(r"[-_ .]", "", word)
            processed_words.add(no_special_chars)

            # Truncate parts with dashes, apce or underscores
            parts = re.split(r"[-_ .]", word)
            processed_words.update(parts)

            
            # Add the word without the first letter (used for username with first letter of the surname...)
            if len(word) > 1:
                processed_words.add(word[1:])
            

            processed_words.add(word)

    # Sort + uniq
    processed_words = sorted(processed_words)


    with open(output_file, "w") as outfile:
        outfile.write("\n".join(processed_words))

# Exemple d'utilisation
input_wordlist = "../scandidat.txt"
output_wordlist = "../wordlist/candidat.new.txt"
exclude_words_list = "/home/kali/share/pentets_notes/pwned.txt"

process_wordlist(input_wordlist, output_wordlist, exclude_words_list)
