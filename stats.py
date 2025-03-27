from collections import defaultdict


def get_num_of_words(file_contents):
    separate_words = file_contents.split()
    word_count = 0
    for word in separate_words:
        word_count += 1
    return word_count

def get_num_character(file_contents):
    characters_dictionary = {}
    for character in file_contents.lower():
        if character not in characters_dictionary:
            characters_dictionary[character] = 0
        characters_dictionary[character] += 1
    return characters_dictionary  # Kein Konvertieren mehr nötig

def sort_on(item):
    return item["count"]  # Klarerer Name für den Zählwert

def sort_dictionary(char_count_dict):
    sorted_list = []
    for char, count in char_count_dict.items():
        sorted_list.append({"char": char, "count": count})  # Einheitliche Namen
    sorted_list.sort(reverse=True, key=sort_on)  # Sortieren ohne Überschreiben
    return sorted_list