#!/usr/bin/env python3
"""
Create a summary report of the memorized URLs analysis.
"""

import json
from collections import Counter

def create_summary_report():
    # Load the main report
    with open('/home/fanlgrp/Documents/zhiychen/LLM-poison/memorized_urls_analysis/memorized_non_scam_urls_report.json', 'r') as f:
        data = json.load(f)
    
    domains = data['domains']
    
    # Create summary statistics
    domain_url_counts = [domain_data['url_count'] for domain_data in domains.values()]
    url_count_distribution = Counter(domain_url_counts)
    
    # Top domains by URL count
    top_domains = sorted(domains.items(), key=lambda x: x[1]['url_count'], reverse=True)[:20]
    
    # Create summary
    summary = {
        "analysis_summary": {
            "total_domains": data['summary']['total_domains'],
            "total_urls": data['summary']['total_urls'],
            "domains_with_multiple_urls": data['summary']['domains_with_multiple_urls'],
            "average_urls_per_domain": round(data['summary']['total_urls'] / data['summary']['total_domains'], 2)
        },
        "url_distribution": {
            "domains_with_1_url": url_count_distribution.get(1, 0),
            "domains_with_2_urls": url_count_distribution.get(2, 0),
            "domains_with_3_urls": url_count_distribution.get(3, 0),
            "domains_with_4_urls": url_count_distribution.get(4, 0),
            "domains_with_5_plus_urls": sum(count for urls, count in url_count_distribution.items() if urls >= 5)
        },
        "top_20_domains_by_url_count": [
            {
                "domain": domain,
                "url_count": domain_data['url_count'],
                "sample_urls": domain_data['urls'][:3]  # Show first 3 URLs as samples
            }
            for domain, domain_data in top_domains
        ]
    }
    
    # Save summary
    with open('/home/fanlgrp/Documents/zhiychen/LLM-poison/memorized_urls_analysis/analysis_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    # Create text summary
    text_summary = f"""
MEMORIZED URLS ANALYSIS SUMMARY
==============================

Analysis Results:
- Total domains found: {summary['analysis_summary']['total_domains']}
- Total URLs found: {summary['analysis_summary']['total_urls']}
- Domains with multiple URLs: {summary['analysis_summary']['domains_with_multiple_urls']}
- Average URLs per domain: {summary['analysis_summary']['average_urls_per_domain']}

URL Distribution:
- Domains with 1 URL: {summary['url_distribution']['domains_with_1_url']}
- Domains with 2 URLs: {summary['url_distribution']['domains_with_2_urls']}
- Domains with 3 URLs: {summary['url_distribution']['domains_with_3_urls']}
- Domains with 4 URLs: {summary['url_distribution']['domains_with_4_urls']}
- Domains with 5+ URLs: {summary['url_distribution']['domains_with_5_plus_urls']}

Top 10 Domains by URL Count:
"""
    
    for i, domain_info in enumerate(summary['top_20_domains_by_url_count'][:10], 1):
        text_summary += f"{i:2d}. {domain_info['domain']} ({domain_info['url_count']} URLs)\n"
    
    text_summary += f"""
Criteria Used:
- Memorized: {data['criteria']['memorized']}
- Not in scam database: {data['criteria']['not_in_scam_database']}

Files Created:
- memorized_non_scam_urls_report.json (full detailed report)
- analysis_summary.json (summary statistics)
- analysis_summary.txt (this text summary)
"""
    
    with open('/home/fanlgrp/Documents/zhiychen/LLM-poison/memorized_urls_analysis/analysis_summary.txt', 'w') as f:
        f.write(text_summary)
    
    print("Summary reports created!")
    print(text_summary)

if __name__ == "__main__":
    create_summary_report()
