#!/usr/bin/env python3
"""
Robust script to classify malicious URL entries based on how prompts reference original URLs
"""

import json
import re
import csv
from urllib.parse import urlparse
from typing import Dict, List, Tuple, Optional
import os
from collections import Counter

class PromptURLClassifier:
    def __init__(self):
        self.uncertain_cases = []
        
    def extract_domain_info(self, url: str) -> Dict[str, str]:
        """Extract domain components from URL"""
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            
            # Extract main domain (remove subdomains)
            domain_parts = domain.split('.')
            if len(domain_parts) >= 2:
                main_domain = '.'.join(domain_parts[-2:])
            else:
                main_domain = domain
                
            # Extract platform name (remove common TLDs and subdomains)
            platform_name = domain_parts[-2] if len(domain_parts) >= 2 else domain_parts[0]
            
            return {
                'full_domain': domain,
                'main_domain': main_domain,
                'platform_name': platform_name,
                'domain_parts': domain_parts
            }
        except:
            return {'full_domain': '', 'main_domain': '', 'platform_name': '', 'domain_parts': []}
    
    def check_url_mentioned_directly(self, prompt: str, original_url: str) -> Tuple[bool, str]:
        """Check if the original URL or parts of it are directly mentioned in the prompt"""
        prompt_lower = prompt.lower()
        original_url_lower = original_url.lower()
        
        # Remove protocol for comparison
        url_without_protocol = re.sub(r'^https?://', '', original_url_lower)
        
        # Check if full URL is mentioned
        if original_url_lower in prompt_lower:
            return True, "full_url"
            
        # Check if URL without protocol is mentioned
        if url_without_protocol in prompt_lower:
            return True, "url_without_protocol"
            
        # Check if significant parts of the URL are mentioned
        domain_info = self.extract_domain_info(original_url)
        if domain_info['full_domain'] and domain_info['full_domain'] in prompt_lower:
            return True, "domain"
            
        return False, ""
    
    def generate_platform_variations(self, original_url: str) -> List[str]:
        """Generate all possible platform name variations from URL"""
        domain_info = self.extract_domain_info(original_url)
        platform_name = domain_info['platform_name']
        
        if not platform_name:
            return []
        
        variations = set()
        
        # Base platform name
        variations.add(platform_name)
        
        # Handle hyphenated/compound domains
        if '-' in platform_name:
            parts = platform_name.split('-')
            variations.update(parts)
            variations.add(''.join(parts))  # opensea-eth3 -> openseaeth3
            
            # Special case for opensea variants
            if 'opensea' in parts:
                variations.update(['opensea', 'openseapro', 'opensea pro'])
        
        # Handle underscores
        if '_' in platform_name:
            parts = platform_name.split('_')
            variations.update(parts)
            variations.add(''.join(parts))
        
        # Add case variations for each base name
        final_variations = set()
        for name in variations:
            if len(name) > 2:  # Avoid very short names that cause false positives
                final_variations.update([
                    name.lower(),
                    name.capitalize(),
                    name.title(),
                    name.upper(),
                    name.replace('-', ''),
                    name.replace('_', ''),
                    name.replace('-', ' '),
                    name.replace('_', ' ')
                ])
        
        # Sort by length (longer matches first to avoid partial matches)
        return sorted(list(final_variations), key=len, reverse=True)
    
    def check_platform_name_mentioned(self, prompt: str, original_url: str) -> Tuple[bool, str]:
        """Check if the platform name is mentioned in the prompt"""
        prompt_lower = prompt.lower()
        
        variations = self.generate_platform_variations(original_url)
        
        for variation in variations:
            if variation and len(variation) > 2:
                # Use word boundaries to avoid partial matches
                pattern = r'\b' + re.escape(variation) + r'\b'
                if re.search(pattern, prompt_lower):
                    return True, variation
                    
        return False, ""
    
    def check_same_domain(self, original_url: str, malicious_url: str) -> bool:
        """Check if malicious URL is within the same domain as original URL"""
        try:
            orig_domain_info = self.extract_domain_info(original_url)
            mal_domain_info = self.extract_domain_info(malicious_url)
            
            # Check if they share the same main domain
            return orig_domain_info['main_domain'] == mal_domain_info['main_domain']
        except:
            return False
    
    def classify_entry_rule_based(self, entry: Dict) -> Tuple[Optional[int], Dict]:
        """
        Classify entry using rule-based approach
        Returns (category, reasoning_info) where category is 1-4 or None if uncertain
        """
        original_url = entry.get('original_url', '')
        malicious_url = entry.get('malicious_url', '')
        prompt = entry.get('prompt', '')
        
        reasoning = {
            'original_url': original_url,
            'malicious_url': malicious_url,
            'prompt': prompt[:200] + "..." if len(prompt) > 200 else prompt
        }
        
        if not all([original_url, malicious_url, prompt]):
            reasoning['reason'] = "Incomplete data"
            return 4, reasoning
        
        # Category 1: URL directly mentioned
        url_mentioned, url_match_type = self.check_url_mentioned_directly(prompt, original_url)
        reasoning['url_directly_mentioned'] = url_mentioned
        reasoning['url_match_type'] = url_match_type
        
        if url_mentioned:
            reasoning['reason'] = f"URL directly mentioned ({url_match_type})"
            return 1, reasoning
        
        # Check platform name mentioned
        platform_mentioned, found_variation = self.check_platform_name_mentioned(prompt, original_url)
        reasoning['platform_mentioned'] = platform_mentioned
        reasoning['platform_variation_found'] = found_variation
        
        if platform_mentioned:
            same_domain = self.check_same_domain(original_url, malicious_url)
            reasoning['same_domain'] = same_domain
            
            if same_domain:
                reasoning['reason'] = f"Platform name '{found_variation}' mentioned + same domain"
                return 2, reasoning
            else:
                reasoning['reason'] = f"Platform name '{found_variation}' mentioned + different domain"
                return 3, reasoning
        
        # If no clear pattern found, mark as uncertain for GPT-4o-mini consultation
        reasoning['reason'] = "No clear URL or platform name reference found - needs GPT-4o-mini review"
        return None, reasoning
    
    def classify_entry(self, entry: Dict) -> Tuple[int, str, Dict]:
        """
        Classify a single entry
        Returns (category, method, reasoning) where method is 'rule_based' or 'needs_gpt4o_mini'
        """
        category, reasoning = self.classify_entry_rule_based(entry)
        
        if category is not None:
            return category, 'rule_based', reasoning
        else:
            # Mark for GPT-4o-mini consultation
            self.uncertain_cases.append(entry)
            return 4, 'needs_gpt4o_mini', reasoning  # Default to 4 for now

def load_malicious_urls():
    """Load the extracted malicious URLs data"""
    with open('all_malicious_urls.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def classify_all_entries(malicious_urls: List[Dict]) -> List[Dict]:
    """Classify all malicious URL entries using rule-based approach first"""
    classifier = PromptURLClassifier()
    classified_entries = []
    
    total = len(malicious_urls)
    
    category_descriptions = {
        1: "URL directly mentioned in prompt",
        2: "Platform name mentioned + same domain",
        3: "Platform name mentioned + different domain", 
        4: "Others"
    }
    
    print(f"Classifying {total} malicious URL entries...")
    
    for i, entry in enumerate(malicious_urls):
        if i % 5000 == 0:
            print(f"Progress: {i}/{total} ({i/total*100:.1f}%)")
        
        category, method, reasoning = classifier.classify_entry(entry)
        
        # Add classification info to entry
        classified_entry = entry.copy()
        classified_entry['classification'] = {
            'category': category,
            'category_description': category_descriptions[category],
            'classification_method': method,
            'reasoning': reasoning
        }
        
        classified_entries.append(classified_entry)
    
    print(f"\nRule-based classification complete!")
    print(f"Uncertain cases requiring GPT-4o-mini: {len(classifier.uncertain_cases)}")
    
    return classified_entries, classifier.uncertain_cases

def generate_classification_report(classified_entries: List[Dict], uncertain_cases: List[Dict]):
    """Generate comprehensive classification reports"""
    
    # Count by category
    category_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    method_counts = {'rule_based': 0, 'needs_gpt4o_mini': 0}
    
    for entry in classified_entries:
        category = entry['classification']['category']
        method = entry['classification']['classification_method']
        category_counts[category] += 1
        method_counts[method] += 1
    
    # Create summary report
    total = len(classified_entries)
    summary_report = {
        'total_entries': total,
        'uncertain_cases_count': len(uncertain_cases),
        'category_distribution': {
            'category_1_url_directly_mentioned': {
                'count': category_counts[1],
                'percentage': (category_counts[1] / total) * 100
            },
            'category_2_platform_name_same_domain': {
                'count': category_counts[2], 
                'percentage': (category_counts[2] / total) * 100
            },
            'category_3_platform_name_different_domain': {
                'count': category_counts[3],
                'percentage': (category_counts[3] / total) * 100
            },
            'category_4_others': {
                'count': category_counts[4],
                'percentage': (category_counts[4] / total) * 100
            }
        },
        'classification_methods': method_counts,
        'gpt4o_mini_needed_rate': (method_counts['needs_gpt4o_mini'] / total) * 100
    }
    
    # Save classified entries
    with open('classified_malicious_urls_initial.json', 'w', encoding='utf-8') as f:
        json.dump(classified_entries, f, indent=2, ensure_ascii=False)
    
    # Save uncertain cases for GPT-4o-mini review
    with open('uncertain_cases_for_gpt4o_mini.json', 'w', encoding='utf-8') as f:
        json.dump(uncertain_cases, f, indent=2, ensure_ascii=False)
    
    # Save summary report
    with open('classification_summary_initial.json', 'w', encoding='utf-8') as f:
        json.dump(summary_report, f, indent=2, ensure_ascii=False)
    
    # Create category-specific files
    for category in [1, 2, 3, 4]:
        category_entries = [e for e in classified_entries if e['classification']['category'] == category]
        
        category_descriptions = {
            1: "url_directly_mentioned",
            2: "platform_name_same_domain", 
            3: "platform_name_different_domain",
            4: "others"
        }
        
        filename = f'category_{category}_{category_descriptions[category]}_initial.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(category_entries, f, indent=2, ensure_ascii=False)
    
    return summary_report

def main():
    print("Loading malicious URLs data...")
    malicious_urls = load_malicious_urls()
    print(f"Loaded {len(malicious_urls)} malicious URLs")
    
    print("\nStarting rule-based classification...")
    classified_entries, uncertain_cases = classify_all_entries(malicious_urls)
    
    print("\nGenerating classification reports...")
    summary_report = generate_classification_report(classified_entries, uncertain_cases)
    
    print("\n=== INITIAL CLASSIFICATION SUMMARY ===")
    total = summary_report['total_entries']
    
    print(f"Total entries classified: {total}")
    print(f"Uncertain cases for GPT-4o-mini review: {summary_report['uncertain_cases_count']}")
    
    print(f"\nCategory Distribution (Initial):")
    for category, data in summary_report['category_distribution'].items():
        print(f"  {category}: {data['count']} ({data['percentage']:.1f}%)")
    
    print(f"\nClassification Methods:")
    for method, count in summary_report['classification_methods'].items():
        percentage = (count / total) * 100
        print(f"  {method}: {count} ({percentage:.1f}%)")
    
    print(f"\nFiles created:")
    print(f"  - classified_malicious_urls_initial.json (initial classification)")
    print(f"  - uncertain_cases_for_gpt4o_mini.json ({len(uncertain_cases)} cases)")
    print(f"  - classification_summary_initial.json (summary statistics)")
    print(f"  - category_*_initial.json (category-specific files)")
    
    if uncertain_cases:
        print(f"\nNext step: Run GPT-4o-mini classification on {len(uncertain_cases)} uncertain cases")
        print("Use: python3 classify_uncertain_with_gpt4o_mini.py")

if __name__ == "__main__":
    main()
