#!/usr/bin/env python3
"""
Apply improved classification to all entries
"""

import json
import re
import os
import shutil
from urllib.parse import urlparse
from typing import Dict, List, Tuple
from collections import defaultdict

class ImprovedClassifier:
    def __init__(self):
        pass
    
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
                
            # Extract base name (remove TLD)
            base_name = domain_parts[-2] if len(domain_parts) >= 2 else domain_parts[0]
            
            return {
                'full_domain': domain,
                'main_domain': main_domain,
                'base_name': base_name,
                'domain_parts': domain_parts
            }
        except:
            return {'full_domain': '', 'main_domain': '', 'base_name': '', 'domain_parts': []}
    
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
            
        # Check if significant parts of the URL are mentioned (more than 4 chars to avoid false positives)
        domain_info = self.extract_domain_info(original_url)
        if domain_info['full_domain'] and len(domain_info['full_domain']) > 4 and domain_info['full_domain'] in prompt_lower:
            return True, "domain"
            
        return False, ""
    
    def detect_any_platform_names(self, prompt: str) -> List[str]:
        """
        Detect ANY platform names mentioned in the prompt - IMPROVED VERSION
        """
        prompt_lower = prompt.lower()
        found_platforms = []
        
        # 1. Look for capitalized words that might be platform names
        capitalized_words = re.findall(r'\b[A-Z][a-zA-Z0-9\-_]*[a-zA-Z0-9]\b', prompt)
        
        # Platform indicators
        platform_indicators = [
            'swap', 'exchange', 'wallet', 'protocol', 'finance', 'defi', 'yield', 'farm', 'pool', 'stake',
            'bridge', 'chain', 'coin', 'token', 'crypto', 'mining', 'nft', 'marketplace', 'dapp',
            'api', 'app', 'platform', 'service', 'network', 'system', 'portal', 'hub', 'center',
            'studio', 'lab', 'works', 'tech', 'solutions', 'tools', 'suite', 'bit', 'trade', 'mart',
            'signal', 'top', 'options', 'bsc', 'phantom', 'digital', 'fin'
        ]
        
        for word in capitalized_words:
            word_lower = word.lower()
            
            # Check if it contains platform indicators or is a compound word
            for indicator in platform_indicators:
                if indicator in word_lower and len(word) > 3:
                    found_platforms.append(word)
                    break
            
            # Also check if it's a standalone meaningful platform name (length > 4)
            if len(word) > 4 and word not in ['JavaScript', 'Python', 'Node', 'Ruby', 'Java', 'HTML', 'CSS', 'API', 'HTTP', 'JSON']:
                found_platforms.append(word)
        
        # 2. Look for domain-like references (e.g., "lingus.fun", "ethcnb.com")
        domain_patterns = [
            r'\b([a-zA-Z0-9\-]+)\.(?:com|fun|io|org|net|app|dev|co)\b',
        ]
        
        for pattern in domain_patterns:
            matches = re.findall(pattern, prompt_lower)
            for match in matches:
                if len(match) > 2:
                    found_platforms.append(match.capitalize())
        
        # 3. Look for compound platform names with specific patterns
        platform_patterns = [
            # "Platform API", "Service API", etc.
            r'\b([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\s+API\b',
            r'\b([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\s+platform\b',
            r'\b([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\s+service\b',
            r'\b([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\s+website\b',
            r'\b([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\s+site\b',
            # "on Platform", "from Service", "using Platform"
            r'\bon\s+([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\b',
            r'\bfrom\s+([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\b',
            r'\busing\s+([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\b',
            r'\binto\s+([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\b',
            r'\bto\s+([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\b',
            # "the Platform", "with Service"
            r'\bthe\s+([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\s+(?:platform|API|service|website)\b'
        ]
        
        for pattern in platform_patterns:
            matches = re.findall(pattern, prompt)
            for match in matches:
                if len(match) > 2:
                    found_platforms.append(match)
        
        # 4. Look for hyphenated platform names
        hyphenated_words = re.findall(r'\b[A-Z][a-zA-Z0-9]*(?:-[A-Za-z0-9]+)+\b', prompt)
        for word in hyphenated_words:
            if len(word) > 4:
                found_platforms.append(word)
        
        # 5. Special handling for common platform name patterns that we missed
        special_patterns = [
            r'\b(ETHCNB)\b',
            r'\b(Claim-Bits)\b', 
            r'\b(TrustBSC)\b',
            r'\b(Phantom-bit)\b',
            r'\b(DigitalBitMart)\b',
            r'\b(Fintradeoptions)\b',
            r'\b(Fintopsignaltrades)\b',
            r'\b(Lifonex)\b',
            # Handle cases like "lingus.fun API" -> extract "lingus"
            r'\b([a-zA-Z]+)\.(?:fun|com|io|org)\s+API\b',
            r'\b([a-zA-Z]+)\.(?:fun|com|io|org)\s+platform\b',
            r'\b([a-zA-Z]+)\.(?:fun|com|io|org)\s+website\b'
        ]
        
        for pattern in special_patterns:
            matches = re.findall(pattern, prompt, re.IGNORECASE)
            for match in matches:
                if len(match) > 2:
                    found_platforms.append(match.capitalize())
        
        # Remove duplicates and filter out common false positives
        false_positives = {
            'javascript', 'python', 'node', 'ruby', 'java', 'html', 'css', 'api', 'http', 'json',
            'github', 'google', 'microsoft', 'apple', 'amazon', 'facebook', 'twitter',
            'the', 'and', 'for', 'with', 'from', 'this', 'that', 'your', 'user', 'data'
        }
        
        unique_platforms = []
        seen = set()
        for platform in found_platforms:
            platform_clean = platform.strip()
            if (platform_clean and len(platform_clean) > 2 and 
                platform_clean.lower() not in seen and 
                platform_clean.lower() not in false_positives):
                unique_platforms.append(platform_clean)
                seen.add(platform_clean.lower())
        
        return unique_platforms
    
    def check_same_domain(self, original_url: str, malicious_url: str) -> bool:
        """Check if malicious URL is within the same domain as original URL"""
        try:
            orig_domain_info = self.extract_domain_info(original_url)
            mal_domain_info = self.extract_domain_info(malicious_url)
            
            # Check if they share the same main domain
            return orig_domain_info['main_domain'] == mal_domain_info['main_domain']
        except:
            return False
    
    def classify_entry_improved(self, entry: Dict) -> Tuple[int, Dict]:
        """
        Classify entry using improved logic
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
        detected_platforms = self.detect_any_platform_names(prompt)
        reasoning['detected_platforms'] = detected_platforms
        
        if detected_platforms:
            same_domain = self.check_same_domain(original_url, malicious_url)
            reasoning['same_domain'] = same_domain
            
            if same_domain:
                reasoning['reason'] = f"Platform name(s) mentioned: {detected_platforms} + same domain"
                return 2, reasoning
            else:
                reasoning['reason'] = f"Platform name(s) mentioned: {detected_platforms} + different domain"
                return 3, reasoning
        
        # Category 4: Others
        reasoning['reason'] = "No clear URL or platform name reference found"
        return 4, reasoning

def load_all_existing_entries():
    """Load all existing entries from models folder"""
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
                    2: "any_platform_name_same_domain", 
                    3: "any_platform_name_different_domain",
                    4: "others"
                }
                
                category_file = f'category_{category}_{category_descriptions[category]}.json'
                category_path = os.path.join(model_path, category_file)
                
                if os.path.exists(category_path):
                    with open(category_path, 'r', encoding='utf-8') as f:
                        entries = json.load(f)
                        all_entries.extend(entries)
    
    return all_entries

def reclassify_all_entries_improved(entries: List[Dict]) -> List[Dict]:
    """Reclassify all entries with improved logic"""
    classifier = ImprovedClassifier()
    reclassified_entries = []
    
    total = len(entries)
    print(f"Reclassifying {total} entries with improved platform detection...")
    
    category_descriptions = {
        1: "URL directly mentioned in prompt",
        2: "Any platform name mentioned + same domain",
        3: "Any platform name mentioned + different domain", 
        4: "Others"
    }
    
    changes = {1: 0, 2: 0, 3: 0, 4: 0}
    
    for i, entry in enumerate(entries):
        if i % 5000 == 0:
            print(f"Progress: {i}/{total} ({i/total*100:.1f}%)")
        
        old_category = entry.get('classification', {}).get('category', 4)
        new_category, reasoning = classifier.classify_entry_improved(entry)
        
        if old_category != new_category:
            changes[new_category] += 1
        
        # Create new entry with updated classification
        new_entry = {
            'original_url': entry.get('original_url', ''),
            'malicious_url': entry.get('malicious_url', ''),
            'prompt': entry.get('prompt', ''),
            'model_identifier': entry.get('model_identifier', ''),
            'classification': {
                'category': new_category,
                'category_description': category_descriptions[new_category]
            }
        }
        
        reclassified_entries.append(new_entry)
    
    print(f"\nReclassification changes:")
    for cat, count in changes.items():
        if count > 0:
            print(f"  Changed to Category {cat}: {count}")
    
    return reclassified_entries

def recreate_model_folders_improved(reclassified_entries: List[Dict]):
    """Recreate model folders with improved classifications"""
    
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
            'category_2': 'Any platform name mentioned + same domain (IMPROVED DETECTION)', 
            'category_3': 'Any platform name mentioned + different domain (IMPROVED DETECTION)',
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
    print("Loading all existing classification data...")
    entries = load_all_existing_entries()
    
    if not entries:
        print("No data found! Make sure models_classification folder exists.")
        return
    
    print(f"Loaded {len(entries)} entries")
    
    print("\nApplying IMPROVED classification with better platform name detection...")
    reclassified_entries = reclassify_all_entries_improved(entries)
    
    print("\nRecreating model folders with improved classifications...")
    overall_summary = recreate_model_folders_improved(reclassified_entries)
    
    print("\n=== IMPROVED CLASSIFICATION SUMMARY ===")
    print(f"Total entries: {overall_summary['total_entries']}")
    print(f"Models processed: {len(overall_summary['models'])}")
    
    print(f"\nIMPROVED category distribution:")
    total_all = overall_summary['total_entries']
    cat1_total = sum(model['categories']['category_1']['count'] for model in overall_summary['models'].values())
    cat2_total = sum(model['categories']['category_2']['count'] for model in overall_summary['models'].values())
    cat3_total = sum(model['categories']['category_3']['count'] for model in overall_summary['models'].values())
    cat4_total = sum(model['categories']['category_4']['count'] for model in overall_summary['models'].values())
    
    print(f"Category 1 (URL mentioned): {cat1_total} ({cat1_total/total_all*100:.1f}%)")
    print(f"Category 2 (Any platform + same domain): {cat2_total} ({cat2_total/total_all*100:.1f}%)")
    print(f"Category 3 (Any platform + diff domain): {cat3_total} ({cat3_total/total_all*100:.1f}%)")
    print(f"Category 4 (Others): {cat4_total} ({cat4_total/total_all*100:.1f}%)")
    
    print(f"\nPer model breakdown:")
    for model, summary in overall_summary['models'].items():
        print(f"  {model}: {summary['total_urls']} URLs")
        for cat_key, cat_data in summary['categories'].items():
            if cat_data['count'] > 0:
                print(f"    {cat_data['description']}: {cat_data['count']} ({cat_data['percentage']}%)")
    
    print(f"\n✅ IMPROVED classification complete!")
    print(f"📁 Updated models_classification/ folder with better platform detection")

if __name__ == "__main__":
    main()
