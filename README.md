[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cDnlIYNC)
# P1: Data Detective

## Summary
This project analyzes a text file by loading and cleaning the text, counting word frequencies, and reporting the top N most common words along with one extra insight.

## Dataset
- File: `data/sample.txt`
- Why I chose it: The opening passage of *Alice's Adventures in Wonderland* by Lewis Carroll (public domain). It has a good mix of common and uncommon words, varied sentence lengths, and repeated words like "rabbit" and "Alice" that make the frequency analysis interesting.

## How to run
```bash
pytest -q
python -m src.project
```

## Approach
- Load text from a file using `open()` with UTF-8 encoding
- Normalize the text by lowercasing and removing all punctuation
- Tokenize into words by splitting on whitespace
- Count word frequencies using a dictionary
- Show the top N words sorted by frequency (alphabetically for ties)
- Report average word length as the extra insight

## Complexity

### `count_words`
- Time: O(n) where n is the total number of words
- Space: O(k) where k is the number of unique words
- Why: We loop through every word exactly once and store one entry per unique word in the dictionary.

### `top_n_words`
- Time: O(k log k) where k is the number of unique words
- Space: O(k) to hold the sorted list
- Why: The dominant cost is `sorted()`, which uses Timsort at O(k log k). Slicing the top N after sorting is O(N).

## Edge-case checklist
- [x] **Empty file** — `tokenize()` returns `[]` for empty/blank input, so `count_words` and `top_n_words` safely return empty results.
- [x] **Punctuation-heavy input** — `normalize_text()` removes all punctuation using `str.translate` before tokenizing, so words like `"rabbit,"` and `"rabbit"` are treated as the same word.
- [x] **Repeated words** — `count_words()` increments the count each time a word is seen, so repeats are handled correctly.
- [x] **Uppercase/lowercase differences** — `normalize_text()` lowercases the entire text first, so `"Alice"` and `"alice"` are counted as one word.
- [x] **n <= 0 for top-N** — `top_n_words()` checks `if n <= 0: return []` before doing any sorting.

## Assistance & sources
- AI used? Y
- What it helped with: Setting up the project structure and explaining how each function should work
- Other sources: [Alice's Adventures in Wonderland](https://www.gutenberg.org/ebooks/11) — Project Gutenberg (public domain)

## Design note (150–250 words)
I chose the opening passage of *Alice's Adventures in Wonderland* because it is public domain, classroom-safe, and long enough to produce meaningful word frequency results. Words like "rabbit", "alice", and "she" appear multiple times, which makes the top-N output genuinely interesting rather than every word appearing just once.

The main design decision was to keep each function small and focused on a single job. `normalize_text` only cleans the text; `tokenize` only splits it; `count_words` only counts. This made each step easy to test and debug independently. If something went wrong, I could tell exactly which function was the problem.

The trickiest part was getting `top_n_words` to sort correctly. Sorting by count descending is straightforward, but also sorting alphabetically for ties required a tuple key `(-count, word)`, which was a small but important detail.

For the extra insight I chose average word length because it is simple, well-defined, and works on any text without needing special cases. One improvement I would make next is filtering out very common short words like "a", "the", and "of" (called stop words) before counting, so the top-N results show more meaningful content words instead of filler words.
