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
#!/usr/bin/env python3
"""
Script to compare two versions of the StarkX-Kernel changelog and highlight differences.
Uses bukandewa's changelog format for parsing and comparison.
"""

import re
import sys
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from difflib import unified_diff


@dataclass
class ChangeEntry:
    """Represents a single change entry in the changelog."""
    commit_hash: str
    author: str
    date: str
    message: str
    change_type: str  # e.g., "Added", "Fixed", "Changed"


@dataclass
class ChangelogVersion:
    """Represents a version block in the changelog."""
    version: str
    date: str
    changes: List[ChangeEntry]


def parse_changelog(file_content: str) -> Dict[str, ChangelogVersion]:
    """
    Parse the changelog content into structured data.
    
    Args:
        file_content: Content of the changelog file
        
    Returns:
        Dictionary mapping version strings to ChangelogVersion objects
    """
    versions = {}
    current_version = None
    
    # Regex patterns for parsing
    version_pattern = re.compile(r'^## \[([^\]]+)\] - (\d{4}-\d{2}-\d{2})$')
    change_pattern = re.compile(
        r'^\*\s*(Added|Fixed|Changed|Removed|Deprecated|Security):\s*(.*?)\s*\(\[([a-f0-9]+)\]\([^)]+\) by ([^)]+)\)$'
    )
    
    for line in file_content.split('\n'):
        version_match = version_pattern.match(line)
        if version_match:
            version, date = version_match.groups()
            current_version = ChangelogVersion(version, date, [])
            versions[version] = current_version
            continue
        
        if current_version:
            change_match = change_pattern.match(line)
            if change_match:
                change_type, message, commit_hash, author = change_match.groups()
                entry = ChangeEntry(
                    commit_hash=commit_hash,
                    author=author,
                    date=current_version.date,
                    message=message,
                    change_type=change_type
                )
                current_version.changes.append(entry)
    
    return versions


def compare_versions(
    old_versions: Dict[str, ChangelogVersion],
    new_versions: Dict[str, ChangelogVersion]
) -> Dict[str, Dict[str, List[ChangeEntry]]]:
    """
    Compare two sets of versions and return the differences.
    
    Args:
        old_versions: Parsed versions from the old changelog
        new_versions: Parsed versions from the new changelog
        
    Returns:
        Dictionary with:
        - 'added_versions': New versions not in old changelog
        - 'removed_versions': Versions removed from old changelog
        - 'changed_versions': Versions with changes between old and new
    """
    result = {
        'added_versions': {},
        'removed_versions': {},
        'changed_versions': {}
    }
    
    # Find added versions
    for version in new_versions:
        if version not in old_versions:
            result['added_versions'][version] = new_versions[version]
    
    # Find removed versions
    for version in old_versions:
        if version not in new_versions:
            result['removed_versions'][version] = old_versions[version]
    
    # Find changed versions
    for version in new_versions:
        if version in old_versions:
            old_changes = {entry.commit_hash: entry for entry in old_versions[version].changes}
            new_changes = {entry.commit_hash: entry for entry in new_versions[version].changes}
            
            added_changes = [
                entry for commit_hash, entry in new_changes.items()
                if commit_hash not in old_changes
            ]
            
            removed_changes = [
                entry for commit_hash, entry in old_changes.items()
                if commit_hash not in new_changes
            ]
            
            if added_changes or removed_changes:
                result['changed_versions'][version] = {
                    'added': added_changes,
                    'removed': removed_changes,
                    'old_version': old_versions[version],
                    'new_version': new_versions[version]
                }
    
    return result


def generate_diff_report(comparison_result: Dict) -> str:
    """
    Generate a human-readable diff report from the comparison result.
    
    Args:
        comparison_result: Result from compare_versions()
        
    Returns:
        Formatted diff report as string
    """
    report = []
    
    # Added versions
    if comparison_result['added_versions']:
        report.append("\n### Added Versions:\n")
        for version, data in comparison_result['added_versions'].items():
            report.append(f"* {version} ({data.date})")
            for change in data.changes:
                report.append(f"  - {change.change_type}: {change.message} ({change.commit_hash[:7]} by {change.author})")
    
    # Removed versions
    if comparison_result['removed_versions']:
        report.append("\n### Removed Versions:\n")
        for version, data in comparison_result['removed_versions'].items():
            report.append(f"* {version} ({data.date})")
    
    # Changed versions
    if comparison_result['changed_versions']:
        report.append("\n### Changed Versions:\n")
        for version, changes in comparison_result['changed_versions'].items():
            report.append(f"* {version}:")
            
            if changes['added']:
                report.append("  - Added changes:")
                for change in changes['added']:
                    report.append(f"    - {change.change_type}: {change.message} ({change.commit_hash[:7]} by {change.author})")
            
            if changes['removed']:
                report.append("  - Removed changes:")
                for change in changes['removed']:
                    report.append(f"    - {change.change_type}: {change.message} ({change.commit_hash[:7]} by {change.author})")
    
    return '\n'.join(report)


def read_file(filename: str) -> str:
    """Read file content with error handling."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError as e:
        print(f"Error reading file {filename}: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("Usage: changelog_diff.py <old_changelog> <new_changelog>", file=sys.stderr)
        sys.exit(1)
    
    old_file = sys.argv[1]
    new_file = sys.argv[2]
    
    old_content = read_file(old_file)
    new_content = read_file(new_file)
    
    old_versions = parse_changelog(old_content)
    new_versions = parse_changelog(new_content)
    
    comparison = compare_versions(old_versions, new_versions)
    report = generate_diff_report(comparison)
    
    print(report)


if __name__ == "__main__":
    main()
```
