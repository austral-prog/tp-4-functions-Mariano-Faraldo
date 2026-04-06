def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

def total_letters(text):
    return count_vowels(text) + count_consonants(text)

def vowel_percentage(text):

    if total_letters(text) == 0:
        return 0.0
    else:
        return round(count_vowels(text) / total_letters(text) * 100, 1)

def analyze_text(text):
    return f"V:{count_vowels(text)} C:{count_consonants(text)} T:{total_letters(text)} P:{vowel_percentage(text)}%"