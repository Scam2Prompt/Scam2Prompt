#!/usr/bin/env python3
"""
Script to analyze malicious domains and URLs from the extracted data
"""

import json
import csv
from collections import Counter, defaultdict
from urllib.parse import urlparse
import re

def load_malicious_urls():
    """Load the extracted malicious URLs data"""
    with open('all_malicious_urls.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_domains(malicious_urls):
    """Analyze domain patterns and statistics"""
    domain_stats = Counter()
    original_domain_stats = Counter()
    model_stats = defaultdict(int)
    confidence_stats = defaultdict(int)
    detector_stats = Counter()
    scam_db_stats = {'in_scam_db': 0, 'not_in_scam_db': 0}
    
    for url_data in malicious_urls:
        # Extract domains
        malicious_domain = url_data.get('extracted_domain', '')
        if malicious_domain:
            domain_stats[malicious_domain] += 1
        
        # Original URL domain
        original_url = url_data.get('original_url', '')
        if original_url:
            original_domain = urlparse(original_url).netloc
            original_domain_stats[original_domain] += 1
        
        # Model statistics
        model = url_data.get('model_identifier', 'unknown')
        model_stats[model] += 1
        
        # Confidence statistics
        confidence = url_data.get('confidence', 0)
        confidence_range = f"{confidence:.1f}"
        confidence_stats[confidence_range] += 1
        
        # Detector statistics
        detectors = url_data.get('detectors', [])
        for detector in detectors:
            detector_stats[detector] += 1
        
        # Scam database statistics
        if url_data.get('in_scam_database', False):
            scam_db_stats['in_scam_db'] += 1
        else:
            scam_db_stats['not_in_scam_db'] += 1
    
    return {
        'malicious_domains': domain_stats,
        'original_domains': original_domain_stats,
        'model_stats': dict(model_stats),
        'confidence_stats': dict(confidence_stats),
        'detector_stats': dict(detector_stats),
        'scam_db_stats': scam_db_stats
    }

def save_domain_analysis(analysis):
    """Save domain analysis to files"""
    
    # Save top malicious domains
    with open('top_malicious_domains.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['domain', 'count', 'percentage'])
        total = sum(analysis['malicious_domains'].values())
        for domain, count in analysis['malicious_domains'].most_common(100):
            percentage = (count / total) * 100
            writer.writerow([domain, count, f"{percentage:.2f}%"])
    
    # Save top original domains
    with open('top_original_domains.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['original_domain', 'count', 'percentage'])
        total = sum(analysis['original_domains'].values())
        for domain, count in analysis['original_domains'].most_common(50):
            percentage = (count / total) * 100
            writer.writerow([domain, count, f"{percentage:.2f}%"])
    
    # Save complete analysis
    with open('domain_analysis.json', 'w', encoding='utf-8') as f:
        # Convert Counter objects to regular dicts for JSON serialization
        serializable_analysis = {}
        for key, value in analysis.items():
            if isinstance(value, Counter):
                serializable_analysis[key] = dict(value)
            else:
                serializable_analysis[key] = value
        json.dump(serializable_analysis, f, indent=2, ensure_ascii=False)

def create_model_comparison_report(malicious_urls):
    """Create a detailed comparison report by model"""
    model_data = defaultdict(lambda: {
        'total_urls': 0,
        'unique_domains': set(),
        'confidence_distribution': Counter(),
        'scam_db_count': 0,
        'detectors_used': Counter()
    })
    
    for url_data in malicious_urls:
        model = url_data.get('model_identifier', 'unknown')
        
        model_data[model]['total_urls'] += 1
        
        domain = url_data.get('extracted_domain', '')
        if domain:
            model_data[model]['unique_domains'].add(domain)
        
        confidence = url_data.get('confidence', 0)
        model_data[model]['confidence_distribution'][f"{confidence:.1f}"] += 1
        
        if url_data.get('in_scam_database', False):
            model_data[model]['scam_db_count'] += 1
        
        detectors = url_data.get('detectors', [])
        for detector in detectors:
            model_data[model]['detectors_used'][detector] += 1
    
    # Convert to serializable format
    model_report = {}
    for model, data in model_data.items():
        model_report[model] = {
            'total_urls': data['total_urls'],
            'unique_domains_count': len(data['unique_domains']),
            'unique_domains': sorted(list(data['unique_domains'])),
            'confidence_distribution': dict(data['confidence_distribution']),
            'scam_db_count': data['scam_db_count'],
            'scam_db_percentage': (data['scam_db_count'] / data['total_urls']) * 100 if data['total_urls'] > 0 else 0,
            'detectors_used': dict(data['detectors_used'])
        }
    
    with open('model_comparison_report.json', 'w', encoding='utf-8') as f:
        json.dump(model_report, f, indent=2, ensure_ascii=False)
    
    return model_report

def main():
    print("Loading malicious URLs data...")
    malicious_urls = load_malicious_urls()
    print(f"Loaded {len(malicious_urls)} malicious URLs")
    
    print("\nAnalyzing domains and statistics...")
    analysis = analyze_domains(malicious_urls)
    
    print("\nSaving domain analysis...")
    save_domain_analysis(analysis)
    
    print("\nCreating model comparison report...")
    model_report = create_model_comparison_report(malicious_urls)
    
    print("\n=== ANALYSIS COMPLETE ===")
    print(f"Total malicious URLs: {len(malicious_urls)}")
    print(f"Unique malicious domains: {len(analysis['malicious_domains'])}")
    print(f"Unique original domains: {len(analysis['original_domains'])}")
    print(f"Models analyzed: {len(analysis['model_stats'])}")
    
    print("\nTop 10 malicious domains:")
    for domain, count in analysis['malicious_domains'].most_common(10):
        print(f"  {domain}: {count}")
    
    print("\nModel statistics:")
    for model, count in analysis['model_stats'].items():
        print(f"  {model}: {count}")
    
    print("\nFiles created:")
    print("  - domain_analysis.json (complete analysis)")
    print("  - top_malicious_domains.csv (top 100 malicious domains)")
    print("  - top_original_domains.csv (top 50 original domains)")
    print("  - model_comparison_report.json (detailed model comparison)")

if __name__ == "__main__":
    main()
