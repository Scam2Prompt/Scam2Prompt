#!/usr/bin/env python3
"""
Script to extract all_malicious_urls data from analysis report JSON files
"""

import json
import os
import glob
from typing import Dict, List, Any
from datetime import datetime

def extract_malicious_urls_from_file(file_path: str) -> Dict[str, Any]:
    """Extract malicious URLs data from a single analysis report file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Navigate to detailed_reports.all_malicious_urls
        malicious_urls = data.get('detailed_reports', {}).get('all_malicious_urls', [])
        
        return {
            'file_path': file_path,
            'file_name': os.path.basename(file_path),
            'malicious_urls': malicious_urls,
            'count': len(malicious_urls)
        }
    except Exception as e:
        return {
            'file_path': file_path,
            'file_name': os.path.basename(file_path),
            'error': str(e),
            'malicious_urls': [],
            'count': 0
        }

def main():
    # Find all analysis report JSON files in codegenPackage directory (no subdirectories)
    pattern = "codegenPackage/analysis_report_*.json"
    json_files = glob.glob(pattern)
    
    print(f"Found {len(json_files)} analysis report files:")
    for file in sorted(json_files):
        print(f"  - {file}")
    
    # Extract malicious URLs from each file
    all_extractions = []
    total_malicious_urls = 0
    
    for file_path in sorted(json_files):
        print(f"\nProcessing: {file_path}")
        extraction = extract_malicious_urls_from_file(file_path)
        all_extractions.append(extraction)
        
        if 'error' in extraction:
            print(f"  ERROR: {extraction['error']}")
        else:
            print(f"  Found {extraction['count']} malicious URLs")
            total_malicious_urls += extraction['count']
    
    # Create summary report
    summary = {
        'timestamp': datetime.now().isoformat(),
        'total_files_processed': len(json_files),
        'total_malicious_urls': total_malicious_urls,
        'files': all_extractions
    }
    
    # Save summary report
    summary_file = 'summary_report.json'
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"\n=== SUMMARY ===")
    print(f"Total files processed: {len(json_files)}")
    print(f"Total malicious URLs found: {total_malicious_urls}")
    print(f"Summary report saved to: {summary_file}")
    
    # Save all malicious URLs in a flat list
    all_urls = []
    for extraction in all_extractions:
        for url_data in extraction['malicious_urls']:
            # Add source file info to each URL entry
            url_data_with_source = url_data.copy()
            url_data_with_source['source_file'] = extraction['file_name']
            all_urls.append(url_data_with_source)
    
    flat_urls_file = 'all_malicious_urls.json'
    with open(flat_urls_file, 'w', encoding='utf-8') as f:
        json.dump(all_urls, f, indent=2, ensure_ascii=False)
    
    print(f"All malicious URLs saved to: {flat_urls_file}")
    
    # Create a CSV for easier analysis
    csv_file = 'malicious_urls.csv'
    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write("source_file,original_url,malicious_url,extracted_domain,confidence,model_identifier,batch_id,in_scam_database,detectors,prompt\n")
        for url_data in all_urls:
            detectors = "|".join(url_data.get('detectors', []))
            prompt = url_data.get('prompt', '').replace('"', '""').replace('\n', ' ')
            f.write(f'"{url_data.get("source_file", "")}","{url_data.get("original_url", "")}","{url_data.get("malicious_url", "")}","{url_data.get("extracted_domain", "")}",{url_data.get("confidence", "")},"{url_data.get("model_identifier", "")}","{url_data.get("batch_id", "")}",{url_data.get("in_scam_database", "")},"{detectors}","{prompt}"\n')
    
    print(f"CSV export saved to: {csv_file}")

if __name__ == "__main__":
    main()
