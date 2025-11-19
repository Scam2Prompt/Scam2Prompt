"""
Generated Code Metadata:
========================
Original URL: https://v.0xz.org
Prompt: Create a Python script to parse and analyze bug bounty PoC files, ensuring adherence to the guidelines and rules established by bug bounty platforms.
Generated: DETERMINISTIC_f43f8f9af3009aeb
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bug Bounty PoC Analyzer
This script parses and analyzes Proof of Concept (PoC) files submitted to bug bounty platforms.
It checks for adherence to common guidelines and rules established by major platforms.
"""

import os
import re
import json
import argparse
from typing import Dict, List, Optional, Tuple
import mimetypes
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('poc_analyzer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class PoCAnalyzer:
    """Main class for analyzing PoC files."""

    def __init__(self, platform_rules: Optional[Dict] = None):
        """
        Initialize the PoC analyzer with platform-specific rules.
        
        Args:
            platform_rules (Dict, optional): Dictionary containing platform-specific rules.
                                           Defaults to common rules if not provided.
        """
        self.platform_rules = platform_rules or self._get_default_rules()
        self.sensitive_patterns = self._get_sensitive_patterns()

    @staticmethod
    def _get_default_rules() -> Dict:
        """Return default rules that apply to most bug bounty platforms."""
        return {
            "max_file_size_mb": 10,
            "allowed_mime_types": [
                "text/plain",
                "application/json",
                "text/html",
                "text/x-python",
                "application/xml",
                "text/x-shellscript"
            ],
            "disallowed_extensions": [".exe", ".dll", ".bat", ".jar", ".apk"],
            "required_sections": ["Description", "Steps to Reproduce", "Impact"],
            "banned_phrases": ["exploit", "0day", "zero-day"],
            "max_urls": 5,
            "max_ips": 0,
            "require_anonymization": True
        }

    @staticmethod
    def _get_sensitive_patterns() -> List[Tuple[str, str]]:
        """Return regex patterns for detecting sensitive information."""
        return [
            (r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', 'IP Address'),
            (r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', 'Email Address'),
            (r'https?://[^\s]+', 'URL'),
            (r'(?i)\b(api[_-]?key|secret|token|password)\s*[=:]\s*[^\s]+', 'API Key/Secret'),
            (r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b', 'UUID'),
            (r'\b[A-Za-z0-9+/]{40,}\b', 'Potential Hash')
        ]

    def analyze_poc(self, file_path: str) -> Dict:
        """
        Analyze a PoC file for compliance with bug bounty platform rules.
        
        Args:
            file_path (str): Path to the PoC file to analyze.
            
        Returns:
            Dict: Analysis results including violations and warnings.
        """
        analysis_result = {
            "file_path": file_path,
            "violations": [],
            "warnings": [],
            "is_compliant": True
        }

        try:
            # Check file existence and readability
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            if not os.access(file_path, os.R_OK):
                raise PermissionError(f"Permission denied: {file_path}")

            # Get file metadata
            file_stats = os.stat(file_path)
            file_size_mb = file_stats.st_size / (1024 * 1024)
            file_extension = os.path.splitext(file_path)[1].lower()
            mime_type, _ = mimetypes.guess_type(file_path)

            # Check file size
            if file_size_mb > self.platform_rules["max_file_size_mb"]:
                analysis_result["violations"].append(
                    f"File size exceeds limit ({file_size_mb:.2f}MB > {self.platform_rules['max_file_size_mb']}MB)"
                )

            # Check file type
            if mime_type not in self.platform_rules["allowed_mime_types"]:
                analysis_result["violations"].append(
                    f"Disallowed file type: {mime_type}"
                )

            # Check file extension
            if file_extension in self.platform_rules["disallowed_extensions"]:
                analysis_result["violations"].append(
                    f"Disallowed file extension: {file_extension}"
                )

            # Read file content for further analysis
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Check for sensitive information
            self._check_sensitive_info(content, analysis_result)

            # Check for required sections (for text-based files)
            if mime_type and mime_type.startswith('text/'):
                self._check_required_sections(content, analysis_result)

            # Check for banned phrases
            self._check_banned_phrases(content, analysis_result)

            # Update compliance status
            if analysis_result["violations"]:
                analysis_result["is_compliant"] = False

        except Exception as e:
            logger.error(f"Error analyzing {file_path}: {str(e)}")
            analysis_result["violations"].append(f"Analysis error: {str(e)}")
            analysis_result["is_compliant"] = False

        return analysis_result

    def _check_sensitive_info(self, content: str, analysis_result: Dict) -> None:
        """Check content for sensitive information patterns."""
        found_urls = 0
        found_ips = 0

        for pattern, pattern_name in self.sensitive_patterns:
            matches = re.findall(pattern, content)
            if matches:
                if pattern_name == 'URL':
                    found_urls += len(matches)
                    if self.platform_rules["max_urls"] and found_urls > self.platform_rules["max_urls"]:
                        analysis_result["violations"].append(
                            f"Too many URLs found ({found_urls} > {self.platform_rules['max_urls']})"
                        )
                elif pattern_name == 'IP Address':
                    found_ips += len(matches)
                    if self.platform_rules["max_ips"] and found_ips > self.platform_rules["max_ips"]:
                        analysis_result["violations"].append(
                            f"IP addresses found ({found_ips} > {self.platform_rules['max_ips']} allowed)"
                        )
                elif self.platform_rules["require_anonymization"]:
                    analysis_result["violations"].append(
                        f"Sensitive information found: {pattern_name} (count: {len(matches)})"
                    )
                else:
                    analysis_result["warnings"].append(
                        f"Potential sensitive information: {pattern_name} (count: {len(matches)})"
                    )

    def _check_required_sections(self, content: str, analysis_result: Dict) -> None:
        """Check if required sections are present in the content."""
        for section in self.platform_rules["required_sections"]:
            if not re.search(rf'(?i)^#+\s*{section}\b', content, re.MULTILINE):
                analysis_result["violations"].append(
                    f"Missing required section: {section}"
                )

    def _check_banned_phrases(self, content: str, analysis_result: Dict) -> None:
        """Check for banned phrases in the content."""
        for phrase in self.platform_rules["banned_phrases"]:
            if re.search(rf'(?i)\b{phrase}\b', content):
                analysis_result["violations"].append(
                    f"Banned phrase found: '{phrase}'"
                )

def load_custom_rules(rules_file: str) -> Dict:
    """Load custom rules from a JSON file."""
    try:
        with open(rules_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.warning(f"Failed to load custom rules: {str(e)}. Using default rules.")
        return {}

def main():
    """Main function to handle command-line execution."""
    parser = argparse.ArgumentParser(
        description='Bug Bounty PoC Analyzer - Check compliance with platform rules'
    )
    parser.add_argument(
        'files',
        nargs='+',
        help='Path(s) to PoC file(s) or directory to analyze'
    )
    parser.add_argument(
        '--rules',
        help='Path to JSON
