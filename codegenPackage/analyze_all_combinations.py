#!/usr/bin/env python3
"""
Comprehensive Analysis Script for Multiple Model Combinations

This script runs the code analysis for multiple LLM model combinations automatically
and generates comprehensive comparison tables for all experiments.

Features:
- Analyzes all 12 model combinations (3 prompt models × 4 code models)
- Generates comparison tables for main metrics
- Analyzes overlap in malicious URLs between models
- Analyzes URL accessibility using malicious_urls_database.json
- Provides insights into model performance and security characteristics
- Formats tables for both terminal display and Google Sheets copy-paste
"""

import subprocess
import sys
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Set, Tuple, Optional
from collections import defaultdict
import os
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import pandas as pd
import upsetplot

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from codeAnalyzer import CodeAnalyzer


class ComprehensiveAnalyzer:
    """
    Comprehensive analyzer that collects results from all model combinations
    and generates detailed comparison tables.
    """
    
    def __init__(self):
        """Initialize the comprehensive analyzer"""
        self.setup_logging()
        
        # Define all model combinations (3 prompt models × 4 code models = 12 combinations)
        self.prompt_models = [
            "azure/gpt-4o",
            "azure/gpt-4o-mini",
            "openrouter/meta-llama/llama-4-scout"
        ]
        
        self.code_models = [
            "azure/gpt-4o",
            "azure/gpt-4o-mini", 
            "openrouter/meta-llama/llama-4-scout",
            "openrouter/deepseek/deepseek-chat-v3-0324"
        ]
        
        # Storage for all analysis results
        self.all_reports = {}  # (prompt_model, code_model) -> report
        self.failed_analyses = []
        
        # Load accessibility database
        self.accessibility_database = self.load_accessibility_database()
    
    def setup_logging(self):
        """Setup comprehensive logging"""
        log_dir = Path("codegenPackage/analysis_logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = log_dir / f"comprehensive_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def load_accessibility_database(self) -> Dict[str, Any]:
        """Load the malicious URLs accessibility database"""
        database_path = Path("browsePackage/malicious_urls_database.json")
        
        if not database_path.exists():
            self.logger.warning(f"⚠️ Accessibility database not found at {database_path}")
            self.logger.warning("   Accessibility analysis will be skipped")
            return {"urls": {}}
        
        try:
            with open(database_path, 'r', encoding='utf-8') as f:
                database = json.load(f)
            
            total_urls = len(database.get("urls", {}))
            accessible_urls = sum(1 for url_data in database.get("urls", {}).values() 
                                if url_data.get("currently_available", False))
            
            self.logger.info(f"✅ Loaded accessibility database with {total_urls} URLs")
            self.logger.info(f"   📊 {accessible_urls}/{total_urls} URLs currently accessible")
            
            return database
        
        except Exception as e:
            self.logger.error(f"❌ Error loading accessibility database: {e}")
            return {"urls": {}}
    
    def is_url_accessible(self, url: str) -> bool:
        """Check if a URL is currently accessible according to the database"""
        if not self.accessibility_database or "urls" not in self.accessibility_database:
            return False
        
        url_data = self.accessibility_database["urls"].get(url, {})
        return url_data.get("currently_available", False)
    
    def extract_accessible_urls_from_experiment(self, experiment_data: Dict) -> Set[str]:
        """Extract accessible URLs from a single experiment's data"""
        accessible_urls = set()
        
        try:
            detailed_reports = experiment_data.get("detailed_reports", {})
            all_malicious_urls = detailed_reports.get("all_malicious_urls", [])
            
            for url_entry in all_malicious_urls:
                malicious_url = url_entry.get("malicious_url", "").strip()
                if malicious_url and self.is_url_accessible(malicious_url):
                    accessible_urls.add(malicious_url)
        
        except Exception as e:
            self.logger.warning(f"Error extracting accessible URLs from experiment data: {e}")
        
        return accessible_urls
    
    def extract_accessible_domains_from_experiment(self, experiment_data: Dict) -> Set[str]:
        """Extract domains that have at least one accessible URL from experiment data"""
        accessible_domains = set()
        
        try:
            detailed_reports = experiment_data.get("detailed_reports", {})
            all_malicious_urls = detailed_reports.get("all_malicious_urls", [])
            
            for url_entry in all_malicious_urls:
                malicious_url = url_entry.get("malicious_url", "").strip()
                domain = url_entry.get("extracted_domain", "").strip()
                # Remove trailing dot if present (safety measure for domains like "example.com.")
                domain = domain.rstrip('.')
                
                if malicious_url and domain and self.is_url_accessible(malicious_url):
                    accessible_domains.add(domain)
        
        except Exception as e:
            self.logger.warning(f"Error extracting accessible domains from experiment data: {e}")
        
        return accessible_domains
    
    def get_accessible_urls_for_combination(self, prompt_model: str, code_model: str) -> Set[str]:
        """Get accessible URLs for a specific model combination"""
        key = (prompt_model, code_model)
        if key not in self.all_reports:
            return set()
        
        report = self.all_reports[key]
        return self.extract_accessible_urls_from_experiment(report)
    
    def get_accessible_domains_for_combination(self, prompt_model: str, code_model: str) -> Set[str]:
        """Get accessible domains for a specific model combination"""
        key = (prompt_model, code_model)
        if key not in self.all_reports:
            return set()
        
        report = self.all_reports[key]
        return self.extract_accessible_domains_from_experiment(report)
    
    def extract_unrelated_accessible_domains_from_experiment(self, experiment_data: Dict) -> Set[str]:
        """Extract unrelated domains that have at least one accessible URL and are not in scam DB"""
        accessible_unrelated_domains = set()
        
        try:
            unrelated_analysis = experiment_data.get("unrelated_domain_analysis", {})
            unrelated_details = unrelated_analysis.get("unrelated_malicious_urls_not_in_scam_db", [])
            
            for entry in unrelated_details:
                malicious_url = entry.get("malicious_url", "").strip()
                domain = entry.get("extracted_domain", "").strip()
                # Remove trailing dot if present (safety measure for domains like "example.com.")
                domain = domain.rstrip('.')
                
                if malicious_url and domain and self.is_url_accessible(malicious_url):
                    accessible_unrelated_domains.add(domain)
        
        except Exception as e:
            self.logger.warning(f"Error extracting unrelated accessible domains: {e}")
        
        return accessible_unrelated_domains
    
    def run_single_analysis(self, prompt_model: str, code_model: str) -> Dict[str, Any]:
        """Run analysis for a specific model combination and return the report"""
        self.logger.info(f"Analyzing: {prompt_model} → {code_model}")
        
        try:
            # Create analyzer for this specific combination
            analyzer = CodeAnalyzer(
                prompt_generation_model=prompt_model,
                code_generation_model=code_model
            )
            
            # Generate report
            report = analyzer.generate_report()
            
            if "error" in report:
                self.logger.error(f"Analysis failed for {prompt_model} → {code_model}: {report['error']}")
                self.failed_analyses.append((prompt_model, code_model, report["error"]))
                return None
            
            self.logger.info(f"✅ Analysis completed for {prompt_model} → {code_model}")
            return report
            
        except Exception as e:
            self.logger.error(f"❌ Error analyzing {prompt_model} → {code_model}: {e}")
            self.failed_analyses.append((prompt_model, code_model, str(e)))
            return None
    
    def collect_all_reports(self):
        """Collect analysis reports for all model combinations"""
        self.logger.info("🚀 Starting comprehensive analysis for all model combinations")
        
        total_combinations = len(self.prompt_models) * len(self.code_models)
        self.logger.info(f"📊 Will analyze {total_combinations} model combinations")
        
        # Run analysis for each combination
        for prompt_model in self.prompt_models:
            for code_model in self.code_models:
                print(f"\n{'='*80}")
                print(f"🔍 Analyzing: {prompt_model} → {code_model}")
                print(f"{'='*80}")
                
                report = self.run_single_analysis(prompt_model, code_model)
                if report is not None:
                    self.all_reports[(prompt_model, code_model)] = report
        
        self.logger.info(f"✅ Collected {len(self.all_reports)} successful reports out of {total_combinations} combinations")
        
        if self.failed_analyses:
            self.logger.warning(f"❌ {len(self.failed_analyses)} analyses failed:")
            for prompt_model, code_model, error in self.failed_analyses:
                self.logger.warning(f"   {prompt_model} → {code_model}: {error}")
    
    def format_table_row(self, row_data: List[Any], widths: List[int]) -> str:
        """Format a table row with proper spacing for both terminal and spreadsheet"""
        formatted_cells = []
        for i, (data, width) in enumerate(zip(row_data, widths)):
            if isinstance(data, float):
                formatted_data = f"{data:.2f}%"
            elif isinstance(data, int):
                formatted_data = f"{data:,}"
            else:
                formatted_data = str(data)
            
            # For terminal display, pad with spaces
            formatted_cells.append(formatted_data.ljust(width))
        
        # Join with tabs for spreadsheet compatibility and pipes for terminal readability
        return "| " + " | ".join(formatted_cells) + " |"
    
    def print_table_header(self, headers: List[str], widths: List[int], title: str):
        """Print a formatted table header"""
        print(f"\n{'='*140}")
        print(f"📊 {title}")
        print(f"{'='*140}")
        
        # Print headers
        header_row = self.format_table_row(headers, widths)
        print(header_row)
        
        # Print separator
        separator_parts = ["─" * width for width in widths]
        separator = "| " + " | ".join(separator_parts) + " |"
        print(separator)
    
    def generate_main_comparison_table(self):
        """Generate the main comparison table for all experiments"""
        headers = [
            "Prompt Model", "Code Model", "Total Files", "Total URLs", "Malicious Files", 
            "Malicious %", "Malicious URLs", "Accessible URLs", "Unique Domains", 
            "Accessible Domains", "Unrelated URLs"
        ]
        widths = [25, 35, 12, 12, 15, 12, 15, 15, 15, 17, 15]
        
        self.print_table_header(headers, widths, "MAIN EXPERIMENT COMPARISON")
        
        table_data = []
        
        # Collect data for all combinations
        for prompt_model in self.prompt_models:
            for code_model in self.code_models:
                key = (prompt_model, code_model)
                if key not in self.all_reports:
                    # Print row for failed analysis
                    row_data = [
                        prompt_model.split('/')[-1], code_model.split('/')[-1], 
                        "FAILED", "FAILED", "FAILED", "FAILED", "FAILED", "FAILED", "FAILED", "FAILED", "FAILED"
                    ]
                    table_data.append(row_data)
                    print(self.format_table_row(row_data, widths))
                    continue
                
                report = self.all_reports[key]
                summary = report.get("summary", {})
                unrelated = report.get("unrelated_domain_analysis", {})
                
                # Get accessibility data
                accessible_urls = self.get_accessible_urls_for_combination(prompt_model, code_model)
                accessible_domains = self.get_accessible_domains_for_combination(prompt_model, code_model)
                
                row_data = [
                    prompt_model.split('/')[-1],  # Shorten model names
                    code_model.split('/')[-1],
                    summary.get("total_code_files_generated", 0),
                    summary.get("total_urls_found", 0),  # NEW: Total URLs found (all URLs)
                    summary.get("code_files_with_malicious_urls", 0),
                    summary.get("percentage_malicious", 0),
                    summary.get("total_malicious_urls_found", 0),  # RENAMED: Now "Malicious URLs"
                    len(accessible_urls),
                    summary.get("total_unique_malicious_domains_found", 0),
                    len(accessible_domains),
                    unrelated.get("unrelated_urls_found", 0)
                ]
                
                table_data.append(row_data)
                print(self.format_table_row(row_data, widths))
        
        # Print Google Sheets version
        print(f"\n📋 GOOGLE SHEETS VERSION - MAIN EXPERIMENT COMPARISON:")
        print("=" * 100)
        
        # Header for Google Sheets (comma-separated)
        gs_header = ",".join(headers)
        print(gs_header)
        
        # Data rows for Google Sheets
        for row_data in table_data:
            # Format the data appropriately for Google Sheets
            gs_row_data = []
            for i, data in enumerate(row_data):
                if isinstance(data, float) and i == 5:  # Malicious % (moved from index 4 to 5)
                    gs_row_data.append(f"{data:.2f}%")
                elif isinstance(data, int) and i >= 2:  # Numeric columns
                    gs_row_data.append(str(data))
                else:
                    gs_row_data.append(str(data))
            
            gs_row = ",".join(gs_row_data)
            print(gs_row)
        
        # Generate key summary numbers
        self.generate_key_summary_numbers()
    
    def generate_key_summary_numbers(self):
        """Generate key summary numbers across all 12 experiments"""
        print(f"\n{'='*80}")
        print(f"📊 KEY SUMMARY NUMBERS - ACROSS ALL 12 EXPERIMENTS")
        print(f"{'='*80}")
        
        # 1. Collect all unique URLs across all experiments
        all_unique_urls = set()
        all_unique_malicious_urls = set()
        malicious_urls_in_scam_db = set()
        
        for (prompt_model, code_model), report in self.all_reports.items():
            # Get all URLs found (from Oracle Results)
            detailed_reports = report.get("detailed_reports", {})
            all_urls_found = detailed_reports.get("all_urls_found", [])
            all_unique_urls.update(all_urls_found)
            
            # Get all malicious URLs
            all_malicious_entries = detailed_reports.get("all_malicious_urls", [])
            for entry in all_malicious_entries:
                malicious_url = entry.get("malicious_url", "").strip()
                if malicious_url:
                    all_unique_malicious_urls.add(malicious_url)
                    
                    # Check if this malicious URL is in scam database
                    if entry.get("in_scam_database", False):
                        malicious_urls_in_scam_db.add(malicious_url)
        
        # Calculate the 3 key numbers
        total_unique_urls = len(all_unique_urls)
        total_unique_malicious_urls = len(all_unique_malicious_urls)
        
        # Ratio: Malicious URLs in scam DB / Total unique malicious URLs
        malicious_in_scam_db_count = len(malicious_urls_in_scam_db)
        ratio_malicious_in_scam_db = (malicious_in_scam_db_count / total_unique_malicious_urls) if total_unique_malicious_urls > 0 else 0
        
        # Print the 3 key numbers
        print(f"1️⃣  Total unique URLs across all experiments: {total_unique_urls:,}")
        print(f"2️⃣  Total unique malicious URLs across all experiments: {total_unique_malicious_urls:,}")
        print(f"3️⃣  Ratio (Malicious URLs in Scam DB ÷ Total Malicious): {ratio_malicious_in_scam_db:.4f}")
        print(f"    └── {malicious_in_scam_db_count:,} in scam DB ÷ {total_unique_malicious_urls:,} total malicious = {ratio_malicious_in_scam_db:.4f}")
        
        # Additional context
        malicious_detection_rate = (total_unique_malicious_urls / total_unique_urls) if total_unique_urls > 0 else 0
        print(f"\n💡 Additional Context:")
        print(f"    📊 Malicious detection rate: {malicious_detection_rate:.4f} ({malicious_detection_rate*100:.2f}%)")
        print(f"    🗂️  Scam database coverage: {ratio_malicious_in_scam_db*100:.2f}% of found malicious URLs")

    def generate_code_model_overlap_analysis(self):
        """Analyze overlap in malicious URLs between code generation models"""
        # Collect malicious URLs by (prompt_model, code_model) combination
        prompt_code_urls = defaultdict(set)  # (prompt_model, code_model) -> set of malicious URLs
        prompt_code_domains = defaultdict(set)  # (prompt_model, code_model) -> set of malicious domains
        
        for (prompt_model, code_model), report in self.all_reports.items():
            detailed_reports = report.get("detailed_reports", {})
            all_malicious_urls = detailed_reports.get("all_malicious_urls", [])
            
            for url_entry in all_malicious_urls:
                malicious_url = url_entry.get("malicious_url", "")
                domain = url_entry.get("extracted_domain", "")
                
                if malicious_url:
                    prompt_code_urls[(prompt_model, code_model)].add(malicious_url)
                if domain:
                    prompt_code_domains[(prompt_model, code_model)].add(domain)
        
        # Generate URL overlap matrices for each prompt model
        for prompt_model in self.prompt_models:
            self._generate_overlap_matrix(prompt_code_urls, prompt_model, "URLs", "URL")
            
        # Generate domain overlap matrices for each prompt model  
        for prompt_model in self.prompt_models:
            self._generate_overlap_matrix(prompt_code_domains, prompt_model, "Domains", "DOMAIN")
    
    def generate_accessible_overlap_analysis(self):
        """Analyze overlap in accessible URLs and domains between code generation models"""
        # Collect accessible URLs and domains by (prompt_model, code_model) combination
        prompt_code_accessible_urls = defaultdict(set)  
        prompt_code_accessible_domains = defaultdict(set)  
        
        for prompt_model in self.prompt_models:
            for code_model in self.code_models:
                accessible_urls = self.get_accessible_urls_for_combination(prompt_model, code_model)
                accessible_domains = self.get_accessible_domains_for_combination(prompt_model, code_model)
                
                prompt_code_accessible_urls[(prompt_model, code_model)] = accessible_urls
                prompt_code_accessible_domains[(prompt_model, code_model)] = accessible_domains
        
        # Generate accessible URL overlap matrices for each prompt model
        for prompt_model in self.prompt_models:
            self._generate_overlap_matrix(prompt_code_accessible_urls, prompt_model, "Accessible URLs", "ACCESSIBLE_URL")
            
        # Generate accessible domain overlap matrices for each prompt model  
        for prompt_model in self.prompt_models:
            self._generate_overlap_matrix(prompt_code_accessible_domains, prompt_model, "Accessible Domains", "ACCESSIBLE_DOMAIN")
    
    def _generate_overlap_matrix(self, data_dict, prompt_model, data_type, matrix_type):
        """Generate a 4x4 overlap matrix for a specific prompt model"""
        prompt_name = prompt_model.split('/')[-1]
        
        # Print terminal version
        print(f"\n{'='*140}")
        print(f"📊 CODE MODEL {matrix_type} OVERLAP MATRIX - Prompt Model: {prompt_name}")
        print(f"{'='*140}")
        
        # Get short model names
        model_names = [model.split('/')[-1] for model in self.code_models]
        
        # Create header for matrix
        header = [""] + model_names
        widths = [20] + [15] * len(model_names)
        
        # Print header
        header_row = self.format_table_row(header, widths)
        print(header_row)
        
        # Print separator
        separator_parts = ["─" * width for width in widths]
        separator = "| " + " | ".join(separator_parts) + " |"
        print(separator)
        
        # Print matrix rows
        for i, model1 in enumerate(self.code_models):
            model1_data = data_dict.get((prompt_model, model1), set())
            
            row_data = [model1.split('/')[-1]]  # Row header
            
            for j, model2 in enumerate(self.code_models):
                model2_data = data_dict.get((prompt_model, model2), set())
                
                if i == j:
                    # Diagonal - show total count
                    row_data.append(f"{len(model1_data):,}")
                else:
                    # Off-diagonal - show overlap count and percentage
                    common_data = model1_data.intersection(model2_data)
                    total_unique = len(model1_data.union(model2_data))
                    overlap_pct = (len(common_data) / total_unique * 100) if total_unique > 0 else 0
                    row_data.append(f"{len(common_data):,} ({overlap_pct:.1f}%)")
            
            print(self.format_table_row(row_data, widths))
        
        # Print Google Sheets version
        print(f"\n📋 GOOGLE SHEETS VERSION - {matrix_type} OVERLAP MATRIX ({prompt_name}):")
        print("=" * 80)
        
        # Header for Google Sheets (comma-separated)
        gs_header = ",".join(header)
        print(gs_header)
        
        # Data rows for Google Sheets
        for i, model1 in enumerate(self.code_models):
            model1_data = data_dict.get((prompt_model, model1), set())
            
            gs_row_data = [model1.split('/')[-1]]
            
            for j, model2 in enumerate(self.code_models):
                model2_data = data_dict.get((prompt_model, model2), set())
                
                if i == j:
                    gs_row_data.append(str(len(model1_data)))
                else:
                    common_data = model1_data.intersection(model2_data)
                    total_unique = len(model1_data.union(model2_data))
                    overlap_pct = (len(common_data) / total_unique * 100) if total_unique > 0 else 0
                    gs_row_data.append(f"{len(common_data)} ({overlap_pct:.1f}%)")
            
            gs_row = ",".join(gs_row_data)
            print(gs_row)
    
    def generate_prompt_model_comparison(self):
        """Compare how prompt generation models affect results"""
        headers = ["Code Model", "Prompt: gpt-4o", "Prompt: gpt-4o-mini", "Difference", "% Difference"]
        widths = [35, 15, 18, 12, 15]
        
        self.print_table_header(headers, widths, "PROMPT MODEL IMPACT ANALYSIS (Malicious URLs)")
        
        table_data = []
        
        for code_model in self.code_models:
            # Get results for both prompt models
            gpt4o_key = ("azure/gpt-4o", code_model)
            gpt4o_mini_key = ("azure/gpt-4o-mini", code_model)
            
            gpt4o_urls = 0
            gpt4o_mini_urls = 0
            
            if gpt4o_key in self.all_reports:
                gpt4o_urls = self.all_reports[gpt4o_key].get("summary", {}).get("total_malicious_urls_found", 0)
            
            if gpt4o_mini_key in self.all_reports:
                gpt4o_mini_urls = self.all_reports[gpt4o_mini_key].get("summary", {}).get("total_malicious_urls_found", 0)
            
            difference = gpt4o_urls - gpt4o_mini_urls
            percentage_diff = (difference / gpt4o_mini_urls * 100) if gpt4o_mini_urls > 0 else 0
            
            row_data = [
                code_model.split('/')[-1],
                gpt4o_urls,
                gpt4o_mini_urls,
                difference,
                percentage_diff
            ]
            
            table_data.append(row_data)
            print(self.format_table_row(row_data, widths))
        
        # Print Google Sheets version
        print(f"\n📋 GOOGLE SHEETS VERSION - PROMPT MODEL IMPACT ANALYSIS:")
        print("=" * 80)
        
        # Header for Google Sheets (comma-separated)
        gs_header = ",".join(headers)
        print(gs_header)
        
        # Data rows for Google Sheets
        for row_data in table_data:
            # Format the data appropriately for Google Sheets
            gs_row_data = [
                str(row_data[0]),  # Code Model
                str(row_data[1]),  # GPT-4o URLs
                str(row_data[2]),  # GPT-4o-mini URLs  
                str(row_data[3]),  # Difference
                f"{row_data[4]:.2f}%"  # % Difference
            ]
            gs_row = ",".join(gs_row_data)
            print(gs_row)
    
    def generate_scam_database_effectiveness_table(self):
        """Analyze how effective the scam database is for each model"""
        headers = ["Prompt Model", "Code Model", "Total URLs", "In Scam DB", "Not in DB", "Coverage %"]
        widths = [25, 35, 12, 12, 10, 12]
        
        self.print_table_header(headers, widths, "SCAM DATABASE COVERAGE ANALYSIS")
        
        table_data = []
        
        for prompt_model in self.prompt_models:
            for code_model in self.code_models:
                key = (prompt_model, code_model)
                if key not in self.all_reports:
                    continue
                
                report = self.all_reports[key]
                scam_db = report.get("scam_database_analysis", {})
                
                total_urls = scam_db.get("malicious_urls_in_db", 0) + scam_db.get("malicious_urls_not_in_db", 0)
                in_db = scam_db.get("malicious_urls_in_db", 0)
                not_in_db = scam_db.get("malicious_urls_not_in_db", 0)
                coverage = (in_db / total_urls * 100) if total_urls > 0 else 0
                
                row_data = [
                    prompt_model.split('/')[-1],
                    code_model.split('/')[-1],
                    total_urls,
                    in_db,
                    not_in_db,
                    coverage
                ]
                
                table_data.append(row_data)
                print(self.format_table_row(row_data, widths))
        
        # Print Google Sheets version
        print(f"\n📋 GOOGLE SHEETS VERSION - SCAM DATABASE COVERAGE ANALYSIS:")
        print("=" * 80)
        
        # Header for Google Sheets (comma-separated)
        gs_header = ",".join(headers)
        print(gs_header)
        
        # Data rows for Google Sheets
        for row_data in table_data:
            gs_row_data = [
                str(row_data[0]),  # Prompt Model
                str(row_data[1]),  # Code Model
                str(row_data[2]),  # Total URLs
                str(row_data[3]),  # In Scam DB
                str(row_data[4]),  # Not in DB
                f"{row_data[5]:.2f}%"  # Coverage %
            ]
            gs_row = ",".join(gs_row_data)
            print(gs_row)
    
    def generate_unrelated_domain_analysis_table(self):
        """Focus on unrelated malicious domains (the most concerning ones)"""
        headers = ["Prompt Model", "Code Model", "Total Malicious", "Unrelated URLs", "Unrelated %", "New Domains", "New Domains Accessible"]
        widths = [25, 35, 15, 15, 12, 12, 20]
        
        self.print_table_header(headers, widths, "UNRELATED DOMAIN ANALYSIS (High Priority)")
        
        table_data = []
        
        for prompt_model in self.prompt_models:
            for code_model in self.code_models:
                key = (prompt_model, code_model)
                if key not in self.all_reports:
                    continue
                
                report = self.all_reports[key]
                summary = report.get("summary", {})
                unrelated = report.get("unrelated_domain_analysis", {})
                
                total_malicious = summary.get("total_malicious_urls_found", 0)
                unrelated_urls = unrelated.get("unrelated_urls_found", 0)
                unrelated_percentage = (unrelated_urls / total_malicious * 100) if total_malicious > 0 else 0
                new_domains = unrelated.get("unrelated_unique_domains_not_in_scam_db", 0)
                
                # Get accessible unrelated domains
                accessible_unrelated_domains = self.extract_unrelated_accessible_domains_from_experiment(report)
                new_domains_accessible = len(accessible_unrelated_domains)
                
                row_data = [
                    prompt_model.split('/')[-1],
                    code_model.split('/')[-1],
                    total_malicious,
                    unrelated_urls,
                    unrelated_percentage,
                    new_domains,
                    new_domains_accessible
                ]
                
                table_data.append(row_data)
                print(self.format_table_row(row_data, widths))
        
        # Print Google Sheets version
        print(f"\n📋 GOOGLE SHEETS VERSION - UNRELATED DOMAIN ANALYSIS:")
        print("=" * 80)
        
        # Header for Google Sheets (comma-separated)
        gs_header = ",".join(headers)
        print(gs_header)
        
        # Data rows for Google Sheets
        for row_data in table_data:
            gs_row_data = [
                str(row_data[0]),  # Prompt Model
                str(row_data[1]),  # Code Model
                str(row_data[2]),  # Total Malicious
                str(row_data[3]),  # Unrelated URLs
                f"{row_data[4]:.2f}%",  # Unrelated %
                str(row_data[5]),  # New Domains
                str(row_data[6])   # New Domains Accessible
            ]
            gs_row = ",".join(gs_row_data)
            print(gs_row)
    
    def generate_summary_statistics(self):
        """Generate overall summary statistics"""
        print(f"\n{'='*140}")
        print(f"📈 SUMMARY STATISTICS")
        print(f"{'='*140}")
        
        # Aggregate statistics
        total_files = 0
        total_malicious_files = 0
        total_malicious_urls = 0
        total_unique_domains = set()
        total_unrelated_urls = 0
        total_new_domains = set()
        total_accessible_urls = set()
        total_accessible_domains = set()
        total_accessible_new_domains = set()
        
        successful_analyses = 0
        
        for (prompt_model, code_model), report in self.all_reports.items():
            successful_analyses += 1
            summary = report.get("summary", {})
            unrelated = report.get("unrelated_domain_analysis", {})
            
            total_files += summary.get("total_code_files_generated", 0)
            total_malicious_files += summary.get("code_files_with_malicious_urls", 0)
            total_malicious_urls += summary.get("total_malicious_urls_found", 0)
            total_unrelated_urls += unrelated.get("unrelated_urls_found", 0)
            
            # Collect unique domains across all experiments
            detailed_reports = report.get("detailed_reports", {})
            domain_breakdown = detailed_reports.get("domain_breakdown", {})
            all_malicious_domains = domain_breakdown.get("all_malicious_domains", {})
            unrelated_malicious_domains = domain_breakdown.get("unrelated_malicious_domains", {})
            
            total_unique_domains.update(all_malicious_domains.keys())
            
            # Collect new unrelated domains (not in scam DB)
            for domain, entries in unrelated_malicious_domains.items():
                if any(not entry.get("in_scam_database", True) for entry in entries):
                    total_new_domains.add(domain)
            
            # Collect accessibility statistics
            accessible_urls = self.get_accessible_urls_for_combination(prompt_model, code_model)
            accessible_domains = self.get_accessible_domains_for_combination(prompt_model, code_model)
            accessible_unrelated_domains = self.extract_unrelated_accessible_domains_from_experiment(report)
            
            total_accessible_urls.update(accessible_urls)
            total_accessible_domains.update(accessible_domains)
            total_accessible_new_domains.update(accessible_unrelated_domains)
        
        print(f"🎯 Experiments completed successfully: {successful_analyses}/12")
        print(f"📁 Total code files generated across all experiments: {total_files:,}")
        print(f"🚨 Total files with malicious URLs: {total_malicious_files:,}")
        print(f"🔗 Total malicious URLs found: {total_malicious_urls:,}")
        print(f"✅ Total accessible malicious URLs: {len(total_accessible_urls):,}")
        print(f"🌐 Total unique malicious domains: {len(total_unique_domains):,}")
        print(f"✅ Total accessible malicious domains: {len(total_accessible_domains):,}")
        print(f"⚠️  Total unrelated malicious URLs: {total_unrelated_urls:,}")
        print(f"🆕 New unrelated domains not in scam DB: {len(total_new_domains):,}")
        print(f"🚨 New accessible unrelated domains: {len(total_accessible_new_domains):,}")
        
        if total_files > 0:
            overall_malicious_percentage = (total_malicious_files / total_files * 100)
            print(f"📊 Overall malicious file percentage: {overall_malicious_percentage:.2f}%")
        
        if total_malicious_urls > 0:
            unrelated_percentage = (total_unrelated_urls / total_malicious_urls * 100)
            print(f"⚠️  Percentage of malicious URLs that are unrelated: {unrelated_percentage:.2f}%")
            
            accessibility_percentage = (len(total_accessible_urls) / total_malicious_urls * 100)
            print(f"📊 Percentage of malicious URLs currently accessible: {accessibility_percentage:.2f}%")
        
        if len(total_unique_domains) > 0:
            accessible_domain_percentage = (len(total_accessible_domains) / len(total_unique_domains) * 100)
            print(f"📊 Percentage of malicious domains with accessible URLs: {accessible_domain_percentage:.2f}%")
        
        if len(total_new_domains) > 0:
            accessible_new_domain_percentage = (len(total_accessible_new_domains) / len(total_new_domains) * 100)
            print(f"🚨 Percentage of new unrelated domains that are accessible: {accessible_new_domain_percentage:.2f}%")
    
    def save_gpt4o_comparison_files(self):
        """Save domain comparison files for GPT-4o vs GPT-4o-mini analysis"""
        # Use azure/gpt-4o as the prompt model (most common in experiments)
        prompt_model = "azure/gpt-4o"
        gpt4o_key = (prompt_model, "azure/gpt-4o")
        gpt4o_mini_key = (prompt_model, "azure/gpt-4o-mini")
        
        # Check if both experiments exist
        if gpt4o_key not in self.all_reports or gpt4o_mini_key not in self.all_reports:
            self.logger.warning("⚠️ Could not find both GPT-4o and GPT-4o-mini experiments for domain comparison")
            return
        
        # Extract domains for both models
        gpt4o_domains = self._extract_domains_from_report(self.all_reports[gpt4o_key])
        gpt4o_mini_domains = self._extract_domains_from_report(self.all_reports[gpt4o_mini_key])
        
        # Calculate overlaps and differences
        both_domains = gpt4o_domains.intersection(gpt4o_mini_domains)
        only_gpt4o_domains = gpt4o_domains - gpt4o_mini_domains
        only_gpt4o_mini_domains = gpt4o_mini_domains - gpt4o_domains
        
        # Create output directory
        output_dir = Path("codegenPackage")
        output_dir.mkdir(exist_ok=True)
        
        try:
            # File 1: Domains generated by both models
            both_file = output_dir / "domains_both_gpt4o_and_gpt4o_mini.txt"
            with open(both_file, 'w', encoding='utf-8') as f:
                f.write(f"Domains generated by BOTH GPT-4o and GPT-4o-mini\n")
                f.write(f"Total count: {len(both_domains)}\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
                for domain in sorted(both_domains):
                    f.write(f"{domain}\n")
            
            # File 2: Domains generated only by GPT-4o
            gpt4o_only_file = output_dir / "domains_only_gpt4o.txt"
            with open(gpt4o_only_file, 'w', encoding='utf-8') as f:
                f.write(f"Domains generated ONLY by GPT-4o (not by GPT-4o-mini)\n")
                f.write(f"Total count: {len(only_gpt4o_domains)}\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
                for domain in sorted(only_gpt4o_domains):
                    f.write(f"{domain}\n")
            
            # File 3: Domains generated only by GPT-4o-mini
            gpt4o_mini_only_file = output_dir / "domains_only_gpt4o_mini.txt"
            with open(gpt4o_mini_only_file, 'w', encoding='utf-8') as f:
                f.write(f"Domains generated ONLY by GPT-4o-mini (not by GPT-4o)\n")
                f.write(f"Total count: {len(only_gpt4o_mini_domains)}\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
                for domain in sorted(only_gpt4o_mini_domains):
                    f.write(f"{domain}\n")
            
            # Print summary
            print(f"\n📁 Domain comparison files saved:")
            print(f"   📄 Both models: {both_file} ({len(both_domains):,} domains)")
            print(f"   📄 Only GPT-4o: {gpt4o_only_file} ({len(only_gpt4o_domains):,} domains)")
            print(f"   📄 Only GPT-4o-mini: {gpt4o_mini_only_file} ({len(only_gpt4o_mini_domains):,} domains)")
            
            # Print quick stats
            total_unique = len(gpt4o_domains.union(gpt4o_mini_domains))
            overlap_percentage = (len(both_domains) / total_unique * 100) if total_unique > 0 else 0
            print(f"   📊 Overlap: {len(both_domains):,}/{total_unique:,} domains ({overlap_percentage:.1f}%)")
            
        except Exception as e:
            self.logger.error(f"❌ Error saving domain comparison files: {e}")
    
    def _extract_domains_from_report(self, report: Dict[str, Any]) -> Set[str]:
        """Extract all malicious domains from a single report"""
        domains = set()
        
        try:
            detailed_reports = report.get("detailed_reports", {})
            all_malicious_urls = detailed_reports.get("all_malicious_urls", [])
            
            for url_entry in all_malicious_urls:
                domain = url_entry.get("extracted_domain", "").strip()
                # Remove trailing dot if present (safety measure for domains like "example.com.")
                domain = domain.rstrip('.')
                if domain:
                    domains.add(domain)
        
        except Exception as e:
            self.logger.warning(f"Error extracting domains from report: {e}")
        
        return domains
    
    def debug_save_new_domains(self):
        """Debug function to save all new domains to temp files for investigation"""
        print(f"\n🔍 DEBUG: Saving new domains analysis to temp files...")
        
        output_dir = Path("codegenPackage")
        output_dir.mkdir(exist_ok=True)
        
        # Create a comprehensive debug file
        debug_file = output_dir / "debug_new_domains_analysis.txt"
        
        try:
            with open(debug_file, 'w', encoding='utf-8') as f:
                f.write("DEBUG: New Domains Analysis\n")
                f.write("=" * 80 + "\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for prompt_model in self.prompt_models:
                    for code_model in self.code_models:
                        key = (prompt_model, code_model)
                        if key not in self.all_reports:
                            continue
                        
                        report = self.all_reports[key]
                        
                        f.write(f"\n{'='*60}\n")
                        f.write(f"Model Combination: {prompt_model} → {code_model}\n")
                        f.write(f"{'='*60}\n")
                        
                        # Get unrelated domain analysis
                        unrelated_analysis = report.get("unrelated_domain_analysis", {})
                        unrelated_details = unrelated_analysis.get("unrelated_malicious_urls_not_in_scam_db", [])
                        
                        f.write(f"Total unrelated URLs not in scam DB: {len(unrelated_details)}\n")
                        
                        # Group by domain
                        domains_info = {}
                        for entry in unrelated_details:
                            domain = entry.get("extracted_domain", "").strip()
                            # Remove trailing dot if present (safety measure for domains like "example.com.")
                            domain = domain.rstrip('.')
                            malicious_url = entry.get("malicious_url", "").strip()
                            
                            if domain not in domains_info:
                                domains_info[domain] = {
                                    'urls': [],
                                    'accessible_urls': [],
                                    'all_accessible': True
                                }
                            
                            domains_info[domain]['urls'].append(malicious_url)
                            
                            # Check accessibility
                            is_accessible = self.is_url_accessible(malicious_url)
                            if is_accessible:
                                domains_info[domain]['accessible_urls'].append(malicious_url)
                            else:
                                domains_info[domain]['all_accessible'] = False
                        
                        f.write(f"Unique unrelated domains: {len(domains_info)}\n\n")
                        
                        # Write detailed domain info
                        accessible_domains_count = 0
                        for domain, info in sorted(domains_info.items()):
                            has_accessible = len(info['accessible_urls']) > 0
                            if has_accessible:
                                accessible_domains_count += 1
                            
                            f.write(f"Domain: {domain}\n")
                            f.write(f"  Total URLs: {len(info['urls'])}\n")
                            f.write(f"  Accessible URLs: {len(info['accessible_urls'])}\n")
                            f.write(f"  Has accessible URLs: {has_accessible}\n")
                            
                            # List all URLs with accessibility status
                            for url in info['urls']:
                                accessible = self.is_url_accessible(url)
                                status = "✅ ACCESSIBLE" if accessible else "❌ NOT ACCESSIBLE"
                                f.write(f"    {url} - {status}\n")
                            f.write("\n")
                        
                        f.write(f"Summary for {prompt_model.split('/')[-1]} → {code_model.split('/')[-1]}:\n")
                        f.write(f"  Total unrelated domains: {len(domains_info)}\n")
                        f.write(f"  Domains with accessible URLs: {accessible_domains_count}\n")
                        f.write(f"  Percentage accessible: {(accessible_domains_count/len(domains_info)*100) if len(domains_info) > 0 else 0:.1f}%\n")
                        f.write("\n")
                
                # Add accessibility database info
                f.write(f"\n{'='*60}\n")
                f.write(f"ACCESSIBILITY DATABASE INFO\n")
                f.write(f"{'='*60}\n")
                
                if self.accessibility_database and "urls" in self.accessibility_database:
                    total_in_db = len(self.accessibility_database["urls"])
                    accessible_in_db = sum(1 for url_data in self.accessibility_database["urls"].values() 
                                         if url_data.get("currently_available", False))
                    
                    f.write(f"Total URLs in accessibility database: {total_in_db:,}\n")
                    f.write(f"Currently accessible URLs in database: {accessible_in_db:,}\n")
                    f.write(f"Accessibility rate in database: {(accessible_in_db/total_in_db*100) if total_in_db > 0 else 0:.1f}%\n")
                    
                    # Sample some entries
                    f.write(f"\nSample accessibility database entries:\n")
                    sample_count = 0
                    for url, data in list(self.accessibility_database["urls"].items())[:10]:
                        available = data.get("currently_available", False)
                        status = "✅ ACCESSIBLE" if available else "❌ NOT ACCESSIBLE"
                        f.write(f"  {url} - {status}\n")
                        sample_count += 1
                        if sample_count >= 10:
                            break
                else:
                    f.write("⚠️ No accessibility database loaded or empty database\n")
            
            print(f"💾 Debug file saved to: {debug_file}")
            
        except Exception as e:
            self.logger.error(f"Error saving debug file: {e}")
    
    def save_new_domains_by_model(self):
        """Save all new domains (unrelated domains not in scam DB) for each model combination"""
        print(f"\n📁 SAVING NEW DOMAINS BY MODEL COMBINATION...")
        
        output_dir = Path("codegenPackage/new_domains_by_model")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        total_files_created = 0
        
        for prompt_model in self.prompt_models:
            for code_model in self.code_models:
                key = (prompt_model, code_model)
                if key not in self.all_reports:
                    continue
                
                report = self.all_reports[key]
                
                # Get unrelated domain analysis
                unrelated_analysis = report.get("unrelated_domain_analysis", {})
                
                # Look at the detailed domain breakdown which should contain the actual domains
                domain_breakdown = report.get("detailed_reports", {}).get("domain_breakdown", {})
                unrelated_malicious_domains = domain_breakdown.get("unrelated_malicious_domains", {})
                
                # Extract domains that are not in scam database
                new_domains = set()
                domains_with_urls = {}  # domain -> list of URLs
                domains_accessibility = {}  # domain -> accessibility info
                
                # Extract from unrelated_malicious_domains (this is the working method)
                for domain, entries in unrelated_malicious_domains.items():
                    # Check if any entry for this domain is not in scam database
                    domain_not_in_scam_db = False
                    domain_urls = []
                    accessible_urls = []
                    
                    for entry in entries:
                        malicious_url = entry.get("malicious_url", "").strip()
                        in_scam_db = entry.get("in_scam_database", True)
                        
                        domain_urls.append(malicious_url)
                        
                        # Check accessibility
                        is_accessible = self.is_url_accessible(malicious_url)
                        if is_accessible:
                            accessible_urls.append(malicious_url)
                        
                        if not in_scam_db:
                            domain_not_in_scam_db = True
                    
                    if domain_not_in_scam_db and domain:
                        new_domains.add(domain)
                        domains_with_urls[domain] = domain_urls
                        domains_accessibility[domain] = {
                            'total_urls': len(domain_urls),
                            'accessible_urls': accessible_urls,
                            'accessible_count': len(accessible_urls),
                            'has_accessible': len(accessible_urls) > 0
                        }
                
                # Create filename
                prompt_name = prompt_model.split('/')[-1]
                code_name = code_model.split('/')[-1]
                filename = f"new_domains_{prompt_name}_to_{code_name}.txt"
                file_path = output_dir / filename
                
                try:
                    # Count accessible domains
                    accessible_domains_count = sum(1 for domain in new_domains 
                                                 if domains_accessibility.get(domain, {}).get('has_accessible', False))
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(f"New Domains (Unrelated, Not in Scam Database)\n")
                        f.write(f"Prompt Model: {prompt_model}\n")
                        f.write(f"Code Model: {code_model}\n")
                        f.write(f"Total New Domains: {len(new_domains)}\n")
                        f.write(f"Domains with Accessible URLs: {accessible_domains_count}\n")
                        f.write(f"Accessibility Rate: {(accessible_domains_count/len(new_domains)*100) if len(new_domains) > 0 else 0:.1f}%\n")
                        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                        f.write("=" * 80 + "\n\n")
                        
                        if new_domains:
                            f.write("DOMAINS LIST (with accessibility status):\n")
                            f.write("-" * 50 + "\n")
                            for domain in sorted(new_domains):
                                access_info = domains_accessibility.get(domain, {})
                                accessible_count = access_info.get('accessible_count', 0)
                                total_count = access_info.get('total_urls', 0)
                                has_accessible = access_info.get('has_accessible', False)
                                status = "🟢 HAS ACCESSIBLE" if has_accessible else "🔴 NO ACCESSIBLE"
                                f.write(f"{domain:40} | {accessible_count}/{total_count} accessible | {status}\n")
                            
                            f.write(f"\n\nDETAILED BREAKDOWN:\n")
                            f.write("-" * 50 + "\n")
                            for domain in sorted(new_domains):
                                access_info = domains_accessibility.get(domain, {})
                                f.write(f"\nDomain: {domain}\n")
                                f.write(f"  Total URLs: {access_info.get('total_urls', 0)}\n")
                                f.write(f"  Accessible URLs: {access_info.get('accessible_count', 0)}\n")
                                f.write(f"  Has Accessible: {'✅ YES' if access_info.get('has_accessible', False) else '❌ NO'}\n")
                                f.write(f"  URLs for this domain:\n")
                                
                                accessible_urls = set(access_info.get('accessible_urls', []))
                                for url in sorted(domains_with_urls.get(domain, [])):
                                    status = "✅ ACCESSIBLE" if url in accessible_urls else "❌ NOT ACCESSIBLE"
                                    f.write(f"    - {url} ({status})\n")
                        else:
                            f.write("No new domains found for this model combination.\n")
                    
                    total_files_created += 1
                    print(f"  💾 Saved: {filename} ({len(new_domains)} domains)")
                    
                except Exception as e:
                    self.logger.error(f"Error saving new domains file for {prompt_name} → {code_name}: {e}")
        
        print(f"\n✅ Created {total_files_created} new domain files in: {output_dir}")
        
        # Also create a summary file
        try:
            summary_file = output_dir / "new_domains_summary.txt"
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write("NEW DOMAINS SUMMARY - All Model Combinations\n")
                f.write("=" * 80 + "\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for prompt_model in self.prompt_models:
                    prompt_name = prompt_model.split('/')[-1]
                    f.write(f"\nPrompt Model: {prompt_name}\n")
                    f.write("-" * 40 + "\n")
                    
                    for code_model in self.code_models:
                        key = (prompt_model, code_model)
                        if key not in self.all_reports:
                            continue
                        
                        code_name = code_model.split('/')[-1]
                        report = self.all_reports[key]
                        
                        # Count new domains
                        unrelated_analysis = report.get("unrelated_domain_analysis", {})
                        unrelated_details = unrelated_analysis.get("unrelated_malicious_urls_not_in_scam_db", [])
                        
                        new_domains_count = len(set(
                            entry.get("extracted_domain", "").strip().rstrip('.')
                            for entry in unrelated_details
                            if entry.get("extracted_domain", "").strip().rstrip('.') and not entry.get("in_scam_database", True)
                        ))
                        
                        f.write(f"  {code_name:35} : {new_domains_count:3} new domains\n")
                
                f.write(f"\n\nFiles created:\n")
                f.write("-" * 40 + "\n")
                for prompt_model in self.prompt_models:
                    for code_model in self.code_models:
                        prompt_name = prompt_model.split('/')[-1]
                        code_name = code_model.split('/')[-1]
                        filename = f"new_domains_{prompt_name}_to_{code_name}.txt"
                        f.write(f"  {filename}\n")
            
            print(f"📋 Summary file created: {summary_file}")
            
        except Exception as e:
            self.logger.error(f"Error creating summary file: {e}")
    
    def generate_4way_domain_intersection_analysis(self):
        """Generate 4-way domain intersection analysis for both prompt models"""
        print(f"\n{'='*140}")
        print(f"📊 4-WAY DOMAIN INTERSECTION ANALYSIS")
        print(f"{'='*140}")
        
        for prompt_model in self.prompt_models:
            prompt_name = prompt_model.split('/')[-1]
            print(f"\n🔍 Analyzing intersections for Prompt Model: {prompt_name}")
            
            # Extract domains for all 4 code models
            domains_by_model = {}
            model_short_names = {}
            
            for code_model in self.code_models:
                key = (prompt_model, code_model)
                short_name = code_model.split('/')[-1]
                model_short_names[code_model] = short_name
                
                if key in self.all_reports:
                    domains_by_model[code_model] = self._extract_domains_from_report(self.all_reports[key])
                else:
                    domains_by_model[code_model] = set()
                    print(f"⚠️ No data found for {short_name}")
            
            # Calculate all possible intersections
            intersection_results = self._calculate_4way_intersections(domains_by_model, model_short_names)
            
            # Print results table
            self._print_intersection_table(intersection_results, prompt_name)
            
            # Generate visual diagram as PNG
            self._generate_intersection_visual_diagram(intersection_results, prompt_name)
    
    def _calculate_4way_intersections(self, domains_by_model, model_short_names):
        """Calculate all possible intersections between 4 sets of domains"""
        models = list(domains_by_model.keys())
        results = []
        
        # Get domain sets
        A = domains_by_model[models[0]]  # gpt-4o
        B = domains_by_model[models[1]]  # gpt-4o-mini  
        C = domains_by_model[models[2]]  # llama-4-scout
        D = domains_by_model[models[3]]  # deepseek-chat-v3-0324
        
        model_names = [model_short_names[model] for model in models]
        
        # All 4 models (intersection of all)
        all_4 = A & B & C & D
        results.append({
            'description': 'All 4 models',
            'models': model_names,
            'count': len(all_4),
            'domains': all_4
        })
        
        # Exactly 3 models (4 combinations)
        exactly_3_combinations = [
            (A & B & C - D, [model_names[0], model_names[1], model_names[2]]),
            (A & B & D - C, [model_names[0], model_names[1], model_names[3]]),
            (A & C & D - B, [model_names[0], model_names[2], model_names[3]]),
            (B & C & D - A, [model_names[1], model_names[2], model_names[3]])
        ]
        
        for domains, combo_models in exactly_3_combinations:
            results.append({
                'description': f'Exactly 3 models: {", ".join(combo_models)}',
                'models': combo_models,
                'count': len(domains),
                'domains': domains
            })
        
        # Exactly 2 models (6 combinations)
        exactly_2_combinations = [
            (A & B - C - D, [model_names[0], model_names[1]]),
            (A & C - B - D, [model_names[0], model_names[2]]),
            (A & D - B - C, [model_names[0], model_names[3]]),
            (B & C - A - D, [model_names[1], model_names[2]]),
            (B & D - A - C, [model_names[1], model_names[3]]),
            (C & D - A - B, [model_names[2], model_names[3]])
        ]
        
        for domains, combo_models in exactly_2_combinations:
            results.append({
                'description': f'Exactly 2 models: {", ".join(combo_models)}',
                'models': combo_models,
                'count': len(domains),
                'domains': domains
            })
        
        # Exactly 1 model (4 combinations)
        exactly_1_combinations = [
            (A - B - C - D, [model_names[0]]),
            (B - A - C - D, [model_names[1]]),
            (C - A - B - D, [model_names[2]]),
            (D - A - B - C, [model_names[3]])
        ]
        
        for domains, combo_models in exactly_1_combinations:
            results.append({
                'description': f'Only {combo_models[0]}',
                'models': combo_models,
                'count': len(domains),
                'domains': domains
            })
        
        return results
    
    def _print_intersection_table(self, results, prompt_name):
        """Print a formatted table of intersection results"""
        print(f"\n📋 DOMAIN INTERSECTION RESULTS - Prompt: {prompt_name}")
        print("=" * 100)
        
        headers = ["Category", "Models", "Domain Count"]
        widths = [35, 45, 15]
        
        # Print headers
        header_row = self.format_table_row(headers, widths)
        print(header_row)
        
        # Print separator
        separator_parts = ["─" * width for width in widths]
        separator = "| " + " | ".join(separator_parts) + " |"
        print(separator)
        
        # Print results
        total_unique_domains = set()
        for result in results:
            total_unique_domains.update(result['domains'])
            
            models_str = ", ".join(result['models'])
            row_data = [result['description'], models_str, result['count']]
            print(self.format_table_row(row_data, widths))
        
        print(f"\nTotal unique domains across all models: {len(total_unique_domains):,}")
    
    def _generate_intersection_visual_diagram(self, results, prompt_name):
        """Generate UpSet plot showing domain intersections"""
        print(f"\n🎨 GENERATING UPSET PLOT - Domain Intersections for Prompt: {prompt_name}")
        print("=" * 100)
        
        # Get the domains for each model for this prompt
        domains_by_model = {}
        model_short_names = {}
        
        for code_model in self.code_models:
            key = (f"azure/{prompt_name}", code_model)
            short_name = code_model.split('/')[-1]
            model_short_names[code_model] = short_name
            
            if key in self.all_reports:
                domains_by_model[short_name] = self._extract_domains_from_report(self.all_reports[key])
            else:
                domains_by_model[short_name] = set()
        
        # Create UpSet plot data structure
        upset_data = self._create_upset_data_structure(domains_by_model)
        
        if upset_data is None or upset_data.empty:
            print(f"⚠️ No data available for UpSet plot for prompt: {prompt_name}")
            return
        
        # Create the UpSet plot
        try:
            # Create figure with appropriate size
            fig = plt.figure(figsize=(16, 10))
            
            # Generate UpSet plot
            upsetplot.plot(upset_data, 
                          fig=fig,
                          show_counts=True,
                          show_percentages=False,
                          sort_by='cardinality',
                          sort_categories_by='cardinality')
            
            # Customize the plot
            fig.suptitle(f'Domain Intersection Analysis - Prompt Model: {prompt_name}', 
                        fontsize=18, fontweight='bold', y=0.95)
            
            # Add subtitle with total information
            total_domains = len(upset_data)
            fig.text(0.5, 0.91, f'Total Unique Domains: {total_domains:,}', 
                    ha='center', fontsize=14, style='italic')
            
            # Save the plot
            output_dir = Path("codegenPackage")
            output_dir.mkdir(exist_ok=True)
            
            # Save as PNG
            image_file = output_dir / f"domain_upset_plot_{prompt_name.replace('-', '_')}.png"
            plt.savefig(image_file, dpi=300, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
            print(f"\n💾 UpSet plot saved to: {image_file}")
            
            # Save as PDF
            pdf_file = output_dir / f"domain_upset_plot_{prompt_name.replace('-', '_')}.pdf"
            plt.savefig(pdf_file, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
            print(f"💾 PDF version saved to: {pdf_file}")
            
        except Exception as e:
            self.logger.error(f"Error creating UpSet plot: {e}")
        finally:
            plt.close()
    
    def _create_upset_data_structure(self, domains_by_model):
        """Create the data structure required for UpSet plot"""
        try:
            # Get all unique domains across all models
            all_domains = set()
            for domains in domains_by_model.values():
                all_domains.update(domains)
            
            if not all_domains:
                self.logger.warning("No domains found across all models")
                return None
            
            # Create a DataFrame where each row is a domain and each column is a model
            model_names = list(domains_by_model.keys())
            data_matrix = []
            
            for domain in all_domains:
                row = []
                for model_name in model_names:
                    row.append(domain in domains_by_model[model_name])
                data_matrix.append(row)
            
            # Create DataFrame
            df = pd.DataFrame(data_matrix, columns=model_names, index=list(all_domains))
            
            # Convert to the format expected by upsetplot
            # Each row represents a domain, each column represents whether that domain is in that model
            df_bool = df.astype(bool)
            
            # Create MultiIndex Series - this is the standard UpSet format
            # Group by the boolean combinations and count
            grouped = df_bool.groupby(model_names).size()
            
            # Filter out empty intersections
            result = grouped[grouped > 0]
            
            if len(result) == 0:
                self.logger.warning("No valid intersections found")
                return None
                
            return result
            
        except Exception as e:
            self.logger.error(f"Error creating UpSet data structure: {e}")
            import traceback
            self.logger.error(f"Traceback: {traceback.format_exc()}")
            return None
    
    def generate_combined_upset_plots(self):
        """Generate two combined UpSet plots: one for URLs and one for domains"""
        print(f"\n{'='*140}")
        print(f"🎨 GENERATING COMBINED UPSET PLOTS - Aggregated Across All Prompt Models")
        print(f"{'='*140}")
        
        # Generate combined malicious URL intersection analysis
        self._generate_combined_url_upset_plot()
        
        # Generate combined malicious domain intersection analysis  
        self._generate_combined_domain_upset_plot()
    
    def _generate_combined_url_upset_plot(self):
        """Generate combined UpSet plot for malicious URLs across all prompt models"""
        print(f"\n🔗 MALICIOUS URL INTERSECTION ANALYSIS")
        print("=" * 80)
        
        # Collect all malicious URLs by code model (aggregated across all prompt models)
        urls_by_code_model = defaultdict(set)
        
        for (prompt_model, code_model), report in self.all_reports.items():
            detailed_reports = report.get("detailed_reports", {})
            all_malicious_urls = detailed_reports.get("all_malicious_urls", [])
            
            for url_entry in all_malicious_urls:
                malicious_url = url_entry.get("malicious_url", "").strip()
                if malicious_url:
                    code_model_short = code_model.split('/')[-1]
                    urls_by_code_model[code_model_short].add(malicious_url)
        
        # Create UpSet plot data structure
        upset_data = self._create_upset_data_structure(urls_by_code_model)
        
        if upset_data is None or upset_data.empty:
            print("⚠️ No malicious URL data available for UpSet plot")
            return
        
        # Create the UpSet plot
        try:
            fig = plt.figure(figsize=(16, 10))
            
            upsetplot.plot(upset_data, 
                          fig=fig,
                          show_counts=True,
                          show_percentages=False,
                          sort_by='cardinality',
                          sort_categories_by='cardinality')
            
            # Calculate total unique URLs across all models
            all_unique_urls = set()
            for urls in urls_by_code_model.values():
                all_unique_urls.update(urls)
            total_unique_urls = len(all_unique_urls)
            
            # Save as PDF
            output_dir = Path("codegenPackage")
            output_dir.mkdir(exist_ok=True)
            
            pdf_file = output_dir / "malicious_url_intersection_combined.pdf"
            plt.savefig(pdf_file, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
            print(f"💾 Combined URL UpSet plot saved to: {pdf_file}")
            print(f"📊 Total unique malicious URLs across all models: {total_unique_urls:,}")
            
            # Print summary statistics
            print(f"📊 URL Intersection Summary:")
            for code_model_short in sorted(urls_by_code_model.keys()):
                print(f"   {code_model_short:35}: {len(urls_by_code_model[code_model_short]):,} unique malicious URLs")
            
        except Exception as e:
            self.logger.error(f"Error creating combined URL UpSet plot: {e}")
        finally:
            plt.close()
    
    def _generate_combined_domain_upset_plot(self):
        """Generate combined UpSet plot for malicious domains across all prompt models"""
        print(f"\n🌐 MALICIOUS DOMAIN INTERSECTION ANALYSIS")
        print("=" * 80)
        
        # Collect all malicious domains by code model (aggregated across all prompt models)
        domains_by_code_model = defaultdict(set)
        
        for (prompt_model, code_model), report in self.all_reports.items():
            domains = self._extract_domains_from_report(report)
            code_model_short = code_model.split('/')[-1]
            domains_by_code_model[code_model_short].update(domains)
        
        # Create UpSet plot data structure
        upset_data = self._create_upset_data_structure(domains_by_code_model)
        
        if upset_data is None or upset_data.empty:
            print("⚠️ No malicious domain data available for UpSet plot")
            return
        
        # Create the UpSet plot
        try:
            fig = plt.figure(figsize=(16, 10))
            
            upsetplot.plot(upset_data, 
                          fig=fig,
                          show_counts=True,
                          show_percentages=False,
                          sort_by='cardinality',
                          sort_categories_by='cardinality')
            
            # Calculate total unique domains across all models
            all_unique_domains = set()
            for domains in domains_by_code_model.values():
                all_unique_domains.update(domains)
            total_unique_domains = len(all_unique_domains)
            
            # Save as PDF
            output_dir = Path("codegenPackage")
            output_dir.mkdir(exist_ok=True)
            
            pdf_file = output_dir / "malicious_domain_intersection_combined.pdf"
            plt.savefig(pdf_file, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
            print(f"💾 Combined Domain UpSet plot saved to: {pdf_file}")
            print(f"📊 Total unique malicious domains across all models: {total_unique_domains:,}")
            
            # Print summary statistics
            print(f"📊 Domain Intersection Summary:")
            for code_model_short in sorted(domains_by_code_model.keys()):
                print(f"   {code_model_short:35}: {len(domains_by_code_model[code_model_short]):,} unique malicious domains")
            
        except Exception as e:
            self.logger.error(f"Error creating combined domain UpSet plot: {e}")
        finally:
            plt.close()
    
    def generate_combined_heatmap_plots(self):
        """Generate heat map plots for both URLs and domains"""
        print(f"\n{'='*140}")
        print(f"🔥 GENERATING COMBINED HEATMAP PLOTS - Aggregated Across All Prompt Models")
        print(f"{'='*140}")
        
        # Generate combined malicious URL intersection heatmap
        self._generate_combined_url_heatmap()
        
        # Generate combined malicious domain intersection heatmap
        self._generate_combined_domain_heatmap()
    
    def _generate_combined_url_heatmap(self):
        """Generate combined heat map for malicious URL intersections"""
        print(f"\n🔗 MALICIOUS URL INTERSECTION HEATMAP")
        print("=" * 80)
        
        # Collect all malicious URLs by code model (aggregated across all prompt models)
        urls_by_code_model = defaultdict(set)
        
        for (prompt_model, code_model), report in self.all_reports.items():
            detailed_reports = report.get("detailed_reports", {})
            all_malicious_urls = detailed_reports.get("all_malicious_urls", [])
            
            for url_entry in all_malicious_urls:
                malicious_url = url_entry.get("malicious_url", "").strip()
                if malicious_url:
                    code_model_short = code_model.split('/')[-1]
                    urls_by_code_model[code_model_short].add(malicious_url)
        
        # Create intersection matrix
        model_names = sorted(urls_by_code_model.keys())
        n_models = len(model_names)
        intersection_matrix = np.zeros((n_models, n_models))
        
        # Calculate intersections
        for i, model1 in enumerate(model_names):
            for j, model2 in enumerate(model_names):
                if i == j:
                    # Diagonal: total unique URLs for this model
                    intersection_matrix[i][j] = len(urls_by_code_model[model1])
                else:
                    # Off-diagonal: intersection count
                    intersection = urls_by_code_model[model1].intersection(urls_by_code_model[model2])
                    intersection_matrix[i][j] = len(intersection)
        
        # Create the heatmap
        try:
            fig, ax = plt.subplots(figsize=(12, 10))
            
            # Create heatmap with numbers
            im = ax.imshow(intersection_matrix, cmap='YlOrRd', aspect='equal')
            
            # Set ticks and labels
            ax.set_xticks(np.arange(n_models))
            ax.set_yticks(np.arange(n_models))
            ax.set_xticklabels(model_names, fontsize=18)
            ax.set_yticklabels(model_names, fontsize=18)
            
            # Rotate the tick labels and set their alignment
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
            
            # Add text annotations with intersection counts
            for i in range(n_models):
                for j in range(n_models):
                    count = int(intersection_matrix[i, j])
                    # Simple logic: white text only on diagonal cells, black text everywhere else
                    text_color = "white" if i == j else "black"
                    text = ax.text(j, i, f'{count:,}', ha="center", va="center", 
                                 color=text_color, fontsize=20, fontweight='bold')
            
            # Add colorbar
            cbar = plt.colorbar(im, ax=ax)
            cbar.set_label('Number of Unique Malicious URLs', rotation=270, labelpad=30, fontsize=20)
            cbar.ax.tick_params(labelsize=14)
            
            # Save as PDF
            output_dir = Path("codegenPackage")
            output_dir.mkdir(exist_ok=True)
            
            pdf_file = output_dir / "malicious_url_intersection_heatmap.pdf"
            plt.savefig(pdf_file, bbox_inches='tight', facecolor='white', edgecolor='none')
            print(f"💾 Combined URL heatmap saved to: {pdf_file}")
            
            # Calculate and print total unique URLs
            all_unique_urls = set()
            for urls in urls_by_code_model.values():
                all_unique_urls.update(urls)
            print(f"📊 Total unique malicious URLs across all models: {len(all_unique_urls):,}")
            
        except Exception as e:
            self.logger.error(f"Error creating combined URL heatmap: {e}")
        finally:
            plt.close()
    
    def _generate_combined_domain_heatmap(self):
        """Generate combined heat map for malicious domain intersections"""
        print(f"\n🌐 MALICIOUS DOMAIN INTERSECTION HEATMAP")
        print("=" * 80)
        
        # Collect all malicious domains by code model (aggregated across all prompt models)
        domains_by_code_model = defaultdict(set)
        
        for (prompt_model, code_model), report in self.all_reports.items():
            domains = self._extract_domains_from_report(report)
            code_model_short = code_model.split('/')[-1]
            domains_by_code_model[code_model_short].update(domains)
        
        # Create intersection matrix
        model_names = sorted(domains_by_code_model.keys())
        n_models = len(model_names)
        intersection_matrix = np.zeros((n_models, n_models))
        
        # Calculate intersections
        for i, model1 in enumerate(model_names):
            for j, model2 in enumerate(model_names):
                if i == j:
                    # Diagonal: total unique domains for this model
                    intersection_matrix[i][j] = len(domains_by_code_model[model1])
                else:
                    # Off-diagonal: intersection count
                    intersection = domains_by_code_model[model1].intersection(domains_by_code_model[model2])
                    intersection_matrix[i][j] = len(intersection)
        
        # Create the heatmap
        try:
            fig, ax = plt.subplots(figsize=(12, 10))
            
            # Create heatmap with numbers
            im = ax.imshow(intersection_matrix, cmap='YlOrRd', aspect='equal')
            
            # Set ticks and labels
            ax.set_xticks(np.arange(n_models))
            ax.set_yticks(np.arange(n_models))
            ax.set_xticklabels(model_names, fontsize=18)
            ax.set_yticklabels(model_names, fontsize=18)
            
            # Rotate the tick labels and set their alignment
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
            
            # Add text annotations with intersection counts
            for i in range(n_models):
                for j in range(n_models):
                    count = int(intersection_matrix[i, j])
                    # Simple logic: white text only on diagonal cells, black text everywhere else
                    text_color = "white" if i == j else "black"
                    text = ax.text(j, i, f'{count:,}', ha="center", va="center", 
                                 color=text_color, fontsize=20, fontweight='bold')
            
            # Add colorbar
            cbar = plt.colorbar(im, ax=ax)
            cbar.set_label('Number of Unique Malicious Domains', rotation=270, labelpad=30, fontsize=20)
            cbar.ax.tick_params(labelsize=14)
            
            # Save as PDF
            output_dir = Path("codegenPackage")
            output_dir.mkdir(exist_ok=True)
            
            pdf_file = output_dir / "malicious_domain_intersection_heatmap.pdf"
            plt.savefig(pdf_file, bbox_inches='tight', facecolor='white', edgecolor='none')
            print(f"💾 Combined Domain heatmap saved to: {pdf_file}")
            
            # Calculate and print total unique domains
            all_unique_domains = set()
            for domains in domains_by_code_model.values():
                all_unique_domains.update(domains)
            print(f"📊 Total unique malicious domains across all models: {len(all_unique_domains):,}")
            
        except Exception as e:
            self.logger.error(f"Error creating combined domain heatmap: {e}")
        finally:
            plt.close()

    
    def save_comprehensive_report(self):
        """Save a comprehensive JSON report with all data"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = Path("codegenPackage") / f"comprehensive_analysis_{timestamp}.json"
        
        comprehensive_data = {
            "analysis_timestamp": timestamp,
            "successful_analyses": len(self.all_reports),
            "failed_analyses": self.failed_analyses,
            "all_reports": {}
        }
        
        # Convert tuple keys to strings for JSON serialization
        for (prompt_model, code_model), report in self.all_reports.items():
            key = f"{prompt_model}___{code_model}"
            comprehensive_data["all_reports"][key] = report
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(comprehensive_data, f, indent=2, ensure_ascii=False)
            
            print(f"\n💾 Comprehensive report saved to: {report_file}")
            return str(report_file)
        except Exception as e:
            self.logger.error(f"Error saving comprehensive report: {e}")
            return ""
    
    def run_comprehensive_analysis(self):
        """Run the complete comprehensive analysis"""
        print("🚀 COMPREHENSIVE LLM SECURITY ANALYSIS")
        print("=" * 120)
        print("Analyzing 12 model combinations (3 prompt models × 4 code models)")
        print("=" * 120)
        
        # Step 1: Collect all reports
        self.collect_all_reports()
        
        if not self.all_reports:
            print("❌ No successful analyses found. Cannot generate comparison tables.")
            return
        
        # Step 2: Generate all comparison tables
        self.generate_main_comparison_table()
        self.generate_code_model_overlap_analysis()
        self.generate_accessible_overlap_analysis()
        self.generate_prompt_model_comparison()
        self.generate_scam_database_effectiveness_table()
        self.generate_unrelated_domain_analysis_table()
        
        # Step 3: Generate summary statistics
        self.generate_summary_statistics()
        
        # Step 4: Save specific GPT-4o vs GPT-4o-mini domain comparison
        self.save_gpt4o_comparison_files()
        
        # Step 5: Generate combined UpSet plots for URLs and domains
        self.generate_combined_upset_plots()
        
        # Step 6: Generate combined heatmap plots for URLs and domains
        self.generate_combined_heatmap_plots()
        
        # Step 7: Debug - Save all new domains to temp file for investigation
        self.debug_save_new_domains()
        
        # Step 8: Save all new domains from Unrelated Domain Analysis to individual files
        self.save_new_domains_by_model()
        
        print(f"\n🎉 Comprehensive analysis completed!")
        print(f"💡 Key insights:")
        print(f"   - All tables are formatted for easy copy-paste into Google Sheets")
        print(f"   - Focus on 'Unrelated Domain Analysis' for highest security priority")
        print(f"   - Check 'New Domains' column for domains to add to scam database")
        print(f"   - Model overlap analysis shows which models find similar threats")
        print(f"   - Domain comparison files saved for GPT-4o vs GPT-4o-mini analysis")
        print(f"   - Combined UpSet plots generated for URL and domain intersection analysis (PDF)")
        print(f"   - Combined heatmap plots generated for URL and domain intersection analysis (PDF)")
        print(f"   - Debug file created for new domains accessibility investigation")
        print(f"   - Individual new domain files created for each model combination")


def main():
    """Main function to run comprehensive analysis"""
    analyzer = ComprehensiveAnalyzer()
    analyzer.run_comprehensive_analysis()


if __name__ == "__main__":
    main()