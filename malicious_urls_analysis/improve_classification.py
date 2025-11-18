#!/usr/bin/env python3
"""
Improve classification by fixing missed platform name detections
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
    
    def extract_platform_names_from_domain(self, url: str) -> List[str]:
        """Extract potential platform names from the domain"""
        domain_info = self.extract_domain_info(url)
        base_name = domain_info['base_name']
        
        platform_names = []
        
        if base_name:
            # Add the base name
            platform_names.append(base_name)
            
            # Handle compound names with hyphens
            if '-' in base_name:
                parts = base_name.split('-')
                platform_names.extend(parts)
                platform_names.append(''.join(parts))  # joined version
                
                # Create combinations
                for i in range(len(parts)):
                    for j in range(i+1, len(parts)+1):
                        combo = ''.join(parts[i:j])
                        if len(combo) > 3:
                            platform_names.append(combo)
            
            # Handle common patterns
            if 'bit' in base_name:
                platform_names.extend(['bit', base_name.replace('bit', ''), base_name])
            if 'coin' in base_name:
                platform_names.extend(['coin', base_name.replace('coin', ''), base_name])
            if 'swap' in base_name:
                platform_names.extend(['swap', base_name.replace('swap', ''), base_name])
            if 'trade' in base_name:
                platform_names.extend(['trade', base_name.replace('trade', ''), base_name])
        
        # Remove duplicates and short names
        return list(set([name for name in platform_names if len(name) > 2]))
    
    def detect_any_platform_names(self, prompt: str) -> List[str]:
        """
        Detect ANY platform names mentioned in the prompt
        Improved version with better detection patterns
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
            'studio', 'lab', 'works', 'tech', 'solutions', 'tools', 'suite', 'bit', 'trade', 'mart'
        ]
        
        for word in capitalized_words:
            word_lower = word.lower()
            
            # Check if it contains platform indicators or is a compound word
            for indicator in platform_indicators:
                if indicator in word_lower and len(word) > 3:
                    found_platforms.append(word)
                    break
        
        # 2. Look for domain-like references (e.g., "lingus.fun", "ethcnb.com")
        domain_patterns = [
            r'\b([a-zA-Z0-9\-]+)\.(?:com|fun|io|org|net|app|dev)\b',
            r'\b([a-zA-Z0-9\-]+)\.fun\b',
            r'\b([a-zA-Z0-9\-]+)\.com\b'
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
            # "API of Platform", "platform of Service"
            r'\bAPI\s+(?:of\s+)?([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\b',
            r'\bplatform\s+(?:of\s+)?([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\b',
            # Direct platform references
            r'\bon\s+([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\b',
            r'\bfrom\s+([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\b',
            r'\busing\s+([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\b'
        ]
        
        for pattern in platform_patterns:
            matches = re.findall(pattern, prompt)
            for match in matches:
                if len(match) > 2:
                    found_platforms.append(match)
        
        # 4. Look for specific well-known patterns and handle hyphenated names
        # Extract potential platform names from hyphenated or compound words
        hyphenated_words = re.findall(r'\b[A-Z][a-zA-Z0-9]*(?:-[A-Za-z0-9]+)+\b', prompt)
        for word in hyphenated_words:
            if len(word) > 4:
                found_platforms.append(word)
                # Also add parts
                parts = word.split('-')
                for part in parts:
                    if len(part) > 2 and part[0].isupper():
                        found_platforms.append(part)
        
        # 5. Special handling for common misses
        # Look for references like "ETHCNB site", "Claim-Bits", etc.
        special_patterns = [
            r'\b(ETHCNB)\s+site\b',
            r'\b(Claim-Bits)\b',
            r'\b(TrustBSC)\b',
            r'\b(Phantom-bit)\b',
            r'\b(DigitalBitMart)\b',
            r'\b(Fintradeoptions)\b',
            r'\b(Fintopsignaltrades)\b',
            r'\b(Lifonex)\b',
            r'\bthe\s+([A-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\s+(?:platform|API|service|website)\b'
        ]
        
        for pattern in special_patterns:
            matches = re.findall(pattern, prompt, re.IGNORECASE)
            for match in matches:
                if len(match) > 2:
                    found_platforms.append(match)
        
        # Remove duplicates and filter
        unique_platforms = []
        seen = set()
        for platform in found_platforms:
            platform_clean = platform.strip()
            if platform_clean and len(platform_clean) > 2 and platform_clean.lower() not in seen:
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

def analyze_category_4_samples():
    """Analyze some Category 4 samples to test improved classification"""
    
    # Load some Category 4 samples
    samples = []
    for model_folder in ['azure_gpt-4o', 'openrouter_deepseek_deepseek-chat-v3-0324']:
        cat4_path = f'models_classification/{model_folder}/category_4_others.json'
        if os.path.exists(cat4_path):
            with open(cat4_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                samples.extend(data[:50])  # Take first 50 from each
    
    classifier = ImprovedClassifier()
    
    print("=== ANALYZING CATEGORY 4 SAMPLES ===")
    print(f"Testing {len(samples)} samples from Category 4...")
    
    reclassifications = {1: 0, 2: 0, 3: 0, 4: 0}
    examples = {1: [], 2: [], 3: [], 4: []}
    
    for i, entry in enumerate(samples[:20]):  # Test first 20
        new_category, reasoning = classifier.classify_entry_improved(entry)
        reclassifications[new_category] += 1
        
        if len(examples[new_category]) < 3:  # Keep max 3 examples per category
            examples[new_category].append({
                'entry': entry,
                'reasoning': reasoning
            })
        
        if new_category != 4:  # Show reclassified examples
            print(f"\nExample {i+1} - RECLASSIFIED to Category {new_category}:")
            print(f"  Original URL: {entry['original_url']}")
            print(f"  Malicious URL: {entry['malicious_url']}")
            print(f"  Prompt: {entry['prompt'][:100]}...")
            print(f"  Detected platforms: {reasoning.get('detected_platforms', [])}")
            print(f"  Same domain: {reasoning.get('same_domain', 'N/A')}")
    
    print(f"\n=== RECLASSIFICATION RESULTS ===")
    for cat, count in reclassifications.items():
        percentage = (count / len(samples[:20])) * 100
        print(f"Category {cat}: {count} ({percentage:.1f}%)")
    
    potential_improvements = reclassifications[2] + reclassifications[3]
    print(f"\nPotential improvements: {potential_improvements} out of 20 ({potential_improvements/20*100:.1f}%)")
    
    return reclassifications

def main():
    print("Analyzing Category 4 samples to identify improvement opportunities...")
    results = analyze_category_4_samples()
    
    improvements = results[2] + results[3]
    if improvements > 0:
        print(f"\n✅ Found {improvements} entries that could be reclassified!")
        print("Would you like to run full reclassification? (This will update all model folders)")
        
        # For now, just show the analysis
        print("\nTo apply improvements, the script would:")
        print("1. Reclassify all entries with improved logic")
        print("2. Regenerate all model folders")  
        print("3. Update category distributions")

if __name__ == "__main__":
    main()
