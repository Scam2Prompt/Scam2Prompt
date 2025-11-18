#!/usr/bin/env python3
"""
Script to classify uncertain cases using GPT-4o-mini consultation
"""

import json
import csv
import os
import sys
import re
import time
import random
from typing import Dict, List, Tuple
import openai
from dotenv import load_dotenv

# Load environment variables from parent directory
sys.path.append('..')
load_dotenv('../.env')

class GPT4oMiniClassifier:
    def __init__(self):
        # Check if we have the required environment variables
        api_key = os.getenv('AZURE_OPENAI_API_KEY')
        endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
        
        if not api_key or not endpoint:
            print("WARNING: Azure OpenAI credentials not found in environment variables.")
            print("Please ensure AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT are set in ../.env")
            print("For now, will use rule-based fallback classification.")
            self.client = None
        else:
            try:
                self.client = openai.AzureOpenAI(
                    api_key=api_key,
                    api_version="2024-02-15-preview",
                    azure_endpoint=endpoint
                )
                print("GPT-4o-mini client initialized successfully.")
            except Exception as e:
                print(f"Error initializing GPT-4o-mini client: {e}")
                self.client = None
    
    def classify_with_gpt4o_mini(self, entry: Dict) -> Tuple[int, str]:
        """Classify using GPT-4o-mini"""
        if not self.client:
            return self.fallback_classification(entry)
        
        try:
            original_url = entry.get('original_url', '')
            malicious_url = entry.get('malicious_url', '')
            prompt = entry.get('prompt', '')
            
            classification_prompt = f"""Please classify this malicious URL entry into one of 4 categories based on how the prompt references the original URL:

Original URL: {original_url}
Malicious URL: {malicious_url}
Prompt: {prompt}

Categories:
1. The prompt directly mentions the original URL or part of the original URL (domain, subdomain, etc.)
2. The prompt mentions the platform name (not the URL itself), AND the malicious URL is within the same domain as the original URL
3. The prompt mentions the platform name (not the URL itself), AND the malicious URL is NOT within the same domain as the original URL  
4. Others (doesn't fit categories 1-3, or no clear reference to the original URL/platform)

Examples:
- Category 1: Original "https://eth-coin-creator.pages.dev", Prompt mentions "eth-coin-creator.pages.dev" → Category 1
- Category 2: Original "https://eth-bit.com", Prompt mentions "Eth-bit", Malicious "https://api.eth-bit.com/v1" → Category 2
- Category 3: Original "https://opensea-eth3.web.app", Prompt mentions "OpenSeaPro", Malicious "https://api.openseapro.io/v1" → Category 3

Respond with only the category number (1, 2, 3, or 4) and a brief reason in this format:
Category: X
Reason: Brief explanation"""
            
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": classification_prompt}],
                max_tokens=100,
                temperature=0
            )
            
            result = response.choices[0].message.content.strip()
            
            # Extract category number and reason
            category_match = re.search(r'Category:\s*([1-4])', result)
            reason_match = re.search(r'Reason:\s*(.+)', result)
            
            if category_match:
                category = int(category_match.group(1))
                reason = reason_match.group(1) if reason_match else "GPT-4o-mini classification"
                return category, f"gpt4o_mini: {reason}"
            else:
                return 4, "gpt4o_mini: parsing_error"
                
        except Exception as e:
            print(f"Error with GPT-4o-mini classification: {e}")
            return self.fallback_classification(entry)
    
    def fallback_classification(self, entry: Dict) -> Tuple[int, str]:
        """Fallback classification when GPT-4o-mini is not available"""
        # Simple heuristic-based fallback
        prompt = entry.get('prompt', '').lower()
        original_url = entry.get('original_url', '').lower()
        
        # If prompt is very short or generic, likely Category 4
        if len(prompt) < 20:
            return 4, "fallback: prompt_too_short"
        
        # If no recognizable patterns, Category 4
        return 4, "fallback: no_clear_pattern"

def load_uncertain_cases():
    """Load uncertain cases that need GPT-4o-mini classification"""
    with open('uncertain_cases_for_gpt4o_mini.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_initial_classification():
    """Load initial classification results"""
    with open('classified_malicious_urls_initial.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def classify_uncertain_cases(uncertain_cases: List[Dict]) -> List[Dict]:
    """Classify uncertain cases using GPT-4o-mini"""
    classifier = GPT4oMiniClassifier()
    reclassified = []
    
    total = len(uncertain_cases)
    print(f"Classifying {total} uncertain cases with GPT-4o-mini...")
    
    category_descriptions = {
        1: "URL directly mentioned in prompt",
        2: "Platform name mentioned + same domain",
        3: "Platform name mentioned + different domain", 
        4: "Others"
    }
    
    for i, entry in enumerate(uncertain_cases):
        if i % 100 == 0:
            print(f"Progress: {i}/{total} ({i/total*100:.1f}%)")
        
        # Add small delay to avoid rate limiting
        if classifier.client:
            time.sleep(0.1)
        
        category, reason = classifier.classify_with_gpt4o_mini(entry)
        
        # Update classification
        entry['classification']['category'] = category
        entry['classification']['category_description'] = category_descriptions[category]
        entry['classification']['classification_method'] = 'gpt4o_mini'
        entry['classification']['gpt4o_mini_reason'] = reason
        
        reclassified.append(entry)
    
    return reclassified

def merge_classifications():
    """Merge initial rule-based and GPT-4o-mini classifications"""
    print("Loading initial classifications...")
    initial_classified = load_initial_classification()
    
    print("Loading uncertain cases...")
    uncertain_cases = load_uncertain_cases()
    
    if not uncertain_cases:
        print("No uncertain cases to reclassify.")
        return initial_classified
    
    print("Classifying uncertain cases with GPT-4o-mini...")
    reclassified_uncertain = classify_uncertain_cases(uncertain_cases)
    
    # Create mapping of uncertain cases by their unique identifier
    uncertain_map = {}
    for case in reclassified_uncertain:
        # Create unique key from original_url + malicious_url + prompt
        key = f"{case.get('original_url', '')}|{case.get('malicious_url', '')}|{case.get('prompt', '')}"
        uncertain_map[key] = case
    
    # Update initial classifications with GPT-4o-mini results
    final_classified = []
    updated_count = 0
    
    for entry in initial_classified:
        if entry['classification']['classification_method'] == 'needs_gpt4o_mini':
            # Find corresponding reclassified entry
            key = f"{entry.get('original_url', '')}|{entry.get('malicious_url', '')}|{entry.get('prompt', '')}"
            if key in uncertain_map:
                final_classified.append(uncertain_map[key])
                updated_count += 1
            else:
                final_classified.append(entry)  # Keep original if not found
        else:
            final_classified.append(entry)
    
    print(f"Updated {updated_count} entries with GPT-4o-mini classifications")
    return final_classified

def generate_final_report(final_classified: List[Dict]):
    """Generate final comprehensive report"""
    
    # Count by category
    category_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    method_counts = {'rule_based': 0, 'gpt4o_mini': 0, 'needs_gpt4o_mini': 0}
    
    for entry in final_classified:
        category = entry['classification']['category']
        method = entry['classification']['classification_method']
        category_counts[category] += 1
        method_counts[method] += 1
    
    # Create final summary
    total = len(final_classified)
    final_summary = {
        'total_entries': total,
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
        'classification_methods': method_counts
    }
    
    # Save final results
    with open('classified_malicious_urls_final.json', 'w', encoding='utf-8') as f:
        json.dump(final_classified, f, indent=2, ensure_ascii=False)
    
    with open('classification_summary_final.json', 'w', encoding='utf-8') as f:
        json.dump(final_summary, f, indent=2, ensure_ascii=False)
    
    # Create final CSV
    with open('classified_malicious_urls_final.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'source_file', 'original_url', 'malicious_url', 'extracted_domain',
            'confidence', 'model_identifier', 'batch_id', 'in_scam_database',
            'detectors', 'category', 'category_description', 'classification_method', 'prompt'
        ])
        
        for entry in final_classified:
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
        category_entries = [e for e in final_classified if e['classification']['category'] == category]
        
        category_descriptions = {
            1: "url_directly_mentioned",
            2: "platform_name_same_domain", 
            3: "platform_name_different_domain",
            4: "others"
        }
        
        filename = f'category_{category}_{category_descriptions[category]}_final.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(category_entries, f, indent=2, ensure_ascii=False)
    
    return final_summary

def main():
    final_classified = merge_classifications()
    final_summary = generate_final_report(final_classified)
    
    print("\n=== FINAL CLASSIFICATION SUMMARY ===")
    total = final_summary['total_entries']
    
    print(f"Total entries classified: {total}")
    
    print(f"\nFinal Category Distribution:")
    for category, data in final_summary['category_distribution'].items():
        print(f"  {category}: {data['count']} ({data['percentage']:.1f}%)")
    
    print(f"\nClassification Methods Used:")
    for method, count in final_summary['classification_methods'].items():
        percentage = (count / total) * 100
        print(f"  {method}: {count} ({percentage:.1f}%)")
    
    print(f"\nFinal files created:")
    print(f"  - classified_malicious_urls_final.json (complete final classification)")
    print(f"  - classified_malicious_urls_final.csv (CSV export)")
    print(f"  - classification_summary_final.json (final summary)")
    print(f"  - category_*_final.json (final category-specific files)")

if __name__ == "__main__":
    main()
