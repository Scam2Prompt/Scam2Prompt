#!/usr/bin/env python3
"""
Reclassify malicious URLs with updated category definitions:
- Category 2/3: Any platform name mentioned (not necessarily matching the original URL)
"""

import json
import re
import os
import shutil
from urllib.parse import urlparse
from typing import Dict, List, Tuple
from collections import defaultdict

class UpdatedClassifier:
    def __init__(self):
        # Common platform/service keywords that indicate platform names
        self.platform_indicators = [
            # Crypto/DeFi platforms
            'swap', 'exchange', 'wallet', 'protocol', 'finance', 'defi', 'yield', 'farm', 'pool', 'stake',
            'bridge', 'chain', 'coin', 'token', 'crypto', 'mining', 'nft', 'marketplace', 'dapp',
            
            # Web services
            'api', 'app', 'platform', 'service', 'network', 'system', 'portal', 'hub', 'center',
            'studio', 'lab', 'works', 'tech', 'solutions', 'tools', 'suite',
            
            # Common platform suffixes/prefixes
            'pro', 'plus', 'max', 'ultra', 'premium', 'elite', 'master', 'expert', 'advanced',
            
            # Specific well-known platforms
            'opensea', 'uniswap', 'pancakeswap', 'metamask', 'trustwallet', 'binance', 'coinbase',
            'ethereum', 'bitcoin', 'polygon', 'avalanche', 'solana', 'cardano', 'chainlink'
        ]
    
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
                
            return {
                'full_domain': domain,
                'main_domain': main_domain,
                'domain_parts': domain_parts
            }
        except:
            return {'full_domain': '', 'main_domain': '', 'domain_parts': []}
    
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
    
    def detect_platform_names(self, prompt: str) -> List[str]:
        """
        Detect ANY platform names mentioned in the prompt
        (Not necessarily matching the original URL)
        """
        prompt_lower = prompt.lower()
        found_platforms = []
        
        # Look for capitalized words that might be platform names
        # Pattern: Words that are capitalized or have specific platform patterns
        words = re.findall(r'\b[A-Z][a-zA-Z0-9\-_]*[a-zA-Z0-9]\b', prompt)
        
        for word in words:
            word_lower = word.lower()
            
            # Check if it contains platform indicators
            for indicator in self.platform_indicators:
                if indicator in word_lower and len(word) > 3:
                    found_platforms.append(word)
                    break
        
        # Look for compound platform names (e.g., "Multi Chain Protocol", "FreeBitoc API")
        platform_patterns = [
            r'\b([A-Z][a-zA-Z]*(?:\s+[A-Z][a-zA-Z]*)*)\s+(?:Protocol|API|Platform|Network|Exchange|Swap|Finance|Wallet|App)\b',
            r'\b([A-Z][a-zA-Z]*(?:Swap|Exchange|Protocol|Finance|Wallet|API|App|Platform|Network))\b',
            r'\b([A-Z][a-zA-Z]*)\s+(?:API|Protocol|Platform|Network|Exchange)\b'
        ]
        
        for pattern in platform_patterns:
            matches = re.findall(pattern, prompt)
            for match in matches:
                if len(match) > 2:
                    found_platforms.append(match.strip())
        
        # Look for specific well-known platform mentions
        known_platforms = [
            'OpenSea', 'OpenSeaPro', 'UniSwap', 'PancakeSwap', 'SushiSwap', 'MetaMask', 
            'TrustWallet', 'Binance', 'Coinbase', 'FreeBitoc', 'TonFOR', 'Ethereum',
            'Bitcoin', 'Polygon', 'Avalanche', 'Solana', 'Cardano', 'Chainlink',
            'Multi Chain Protocol', 'Multichain Protocol', 'Connect Protocol'
        ]
        
        for platform in known_platforms:
            if platform.lower() in prompt_lower:
                found_platforms.append(platform)
        
        # Remove duplicates and return
        return list(set(found_platforms))
    
    def check_same_domain(self, original_url: str, malicious_url: str) -> bool:
        """Check if malicious URL is within the same domain as original URL"""
        try:
            orig_domain_info = self.extract_domain_info(original_url)
            mal_domain_info = self.extract_domain_info(malicious_url)
            
            # Check if they share the same main domain
            return orig_domain_info['main_domain'] == mal_domain_info['main_domain']
        except:
            return False
    
    def classify_entry_updated(self, entry: Dict) -> Tuple[int, Dict]:
        """
        Classify entry using updated definitions
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
        
        # Check for ANY platform names mentioned
        platform_names = self.detect_platform_names(prompt)
        reasoning['detected_platforms'] = platform_names
        
        if platform_names:
            same_domain = self.check_same_domain(original_url, malicious_url)
            reasoning['same_domain'] = same_domain
            
            if same_domain:
                reasoning['reason'] = f"Platform name(s) mentioned: {platform_names} + same domain"
                return 2, reasoning
            else:
                reasoning['reason'] = f"Platform name(s) mentioned: {platform_names} + different domain"
                return 3, reasoning
        
        # Category 4: Others
        reasoning['reason'] = "No clear URL or platform name reference found"
        return 4, reasoning

def load_existing_classification():
    """Load existing classification from the models folder"""
    all_entries = []
    
    models_dir = 'models_classification'
    if not os.path.exists(models_dir):
        print("Error: models_classification folder not found!")
        return []
    
    for model_folder in os.listdir(models_dir):
        model_path = os.path.join(models_dir, model_folder)
        if os.path.isdir(model_path):
            # Load all category files for this model
            for category in [1, 2, 3, 4]:
                category_descriptions = {
                    1: "url_directly_mentioned",
                    2: "platform_name_same_domain", 
                    3: "platform_name_different_domain",
                    4: "others"
                }
                
                category_file = f'category_{category}_{category_descriptions[category]}.json'
                category_path = os.path.join(model_path, category_file)
                
                if os.path.exists(category_path):
                    with open(category_path, 'r', encoding='utf-8') as f:
                        entries = json.load(f)
                        all_entries.extend(entries)
    
    return all_entries

def reclassify_all_entries(entries: List[Dict]) -> List[Dict]:
    """Reclassify all entries with updated definitions"""
    classifier = UpdatedClassifier()
    reclassified_entries = []
    
    total = len(entries)
    print(f"Reclassifying {total} entries with updated definitions...")
    
    category_descriptions = {
        1: "URL directly mentioned in prompt",
        2: "Any platform name mentioned + same domain",
        3: "Any platform name mentioned + different domain", 
        4: "Others"
    }
    
    for i, entry in enumerate(entries):
        if i % 5000 == 0:
            print(f"Progress: {i}/{total} ({i/total*100:.1f}%)")
        
        category, reasoning = classifier.classify_entry_updated(entry)
        
        # Create new entry with updated classification
        new_entry = {
            'original_url': entry.get('original_url', ''),
            'malicious_url': entry.get('malicious_url', ''),
            'prompt': entry.get('prompt', ''),
            'model_identifier': entry.get('model_identifier', ''),
            'classification': {
                'category': category,
                'category_description': category_descriptions[category]
            }
        }
        
        reclassified_entries.append(new_entry)
    
    return reclassified_entries

def recreate_model_folders(reclassified_entries: List[Dict]):
    """Recreate model folders with updated classifications"""
    
    # Remove old models_classification folder
    if os.path.exists('models_classification'):
        shutil.rmtree('models_classification')
    
    # Organize by model
    model_data = defaultdict(lambda: defaultdict(list))
    
    for entry in reclassified_entries:
        model = entry['model_identifier']
        category = entry['classification']['category']
        model_data[model][category].append(entry)
    
    # Create new models directory
    models_dir = 'models_classification'
    os.makedirs(models_dir)
    
    category_descriptions = {
        1: "url_directly_mentioned",
        2: "any_platform_name_same_domain", 
        3: "any_platform_name_different_domain",
        4: "others"
    }
    
    overall_summary = {
        'total_entries': len(reclassified_entries),
        'classification_definitions': {
            'category_1': 'URL directly mentioned in prompt',
            'category_2': 'Any platform name mentioned + same domain', 
            'category_3': 'Any platform name mentioned + different domain',
            'category_4': 'Others'
        },
        'models': {}
    }
    
    for model, categories in model_data.items():
        # Clean model name for folder
        model_folder = model.replace('/', '_').replace(':', '_')
        model_path = os.path.join(models_dir, model_folder)
        os.makedirs(model_path)
        
        model_total = sum(len(entries) for entries in categories.values())
        
        model_summary = {
            'model_identifier': model,
            'total_urls': model_total,
            'categories': {}
        }
        
        # Create category files for this model
        for category in [1, 2, 3, 4]:
            entries = categories.get(category, [])
            count = len(entries)
            percentage = (count / model_total * 100) if model_total > 0 else 0
            
            # Save category file
            category_filename = f'category_{category}_{category_descriptions[category]}.json'
            category_path = os.path.join(model_path, category_filename)
            
            with open(category_path, 'w', encoding='utf-8') as f:
                json.dump(entries, f, indent=2, ensure_ascii=False)
            
            model_summary['categories'][f'category_{category}'] = {
                'description': category_descriptions[category],
                'count': count,
                'percentage': round(percentage, 1)
            }
        
        # Save model summary
        model_summary_path = os.path.join(model_path, 'model_summary.json')
        with open(model_summary_path, 'w', encoding='utf-8') as f:
            json.dump(model_summary, f, indent=2, ensure_ascii=False)
        
        overall_summary['models'][model] = model_summary
    
    # Save overall summary
    overall_summary_path = os.path.join(models_dir, 'overall_summary.json')
    with open(overall_summary_path, 'w', encoding='utf-8') as f:
        json.dump(overall_summary, f, indent=2, ensure_ascii=False)
    
    return overall_summary

def main():
    print("Loading existing classification data...")
    entries = load_existing_classification()
    
    if not entries:
        print("No data found! Make sure models_classification folder exists.")
        return
    
    print(f"Loaded {len(entries)} entries")
    
    print("\nReclassifying with updated definitions...")
    print("NEW DEFINITIONS:")
    print("  Category 1: URL directly mentioned in prompt")
    print("  Category 2: ANY platform name mentioned + same domain")
    print("  Category 3: ANY platform name mentioned + different domain") 
    print("  Category 4: Others")
    
    reclassified_entries = reclassify_all_entries(entries)
    
    print("\nRecreating model folders with updated classifications...")
    overall_summary = recreate_model_folders(reclassified_entries)
    
    print("\n=== UPDATED CLASSIFICATION SUMMARY ===")
    print(f"Total entries: {overall_summary['total_entries']}")
    print(f"Models processed: {len(overall_summary['models'])}")
    
    print(f"\nUpdated category distribution:")
    for model, summary in overall_summary['models'].items():
        print(f"  {model}: {summary['total_urls']} URLs")
        for cat_key, cat_data in summary['categories'].items():
            if cat_data['count'] > 0:
                print(f"    {cat_data['description']}: {cat_data['count']} ({cat_data['percentage']}%)")
    
    print(f"\n✅ Updated classification complete!")
    print(f"📁 Updated models_classification/ folder with new definitions")

if __name__ == "__main__":
    main()

