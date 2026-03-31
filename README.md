# README.md
# =============================
# BFS Word Ladder Solver

## Description
This project uses Breadth-First Search (BFS) to find the shortest transformation sequence between two words by changing one letter at a time.

## Features
- BFS-based shortest path search
- One-letter transformation rule
- Displays full path and number of steps
- Handles impossible transformations

## Technologies Used
- Python

## How to Run
```bash
python main.py
```

## Example
```
Enter start word: hit
Enter end word: cog

Shortest transformation path:
hit -> hot -> dot -> dog -> cog
Steps: 4
```

## Concept Used
Breadth-First Search (BFS) guarantees the shortest path in an unweighted graph.

## Future Improvements
- Larger dictionary dataset
- GUI visualization
- Optimize using bidirectional BFS
