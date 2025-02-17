def word_count(words):
    return len(words)


def sort_on(dict):
    return dict["count"]


def main():
    file_path = "books/frankenstein.txt" 
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        
        lowered_string = file_contents.lower() 
        letter_counts = {}
        for letter in lowered_string:
            if letter not in letter_counts:
                letter_counts[letter] = 0
            letter_counts[letter] += 1

        
        # convert the dictionary into a list
        letter_counts_list = []
        for letter_key in letter_counts:
            if letter_key >= 'a' and letter_key <= 'z':
                letter_counts_list.append({"letter": letter_key, "count": letter_counts[letter_key]})


        print(f"--- Begin report of {file_path} ---")
        print(f"{word_count(words)} words found in the document")
        print("")
        letter_counts_list.sort(reverse=True, key=sort_on)
        for letter_info in letter_counts_list:
            letter = letter_info["letter"]
            count = letter_info["count"]
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")

main()
