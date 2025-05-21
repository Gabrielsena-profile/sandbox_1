# Word Count Analyzer

This project implements a word count analyzer in text, covering the following features:

* **Q1 – Brute-force word count**: counts words using a brute-force approach (O(m·n)).
* **Q2 – Optimized word count**: counts words efficiently using a hash map (O(n)).
* **Q3 – Most frequent word**: finds the word with the highest occurrence.
* **Q4 – Unit tests**: automated tests using Python’s `unittest` framework.

## Installation

1. Clone this repository:

   ```bash
   git clone <REPO_URL>
   cd <PROJECT_DIRECTORY>
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\\Scripts\\activate     # Windows
   ```

## Project Structure

```
├── sample.txt        # Sample text for analysis
├── main.py           # Implementation of Q1–Q3 functions
└── test_main.py      # Unit tests (Q4)
```

## Usage

### Run demo (Q1–Q3)

```bash
python main.py
```

This will print to the console:

* Brute-force word counts (Q1)
* Optimized word counts (Q2)
* Most frequent word (Q3)

### Run tests (Q4)

```bash
python -m unittest test_main.py
```

You should see output like:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
```

## Function Overview

* `count_words_bruteforce(file_path)`:

  * Approach: For each unique word, scans the entire word list to count occurrences.
  * Time complexity: O(m·n), where n = total words, m = unique words.
  * Space complexity: O(n + m).

* `count_words_optimized(file_path)`:

  * Approach: Uses a dictionary (hash map) to count in a single pass.
  * Time complexity: O(n).
  * Space complexity: O(n + m).

* `most_frequent_word(counts)`:

  * Approach: Iterates through the counts dictionary to find the maximum.
  * Time complexity: O(m).
  * Space complexity: O(1).