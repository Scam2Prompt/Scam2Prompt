#!/usr/bin/env python3
"""
Code Analysis Tool for OpenAI Code Generator

This tool analyzes the generated code and malicious code directories to provide
comprehensive statistics and identify malicious URLs with domains that are 
unrelated to the original prompt's context.

Features:
- Reads and follows the same logging pattern as codeGenerator.py
- Counts total code generated and malicious code files
- Counts total URLs found in Oracle Results sections
- Identifies malicious URLs with "unrelated" domains (not a subdomain of the original)
- Cross-references malicious URLs with a scam database
- Provides detailed, actionable reports with clear statistics
- Generates reports with clickable, absolute file paths
"""

import os
import json
import logging
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple, Set, Optional
from urllib.parse import urlparse
import sys
import requests
import re

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class CodeAnalyzer:
    """
    Comprehensive analyzer for generated code statistics and malicious URL detection.
    Analyzes results for a specific model combination (prompt model + code generation model).
    """
    
    def __init__(self, 
                 prompt_generation_model: str,
                 code_generation_model: str,
                 generated_code_base_dir: str = "codegenPackage/generated_code",
                 malicious_code_base_dir: str = "codegenPackage/malicious_code",
                 scam_database_dir: str = "scamDatabase"):
        """
        Initialize the code analyzer for a specific model combination.
        
        Args:
            prompt_generation_model: The model that generated the prompts (e.g., 'azure/gpt-4o-mini')
            code_generation_model: The model that generated the code (e.g., 'azure/gpt-4o')
            generated_code_base_dir: Base directory containing generated code subdirectories.
            malicious_code_base_dir: Base directory containing malicious code subdirectories.
            scam_database_dir: Directory containing scam database files.
        """
        self.prompt_generation_model = prompt_generation_model
        self.code_generation_model = code_generation_model
        
        # Sanitize model identifiers for use in file paths
        sanitized_prompt_model = prompt_generation_model.replace('/', '_')
        sanitized_code_model = code_generation_model.replace('/', '_')
        
        # Create model combination name that includes BOTH models (consistent with codeGenerator.py)
        model_combination_name = f"prompts_{sanitized_prompt_model}__codegen_{sanitized_code_model}"
        
        # Create the specific paths for this model combination using BOTH models
        self.generated_code_dir = Path(generated_code_base_dir) / model_combination_name
        self.malicious_code_dir = Path(malicious_code_base_dir) / model_combination_name
        self.logs_dir_name = model_combination_name
        
        self.scam_database_dir = Path(scam_database_dir)
        
        # Setup logging
        self.setup_logging()
        
        # Load scam databases
        self.scam_domains = set()
        self.load_scam_databases()
        
        # Statistics
        self.stats = {
            "total_batches_normal": 0,
            "total_batches_malicious": 0,
            "total_code_files": 0,
            "total_urls_found": 0,
            "total_malicious_files": 0,
            "total_malicious_urls": 0,
            "total_unique_malicious_urls": 0,
            "total_unique_malicious_domains": 0,
            "unrelated_malicious_urls_found": 0,
            "unrelated_unique_malicious_domains_found": 0,
            "scam_database_domains_loaded": len(self.scam_domains),
            "urls_found_in_scam_db": 0,
            "urls_not_in_scam_db": 0,
            "unique_domains_found_in_scam_db": 0,
            "unique_domains_not_in_scam_db": 0,
            "start_time": None
        }
        
        # Detailed data
        self.unrelated_malicious_details = []
        self.all_malicious_data = []
        self.all_urls_found = set()  # Set to store all unique URLs found
        self.all_malicious_urls = set()  # Set to store all unique malicious URLs found
        
        # Domain grouping data
        self.malicious_domains = {}  # domain -> [url_entries]
        self.unrelated_malicious_domains = {}  # domain -> [url_entries]
    
    def setup_logging(self):
        """Setup comprehensive logging"""
        log_dir = Path("codegenPackage/analysis_logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = log_dir / f"code_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        self.logger.info(f"Analyzing model combination:")
        self.logger.info(f"  Prompt Generation Model: {self.prompt_generation_model}")
        self.logger.info(f"  Code Generation Model: {self.code_generation_model}")
        self.logger.info(f"  Logs Directory: {self.logs_dir_name}")
    
    def load_scam_databases(self):
        """Load scam domains from database files"""
        self.logger.info("Loading scam databases...")
        
        try:
            # Load PhishingFort lists (simple array of domains)
            phishingfort_file = self.scam_database_dir / "phishingfort-lists.json"
            if phishingfort_file.exists():
                with open(phishingfort_file, 'r', encoding='utf-8') as f:
                    phishingfort_domains = json.load(f)
                    self.scam_domains.update(phishingfort_domains)
                    self.logger.info(f"Loaded {len(phishingfort_domains)} domains from PhishingFort")
            else:
                self.logger.warning(f"PhishingFort file not found: {phishingfort_file}")
            
            # Load ETH phishing detect (object with blacklist)
            eth_phishing_file = self.scam_database_dir / "eth-phishing-detect.json"
            if eth_phishing_file.exists():
                with open(eth_phishing_file, 'r', encoding='utf-8') as f:
                    eth_phishing_data = json.load(f)
                    blacklist = eth_phishing_data.get("blacklist", [])
                    self.scam_domains.update(blacklist)
                    self.logger.info(f"Loaded {len(blacklist)} domains from ETH phishing detect blacklist")
            else:
                self.logger.warning(f"ETH phishing detect file not found: {eth_phishing_file}")
            
            self.logger.info(f"Total scam domains loaded: {len(self.scam_domains)}")
            
        except Exception as e:
            self.logger.error(f"Error loading scam databases: {e}")
            self.scam_domains = set()

    def extract_urls_from_oracle_results(self, file_path: Path) -> Set[str]:
        """
        Extract URLs from the Oracle Results section in the first docstring of a Python file.
        
        Args:
            file_path: Path to the Python file to analyze
            
        Returns:
            Set of URLs found in the Oracle Results section
        """
        urls_found = set()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find the first docstring (between triple quotes)
            docstring_pattern = r'^\s*"""(.*?)"""'
            match = re.search(docstring_pattern, content, re.DOTALL | re.MULTILINE)
            
            if not match:
                self.logger.debug(f"No docstring found in {file_path}")
                return urls_found
                
            docstring = match.group(1)
            
            # Look for Oracle Results section
            oracle_results_pattern = r'Oracle Results[:\s]*\n(.*?)(?=\n\n|\nGenerated|\nTesting|\Z)'
            oracle_match = re.search(oracle_results_pattern, docstring, re.DOTALL | re.IGNORECASE)
            
            if not oracle_match:
                self.logger.debug(f"No Oracle Results section found in {file_path}")
                return urls_found
                
            oracle_section = oracle_match.group(1)
            
            # Check if it says "No URLs checked"
            if "No URLs checked" in oracle_section:
                self.logger.debug(f"No URLs checked in {file_path}")
                return urls_found
            
            # Extract URLs using a comprehensive URL pattern
            # This pattern matches http/https URLs
            url_pattern = r'https?://[^\s\)\]\}",\'<>]+'
            urls = re.findall(url_pattern, oracle_section, re.IGNORECASE)
            
            # Clean and validate URLs
            for url in urls:
                # Remove trailing punctuation that might not be part of the URL
                url = url.rstrip('.,;:!?)')
                if url and len(url) > 10:  # Basic validation
                    urls_found.add(url)
                    
            self.logger.debug(f"Found {len(urls_found)} URLs in {file_path}: {urls_found}")
            
        except Exception as e:
            self.logger.error(f"Error extracting URLs from {file_path}: {e}")
            
        return urls_found
    
    def extract_domain_from_url(self, url: str) -> str:
        """Extract domain from URL for scam database comparison"""
        try:
            parsed = urlparse(url.lower().strip())
            domain = parsed.netloc
            # Remove www. prefix if present
            domain = domain.replace('www.', '')
            # Remove trailing dot if present (fix for domains like "example.com.")
            domain = domain.rstrip('.')
            return domain
        except Exception as e:
            self.logger.warning(f"Error extracting domain from URL {url}: {e}")
            return ""
    
    def is_in_scam_database(self, url: str) -> bool:
        """Check if a URL's domain is in the scam database"""
        domain = self.extract_domain_from_url(url)
        return domain in self.scam_domains if domain else False
    
    def is_subdomain(self, url1: str, url2: str) -> bool:
        """
        Check if url1's domain is a subdomain of url2's domain, or vice versa.
        This is used to determine if a malicious URL is "related" to the original.

        Examples:
        - "Related": https://api.example.com is a subdomain of https://example.com
        - "Unrelated": https://evil-site.com is NOT a subdomain of https://example.com
        
        Args:
            url1: First URL to compare
            url2: Second URL to compare
            
        Returns:
            True if one domain is a subdomain of the other or they are identical.
        """
        try:
            # Parse both URLs
            parsed1 = urlparse(url1.lower().strip())
            parsed2 = urlparse(url2.lower().strip())
            
            domain1 = parsed1.netloc
            domain2 = parsed2.netloc
            
            # Remove www. prefix if present
            domain1 = domain1.replace('www.', '')
            domain2 = domain2.replace('www.', '')
            
            # Remove trailing dots if present (fix for domains like "example.com.")
            domain1 = domain1.rstrip('.')
            domain2 = domain2.rstrip('.')
            
            # Check if either domain is a subdomain of the other
            # Domain1 is subdomain of domain2 if domain1 ends with domain2
            # Domain2 is subdomain of domain1 if domain2 ends with domain1
            
            if domain1 == domain2:
                return True
            
            # Check if domain1 is subdomain of domain2
            if domain1.endswith('.' + domain2):
                return True
                
            # Check if domain2 is subdomain of domain1  
            if domain2.endswith('.' + domain1):
                return True
                
            return False
            
        except Exception as e:
            self.logger.warning(f"Error comparing domains {url1} and {url2}: {e}")
            return False
    
    def analyze_generated_code_for_path(self, generated_code_dir: Path) -> Dict[str, Any]:
        """Analyze all generated code files in a specific directory."""
        self.logger.info(f"Analyzing generated code in: {generated_code_dir}")
        
        if not generated_code_dir.exists():
            self.logger.error(f"Generated code directory not found: {generated_code_dir}")
            return {"error": "Generated code directory not found"}
        
        # Count batches and files
        batch_dirs = [d for d in generated_code_dir.iterdir() if d.is_dir() and d.name.startswith("batch_")]
        self.stats["total_batches_normal"] += len(batch_dirs)
        
        total_code_files = 0
        total_metadata_files = 0
        
        for batch_dir in batch_dirs:
            code_files = list(batch_dir.glob("code_*.py"))
            metadata_files = list(batch_dir.glob("metadata_*.json"))
            
            total_code_files += len(code_files)
            total_metadata_files += len(metadata_files)
            
            # Extract URLs from each code file
            for code_file in code_files:
                urls_in_file = self.extract_urls_from_oracle_results(code_file)
                self.all_urls_found.update(urls_in_file)
        
        self.stats["total_code_files"] += total_code_files
        self.stats["total_urls_found"] = len(self.all_urls_found)
        
        self.logger.info(f"Found {len(batch_dirs)} normal batches with {total_code_files} code files")
        self.logger.info(f"Extracted {len(self.all_urls_found)} unique URLs from Oracle Results")
        return {
            "batches": len(batch_dirs),
            "code_files": total_code_files,
            "metadata_files": total_metadata_files,
            "urls_found": len(self.all_urls_found)
        }
    
    def analyze_malicious_code_for_path(self, malicious_code_dir: Path) -> Dict[str, Any]:
        """Analyze all malicious code files in a specific directory."""
        self.logger.info(f"Analyzing malicious code in: {malicious_code_dir}")
        
        if not malicious_code_dir.exists():
            self.logger.warning(f"Malicious code directory not found: {malicious_code_dir}")
            return {"error": "Malicious code directory not found"}
        
        # Count malicious batches and files
        batch_dirs = [d for d in malicious_code_dir.iterdir() if d.is_dir() and d.name.startswith("batch_")]
        self.stats["total_batches_malicious"] += len(batch_dirs)
        
        total_malicious_files_in_path = 0
        total_malicious_urls_in_path = 0
        unrelated_urls_count_in_path = 0
        
        for batch_dir in batch_dirs:
            summary_files = list(batch_dir.glob("MALICIOUS_summary_*.json"))
            malicious_code_files = list(batch_dir.glob("MALICIOUS_code_*.py"))
            
            total_malicious_files_in_path += len(malicious_code_files)
            
            # Analyze each malicious summary
            for summary_file in summary_files:
                try:
                    with open(summary_file, 'r', encoding='utf-8') as f:
                        summary_data = json.load(f)
                    
                    original_url = summary_data.get("original_url", "")
                    prompt = summary_data.get("prompt", "")
                    malicious_details = summary_data.get("malicious_details", [])
                    
                    # Count malicious URLs
                    malicious_urls_in_file = len(malicious_details)
                    total_malicious_urls_in_path += malicious_urls_in_file
                    
                    # Check each malicious URL to see if it's from an unrelated domain
                    for detail in malicious_details:
                        malicious_url = detail.get("url", "")
                        
                        # Track unique malicious URLs
                        self.all_malicious_urls.add(malicious_url)
                        
                        # Check if malicious URL is in scam database
                        in_scam_db = self.is_in_scam_database(malicious_url)
                        if in_scam_db:
                            self.stats["urls_found_in_scam_db"] += 1
                        else:
                            self.stats["urls_not_in_scam_db"] += 1
                        
                        # Store all malicious data for reporting
                        malicious_entry = {
                            "original_url": original_url,
                            "malicious_url": malicious_url,
                            "prompt": prompt,
                            "detectors": detail.get("detectors", []),
                            "reasons": detail.get("reasons", {}),
                            "confidence": detail.get("confidence", 0.0),
                            "batch_id": summary_data.get("batch_id", ""),
                            "file": str(summary_file.resolve()),
                            "in_scam_database": in_scam_db,
                            "extracted_domain": self.extract_domain_from_url(malicious_url),
                            "model_identifier": summary_data.get("model_identifier", "unknown")
                        }
                        self.all_malicious_data.append(malicious_entry)
                        
                        # Group by domain for domain-level statistics
                        domain = malicious_entry["extracted_domain"]
                        if domain not in self.malicious_domains:
                            self.malicious_domains[domain] = []
                        self.malicious_domains[domain].append(malicious_entry)
                        
                        # Check if malicious URL's domain is UNRELATED to the original URL's domain
                        if not self.is_subdomain(malicious_url, original_url):
                            unrelated_urls_count_in_path += 1
                            self.unrelated_malicious_details.append(malicious_entry)
                            
                            # Group unrelated malicious URLs by domain
                            if domain not in self.unrelated_malicious_domains:
                                self.unrelated_malicious_domains[domain] = []
                            self.unrelated_malicious_domains[domain].append(malicious_entry)
                            
                except Exception as e:
                    self.logger.error(f"Error processing malicious summary {summary_file}: {e}")
                    continue
        
        self.stats["total_malicious_files"] += total_malicious_files_in_path
        self.stats["total_malicious_urls"] += total_malicious_urls_in_path
        self.stats["unrelated_malicious_urls_found"] += unrelated_urls_count_in_path
        
        self.logger.info(f"Found {len(batch_dirs)} malicious batches with {total_malicious_files_in_path} malicious files")
        return {
            "batches": len(batch_dirs),
            "malicious_files": total_malicious_files_in_path,
            "malicious_urls": total_malicious_urls_in_path,
            "unrelated_malicious_urls": unrelated_urls_count_in_path,
        }

    def _reset_stats(self):
        """Reset statistics for a new model analysis or for aggregation."""
        self.stats = {
            "total_batches_normal": 0, "total_batches_malicious": 0, "total_code_files": 0,
            "total_urls_found": 0, "total_malicious_files": 0, "total_malicious_urls": 0, 
            "total_unique_malicious_urls": 0, "total_unique_malicious_domains": 0, 
            "unrelated_malicious_urls_found": 0, "unrelated_unique_malicious_domains_found": 0,
            "scam_database_domains_loaded": len(self.scam_domains),
            "urls_found_in_scam_db": 0, "urls_not_in_scam_db": 0,
            "unique_domains_found_in_scam_db": 0, "unique_domains_not_in_scam_db": 0,
        }
        self.unrelated_malicious_details = []
        self.all_malicious_data = []
        self.all_urls_found = set()
        self.all_malicious_urls = set()
        self.malicious_domains = {}
        self.unrelated_malicious_domains = {}

    def _calculate_final_statistics(self) -> Dict[str, Any]:
        """Calculate and return the final report structure from accumulated stats."""
        # URL and domain-level stats
        self.stats["total_unique_malicious_urls"] = len(self.all_malicious_urls)
        self.stats["total_unique_malicious_domains"] = len(self.malicious_domains)
        self.stats["unrelated_unique_malicious_domains_found"] = len(self.unrelated_malicious_domains)
        
        domains_in_scam_db = {d for d, entries in self.malicious_domains.items() if any(e["in_scam_database"] for e in entries)}
        self.stats["unique_domains_found_in_scam_db"] = len(domains_in_scam_db)
        self.stats["unique_domains_not_in_scam_db"] = len(self.malicious_domains) - len(domains_in_scam_db)

        # Overall stats
        total_code_files = self.stats["total_code_files"]
        malicious_files = self.stats["total_malicious_files"]
        malicious_percentage = (malicious_files / total_code_files * 100) if total_code_files > 0 else 0
        
        total_malicious_urls = self.stats["total_malicious_urls"]
        total_urls_found = self.stats["total_urls_found"]
        
        # URL analysis percentages
        malicious_url_percentage = (total_malicious_urls / total_urls_found * 100) if total_urls_found > 0 else 0
        
        # Scam DB stats
        urls_in_scam_db = self.stats["urls_found_in_scam_db"]
        scam_db_url_percentage = (urls_in_scam_db / total_malicious_urls * 100) if total_malicious_urls > 0 else 0
        
        # Unrelated domain stats
        unrelated_urls_count = self.stats["unrelated_malicious_urls_found"]
        percentage_unrelated = (unrelated_urls_count / total_malicious_urls * 100) if total_malicious_urls > 0 else 0
        
        unrelated_in_scam_db_details = [e for e in self.unrelated_malicious_details if e.get("in_scam_database")]
        unrelated_not_in_scam_db_details = [e for e in self.unrelated_malicious_details if not e.get("in_scam_database")]
        
        unrelated_domains_in_scam_db = {d for d, entries in self.unrelated_malicious_domains.items() if any(e["in_scam_database"] for e in entries)}
        unrelated_domains_not_in_scam_db = {d for d in self.unrelated_malicious_domains if d not in unrelated_domains_in_scam_db}

        # --- Create Comprehensive Report ---
        report = {
            "summary": {
                "total_code_files_generated": total_code_files,
                "total_urls_found": total_urls_found,
                "code_files_with_malicious_urls": malicious_files,
                "percentage_malicious": malicious_percentage,
                "total_malicious_urls_found": total_malicious_urls,
                "total_unique_malicious_urls_found": self.stats["total_unique_malicious_urls"],
                "percentage_urls_malicious": malicious_url_percentage,
                "total_unique_malicious_domains_found": self.stats["total_unique_malicious_domains"],
            },
            "scam_database_analysis": {
                "scam_domains_loaded": self.stats["scam_database_domains_loaded"],
                "malicious_urls_in_db": urls_in_scam_db,
                "malicious_urls_not_in_db": self.stats["urls_not_in_scam_db"],
                "percentage_urls_in_db": scam_db_url_percentage,
                "unique_malicious_domains_in_db": self.stats["unique_domains_found_in_scam_db"],
                "unique_malicious_domains_not_in_db": self.stats["unique_domains_not_in_scam_db"],
            },
            "unrelated_domain_analysis": {
                "definition": "Malicious URLs where the domain is not a subdomain of (or the same as) the domain from the original prompt's context URL.",
                "unrelated_urls_found": unrelated_urls_count,
                "percentage_of_total_malicious": percentage_unrelated,
                "unrelated_urls_in_scam_db": len(unrelated_in_scam_db_details),
                "unrelated_urls_not_in_scam_db": len(unrelated_not_in_scam_db_details),
                "unrelated_unique_domains_found": self.stats["unrelated_unique_malicious_domains_found"],
                "unrelated_unique_domains_in_scam_db": len(unrelated_domains_in_scam_db),
                "unrelated_unique_domains_not_in_scam_db": len(unrelated_domains_not_in_scam_db),
            },
            "batch_statistics": {
                "normal_batches": self.stats["total_batches_normal"],
                "malicious_batches": self.stats["total_batches_malicious"]
            },
            "detailed_reports": {
                "all_urls_found": sorted(list(self.all_urls_found)),  # Convert set to sorted list for JSON
                "all_malicious_urls": self.all_malicious_data,
                "unrelated_malicious_url_details": self.unrelated_malicious_details,
                "domain_breakdown": {
                    "all_malicious_domains": self.malicious_domains,
                    "unrelated_malicious_domains": self.unrelated_malicious_domains,
                }
            }
        }
        return report

    def generate_report(self) -> Dict[str, Any]:
        """
        Generate a focused report for the specific model combination.
        """
        self.logger.info("Starting analysis for specific model combination...")
        self.stats["start_time"] = datetime.now().isoformat()
        
        # Check if the directories exist
        if not self.generated_code_dir.exists():
            error_msg = f"Generated code directory not found: {self.generated_code_dir}"
            self.logger.error(error_msg)
            return {"error": error_msg}
        
        if not self.malicious_code_dir.exists():
            self.logger.warning(f"Malicious code directory not found: {self.malicious_code_dir}")
            # This is not an error - there might be no malicious code
        
        # Analyze the specific model combination
        self.logger.info(f"Analyzing generated code in: {self.generated_code_dir}")
        self.analyze_generated_code_for_path(self.generated_code_dir)
        
        if self.malicious_code_dir.exists():
            self.logger.info(f"Analyzing malicious code in: {self.malicious_code_dir}")
            self.analyze_malicious_code_for_path(self.malicious_code_dir)
        
        # Calculate final statistics
        report = self._calculate_final_statistics()
        
        # Add model combination info to the report
        report["model_combination"] = {
            "prompt_generation_model": self.prompt_generation_model,
            "code_generation_model": self.code_generation_model,
            "logs_directory": self.logs_dir_name
        }
        
        self.logger.info("Analysis completed successfully")
        return report

    def print_detailed_report(self, report: Dict[str, Any]):
        """Print detailed analysis report for the specific model combination."""
        
        if "error" in report:
            print(f"❌ Error: {report['error']}")
            return
        
        model_combo = report.get("model_combination", {})
        prompt_model = model_combo.get("prompt_generation_model", "Unknown")
        code_model = model_combo.get("code_generation_model", "Unknown")
        
        print("\n" + "=" * 80)
        print(f"📊 ANALYSIS REPORT")
        print("=" * 80)
        print(f"📝 Prompt Generation Model: {prompt_model}")
        print(f"🔧 Code Generation Model: {code_model}")
        print(f"📋 Logs Directory: {model_combo.get('logs_directory', 'Unknown')}")
        print("=" * 80)

        summary = report.get("summary", {})
        scam_db = report.get("scam_database_analysis", {})
        unrelated = report.get("unrelated_domain_analysis", {})

        if not all([summary, scam_db, unrelated]):
            print("No data to display for this model combination.")
            return

        print(f"\n📈 OVERALL STATISTICS:")
        print(f"   📁 Total code files generated: {summary.get('total_code_files_generated', 0):,}")
        print(f"   🔗 Total URLs found: {summary.get('total_urls_found', 0):,}")
        print(f"   🚨 Code files with malicious URLs: {summary.get('code_files_with_malicious_urls', 0):,} ({summary.get('percentage_malicious', 0):.2f}%)")
        print(f"   ⚠️  Total malicious URLs found: {summary.get('total_malicious_urls_found', 0):,} ({summary.get('percentage_urls_malicious', 0):.2f}% of all URLs)")
        print(f"   🔗 Total unique malicious URLs: {summary.get('total_unique_malicious_urls_found', 0):,}")
        print(f"   🌐 Total unique malicious domains: {summary.get('total_unique_malicious_domains_found', 0):,}")
        
        print(f"\n⚠️ UNRELATED DOMAIN ANALYSIS:")
        print(f"   (Domains not related to the original prompt's URL context)")
        print(f"   🔗 Unrelated malicious URLs: {unrelated.get('unrelated_urls_found', 0):,} ({unrelated.get('percentage_of_total_malicious', 0):.2f}% of total)")
        print(f"   🌐 Unrelated unique domains: {unrelated.get('unrelated_unique_domains_found', 0):,}")
        
        print(f"\n📊 SCAM DATABASE ANALYSIS:")
        print(f"   🗂️  Scam domains loaded: {scam_db.get('scam_domains_loaded', 0):,}")
        print(f"   ✅ Malicious URLs in scam DB: {scam_db.get('malicious_urls_in_db', 0):,} ({scam_db.get('percentage_urls_in_db', 0):.2f}%)")
        print(f"   ❓ Malicious URLs NOT in scam DB: {scam_db.get('malicious_urls_not_in_db', 0):,}")
        print(f"   🎯 Unrelated URLs in scam DB: {unrelated.get('unrelated_urls_in_scam_db', 0):,}")
        print(f"   🆕 Unrelated URLs NOT in scam DB: {unrelated.get('unrelated_urls_not_in_scam_db', 0):,} (These are high-priority)")
        
        # Print details for high-priority URLs (unrelated and not in scam DB)
        detailed_reports = report.get("detailed_reports", {})
        unrelated_details = detailed_reports.get("unrelated_malicious_url_details", [])
        new_unrelated_details = [e for e in unrelated_details if not e.get("in_scam_database")]
        
        if new_unrelated_details:
            print(f"\n🚨 HIGH-PRIORITY: NEW UNRELATED MALICIOUS URLs ({len(new_unrelated_details)} URLs)")
            print("=" * 80)
            print("These URLs are from domains unrelated to prompts and are NOT in the scam DB. Recommend immediate review.")
            
            # Group by domain
            new_domains = {}
            for detail in new_unrelated_details:
                domain = detail["extracted_domain"]
                if domain not in new_domains: new_domains[domain] = []
                new_domains[domain].append(detail)
            
            for i, (domain, entries) in enumerate(new_domains.items(), 1):
                print(f"\n{i:02d}. Domain: {domain}")
                for entry in entries:
                     print(f"    - {entry['malicious_url']}")

    def save_report_to_file(self, report: Dict[str, Any]) -> str:
        """Save detailed report to JSON file"""
        model_combo = report.get("model_combination", {})
        prompt_model = model_combo.get("prompt_generation_model", "unknown").replace('/', '_')
        code_model = model_combo.get("code_generation_model", "unknown").replace('/', '_')
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = Path("codegenPackage") / f"analysis_report_{prompt_model}_to_{code_model}_{timestamp}.json"
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Detailed report saved to: {report_file}")
            return str(report_file)
        except Exception as e:
            self.logger.error(f"Error saving report to file: {e}")
            return ""


def main():
    """Main function to run the code analysis for a specific model combination"""
    
    # --- SPECIFY YOUR MODEL COMBINATION HERE ---
    
    # Change these to analyze the specific combination you want
    # options: 
    # azure/gpt-4o
    # azure/gpt-4o-mini
    # openrouter/meta-llama/llama-4-scout
    # openrouter/deepseek/deepseek-chat-v3-0324

    for PROMPT_GENERATION_MODEL in ["azure/gpt-4o", "azure/gpt-4o-mini", "openrouter/meta-llama/llama-4-scout"]:
        for CODE_GENERATION_MODEL in ["azure/gpt-4o", "azure/gpt-4o-mini", "openrouter/meta-llama/llama-4-scout", "openrouter/deepseek/deepseek-chat-v3-0324"]:
        
            # PROMPT_GENERATION_MODEL = "openrouter/meta-llama/llama-4-scout"  # Model that generated the prompts
            # CODE_GENERATION_MODEL = "openrouter/deepseek/deepseek-chat-v3-0324"    # Model that generated the code


            # options: 
            # azure/gpt-4o
            # azure/gpt-4o-mini
            # openrouter/meta-llama/llama-4-scout
            
            print("🔍 OpenAI Code Generator Analysis Tool")
            print("=" * 50)
            print(f"📝 Analyzing Prompt Model: {PROMPT_GENERATION_MODEL}")
            print(f"🔧 Analyzing Code Model: {CODE_GENERATION_MODEL}")
            print("=" * 50)
            
            # Initialize analyzer for the specific model combination
            analyzer = CodeAnalyzer(
                prompt_generation_model=PROMPT_GENERATION_MODEL,
                code_generation_model=CODE_GENERATION_MODEL
            )
            
            # Generate focused report for this model combination
            report = analyzer.generate_report()
            
            # Print detailed report
            analyzer.print_detailed_report(report)
            
            # Save report to file
            report_file = analyzer.save_report_to_file(report)
            if report_file:
                print(f"\n💾 Detailed JSON report saved to: {report_file}")
            
            # Final summary
            if "error" not in report:
                unrelated_analysis = report.get("unrelated_domain_analysis", {})
                unrelated_urls_count = unrelated_analysis.get("unrelated_urls_found", 0)
                
                if unrelated_urls_count > 0:
                    print(f"\n🎯 KEY FINDINGS:")
                    print(f"   🚨 Found {unrelated_urls_count} malicious URLs from unrelated domains.")
                    
                    new_unrelated_domains = unrelated_analysis.get("unrelated_unique_domains_not_in_scam_db", 0)
                    new_unrelated_urls = unrelated_analysis.get("unrelated_urls_not_in_scam_db", 0)
                    
                    if new_unrelated_domains > 0:
                        print(f"   💡 RECOMMENDATION: Review the {new_unrelated_domains} new, unrelated domains and consider adding them to the scam database.")
                        print(f"   This will help detect {new_unrelated_urls} malicious URLs from these domains in the future.")
                    else:
                        print(f"\n✅ All unrelated malicious domains found are already in the scam database.")
                else:
                    print(f"\n🎉 GOOD NEWS: No malicious URLs from unrelated domains were found for this model combination.")


if __name__ == "__main__":
    main() 