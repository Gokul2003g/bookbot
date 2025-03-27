def count_words(file_contents):
    words = file_contents.split()
    num_of_words = len(words)
    return num_of_words


def character_frequency(file_contents):
    file_contents = file_contents.lower()
    frequency = dict()
    for char in file_contents:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


def list_of_dicts(frequency):
    list_of_dictionaries = []
    for k in frequency:
        dictionary = dict()
        dictionary["name"] = k
        dictionary["num"] = frequency[k]
        list_of_dictionaries.append(dictionary)
    return list_of_dictionaries
