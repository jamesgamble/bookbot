def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list
