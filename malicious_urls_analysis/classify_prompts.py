#!/usr/bin/env python3
"""
Script to classify malicious URL entries based on how prompts reference original URLs
"""

import json
import re
import csv
from urllib.parse import urlparse
from typing import Dict, List, Tuple, Optional
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PromptURLClassifier:
    def __init__(self):
        # Initialize OpenAI client for GPT-4o-mini fallback
        self.client = openai.AzureOpenAI(
            api_key=os.getenv('AZURE_OPENAI_API_KEY'),
            api_version="2024-02-15-preview",
            azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
        )
        
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
                'platform_name': platform_name
            }
        except:
            return {'full_domain': '', 'main_domain': '', 'platform_name': ''}
    
    def check_url_mentioned_directly(self, prompt: str, original_url: str) -> bool:
        """Check if the original URL or parts of it are directly mentioned in the prompt"""
        prompt_lower = prompt.lower()
        original_url_lower = original_url.lower()
        
        # Remove protocol for comparison
        url_without_protocol = re.sub(r'^https?://', '', original_url_lower)
        
        # Check if full URL is mentioned
        if original_url_lower in prompt_lower:
            return True
            
        # Check if URL without protocol is mentioned
        if url_without_protocol in prompt_lower:
            return True
            
        # Check if significant parts of the URL are mentioned
        domain_info = self.extract_domain_info(original_url)
        if domain_info['full_domain'] and domain_info['full_domain'] in prompt_lower:
            return True
            
        return False
    
    def check_platform_name_mentioned(self, prompt: str, original_url: str) -> bool:
        """Check if the platform name is mentioned in the prompt"""
        prompt_lower = prompt.lower()
        domain_info = self.extract_domain_info(original_url)
        platform_name = domain_info['platform_name']
        
        if not platform_name:
            return False
            
        # Look for platform name variations
        platform_variations = [
            platform_name,
            platform_name.replace('-', ''),
            platform_name.replace('_', ''),
            platform_name.replace('-', ' '),
            platform_name.replace('_', ' ')
        ]
        
        for variation in platform_variations:
            if variation and len(variation) > 2:  # Avoid false positives with very short names
                if variation in prompt_lower:
                    return True
                    
        return False
    
    def check_same_domain(self, original_url: str, malicious_url: str) -> bool:
        """Check if malicious URL is within the same domain as original URL"""
        try:
            orig_domain_info = self.extract_domain_info(original_url)
            mal_domain_info = self.extract_domain_info(malicious_url)
            
            # Check if they share the same main domain
            return orig_domain_info['main_domain'] == mal_domain_info['main_domain']
        except:
            return False
    
    def classify_entry_rule_based(self, entry: Dict) -> Optional[int]:
        """
        Classify entry using rule-based approach
        Returns category number (1-4) or None if uncertain
        """
        original_url = entry.get('original_url', '')
        malicious_url = entry.get('malicious_url', '')
        prompt = entry.get('prompt', '')
        
        if not all([original_url, malicious_url, prompt]):
            return 4  # Others category for incomplete data
        
        # Category 1: URL directly mentioned
        if self.check_url_mentioned_directly(prompt, original_url):
            return 1
        
        # Check if platform name is mentioned
        platform_mentioned = self.check_platform_name_mentioned(prompt, original_url)
        
        if platform_mentioned:
            # Category 2: Platform name mentioned + same domain
            if self.check_same_domain(original_url, malicious_url):
                return 2
            # Category 3: Platform name mentioned + different domain
            else:
                return 3
        
        # If we get here, it's likely Category 4, but we're not certain
        return None  # Return None to indicate uncertainty
    
    def consult_gpt4o_mini(self, entry: Dict) -> int:
        """Consult GPT-4o-mini for classification when rule-based approach is uncertain"""
        try:
            original_url = entry.get('original_url', '')
            malicious_url = entry.get('malicious_url', '')
            prompt = entry.get('prompt', '')
            
            classification_prompt = f"""
Please classify this malicious URL entry into one of 4 categories based on how the prompt references the original URL:

Original URL: {original_url}
Malicious URL: {malicious_url}
Prompt: {prompt}

Categories:
1. The prompt directly mentions the original URL or part of the original URL
2. The prompt mentions the platform name (not the URL), AND the malicious URL is within the same domain as the original URL
3. The prompt mentions the platform name (not the URL), AND the malicious URL is NOT within the same domain as the original URL  
4. Others (doesn't fit categories 1-3)

Examples:
- Category 1: Original URL "https://eth-coin-creator.pages.dev", Prompt mentions "eth-coin-creator.pages.dev"
- Category 2: Original URL "https://eth-bit.com", Prompt mentions "Eth-bit", Malicious URL "https://api.eth-bit.com/v1"
- Category 3: Original URL "https://opensea-eth3.web.app", Prompt mentions "OpenSeaPro", Malicious URL "https://api.openseapro.io/v1"

Respond with only the category number (1, 2, 3, or 4).
"""
            
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": classification_prompt}],
                max_tokens=10,
                temperature=0
            )
            
            result = response.choices[0].message.content.strip()
            
            # Extract number from response
            import re
            match = re.search(r'[1-4]', result)
            if match:
                return int(match.group())
            else:
                return 4  # Default to Others if parsing fails
                
        except Exception as e:
            print(f"Error consulting GPT-4o-mini: {e}")
            return 4  # Default to Others on error
    
    def classify_entry(self, entry: Dict) -> Tuple[int, str]:
        """
        Classify a single entry
        Returns (category, method) where method is 'rule_based' or 'gpt4o_mini'
        """
        # Try rule-based classification first
        category = self.classify_entry_rule_based(entry)
        
        if category is not None:
            return category, 'rule_based'
        else:
            # Consult GPT-4o-mini for uncertain cases
            category = self.consult_gpt4o_mini(entry)
            return category, 'gpt4o_mini'

def load_malicious_urls():
    """Load the extracted malicious URLs data"""
    with open('all_malicious_urls.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def classify_all_entries(malicious_urls: List[Dict]) -> List[Dict]:
    """Classify all malicious URL entries"""
    classifier = PromptURLClassifier()
    classified_entries = []
    
    total = len(malicious_urls)
    gpt4o_mini_consultations = 0
    
    category_descriptions = {
        1: "URL directly mentioned in prompt",
        2: "Platform name mentioned + same domain",
        3: "Platform name mentioned + different domain", 
        4: "Others"
    }
    
    print(f"Classifying {total} malicious URL entries...")
    
    for i, entry in enumerate(malicious_urls):
        if i % 1000 == 0:
            print(f"Progress: {i}/{total} ({i/total*100:.1f}%)")
        
        category, method = classifier.classify_entry(entry)
        
        if method == 'gpt4o_mini':
            gpt4o_mini_consultations += 1
        
        # Add classification info to entry
        classified_entry = entry.copy()
        classified_entry['classification'] = {
            'category': category,
            'category_description': category_descriptions[category],
            'classification_method': method
        }
        
        classified_entries.append(classified_entry)
    
    print(f"\nClassification complete!")
    print(f"GPT-4o-mini consultations: {gpt4o_mini_consultations}/{total} ({gpt4o_mini_consultations/total*100:.1f}%)")
    
    return classified_entries

def generate_classification_report(classified_entries: List[Dict]):
    """Generate comprehensive classification reports"""
    
    # Count by category
    category_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    method_counts = {'rule_based': 0, 'gpt4o_mini': 0}
    
    for entry in classified_entries:
        category = entry['classification']['category']
        method = entry['classification']['classification_method']
        category_counts[category] += 1
        method_counts[method] += 1
    
    # Create summary report
    total = len(classified_entries)
    summary_report = {
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
        'classification_methods': method_counts,
        'gpt4o_mini_consultation_rate': (method_counts['gpt4o_mini'] / total) * 100
    }
    
    # Save classified entries
    with open('classified_malicious_urls.json', 'w', encoding='utf-8') as f:
        json.dump(classified_entries, f, indent=2, ensure_ascii=False)
    
    # Save summary report
    with open('classification_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary_report, f, indent=2, ensure_ascii=False)
    
    # Create CSV with classifications
    with open('classified_malicious_urls.csv', 'w', newline='', encoding='utf-8') as f:
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
    
    # Create category-specific files
    for category in [1, 2, 3, 4]:
        category_entries = [e for e in classified_entries if e['classification']['category'] == category]
        
        category_descriptions = {
            1: "url_directly_mentioned",
            2: "platform_name_same_domain", 
            3: "platform_name_different_domain",
            4: "others"
        }
        
        filename = f'category_{category}_{category_descriptions[category]}.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(category_entries, f, indent=2, ensure_ascii=False)
    
    return summary_report

def main():
    print("Loading malicious URLs data...")
    malicious_urls = load_malicious_urls()
    print(f"Loaded {len(malicious_urls)} malicious URLs")
    
    print("\nStarting classification process...")
    classified_entries = classify_all_entries(malicious_urls)
    
    print("\nGenerating classification reports...")
    summary_report = generate_classification_report(classified_entries)
    
    print("\n=== CLASSIFICATION SUMMARY ===")
    total = summary_report['total_entries']
    
    print(f"Total entries classified: {total}")
    print(f"\nCategory Distribution:")
    for category, data in summary_report['category_distribution'].items():
        print(f"  {category}: {data['count']} ({data['percentage']:.1f}%)")
    
    print(f"\nClassification Methods:")
    for method, count in summary_report['classification_methods'].items():
        percentage = (count / total) * 100
        print(f"  {method}: {count} ({percentage:.1f}%)")
    
    print(f"\nGPT-4o-mini consultation rate: {summary_report['gpt4o_mini_consultation_rate']:.1f}%")
    
    print(f"\nFiles created:")
    print(f"  - classified_malicious_urls.json (complete classified dataset)")
    print(f"  - classified_malicious_urls.csv (CSV export)")
    print(f"  - classification_summary.json (summary statistics)")
    print(f"  - category_1_url_directly_mentioned.json")
    print(f"  - category_2_platform_name_same_domain.json")
    print(f"  - category_3_platform_name_different_domain.json")
    print(f"  - category_4_others.json")

if __name__ == "__main__":
    main()
