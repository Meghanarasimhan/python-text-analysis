### Python Text Analysis

A Python script for analyzing text files by counting and manipulating character frequencies.

## Overview
This project contains a Python script (HW1.py) that performs character counting and merging operations on text files. The script analyzes a text file, counts characters (excluding spaces and special characters), creates random distributions of these character counts, and then merges them back together.

## Features

Character counting with dictionary data structures
Random character distribution creation
Dictionary merging operations
Built-in testing to validate results

## Requirements

Python 3.x
Text file for analysis (default: 'HadoopBlurb.txt')

## Usage

Clone this repository:
```
git clone https://github.com/Meghanarasimhan/python-text-analysis.git
cd python-text-analysis
```

Run the script with a text file:
```
python HW1.py --file-path path/to/your/text/file.txt
```

## How It Works
The script performs the following operations:

Character Counting: Reads the input file and counts all alphanumeric characters, storing results in a dictionary.
Random Distribution: Creates three separate dictionaries and randomly assigns each word's characters to one of these dictionaries.
Dictionary Merging: Combines the three random dictionaries back into one, adding the character counts.
Validation: Tests that the merged dictionary matches the original character counts.

# Example Output
Character counts: {'H': 10, 'a': 42, 'd': 15, 'o': 25, 'p': 8, ...}
(a) The total dictionary has 37 keys.

# Random character count dictionaries: [{'H': 3, 'a': 15, ...}, {'d': 7, 'o': 8, ...}, {'p': 4, 'a': 10, ...}]

Merged character count dictionary: {'H': 10, 'a': 42, 'd': 15, 'o': 25, 'p': 8, ...}
(a) The merged dictionary has 37 keys.
(b) The key with the maximum value in merged dictionary is 'a' with count 42.

Test passed: Merged counts match char counts.
