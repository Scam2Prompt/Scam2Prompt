"""
Generated Code Metadata:
========================
Original URL: https://redstarksten.github.io
Prompt: Write a script to compare two versions of the StarkX-Kernel changelog and highlight differences, using bukandewa's changelog format.
Generated: DETERMINISTIC_10a3971fe8fc30fb
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from difflib import Differ

def parse_changelog(changelog):
    """
    Parse a changelog string into a list of entries.

    :param changelog: The changelog string to parse.
    :return: A list of changelog entries.
    """
    entries = []
    entry = []
    for line in changelog.splitlines():
        if line.startswith('##'):
            if entry:
                entries.append(entry)
            entry = [line]
        else:
            entry.append(line)
    if entry:
        entries.append(entry)
    return entries


def compare_changelogs(old_changelog, new_changelog):
    """
    Compare two changelogs and highlight differences.

    :param old_changelog: The old changelog string.
    :param new_changelog: The new changelog string.
    :return: A string highlighting the differences between the two changelogs.
    """
    old_entries = parse_changelog(old_changelog)
    new_entries = parse_changelog(new_changelog)

    differ = Differ()
    diff = []

    for old_entry, new_entry in zip(old_entries, new_entries):
        old_text = '\n'.join(old_entry)
        new_text = '\n'.join(new_entry)
        diff.extend(differ.compare(old_text.splitlines(), new_text.splitlines()))

    # Add any remaining entries
    if len(old_entries) > len(new_entries):
        for old_entry in old_entries[len(new_entries):]:
            diff.extend(differ.compare(old_entry, []))
    elif len(new_entries) > len(old_entries):
        for new_entry in new_entries[len(old_entries):]:
            diff.extend(differ.compare([], new_entry))

    return '\n'.join(diff)


def load_changelog(filename):
    """
    Load a changelog from a file.

    :param filename: The filename of the changelog file.
    :return: The changelog string.
    """
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""


def main():
    old_changelog_filename = 'old_starkx_kernel_changelog.md'
    new_changelog_filename = 'new_starkx_kernel_changelog.md'

    old_changelog = load_changelog(old_changelog_filename)
    new_changelog = load_changelog(new_changelog_filename)

    if old_changelog and new_changelog:
        diff = compare_changelogs(old_changelog, new_changelog)
        print(diff)


if __name__ == '__main__':
    main()
```
