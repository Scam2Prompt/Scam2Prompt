#!/usr/bin/env python3
"""
Malicious URL Validation Tool

This tool reads analysis reports from the codegenPackage folder, extracts all malicious URLs,
checks if they are still accessible today, and maintains a simple JSON database of results.

Features:
- Reads all analysis report JSON files from codegenPackage
- Extracts malicious URLs from "detailed_reports"."all_malicious_urls" arrays
- Uses optimized quick URL checking (HEAD requests, short timeouts)
- Maintains a simple JSON database for cross-platform compatibility
- Provides regular progress reporting
- Handles deduplication of URLs across multiple reports
- Tracks accessibility status and response times
"""

import os
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Any, Optional
from urllib.parse import urlparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import our quick URL checking functions
from browsePackage.web_accessor import WebAccessor


class MaliciousURLValidator:
    """
    Validates malicious URLs found in analysis reports and maintains a JSON database
    of accessibility results.
    """
    
    def __init__(self, 
                 reports_dir: str = "../codegenPackage",
                 database_file: str = "malicious_urls_database.json",
                 max_workers: int = 20,
                 timeout_per_url: int = 5):
        """
        Initialize the URL validator.
        
        Args:
            reports_dir: Directory containing analysis report JSON files
            database_file: Path to JSON database file for storing results
            max_workers: Maximum concurrent workers for URL checking
            timeout_per_url: Timeout in seconds per URL check
        """
        self.reports_dir = Path(reports_dir)
        self.database_file = Path(database_file)
        self.max_workers = max_workers
        self.timeout_per_url = timeout_per_url
        
        # Initialize web accessor for URL checking
        self.web_accessor = WebAccessor()
        
        # Setup logging
        self.setup_logging()
        
        # Load existing database
        self.database = self.load_database()
        
        # Statistics
        self.stats = {
            "reports_processed": 0,
            "total_malicious_urls_found": 0,
            "unique_urls_to_check": 0,
            "urls_already_in_database": 0,
            "new_urls_checked": 0,
            "currently_accessible": 0,
            "currently_inaccessible": 0,
            "processing_start_time": None,
            "last_update_time": None
        }
    
    def setup_logging(self):
        """Setup comprehensive logging"""
        log_dir = Path("validation_logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = log_dir / f"url_validation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"URL Validation started - Log file: {log_file}")
    
    def load_database(self) -> Dict[str, Any]:
        """Load existing URL database or create new one"""
        if self.database_file.exists():
            try:
                with open(self.database_file, 'r', encoding='utf-8') as f:
                    database = json.load(f)
                self.logger.info(f"Loaded existing database with {len(database.get('urls', {}))} URLs")
                return database
            except Exception as e:
                self.logger.error(f"Error loading database file: {e}")
                self.logger.info("Creating new database")
        
        # Create new database structure
        return {
            "metadata": {
                "created_at": datetime.now().isoformat(),
                "last_updated": None,
                "total_urls": 0,
                "last_validation_run": None
            },
            "urls": {}  # url -> validation_data
        }
    
    def save_database(self):
        """Save the database to JSON file"""
        try:
            # Update metadata
            self.database["metadata"]["last_updated"] = datetime.now().isoformat()
            self.database["metadata"]["total_urls"] = len(self.database["urls"])
            self.database["metadata"]["last_validation_run"] = datetime.now().isoformat()
            
            # Save to file with backup
            backup_file = self.database_file.with_suffix('.json.backup')
            if self.database_file.exists():
                # Create backup of existing file
                self.database_file.rename(backup_file)
            
            with open(self.database_file, 'w', encoding='utf-8') as f:
                json.dump(self.database, f, indent=2, ensure_ascii=False)
            
            # Remove backup if save was successful
            if backup_file.exists():
                backup_file.unlink()
                
            self.logger.info(f"Database saved with {len(self.database['urls'])} URLs")
            
        except Exception as e:
            self.logger.error(f"Error saving database: {e}")
            # Restore backup if it exists
            if backup_file.exists():
                backup_file.rename(self.database_file)
                self.logger.info("Restored database from backup")
    
    def find_analysis_reports(self) -> List[Path]:
        """Find all analysis report JSON files"""
        report_files = []
        
        # Look for individual analysis reports
        pattern_individual = "analysis_report_*.json"
        individual_reports = list(self.reports_dir.glob(pattern_individual))
        report_files.extend(individual_reports)
        
        # Look for comprehensive analysis reports
        pattern_comprehensive = "comprehensive_analysis_*.json"
        comprehensive_reports = list(self.reports_dir.glob(pattern_comprehensive))
        report_files.extend(comprehensive_reports)
        
        # Also check archived reports
        archived_dir = self.reports_dir / "archived_analysis_reports"
        if archived_dir.exists():
            archived_reports = list(archived_dir.glob("analysis_report_*.json"))
            report_files.extend(archived_reports)
        
        self.logger.info(f"Found {len(report_files)} analysis report files")
        return sorted(report_files, key=lambda x: x.stat().st_mtime, reverse=True)  # Newest first
    
    def extract_urls_from_report(self, report_file: Path) -> Set[str]:
        """Extract malicious URLs from a single analysis report"""
        urls = set()
        
        try:
            with open(report_file, 'r', encoding='utf-8') as f:
                report_data = json.load(f)
            
            # Handle comprehensive reports (multiple experiments)
            if "all_reports" in report_data:
                self.logger.debug(f"Processing comprehensive report: {report_file.name}")
                for experiment_key, experiment_data in report_data["all_reports"].items():
                    urls.update(self._extract_urls_from_single_experiment(experiment_data))
            
            # Handle individual experiment reports
            elif "detailed_reports" in report_data:
                self.logger.debug(f"Processing individual report: {report_file.name}")
                urls.update(self._extract_urls_from_single_experiment(report_data))
            
            else:
                self.logger.warning(f"Unknown report format in {report_file.name}")
        
        except Exception as e:
            self.logger.error(f"Error processing report {report_file.name}: {e}")
        
        return urls
    
    def _extract_urls_from_single_experiment(self, experiment_data: Dict) -> Set[str]:
        """Extract URLs from a single experiment's data"""
        urls = set()
        
        try:
            detailed_reports = experiment_data.get("detailed_reports", {})
            all_malicious_urls = detailed_reports.get("all_malicious_urls", [])
            
            for url_entry in all_malicious_urls:
                malicious_url = url_entry.get("malicious_url", "").strip()
                if malicious_url:
                    # Clean and normalize URL
                    cleaned_url = self._clean_url(malicious_url)
                    if cleaned_url:
                        urls.add(cleaned_url)
        
        except Exception as e:
            self.logger.warning(f"Error extracting URLs from experiment data: {e}")
        
        return urls
    
    def _clean_url(self, url: str) -> Optional[str]:
        """Clean and validate URL format"""
        try:
            url = url.strip()
            
            # Skip empty URLs
            if not url:
                return None
            
            # Skip obviously invalid URLs
            if any(char in url for char in [' ', '\n', '\t']):
                return None
                
            # Add protocol if missing
            if not url.startswith(('http://', 'https://')):
                url = f"https://{url}"
            
            # Basic URL validation
            parsed = urlparse(url)
            if not all([parsed.scheme, parsed.netloc]):
                return None
            
            return url
            
        except Exception:
            return None
    
    def collect_all_malicious_urls(self) -> Set[str]:
        """Collect all unique malicious URLs from all analysis reports"""
        self.logger.info("🔍 Collecting malicious URLs from analysis reports...")
        
        all_urls = set()
        report_files = self.find_analysis_reports()
        
        for i, report_file in enumerate(report_files, 1):
            self.logger.info(f"Processing report {i}/{len(report_files)}: {report_file.name}")
            
            urls_from_report = self.extract_urls_from_report(report_file)
            all_urls.update(urls_from_report)
            
            self.stats["reports_processed"] += 1
            
            # Progress update
            if i % 5 == 0 or i == len(report_files):
                self.logger.info(f"  Progress: {i}/{len(report_files)} reports processed, "
                               f"{len(all_urls)} unique URLs found so far")
        
        self.stats["total_malicious_urls_found"] = len(all_urls)
        self.logger.info(f"✅ Collected {len(all_urls)} unique malicious URLs from {len(report_files)} reports")
        
        return all_urls
    
    def filter_urls_to_check(self, all_urls: Set[str]) -> Set[str]:
        """Filter URLs to only check those not recently validated"""
        urls_to_check = set()
        current_time = datetime.now()
        
        for url in all_urls:
            url_data = self.database["urls"].get(url)
            
            if url_data is None:
                # URL not in database, need to check
                urls_to_check.add(url)
            else:
                # Check if we need to re-validate (e.g., if last check was more than 7 days ago)
                last_checked = url_data.get("last_checked")
                if last_checked:
                    try:
                        last_checked_dt = datetime.fromisoformat(last_checked)
                        days_since_check = (current_time - last_checked_dt).days
                        
                        # Re-check if more than 7 days old
                        if days_since_check > 7:
                            urls_to_check.add(url)
                        else:
                            self.stats["urls_already_in_database"] += 1
                    except Exception:
                        # Invalid date format, re-check
                        urls_to_check.add(url)
                else:
                    # No last_checked field, re-check
                    urls_to_check.add(url)
        
        self.stats["unique_urls_to_check"] = len(urls_to_check)
        self.logger.info(f"📊 URLs to check: {len(urls_to_check)} new/stale, "
                        f"{self.stats['urls_already_in_database']} recently validated")
        
        return urls_to_check
    
    def validate_urls(self, urls_to_check: Set[str]):
        """Validate accessibility of URLs using parallel processing"""
        if not urls_to_check:
            self.logger.info("✅ No URLs need validation")
            return
        
        self.logger.info(f"🚀 Starting validation of {len(urls_to_check)} URLs "
                        f"with {self.max_workers} workers...")
        
        urls_list = list(urls_to_check)
        start_time = time.time()
        completed = 0
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all validation tasks
            future_to_url = {
                executor.submit(self._validate_single_url, url): url 
                for url in urls_list
            }
            
            # Process results as they complete
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                
                try:
                    result = future.result()
                    self._store_validation_result(url, result)
                    
                    # Update statistics
                    if result['available']:
                        self.stats["currently_accessible"] += 1
                    else:
                        self.stats["currently_inaccessible"] += 1
                    
                    completed += 1
                    self.stats["new_urls_checked"] = completed
                    
                    # Progress reporting
                    if completed % 50 == 0 or completed == len(urls_list):
                        elapsed = time.time() - start_time
                        rate = completed / elapsed if elapsed > 0 else 0
                        accessible_pct = (self.stats["currently_accessible"] / completed * 100) if completed > 0 else 0
                        
                        self.logger.info(f"  Progress: {completed}/{len(urls_list)} ({completed/len(urls_list)*100:.1f}%) | "
                                       f"Accessible: {self.stats['currently_accessible']} ({accessible_pct:.1f}%) | "
                                       f"Rate: {rate:.1f} URLs/s")
                        
                        # Save database periodically
                        if completed % 100 == 0:
                            self.save_database()
                
                except Exception as e:
                    self.logger.error(f"Error validating URL {url}: {e}")
                    # Store error result
                    error_result = {
                        'available': False,
                        'error': f"Validation error: {str(e)}",
                        'status_code': None,
                        'response_time_ms': None,
                        'checked_at': datetime.now().isoformat()
                    }
                    self._store_validation_result(url, error_result)
                    completed += 1
        
        elapsed = time.time() - start_time
        self.logger.info(f"✅ URL validation completed in {elapsed:.1f}s")
        self.logger.info(f"📊 Results: {self.stats['currently_accessible']}/{completed} URLs accessible "
                        f"({self.stats['currently_accessible']/completed*100:.1f}%)")
    
    def _validate_single_url(self, url: str) -> Dict[str, Any]:
        """Validate a single URL using the web accessor's quick check"""
        try:
            result = self.web_accessor.quick_availability_check(
                url, 
                timeout=self.timeout_per_url, 
                try_both_protocols=True
            )
            
            # Add timestamp
            result['checked_at'] = datetime.now().isoformat()
            
            return result
            
        except Exception as e:
            return {
                'available': False,
                'error': f"Exception during validation: {str(e)}",
                'status_code': None,
                'response_time_ms': None,
                'checked_at': datetime.now().isoformat()
            }
    
    def _store_validation_result(self, url: str, result: Dict[str, Any]):
        """Store validation result in database"""
        # Initialize URL entry if it doesn't exist
        if url not in self.database["urls"]:
            self.database["urls"][url] = {
                "first_seen": datetime.now().isoformat(),
                "validation_history": []
            }
        
        # Add current validation result
        validation_entry = {
            "timestamp": result['checked_at'],
            "available": result['available'],
            "status_code": result.get('status_code'),
            "response_time_ms": result.get('response_time_ms'),
            "error": result.get('error'),
            "protocol_used": result.get('protocol_used'),
            "redirect_count": result.get('redirect_count', 0),
            "final_url": result.get('final_url', url)
        }
        
        # Update URL data
        url_data = self.database["urls"][url]
        url_data["last_checked"] = result['checked_at']
        url_data["currently_available"] = result['available']
        url_data["validation_history"].append(validation_entry)
        
        # Keep only last 10 validation entries to prevent database bloat
        if len(url_data["validation_history"]) > 10:
            url_data["validation_history"] = url_data["validation_history"][-10:]
    
    def generate_summary_report(self) -> Dict[str, Any]:
        """Generate a summary report of the validation results"""
        total_urls = len(self.database["urls"])
        currently_accessible = sum(1 for url_data in self.database["urls"].values() 
                                 if url_data.get("currently_available", False))
        currently_inaccessible = total_urls - currently_accessible
        
        # Analyze accessibility patterns
        never_accessible = sum(1 for url_data in self.database["urls"].values() 
                             if all(not entry["available"] for entry in url_data.get("validation_history", [])))
        
        recently_checked = sum(1 for url_data in self.database["urls"].values() 
                             if url_data.get("last_checked") and 
                             (datetime.now() - datetime.fromisoformat(url_data["last_checked"])).days <= 7)
        
        summary = {
            "validation_summary": {
                "total_unique_malicious_urls": total_urls,
                "currently_accessible": currently_accessible,
                "currently_inaccessible": currently_inaccessible,
                "accessibility_percentage": (currently_accessible / total_urls * 100) if total_urls > 0 else 0,
                "never_accessible": never_accessible,
                "recently_validated": recently_checked
            },
            "processing_statistics": self.stats,
            "database_info": self.database["metadata"]
        }
        
        return summary
    
    def print_summary_report(self, summary: Dict[str, Any]):
        """Print a formatted summary report"""
        print("\n" + "=" * 80)
        print("📊 MALICIOUS URL VALIDATION SUMMARY")
        print("=" * 80)
        
        val_summary = summary["validation_summary"]
        processing = summary["processing_statistics"]
        
        print(f"\n📈 VALIDATION RESULTS:")
        print(f"   📁 Total unique malicious URLs found: {val_summary['total_unique_malicious_urls']:,}")
        print(f"   ✅ Currently accessible: {val_summary['currently_accessible']:,} "
              f"({val_summary['accessibility_percentage']:.1f}%)")
        print(f"   ❌ Currently inaccessible: {val_summary['currently_inaccessible']:,}")
        print(f"   🚫 Never accessible: {val_summary['never_accessible']:,}")
        print(f"   🔄 Recently validated (last 7 days): {val_summary['recently_validated']:,}")
        
        print(f"\n🔍 PROCESSING STATISTICS:")
        print(f"   📄 Reports processed: {processing['reports_processed']}")
        print(f"   🆕 New URLs checked this run: {processing['new_urls_checked']}")
        print(f"   ⏱️  URLs already in database: {processing['urls_already_in_database']}")
        
        if processing["processing_start_time"]:
            start_time = datetime.fromisoformat(processing["processing_start_time"])
            elapsed = (datetime.now() - start_time).total_seconds()
            print(f"   ⏱️  Total processing time: {elapsed:.1f} seconds")
    
    def run_validation(self):
        """Run the complete validation process"""
        print("🚀 Malicious URL Validation Tool")
        print("=" * 80)
        print(f"📂 Reports directory: {self.reports_dir}")
        print(f"💾 Database file: {self.database_file}")
        print(f"👥 Max workers: {self.max_workers}")
        print(f"⏱️  Timeout per URL: {self.timeout_per_url}s")
        print("=" * 80)
        
        self.stats["processing_start_time"] = datetime.now().isoformat()
        
        try:
            # Step 1: Collect all malicious URLs from reports
            all_urls = self.collect_all_malicious_urls()
            
            if not all_urls:
                self.logger.warning("No malicious URLs found in reports")
                return
            
            # Step 2: Filter URLs that need checking
            urls_to_check = self.filter_urls_to_check(all_urls)
            
            # Step 3: Validate URLs
            self.validate_urls(urls_to_check)
            
            # Step 4: Save final database
            self.save_database()
            
            # Step 5: Generate and display summary
            summary = self.generate_summary_report()
            self.print_summary_report(summary)
            
            # Step 6: Save summary report
            self._save_summary_report(summary)
            
            print(f"\n✅ Validation completed successfully!")
            print(f"💾 Database saved to: {self.database_file}")
            print(f"📋 Summary report saved")
            
        except Exception as e:
            self.logger.error(f"Error during validation process: {e}")
            raise
    
    def _save_summary_report(self, summary: Dict[str, Any]):
        """Save summary report to file"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            summary_file = Path(f"url_validation_summary_{timestamp}.json")
            
            with open(summary_file, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
                
            self.logger.info(f"Summary report saved to: {summary_file}")
            
        except Exception as e:
            self.logger.error(f"Error saving summary report: {e}")


def main():
    """Main function to run URL validation"""
    
    # Configuration - adjust these as needed
    REPORTS_DIRECTORY = "../codegenPackage"
    DATABASE_FILE = "malicious_urls_database.json"
    MAX_WORKERS = 20  # Concurrent workers for URL checking
    TIMEOUT_PER_URL = 5  # Seconds per URL
    
    # Initialize and run validator
    validator = MaliciousURLValidator(
        reports_dir=REPORTS_DIRECTORY,
        database_file=DATABASE_FILE,
        max_workers=MAX_WORKERS,
        timeout_per_url=TIMEOUT_PER_URL
    )
    
    validator.run_validation()


if __name__ == "__main__":
    main()
