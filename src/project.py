"""Project 1 starter: Data Detective.

Implement the required functions below.
Use standard library only.
"""

from __future__ import annotations

import string
from pathlib import Path


def load_text(path: str) -> str:
    """Load and return the full text from a UTF-8 file."""
    with open(path, encoding="utf-8") as f:
        return f.read()


def normalize_text(text: str) -> str:
    """Return a normalized version of the text.

    - lowercase the text
    - remove punctuation
    - collapse extra whitespace
    """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    # collapse multiple spaces/newlines into a single space
    text = " ".join(text.split())
    return text


def tokenize(text: str) -> list[str]:
    """Split normalized text into a list of words."""
    if not text.strip():
        return []
    return text.split()


def count_words(words: list[str]) -> dict[str, int]:
    """Count how many times each word appears."""
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return the top N words as (word, count) tuples.

    - if n <= 0, return []
    - sort by count descending
    - for ties, sort alphabetically
    """
    if n <= 0:
        return []
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:n]


def extra_insight(words: list[str], counts: dict[str, int]) -> object:
    """Return the average word length across all words.

    Returns 0.0 if the word list is empty.
    """
    if not words:
        return 0.0
    avg = sum(len(w) for w in words) / len(words)
    return round(avg, 2)


def run_demo(path: str, n: int = 10) -> dict[str, object]:
    """Run the full analysis pipeline and return summary data."""
    text = load_text(path)
    normalized = normalize_text(text)
    words = tokenize(normalized)
    counts = count_words(words)

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": top_n_words(counts, n),
        "extra_insight": extra_insight(words, counts),
    }


if __name__ == "__main__":
    demo_path = Path("data/sample.txt")
    if demo_path.exists():
        results = run_demo(str(demo_path), n=10)
        print(f"Total words    : {results['total_words']}")
        print(f"Unique words   : {results['unique_words']}")
        print(f"Avg word length: {results['extra_insight']}")
        print("\nTop words:")
        for word, count in results["top_words"]:
            print(f"  {word:<20} {count}")
    else:
        print("No demo file found at data/sample.txt")