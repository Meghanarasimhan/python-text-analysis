"""
This Python script performs character counting and merging operations on a text file.

Usage:
1. Ensure that the text file 'HadoopBlurb.txt' is located in the same directory as this script.
2. Run this script using Python 3.x.

Example. Run the below command to execute the script:
    $ python HW1.py --file-path path/to/HadoopBlurb.txt

This script will:
- Read the text file 'HadoopBlurb.txt'.
- Compute the total character count using a dictionary, excluding spaces and special characters.
- Create three different character count dictionaries, assigning characters at random.
- Merge the three dictionaries into one, adding the counts.
- Print the character counts, random character count dictionaries, and merged character count dictionary.
- Perform a test to check if the merged counts match the initial character counts.

"""

# IMPORTS
import argparse
import re
import random

from typing import Dict, List


def count_characters(file_path: str) -> Dict[str, int]:
    """
    Read a text file and compute total character count using a dictionary.
    Exclude spaces and special characters.
    
    Args:
    - file_path: Path to the text file
    
    Returns:
    - char_counts: Dictionary containing character counts
    """
    char_counts: Dict[str, int] = {}
    with open(file_path, 'r') as file:
        text = file.read()

    # TODO Your implementation here
    # Spliting by space to get words
    words = text.split(' ')
    
    for word in words:
        # Processing each character in the word
        for char in word:
            # Only counting alphanumeric characters
            if char.isalnum():
                if char in char_counts:
                    char_counts[char] += 1
                else:
                    char_counts[char] = 1

    return char_counts



def create_random_character_count_dicts(file_path: str) -> List[Dict[str, int]]:
    """
    Create three different character count dictionaries,
    assigning characters at random.
    
    Args:
    - file_path: Path to the text file
    
    Returns:
    - char_counts: List containing three character count dictionaries
    """
    char_counts: List[Dict[str, int]] = [{}, {}, {}]
    with open(file_path, 'r') as file:
        text = file.read()

    # TODO Your implementation here
     # Spliting by space to get words
    words = text.split(' ')
    
    for word in words:
        # Choosing a random dictionary for this word
        random_dict_index = random.randint(0, 2)
        
        # Adding all characters of this word to the chosen dictionary
        for char in word:
            if char.isalnum():
                if char in char_counts[random_dict_index]:
                    char_counts[random_dict_index][char] += 1
                else:
                    char_counts[random_dict_index][char] = 1

    return char_counts


def merge_character_count_dicts(char_counts_list: List[Dict[str, int]]) -> Dict[str, int]:
    """
    Merge three dictionaries into one (adding the counts).
    
    Args:
    - char_counts_list: List containing three character count dictionaries
    
    Returns:
    - merged_counts: Dictionary containing merged character counts
    """
    merged_counts: Dict[str, int] = {}

    # TODO Your implementation here
    # Processing all keys from all dictionaries
    for char_dict in char_counts_list:
        for char, count in char_dict.items():
            if char in merged_counts:
                merged_counts[char] += count
            else:
                merged_counts[char] = count

    return merged_counts


def test_merge_character_count_dicts(char_counts: Dict[str, int], merged_counts: Dict[str, int]) -> bool:
    """
    Test function to check if merged character counts match the character counts.
    
    Args:
    - char_counts: Dictionary containing character counts from count_characters function
    - merged_counts: Dictionary containing merged character counts from merge_character_count_dicts function
    
    Returns:
    - test_result: True if test passes, False otherwise
    """
    # Check if all characters in char_counts are present in merged_counts
    for char, count in char_counts.items():
        if char not in merged_counts or merged_counts[char] != count:
            print(f"Test failed: Merged counts do not match char counts.")
            return False

    print("Test passed: Merged counts match char counts.")
    return True


def main():
    file_path=None
    # Make sure to handle passing in the filepath argument.

    
    # Part 1: Count characters
    char_counts: Dict[str, int] = count_characters(file_path)
    print(f"Character counts: {char_counts}")
    # TODO Print the number of keys and key with the max value here
    print(f"(a) The total dictionary has {len(char_counts)} keys.")

    # Part 2: Create random character count dictionaries
    random_char_counts: List[Dict[str, int]] = create_random_character_count_dicts(file_path)
    print(f"\nRandom character count dictionaries: {random_char_counts}")
    
    # Part 3: Merge character count dictionaries
    merged_counts: Dict[str, int] = merge_character_count_dicts(random_char_counts)
    print(f"\nMerged character count dictionary: {merged_counts}")
    
    # TODO Print the number of keys and key with the max value here
    print(f"(a) The merged dictionary has {len(merged_counts)} keys.")
    max_key_merged = max(merged_counts, key=merged_counts.get)
    print(f"(b) The key with the maximum value in merged dictionary is '{max_key_merged}' with count {merged_counts[max_key_merged]}.")
    
    # Test if merged counts match char counts

    test_result: bool = test_merge_character_count_dicts(char_counts, merged_counts)
    if not test_result:
        raise ValueError("Test failed: Merged counts do not match char counts.")

if __name__ == "__main__":
    main()
    # You need to be able to run this file with the command python HW1.py --file-path path/to/HadoopBlurb.txt