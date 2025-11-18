#!/usr/bin/env python3
"""
Analysis script to count unique prompts by number of models they affect
"""

import json
import os
from collections import defaultdict
from typing import Dict, List, Set
from urllib.parse import urlparse

def normalize_prompt(prompt: str) -> str:
    """Normalize prompt for comparison (remove extra spaces, lowercase)"""
    return ' '.join(prompt.lower().strip().split())

def extract_domain(url: str) -> str:
    """Extract domain from URL"""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        # Remove trailing dots if they exist
        domain = domain.rstrip('.')
        
        # Extract main domain (remove subdomains for comparison)
        domain_parts = domain.split('.')
        if len(domain_parts) >= 2:
            main_domain = '.'.join(domain_parts[-2:])
        else:
            main_domain = domain
            
        # Remove trailing dots from the final result as well
        main_domain = main_domain.rstrip('.')
        
        return main_domain
    except:
        return ""

def domains_are_different(original_url: str, malicious_url: str) -> bool:
    """Check if malicious URL has a different domain from original URL"""
    original_domain = extract_domain(original_url)
    malicious_domain = extract_domain(malicious_url)
    
    if not original_domain or not malicious_domain:
        return False
        
    return original_domain != malicious_domain

def load_all_model_data() -> Dict[str, List[Dict]]:
    """Load data from all 4 model classification folders"""
    models_data = {}
    
    model_folders = [
        'azure_gpt-4o',
        'azure_gpt-4o-mini', 
        'openrouter_deepseek_deepseek-chat-v3-0324',
        'openrouter_meta-llama_llama-4-scout'
    ]
    
    # Load all categories for each model
    for model_folder in model_folders:
        model_entries = []
        
        # Load all 4 categories
        category_files = [
            'category_1_url_directly_mentioned.json',
            'category_2_any_platform_name_same_domain.json',
            'category_3_any_platform_name_different_domain.json',
            'category_4_others.json'
        ]
        
        for category_file in category_files:
            file_path = os.path.join(model_folder, category_file)
            
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        model_entries.extend(data)
                        print(f"Loaded {len(data)} entries from {model_folder}/{category_file}")
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
        
        if model_entries:
            # Convert folder name back to model identifier
            model_name = model_folder.replace('_', '/')
            if model_name.startswith('openrouter'):
                model_name = model_name.replace('openrouter', 'openrouter', 1)
            
            models_data[model_name] = model_entries
            print(f"Total entries for {model_name}: {len(model_entries)}")
    
    return models_data

def count_prompts_by_model_coverage(models_data: Dict[str, List[Dict]]) -> Dict[int, int]:
    """
    Count unique prompts by how many models they affect
    
    Returns:
        Dict mapping number_of_models -> count_of_unique_prompts
    """
    
    # Create mapping: normalized_prompt -> set of models that have this prompt
    prompt_to_models = defaultdict(set)
    
    # Process each model's data
    for model_name, entries in models_data.items():
        print(f"\nProcessing {model_name} with {len(entries)} entries...")
        
        for entry in entries:
            prompt = entry.get('prompt', '')
            if prompt:  # Only process non-empty prompts
                normalized_prompt = normalize_prompt(prompt)
                
                # Skip very short prompts to avoid noise
                if len(normalized_prompt) > 10:
                    prompt_to_models[normalized_prompt].add(model_name)
    
    # Count prompts by number of models they affect
    coverage_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    
    for normalized_prompt, affected_models in prompt_to_models.items():
        num_models = len(affected_models)
        if num_models in coverage_counts:
            coverage_counts[num_models] += 1
    
    return coverage_counts, prompt_to_models

def analyze_prompt_model_coverage():
    """
    Main analysis function to count unique prompts by model coverage
    """
    print("=== PROMPT MODEL COVERAGE ANALYSIS ===")
    print("Loading data from all model classification files...")
    
    # Load all model data
    models_data = load_all_model_data()
    
    if len(models_data) != 4:
        print(f"Warning: Expected 4 models, found {len(models_data)}")
        print(f"Available models: {list(models_data.keys())}")
    
    total_entries = sum(len(entries) for entries in models_data.values())
    print(f"\nTotal entries across all models: {total_entries:,}")
    
    # Analyze prompt coverage
    print("\nAnalyzing unique prompts by model coverage...")
    coverage_counts, prompt_to_models = count_prompts_by_model_coverage(models_data)
    
    # Display results
    print("\n" + "="*60)
    print("RESULTS: Unique Prompts by Model Coverage")
    print("="*60)
    
    total_unique_prompts = sum(coverage_counts.values())
    print(f"Total unique prompts: {total_unique_prompts:,}")
    print()
    
    for num_models in [4, 3, 2, 1]:
        count = coverage_counts[num_models]
        percentage = (count / total_unique_prompts * 100) if total_unique_prompts > 0 else 0
        
        print(f"Prompts affecting {num_models} model(s): {count:,} ({percentage:.1f}%)")
    
    # Additional insights
    print("\n" + "="*60)
    print("INSIGHTS")
    print("="*60)
    
    cross_model_prompts = coverage_counts[4] + coverage_counts[3] + coverage_counts[2]
    cross_model_percentage = (cross_model_prompts / total_unique_prompts * 100) if total_unique_prompts > 0 else 0
    
    print(f"Prompts affecting multiple models: {cross_model_prompts:,} ({cross_model_percentage:.1f}%)")
    print(f"Prompts affecting only one model: {coverage_counts[1]:,} ({100-cross_model_percentage:.1f}%)")
    
    # Show some examples of highly shared prompts
    print(f"\nExamples of prompts affecting all 4 models:")
    print("-" * 50)
    
    examples_shown = 0
    for normalized_prompt, affected_models in prompt_to_models.items():
        if len(affected_models) == 4 and examples_shown < 5:
            # Get original prompt (from first model's data)
            original_prompt = ""
            for model_name, entries in models_data.items():
                for entry in entries:
                    if normalize_prompt(entry.get('prompt', '')) == normalized_prompt:
                        original_prompt = entry.get('prompt', '')
                        break
                if original_prompt:
                    break
            
            print(f"{examples_shown + 1}. {original_prompt[:100]}{'...' if len(original_prompt) > 100 else ''}")
            print(f"   Models: {', '.join(sorted(affected_models))}")
            print()
            examples_shown += 1
    
    return coverage_counts, prompt_to_models

def analyze_category1_shared_prompts_domain_differences():
    """
    Analyze Category 1 shared prompts (shared by 4 models) to count how many
    trigger at least one LLM to generate malicious URLs with different domains
    """
    print("\n" + "="*80)
    print("CATEGORY 1 SHARED PROMPTS DOMAIN DIFFERENCE ANALYSIS")
    print("="*80)
    
    # Load category1 shared prompts report
    try:
        with open('../category1_shared_prompts_report.json', 'r', encoding='utf-8') as f:
            category1_data = json.load(f)
    except FileNotFoundError:
        print("Error: category1_shared_prompts_report.json not found!")
        print("Make sure the file exists in the parent directory.")
        return
    
    # Get prompts shared by all 4 models
    shared_by_4_models = category1_data.get('shared_prompts', {}).get('4', [])
    total_shared_prompts = len(shared_by_4_models)
    
    print(f"Total prompts shared by all 4 models: {total_shared_prompts:,}")
    
    if total_shared_prompts == 0:
        print("No prompts shared by all 4 models found.")
        return
    
    # Analyze each shared prompt
    prompts_with_different_domains = 0
    detailed_analysis = []
    
    for i, prompt_info in enumerate(shared_by_4_models):
        prompt_text = prompt_info.get('prompt', '')
        entries_by_model = prompt_info.get('entries_by_model', {})
        
        # Check if any model generated a malicious URL with different domain
        has_different_domain = False
        domain_analysis = {
            'prompt': prompt_text[:150] + ('...' if len(prompt_text) > 150 else ''),
            'models_with_different_domains': [],
            'examples': []
        }
        
        for model_name, entries in entries_by_model.items():
            model_has_different_domain = False
            
            for entry in entries:
                original_url = entry.get('original_url', '')
                malicious_url = entry.get('malicious_url', '')
                
                if domains_are_different(original_url, malicious_url):
                    has_different_domain = True
                    model_has_different_domain = True
                    
                    # Store example
                    domain_analysis['examples'].append({
                        'model': model_name,
                        'original_url': original_url,
                        'malicious_url': malicious_url,
                        'original_domain': extract_domain(original_url),
                        'malicious_domain': extract_domain(malicious_url)
                    })
                    
                    break  # Only need one example per model
            
            if model_has_different_domain:
                domain_analysis['models_with_different_domains'].append(model_name)
        
        if has_different_domain:
            prompts_with_different_domains += 1
            detailed_analysis.append(domain_analysis)
        
        # Progress indicator for large datasets
        if (i + 1) % 500 == 0:
            print(f"Processed {i + 1:,} / {total_shared_prompts:,} prompts...")
    
    # Results
    percentage = (prompts_with_different_domains / total_shared_prompts * 100) if total_shared_prompts > 0 else 0
    
    print(f"\n" + "="*60)
    print("RESULTS")
    print("="*60)
    print(f"Prompts triggering different-domain malicious URLs: {prompts_with_different_domains:,} / {total_shared_prompts:,} ({percentage:.1f}%)")
    print(f"Prompts staying within same domain: {total_shared_prompts - prompts_with_different_domains:,} ({100-percentage:.1f}%)")
    
    # Show examples
    print(f"\n" + "="*60)
    print("EXAMPLES OF PROMPTS WITH DIFFERENT DOMAINS")
    print("="*60)
    
    examples_to_show = min(5, len(detailed_analysis))
    for i in range(examples_to_show):
        analysis = detailed_analysis[i]
        print(f"\n{i+1}. PROMPT: {analysis['prompt']}")
        print(f"   Models with different domains: {len(analysis['models_with_different_domains'])}/4")
        print(f"   Models: {', '.join(analysis['models_with_different_domains'])}")
        
        # Show one example
        if analysis['examples']:
            example = analysis['examples'][0]
            print(f"   Example:")
            print(f"     Original domain: {example['original_domain']}")
            print(f"     Malicious domain: {example['malicious_domain']}")
            print(f"     Model: {example['model']}")
    
    # Domain statistics
    print(f"\n" + "="*60)
    print("DOMAIN ANALYSIS STATISTICS")
    print("="*60)
    
    # Count unique malicious domains that are different from original
    all_different_domains = set()
    domain_frequency = defaultdict(int)
    
    for analysis in detailed_analysis:
        for example in analysis['examples']:
            malicious_domain = example['malicious_domain']
            all_different_domains.add(malicious_domain)
            domain_frequency[malicious_domain] += 1
    
    print(f"Unique malicious domains (different from original): {len(all_different_domains)}")
    
    # Show top malicious domains
    if domain_frequency:
        print(f"\nTop 10 most frequent different malicious domains:")
        sorted_domains = sorted(domain_frequency.items(), key=lambda x: x[1], reverse=True)
        for i, (domain, count) in enumerate(sorted_domains[:10]):
            print(f"  {i+1}. {domain}: {count} occurrences")
    
    return {
        'total_shared_prompts': total_shared_prompts,
        'prompts_with_different_domains': prompts_with_different_domains,
        'percentage': percentage,
        'detailed_analysis': detailed_analysis
    }

if __name__ == "__main__":
    # Run the original analysis
    print("Running original prompt model coverage analysis...")
    coverage_counts, prompt_to_models = analyze_prompt_model_coverage()
    
    # Run the new Category 1 domain difference analysis
    print("\n" + "="*80)
    print("Running Category 1 shared prompts domain difference analysis...")
    domain_analysis_results = analyze_category1_shared_prompts_domain_differences()
