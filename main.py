import re
from collections import defaultdict

def count_words_bruteforce(file_path):
    """
    Q1 – Brute-force word count:
    Reads the file, strips out punctuation, lowercases everything,
    then for each unique word scans the entire list to count occurrences.
    
    Time complexity: O(m·n) where n = total words, m = unique words
    Space complexity: O(n + m)
    """
    if file_path is None:
        raise TypeError("file_path cannot be None")
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    clean = re.sub(r'[^\w\s]', '', text).lower()
    words = clean.split()
    counts = {}
    for word in set(words):
        counts[word] = sum(1 for w in words if w == word)
    return counts

def count_words_optimized(file_path):
    """
    Q2 – Optimized word count using a hash map:
    Reads and normalizes text, then does a single pass to tally counts.
    
    Time complexity: O(n)
    Space complexity: O(n + m)
    """
    if file_path is None:
        raise TypeError("file_path cannot be None")
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    clean = re.sub(r'[^\w\s]', '', text).lower()
    words = clean.split()
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    return dict(counts)

def most_frequent_word(counts):
    """
    Q3 – Find the word with the highest count:
    Given a dict word→count, returns (word, count) for the max entry.
    
    Time complexity: O(m)
    Space complexity: O(1)
    """
    if not counts:
        return None, 0
    
    max_word, max_count = None, 0
    for word, count in counts.items():
        if count > max_count:
            max_word, max_count = word, count
    return max_word, max_count

def main(file_path='sample.txt'):
    """
    Main function to execute the word count and find the most frequent word.
    """
    # Q1: Brute-force word count
    counts_bruteforce = count_words_bruteforce(file_path)
    print("Brute-force word count:", counts_bruteforce)

    # Q2: Optimized word count
    counts_optimized = count_words_optimized(file_path)
    print("Optimized word count:", counts_optimized)

    # Q3: Most frequent word
    most_frequent = most_frequent_word(counts_optimized)
    print("Most frequent word:", most_frequent)

if __name__ == "__main__":
    main()
