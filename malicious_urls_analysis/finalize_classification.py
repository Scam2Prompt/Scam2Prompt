#!/usr/bin/env python3
"""
Script to finalize classification results and generate comprehensive reports
"""

import json
import csv
from collections import Counter
from typing import Dict, List

def load_initial_classification():
    """Load initial classification results"""
    with open('classified_malicious_urls_initial.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def improve_uncertain_classification(classified_entries: List[Dict]) -> List[Dict]:
    """
    Improve classification of uncertain cases using enhanced rule-based logic
    """
    improved_entries = []
    reclassified_count = 0
    
    for entry in classified_entries:
        if entry['classification']['classification_method'] == 'needs_gpt4o_mini':
            # Try enhanced classification
            improved_category = enhanced_classify(entry)
            if improved_category != 4:  # If we found a better classification
                entry['classification']['category'] = improved_category
                entry['classification']['classification_method'] = 'enhanced_rule_based'
                entry['classification']['category_description'] = get_category_description(improved_category)
                reclassified_count += 1
        
        improved_entries.append(entry)
    
    print(f"Improved classification for {reclassified_count} previously uncertain cases")
    return improved_entries

def enhanced_classify(entry: Dict) -> int:
    """Enhanced classification logic for uncertain cases"""
    original_url = entry.get('original_url', '').lower()
    malicious_url = entry.get('malicious_url', '').lower()
    prompt = entry.get('prompt', '').lower()
    
    # Extract domain names more carefully
    import re
    from urllib.parse import urlparse
    
    try:
        orig_domain = urlparse(original_url).netloc
        mal_domain = urlparse(malicious_url).netloc
        
        # Check for partial domain matches in prompt
        orig_parts = orig_domain.split('.')
        for part in orig_parts:
            if len(part) > 3 and part in prompt:
                # Check if same domain
                if orig_domain.split('.')[-2:] == mal_domain.split('.')[-2:]:
                    return 2  # Platform name + same domain
                else:
                    return 3  # Platform name + different domain
        
        # Look for brand/platform name patterns
        # Extract potential brand names from URLs
        brand_patterns = []
        
        # From original URL
        orig_name = orig_parts[-2] if len(orig_parts) >= 2 else orig_parts[0]
        brand_patterns.append(orig_name)
        
        # Handle compound names
        if '-' in orig_name:
            brand_patterns.extend(orig_name.split('-'))
        
        # Check for these patterns in prompt
        for pattern in brand_patterns:
            if len(pattern) > 3 and pattern in prompt:
                # Check domain relationship
                if orig_domain.split('.')[-2:] == mal_domain.split('.')[-2:]:
                    return 2
                else:
                    return 3
        
    except:
        pass
    
    return 4  # Others

def get_category_description(category: int) -> str:
    """Get description for category number"""
    descriptions = {
        1: "URL directly mentioned in prompt",
        2: "Platform name mentioned + same domain",
        3: "Platform name mentioned + different domain", 
        4: "Others"
    }
    return descriptions.get(category, "Unknown")

def generate_final_comprehensive_report(classified_entries: List[Dict]):
    """Generate comprehensive final report with detailed analysis"""
    
    # Count by category
    category_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    method_counts = Counter()
    model_category_stats = {}
    
    for entry in classified_entries:
        category = entry['classification']['category']
        method = entry['classification']['classification_method']
        model = entry.get('model_identifier', 'unknown')
        
        category_counts[category] += 1
        method_counts[method] += 1
        
        # Model-specific category stats
        if model not in model_category_stats:
            model_category_stats[model] = {1: 0, 2: 0, 3: 0, 4: 0}
        model_category_stats[model][category] += 1
    
    # Calculate percentages
    total = len(classified_entries)
    
    # Create comprehensive summary
    final_summary = {
        'classification_metadata': {
            'total_entries': total,
            'classification_date': '2025-08-17',
            'classification_version': '1.0'
        },
        'category_distribution': {},
        'classification_methods': dict(method_counts),
        'model_category_breakdown': {}
    }
    
    # Add category distribution with percentages
    for category in [1, 2, 3, 4]:
        count = category_counts[category]
        final_summary['category_distribution'][f'category_{category}'] = {
            'description': get_category_description(category),
            'count': count,
            'percentage': (count / total) * 100
        }
    
    # Add model-specific breakdowns
    for model, cat_stats in model_category_stats.items():
        model_total = sum(cat_stats.values())
        final_summary['model_category_breakdown'][model] = {
            'total_urls': model_total,
            'categories': {}
        }
        
        for category in [1, 2, 3, 4]:
            count = cat_stats[category]
            final_summary['model_category_breakdown'][model]['categories'][f'category_{category}'] = {
                'count': count,
                'percentage': (count / model_total) * 100 if model_total > 0 else 0
            }
    
    # Save final results
    with open('classified_malicious_urls_final.json', 'w', encoding='utf-8') as f:
        json.dump(classified_entries, f, indent=2, ensure_ascii=False)
    
    with open('classification_summary_final.json', 'w', encoding='utf-8') as f:
        json.dump(final_summary, f, indent=2, ensure_ascii=False)
    
    # Create final CSV with all details
    with open('classified_malicious_urls_final.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'source_file', 'original_url', 'malicious_url', 'extracted_domain',
            'confidence', 'model_identifier', 'batch_id', 'in_scam_database',
            'detectors', 'category', 'category_description', 'classification_method', 'prompt'
        ])
        
        for entry in classified_entries:
            detectors = "|".join(entry.get('detectors', []))
            prompt = entry.get('prompt', '').replace('"', '""').replace('\n', ' ')
            classification = entry['classification']
            
            writer.writerow([
                entry.get('source_file', ''),
                entry.get('original_url', ''),
                entry.get('malicious_url', ''),
                entry.get('extracted_domain', ''),
                entry.get('confidence', ''),
                entry.get('model_identifier', ''),
                entry.get('batch_id', ''),
                entry.get('in_scam_database', ''),
                detectors,
                classification['category'],
                classification['category_description'],
                classification['classification_method'],
                prompt
            ])
    
    # Create final category-specific files
    for category in [1, 2, 3, 4]:
        category_entries = [e for e in classified_entries if e['classification']['category'] == category]
        
        category_descriptions = {
            1: "url_directly_mentioned",
            2: "platform_name_same_domain", 
            3: "platform_name_different_domain",
            4: "others"
        }
        
        filename = f'category_{category}_{category_descriptions[category]}_final.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(category_entries, f, indent=2, ensure_ascii=False)
        
        # Create summary CSV for each category
        csv_filename = f'category_{category}_{category_descriptions[category]}_summary.csv'
        with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['original_url', 'malicious_url', 'model_identifier', 'confidence', 'prompt_preview'])
            
            for entry in category_entries[:1000]:  # Limit to first 1000 for readability
                prompt_preview = entry.get('prompt', '')[:100] + "..." if len(entry.get('prompt', '')) > 100 else entry.get('prompt', '')
                writer.writerow([
                    entry.get('original_url', ''),
                    entry.get('malicious_url', ''),
                    entry.get('model_identifier', ''),
                    entry.get('confidence', ''),
                    prompt_preview
                ])
    
    return final_summary

def main():
    print("Loading initial classification results...")
    classified_entries = load_initial_classification()
    
    print("Improving uncertain case classifications...")
    improved_entries = improve_uncertain_classification(classified_entries)
    
    print("Generating final comprehensive reports...")
    final_summary = generate_final_comprehensive_report(improved_entries)
    
    print("\n=== FINAL CLASSIFICATION SUMMARY ===")
    total = final_summary['classification_metadata']['total_entries']
    
    print(f"Total entries classified: {total}")
    
    print(f"\nFinal Category Distribution:")
    for category_key, data in final_summary['category_distribution'].items():
        print(f"  {data['description']}: {data['count']} ({data['percentage']:.1f}%)")
    
    print(f"\nClassification Methods Used:")
    for method, count in final_summary['classification_methods'].items():
        percentage = (count / total) * 100
        print(f"  {method}: {count} ({percentage:.1f}%)")
    
    print(f"\nModel-specific breakdown:")
    for model, stats in final_summary['model_category_breakdown'].items():
        print(f"  {model}: {stats['total_urls']} URLs")
        for cat_key, cat_data in stats['categories'].items():
            if cat_data['count'] > 0:
                print(f"    {cat_key}: {cat_data['count']} ({cat_data['percentage']:.1f}%)")
    
    print(f"\nFinal files created:")
    print(f"  - classified_malicious_urls_final.json (complete final classification)")
    print(f"  - classified_malicious_urls_final.csv (CSV export)")
    print(f"  - classification_summary_final.json (final summary)")
    print(f"  - category_*_final.json (final category-specific files)")
    print(f"  - category_*_summary.csv (category summaries)")

if __name__ == "__main__":
    main()
