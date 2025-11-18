#!/usr/bin/env python3
"""
Script to extract shared prompts from category3_shared_prompts_report.json
and convert to markdown format as specified.
"""

import json
import os
from typing import Dict, List, Set
from collections import defaultdict

def clean_model_name(model_identifier: str) -> str:
    """Clean up model identifier to a shorter name."""
    model_mapping = {
        "azure/gpt-4o": "gpt-4o",
        "azure/gpt-4o-mini": "gpt-4o-mini", 
        "openrouter/deepseek/deepseek-chat-v3-0324": "deepseek-chat-v3-0324",
        "openrouter/meta-llama/llama-4-scout": "llama-4-scout"
    }
    return model_mapping.get(model_identifier, model_identifier)

def extract_shared_prompts_to_markdown(input_file: str, output_file: str):
    """Extract shared prompts and convert to markdown format."""
    
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract shared_prompts section
    shared_prompts = data.get('shared_prompts', {})
    
    markdown_content = []
    markdown_content.append("# Shared Prompts Analysis")
    markdown_content.append("")
    markdown_content.append("This document contains prompts that were shared across multiple LLM models and the malicious URLs they generated.")
    markdown_content.append("")
    
    # Add summary
    summary = data.get('summary', {})
    markdown_content.append("## Summary")
    markdown_content.append("")
    markdown_content.append(f"- **Shared by 4 models**: {summary.get('shared_by_4_models', 0)}")
    markdown_content.append(f"- **Shared by 3 models**: {summary.get('shared_by_3_models', 0)}")
    markdown_content.append(f"- **Shared by 2 models**: {summary.get('shared_by_2_models', 0)}")
    markdown_content.append(f"- **Total shared prompts**: {summary.get('total_shared_prompts', 0)}")
    markdown_content.append("")
    markdown_content.append("---")
    markdown_content.append("")
    
    # Process each category (4, 3, 2 models)
    for model_count in ['4', '3', '2']:
        if model_count not in shared_prompts:
            continue
            
        prompts_list = shared_prompts[model_count]
        if not prompts_list:
            continue
            
        markdown_content.append(f"## Prompts Shared by {model_count} Models")
        markdown_content.append("")
        
        for prompt_data in prompts_list:
            # Extract basic info
            prompt = prompt_data.get('prompt', '')
            entries_by_model = prompt_data.get('entries_by_model', {})
            
            # Get original URL (should be the same for all entries of this prompt)
            original_url = None
            for model_entries in entries_by_model.values():
                if model_entries:
                    original_url = model_entries[0].get('original_url', '')
                    break
            
            # Add prompt entry (no empty lines within entry)
            markdown_content.append(f"**Prompt**: {prompt}")
            markdown_content.append(f"**Original_url**: {original_url}")
            markdown_content.append("**Poisoned LLM**:")
            
            # Process each model in a consistent order
            model_order = ['azure/gpt-4o', 'azure/gpt-4o-mini', 'openrouter/deepseek/deepseek-chat-v3-0324', 'openrouter/meta-llama/llama-4-scout']
            counter = 1
            
            for model_identifier in model_order:
                if model_identifier not in entries_by_model:
                    continue
                    
                clean_name = clean_model_name(model_identifier)
                model_entries = entries_by_model[model_identifier]
                
                # Collect unique malicious URLs for this model
                malicious_urls = []
                for entry in model_entries:
                    malicious_url = entry.get('malicious_url', '')
                    if malicious_url and malicious_url not in malicious_urls:
                        malicious_urls.append(malicious_url)
                
                # Format the output - use tabs to separate multiple URLs
                if len(malicious_urls) == 1:
                    markdown_content.append(f"  {counter}. {clean_name}: malicious_url: {malicious_urls[0]}")
                else:
                    # Join multiple URLs with tabs
                    urls_joined = "\t".join(malicious_urls)
                    markdown_content.append(f"  {counter}. {clean_name}: malicious_url: {urls_joined}")
                
                counter += 1
            
            # Add TWO empty lines between entries
            markdown_content.append("")
            markdown_content.append("")
    
    # Write to output file
    print(f"Writing to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_content))
    
    print(f"Successfully converted {len(shared_prompts.get('4', [])) + len(shared_prompts.get('3', [])) + len(shared_prompts.get('2', []))} shared prompts to markdown format.")

def main():
    input_file = "category3_shared_prompts_report.json"
    output_file = "shared_prompts_analysis.md"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return
    
    extract_shared_prompts_to_markdown(input_file, output_file)
    print(f"Markdown file created: {output_file}")

if __name__ == "__main__":
    main()
