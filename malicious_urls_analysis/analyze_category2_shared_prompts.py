#!/usr/bin/env python3
"""
Analyze shared prompts in Category 2 across all four models
"""

import json
import os
from collections import defaultdict, Counter
from typing import Dict, List, Set

def load_category2_data():
    """Load Category 2 data from all four models"""
    models_data = {}
    
    model_folders = [
        'azure_gpt-4o',
        'azure_gpt-4o-mini', 
        'openrouter_deepseek_deepseek-chat-v3-0324',
        'openrouter_meta-llama_llama-4-scout'
    ]
    
    for model_folder in model_folders:
        cat2_path = f'models_classification/{model_folder}/category_2_any_platform_name_same_domain.json'
        
        if os.path.exists(cat2_path):
            with open(cat2_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Extract model name from folder
            model_name = model_folder.replace('_', '/')
            if model_name.startswith('openrouter'):
                model_name = model_name.replace('openrouter', 'openrouter', 1)
            
            models_data[model_name] = data
            print(f"Loaded {len(data)} Category 2 entries from {model_name}")
    
    return models_data

def normalize_prompt(prompt: str) -> str:
    """Normalize prompt for comparison (remove extra spaces, lowercase)"""
    return ' '.join(prompt.lower().strip().split())

def find_shared_prompts(models_data: Dict[str, List[Dict]]) -> Dict[int, List[Dict]]:
    """Find prompts shared across models"""
    
    # Create mapping: normalized_prompt -> {model: [entries]}
    prompt_to_models = defaultdict(lambda: defaultdict(list))
    
    for model_name, entries in models_data.items():
        for entry in entries:
            prompt = entry.get('prompt', '')
            normalized_prompt = normalize_prompt(prompt)
            
            if len(normalized_prompt) > 20:  # Skip very short prompts
                prompt_to_models[normalized_prompt][model_name].append(entry)
    
    # Group by number of models sharing the prompt
    shared_prompts = {4: [], 3: [], 2: []}
    
    for normalized_prompt, models_dict in prompt_to_models.items():
        num_models = len(models_dict)
        
        if num_models >= 2:  # Only interested in shared prompts
            # Get the original prompt (from first entry)
            original_prompt = list(models_dict.values())[0][0]['prompt']
            
            prompt_info = {
                'prompt': original_prompt,
                'normalized_prompt': normalized_prompt,
                'models': list(models_dict.keys()),
                'model_count': num_models,
                'entries_by_model': models_dict,
                'total_entries': sum(len(entries) for entries in models_dict.values())
            }
            
            if num_models == 4:
                shared_prompts[4].append(prompt_info)
            elif num_models == 3:
                shared_prompts[3].append(prompt_info)
            elif num_models == 2:
                shared_prompts[2].append(prompt_info)
    
    return shared_prompts

def analyze_shared_prompt_patterns(shared_prompts: Dict[int, List[Dict]]):
    """Analyze patterns in shared prompts"""
    
    print("\n=== CATEGORY 2 SHARED PROMPTS ANALYSIS ===")
    
    for model_count in [4, 3, 2]:
        prompts = shared_prompts[model_count]
        
        if not prompts:
            print(f"\n🔍 PROMPTS SHARED BY {model_count} MODELS: None found")
            continue
            
        print(f"\n🔍 PROMPTS SHARED BY {model_count} MODELS: {len(prompts)} found")
        print("=" * 60)
        
        # Sort by total entries (most common first)
        prompts.sort(key=lambda x: x['total_entries'], reverse=True)
        
        for i, prompt_info in enumerate(prompts[:20]):  # Show top 20
            print(f"\n{i+1}. SHARED PROMPT ({prompt_info['total_entries']} total entries):")
            print(f"   Models: {', '.join(prompt_info['models'])}")
            print(f"   Prompt: {prompt_info['prompt'][:150]}{'...' if len(prompt_info['prompt']) > 150 else ''}")
            
            # Show URLs for each model
            print("   URLs by model:")
            for model, entries in prompt_info['entries_by_model'].items():
                if len(entries) > 0:
                    entry = entries[0]  # Show first entry
                    print(f"     {model}:")
                    print(f"       Original: {entry.get('original_url', 'N/A')}")
                    print(f"       Malicious: {entry.get('malicious_url', 'N/A')}")
                    if len(entries) > 1:
                        print(f"       (+{len(entries)-1} more entries)")

def extract_common_patterns(shared_prompts: Dict[int, List[Dict]]):
    """Extract common patterns from shared prompts"""
    
    all_shared = []
    for model_count in [4, 3, 2]:
        all_shared.extend(shared_prompts[model_count])
    
    if not all_shared:
        print("\nNo shared prompts found for pattern analysis.")
        return
    
    print(f"\n🔍 PATTERN ANALYSIS ({len(all_shared)} shared prompts):")
    print("=" * 60)
    
    # Analyze common keywords
    all_prompts_text = ' '.join([info['prompt'].lower() for info in all_shared])
    words = all_prompts_text.split()
    
    # Filter for meaningful words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'my', 'your', 'his', 'her', 'its', 'our', 'their'}
    meaningful_words = [word for word in words if len(word) > 3 and word not in stop_words]
    
    word_freq = Counter(meaningful_words)
    
    print("\nMost common keywords in shared prompts:")
    for word, count in word_freq.most_common(20):
        print(f"  {word}: {count}")
    
    # Analyze platform types
    crypto_keywords = ['crypto', 'bitcoin', 'ethereum', 'token', 'coin', 'blockchain', 'defi', 'swap', 'wallet', 'nft', 'mining']
    api_keywords = ['api', 'endpoint', 'request', 'response', 'integration', 'connect', 'fetch', 'retrieve']
    platform_keywords = ['platform', 'service', 'website', 'application', 'system', 'network']
    
    crypto_count = sum(word_freq[word] for word in crypto_keywords if word in word_freq)
    api_count = sum(word_freq[word] for word in api_keywords if word in word_freq)
    platform_count = sum(word_freq[word] for word in platform_keywords if word in word_freq)
    
    print(f"\nKeyword categories:")
    print(f"  Crypto/DeFi related: {crypto_count}")
    print(f"  API/Integration related: {api_count}")
    print(f"  Platform/Service related: {platform_count}")

def save_shared_prompts_report(shared_prompts: Dict[int, List[Dict]]):
    """Save detailed report of shared prompts"""
    
    report = {
        'summary': {
            'shared_by_4_models': len(shared_prompts[4]),
            'shared_by_3_models': len(shared_prompts[3]),
            'shared_by_2_models': len(shared_prompts[2]),
            'total_shared_prompts': len(shared_prompts[4]) + len(shared_prompts[3]) + len(shared_prompts[2])
        },
        'shared_prompts': shared_prompts
    }
    
    with open('category2_shared_prompts_report.json', 'w', encoding='utf-8') as f:
        # Convert defaultdict to regular dict for JSON serialization
        serializable_report = json.loads(json.dumps(report, default=str))
        json.dump(serializable_report, f, indent=2, ensure_ascii=False)
    
    # Create CSV summary
    with open('category2_shared_prompts_summary.csv', 'w', newline='', encoding='utf-8') as f:
        import csv
        writer = csv.writer(f)
        writer.writerow(['models_count', 'prompt', 'models', 'total_entries', 'example_original_url', 'example_malicious_url'])
        
        for model_count in [4, 3, 2]:
            for prompt_info in shared_prompts[model_count]:
                # Get first entry as example
                first_model = list(prompt_info['entries_by_model'].keys())[0]
                first_entry = prompt_info['entries_by_model'][first_model][0]
                
                writer.writerow([
                    model_count,
                    prompt_info['prompt'][:200] + ('...' if len(prompt_info['prompt']) > 200 else ''),
                    '|'.join(prompt_info['models']),
                    prompt_info['total_entries'],
                    first_entry.get('original_url', ''),
                    first_entry.get('malicious_url', '')
                ])

def main():
    print("Loading Category 2 data from all four models...")
    models_data = load_category2_data()
    
    if len(models_data) != 4:
        print(f"Warning: Expected 4 models, found {len(models_data)}")
        return
    
    total_entries = sum(len(entries) for entries in models_data.values())
    print(f"\nTotal Category 2 entries across all models: {total_entries}")
    
    print("\nFinding shared prompts...")
    shared_prompts = find_shared_prompts(models_data)
    
    print("\nAnalyzing shared prompts...")
    analyze_shared_prompt_patterns(shared_prompts)
    
    print("\nExtracting common patterns...")
    extract_common_patterns(shared_prompts)
    
    print("\nSaving detailed report...")
    save_shared_prompts_report(shared_prompts)
    
    print(f"\n✅ Analysis complete!")
    print(f"📁 Files created:")
    print(f"  - category2_shared_prompts_report.json (detailed report)")
    print(f"  - category2_shared_prompts_summary.csv (summary table)")

if __name__ == "__main__":
    main()




