#!/usr/bin/env python3
"""
Script to analyze URLs that are memorized but not in scam database.
"""

import json
import os
from urllib.parse import urlparse
from collections import defaultdict
import glob

def extract_domain(url):
    """Extract domain from URL"""
    try:
        parsed = urlparse(url)
        return parsed.netloc.lower()
    except:
        return None

def load_memorized_urls(verification_report_path):
    """Load URLs that are marked as memorized from the verification report"""
    print(f"Loading memorized URLs from: {verification_report_path}")
    memorized_urls = set()
    
    with open(verification_report_path, 'r') as f:
        data = json.load(f)
    
    for url, url_data in data.get('urls', {}).items():
        classification = url_data.get('classification', {})
        if classification.get('is_memorized', False):
            memorized_urls.add(url)
    
    print(f"Found {len(memorized_urls)} memorized URLs")
    return memorized_urls

def load_scam_database_status(analysis_reports_dir):
    """Load scam database status for all malicious URLs from analysis reports"""
    print(f"Loading scam database status from: {analysis_reports_dir}")
    url_scam_status = {}
    
    # Find all analysis report files
    pattern = os.path.join(analysis_reports_dir, "analysis_report_*.json")
    report_files = glob.glob(pattern)
    
    print(f"Found {len(report_files)} analysis report files")
    
    for report_file in report_files:
        print(f"Processing: {os.path.basename(report_file)}")
        try:
            with open(report_file, 'r') as f:
                data = json.load(f)
            
            # Look for detailed_reports section
            detailed_reports = data.get('detailed_reports', {})
            
            # Get malicious URLs from all_malicious_urls section
            malicious_data = detailed_reports.get('all_malicious_urls', [])
            
            for entry in malicious_data:
                if isinstance(entry, dict):
                    malicious_url = entry.get('malicious_url')
                    in_scam_db = entry.get('in_scam_database', False)
                    
                    if malicious_url:
                        url_scam_status[malicious_url] = in_scam_db
        
        except Exception as e:
            print(f"Error processing {report_file}: {e}")
    
    print(f"Loaded scam database status for {len(url_scam_status)} URLs")
    return url_scam_status

def analyze_and_group_urls(memorized_urls, url_scam_status):
    """Find URLs that are memorized but not in scam database, grouped by domain"""
    print("Analyzing URLs...")
    
    # Find URLs that are memorized but not in scam database
    target_urls = []
    
    for url in memorized_urls:
        # Check if this URL has scam database information
        if url in url_scam_status:
            is_in_scam_db = url_scam_status[url]
            if not is_in_scam_db:  # Not in scam database
                target_urls.append(url)
        else:
            # If no scam database info, we might want to include it
            # but let's be conservative and only include URLs we have info for
            pass
    
    print(f"Found {len(target_urls)} URLs that are memorized but not in scam database")
    
    # Group by domain
    domain_groups = defaultdict(list)
    
    for url in target_urls:
        domain = extract_domain(url)
        if domain:
            domain_groups[domain].append({
                'url': url,
                'is_memorized': True,
                'in_scam_database': False
            })
    
    return dict(domain_groups)

def create_report(domain_groups, output_path):
    """Create the final JSON report"""
    print(f"Creating report at: {output_path}")
    
    # Calculate statistics
    total_urls = sum(len(urls) for urls in domain_groups.values())
    total_domains = len(domain_groups)
    
    report = {
        "analysis_timestamp": "2025-01-23T00:00:00",
        "description": "URLs that are memorized (found in DNS history/archives) but not in scam database",
        "criteria": {
            "memorized": "URL found in DNS history or certificate transparency logs",
            "not_in_scam_database": "URL not flagged in scam database"
        },
        "summary": {
            "total_domains": total_domains,
            "total_urls": total_urls,
            "domains_with_multiple_urls": sum(1 for urls in domain_groups.values() if len(urls) > 1)
        },
        "domains": {}
    }
    
    # Sort domains by number of URLs (descending)
    sorted_domains = sorted(domain_groups.items(), key=lambda x: len(x[1]), reverse=True)
    
    for domain, urls in sorted_domains:
        report["domains"][domain] = {
            "domain": domain,
            "url_count": len(urls),
            "urls": sorted(urls, key=lambda x: x['url'])
        }
    
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Report created successfully!")
    print(f"Total domains: {total_domains}")
    print(f"Total URLs: {total_urls}")
    
    return report

def main():
    # Paths
    verification_report_path = "/home/fanlgrp/Documents/zhiychen/LLM-poison/url_verification_experiment/results/optimized_url_verification_report_20250813_184836.json"
    analysis_reports_dir = "/home/fanlgrp/Documents/zhiychen/LLM-poison/codegenPackage"
    output_path = "/home/fanlgrp/Documents/zhiychen/LLM-poison/memorized_urls_analysis/memorized_non_scam_urls_report.json"
    
    # Step 1: Load memorized URLs
    memorized_urls = load_memorized_urls(verification_report_path)
    
    # Step 2: Load scam database status
    url_scam_status = load_scam_database_status(analysis_reports_dir)
    
    # Step 3: Analyze and group URLs
    domain_groups = analyze_and_group_urls(memorized_urls, url_scam_status)
    
    # Step 4: Create report
    report = create_report(domain_groups, output_path)
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
