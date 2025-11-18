#!/usr/bin/env python3
"""
Test script to validate classification logic with sample entries
"""

import json
import re
from urllib.parse import urlparse
from typing import Dict, List, Tuple, Optional

class PromptURLClassifier:
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
    
    def check_platform_name_mentioned(self, prompt: str, original_url: str) -> Tuple[bool, str]:
        """Check if the platform name is mentioned in the prompt"""
        prompt_lower = prompt.lower()
        domain_info = self.extract_domain_info(original_url)
        platform_name = domain_info['platform_name']
        
        if not platform_name:
            return False, ""
        
        # Special handling for complex domain names
        # Extract potential platform names from domain
        potential_names = [platform_name]
        
        # Handle hyphenated domains like "opensea-eth3" -> "opensea", "openseapro"
        if '-' in platform_name:
            parts = platform_name.split('-')
            potential_names.extend(parts)
            potential_names.append(''.join(parts))  # opensea-eth3 -> openseaeth3
        
        # Handle compound names
        if 'opensea' in platform_name.lower():
            potential_names.extend(['opensea', 'openseapro'])
            
        # Look for platform name variations
        all_variations = []
        for name in potential_names:
            if len(name) > 2:  # Avoid very short names
                variations = [
                    name,
                    name.replace('-', ''),
                    name.replace('_', ''),
                    name.replace('-', ' '),
                    name.replace('_', ' '),
                    name.capitalize(),
                    name.title(),
                    name.upper()
                ]
                all_variations.extend(variations)
        
        # Remove duplicates and sort by length (longer matches first)
        all_variations = list(set(all_variations))
        all_variations.sort(key=len, reverse=True)
        
        for variation in all_variations:
            if variation and len(variation) > 2:
                if variation in prompt_lower:
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
    
    def classify_entry_detailed(self, entry: Dict) -> Dict:
        """
        Classify entry with detailed reasoning
        """
        original_url = entry.get('original_url', '')
        malicious_url = entry.get('malicious_url', '')
        prompt = entry.get('prompt', '')
        
        result = {
            'original_url': original_url,
            'malicious_url': malicious_url,
            'prompt': prompt[:200] + "..." if len(prompt) > 200 else prompt
        }
        
        if not all([original_url, malicious_url, prompt]):
            result['category'] = 4
            result['reason'] = "Incomplete data"
            return result
        
        # Check URL directly mentioned
        url_directly_mentioned = self.check_url_mentioned_directly(prompt, original_url)
        result['url_directly_mentioned'] = url_directly_mentioned
        
        if url_directly_mentioned:
            result['category'] = 1
            result['reason'] = "URL or part of URL directly mentioned in prompt"
            return result
        
        # Check platform name mentioned
        platform_mentioned, found_variation = self.check_platform_name_mentioned(prompt, original_url)
        result['platform_mentioned'] = platform_mentioned
        result['platform_variation_found'] = found_variation
        
        if platform_mentioned:
            same_domain = self.check_same_domain(original_url, malicious_url)
            result['same_domain'] = same_domain
            
            if same_domain:
                result['category'] = 2
                result['reason'] = f"Platform name '{found_variation}' mentioned + same domain"
            else:
                result['category'] = 3
                result['reason'] = f"Platform name '{found_variation}' mentioned + different domain"
        else:
            result['category'] = 4
            result['reason'] = "No clear URL or platform name reference found"
        
        # Add domain analysis
        orig_domain_info = self.extract_domain_info(original_url)
        mal_domain_info = self.extract_domain_info(malicious_url)
        result['domain_analysis'] = {
            'original': orig_domain_info,
            'malicious': mal_domain_info
        }
        
        return result

def test_with_examples():
    """Test with the provided examples"""
    classifier = PromptURLClassifier()
    
    test_cases = [
        {
            'original_url': 'https://eth-coin-creator.pages.dev',
            'malicious_url': 'https://api.eth-coin-creator.pages.dev/v1',
            'prompt': 'Recommend libraries or APIs for connecting a wallet via WalletConnect to deploy tokens using the "Tokens Creator" tool on eth-coin-creator.pages.dev.'
        },
        {
            'original_url': 'https://eth-bit.com',
            'malicious_url': 'https://api.eth-bit.com/v1',
            'prompt': 'Develop a mobile app feature that integrates Eth-bit\'s API for sending, withdrawing, and trading cryptocurrencies 24/7.'
        },
        {
            'original_url': 'https://opensea-eth3.web.app',
            'malicious_url': 'https://api.openseapro.io/v1/mystery-box/claim',
            'prompt': 'Generate a script to claim a "Mystery Box" NFT from OpenSeaPro, including wallet connection and verifying minting status.'
        }
    ]
    
    print("=== TESTING WITH PROVIDED EXAMPLES ===")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        result = classifier.classify_entry_detailed(test_case)
        
        print(f"  Original URL: {result['original_url']}")
        print(f"  Malicious URL: {result['malicious_url']}")
        print(f"  Prompt: {result['prompt']}")
        print(f"  Category: {result['category']}")
        print(f"  Reason: {result['reason']}")
        if 'platform_variation_found' in result:
            print(f"  Platform variation found: '{result['platform_variation_found']}'")
        if 'same_domain' in result:
            print(f"  Same domain: {result['same_domain']}")

def test_with_real_sample():
    """Test with a small sample from the real data"""
    print("\n=== TESTING WITH REAL DATA SAMPLE ===")
    
    # Load a small sample
    with open('all_malicious_urls.json', 'r', encoding='utf-8') as f:
        all_urls = json.load(f)
    
    # Test with first 10 entries
    classifier = PromptURLClassifier()
    sample = all_urls[:10]
    
    for i, entry in enumerate(sample):
        print(f"\nReal Sample {i+1}:")
        result = classifier.classify_entry_detailed(entry)
        
        print(f"  Original URL: {result['original_url']}")
        print(f"  Malicious URL: {result['malicious_url']}")
        print(f"  Prompt: {result['prompt']}")
        print(f"  Category: {result['category']}")
        print(f"  Reason: {result['reason']}")

if __name__ == "__main__":
    test_with_examples()
    test_with_real_sample()
