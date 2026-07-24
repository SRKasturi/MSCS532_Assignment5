# Assignment 5 – Quicksort Algorithm

## Files
- quicksort.py
- Assignment_5_Quicksort_Report.docx

## Requirements
Python 3.x

## Run
```bash
python quicksort.py
```

The program:
1. Runs deterministic Quicksort.
2. Runs randomized Quicksort.
3. Benchmarks both implementations on random input sizes.

## Summary
- Deterministic Quicksort:
  - Best: O(n log n)
  - Average: O(n log n)
  - Worst: O(n^2)

- Randomized Quicksort:
  - Expected: O(n log n)
  - Worst: O(n^2) (very unlikely)

Randomization greatly reduces the probability of worst-case behavior.