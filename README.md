# DSA Search Algorithms

Python implementations of linear search, binary search, binary search tree search, and red-black tree search, with a Pygame interface for runtime comparison.

## Run

Requires Python 3 and Pygame.

```bash
python3 -m pip install -r requirements.txt
python3 mst_visual.py
```

Select one or more algorithms, enter an input size from 10 to 10,000, choose a present or missing target, and click **Run Search**. Displayed times are totals in milliseconds for 1,000 searches of the same target; sorting and tree construction are excluded. Present mode uses the last array element, so linear search examines the entire array.

- `mst_project.py`: four searches, input generator, and tree construction. Run it directly for a console example.
- `mst_visual.py`: comparison interface.

The red-black tree is constructed directly from sorted unique values without insertion rotations. The ordinary BST uses recursive insertion and search and can exceed Python's recursion limit on sufficiently skewed input.
