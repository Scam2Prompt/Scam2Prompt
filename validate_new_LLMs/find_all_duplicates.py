#!/usr/bin/env python3
"""
Comprehensive Duplicate File Detector

Scans all problematic prompts and reports duplicate files with complete paths
for manual review and decision-making.
"""

import json
import hashlib
import sys
from pathlib import Path
from typing import List, Dict, Any, Tuple

# Add current directory to path
sys.path.append('.')

from rerun_problematic_prompts import ProblematicPromptsReRunner


def find_all_duplicates(model_identifier: str = 'openai/gpt-5') -> List[Dict[str, Any]]:
    """Find all duplicate files for the specified model"""
    
    # Load the problematic prompts file
    sanitized_model = model_identifier.replace('/', '_')
    collection_dir = Path('problematic_files_collection_20250922_003407')
    prompts_file = collection_dir / sanitized_model / "prompts" / f"{sanitized_model}_problematic_prompts.json"
    
    if not prompts_file.exists():
        print(f"❌ Prompts file not found: {prompts_file}")
        return []
    
    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    prompts_list = data.get('problematic_prompts', [])
    print(f"📊 Scanning {len(prompts_list)} problematic prompts for duplicates...")
    
    # Initialize rerunner for categorization
    rerunner = ProblematicPromptsReRunner(model_identifier)
    
    duplicates = []
    
    for i, prompt_info in enumerate(prompts_list):
        if i % 100 == 0:
            print(f"   Progress: {i}/{len(prompts_list)}")
            
        prompt_idx = prompt_info.get('prompt_index')
        prompt_hash = hashlib.md5(prompt_info['prompt'].encode()).hexdigest()[:8]
        filename = f'{sanitized_model}_validation_{prompt_idx:03d}_{prompt_hash}.py'
        
        # Check if files exist in both directories
        generated_file = Path(f'validation_results/{sanitized_model}/generated_code/{filename}')
        malicious_file = Path(f'validation_results/{sanitized_model}/malicious_code/{filename}')
        
        if generated_file.exists() and malicious_file.exists():
            # Categorize both files
            try:
                gen_category = rerunner.categorize_python_file_completion(generated_file)
                mal_category = rerunner.categorize_python_file_completion(malicious_file)
                
                # Get file sizes and modification times
                gen_size = generated_file.stat().st_size
                mal_size = malicious_file.stat().st_size
                gen_mtime = generated_file.stat().st_mtime
                mal_mtime = malicious_file.stat().st_mtime
                
                # Determine recommendation
                priority_order = {
                    'completed': 5,
                    'content_filtered': 4, 
                    'repeated': 3,
                    'unfinished_special': 3,
                    'unfinished_others': 3,
                    'incomplete': 1
                }
                
                gen_priority = priority_order.get(gen_category, 0)
                mal_priority = priority_order.get(mal_category, 0)
                
                if mal_priority > gen_priority:
                    recommended_keep = 'malicious'
                    recommended_remove = 'generated'
                elif gen_priority > mal_priority:
                    recommended_keep = 'generated'
                    recommended_remove = 'malicious'
                else:
                    # Same priority - prefer malicious_code
                    recommended_keep = 'malicious'
                    recommended_remove = 'generated'
                
                duplicate_info = {
                    'prompt_index': prompt_idx,
                    'prompt_hash': prompt_hash,
                    'filename': filename,
                    'generated_file': generated_file.absolute(),
                    'malicious_file': malicious_file.absolute(),
                    'generated_category': gen_category,
                    'malicious_category': mal_category,
                    'generated_size': gen_size,
                    'malicious_size': mal_size,
                    'generated_mtime': gen_mtime,
                    'malicious_mtime': mal_mtime,
                    'recommended_keep': recommended_keep,
                    'recommended_remove': recommended_remove,
                    'collection_points_to': prompt_info.get('python_file', ''),
                    'prompt_preview': prompt_info.get('prompt', '')[:100] + '...'
                }
                
                duplicates.append(duplicate_info)
                
            except Exception as e:
                print(f"   ⚠️  Error processing prompt {prompt_idx}: {e}")
    
    return duplicates


def print_duplicates_report(duplicates: List[Dict[str, Any]]) -> None:
    """Print a comprehensive report of all duplicates"""
    
    if not duplicates:
        print("✅ No duplicate files found!")
        return
    
    print(f"\n🔍 DUPLICATE FILES REPORT")
    print(f"=" * 80)
    print(f"Found {len(duplicates)} duplicate files that need manual review")
    print()
    
    for i, dup in enumerate(duplicates, 1):
        print(f"📄 DUPLICATE #{i}: Prompt {dup['prompt_index']}")
        print(f"   Prompt: {dup['prompt_preview']}")
        print(f"   Collection points to: {dup['collection_points_to']}")
        print()
        print(f"   🗂️  GENERATED FILE:")
        print(f"      Path: {dup['generated_file']}")
        print(f"      Category: {dup['generated_category']}")
        print(f"      Size: {dup['generated_size']:,} bytes")
        print()
        print(f"   🗂️  MALICIOUS FILE:")
        print(f"      Path: {dup['malicious_file']}")
        print(f"      Category: {dup['malicious_category']}")
        print(f"      Size: {dup['malicious_size']:,} bytes")
        print()
        print(f"   💡 RECOMMENDATION:")
        print(f"      Keep: {dup['recommended_keep'].upper()} file ({dup[f'{dup[\"recommended_keep\"]}_category']})")
        print(f"      Remove: {dup['recommended_remove'].upper()} file ({dup[f'{dup[\"recommended_remove\"]}_category']})")
        print()
        print(f"   🗑️  TO REMOVE: {dup[f'{dup[\"recommended_remove\"]}_file']}")
        print(f"   ✅ TO KEEP: {dup[f'{dup[\"recommended_keep\"]}_file']}")
        print()
        print("-" * 80)
        print()


def save_duplicates_csv(duplicates: List[Dict[str, Any]], filename: str = 'duplicate_files_review.csv') -> None:
    """Save duplicates to CSV for easy review"""
    
    if not duplicates:
        return
    
    import csv
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'Prompt_Index', 'Filename', 'Generated_Path', 'Malicious_Path',
            'Generated_Category', 'Malicious_Category', 'Generated_Size', 'Malicious_Size',
            'Recommended_Keep', 'Recommended_Remove', 'Collection_Points_To', 'Prompt_Preview'
        ])
        
        # Data
        for dup in duplicates:
            writer.writerow([
                dup['prompt_index'],
                dup['filename'],
                dup['generated_file'],
                dup['malicious_file'],
                dup['generated_category'],
                dup['malicious_category'],
                dup['generated_size'],
                dup['malicious_size'],
                dup['recommended_keep'],
                dup['recommended_remove'],
                dup['collection_points_to'],
                dup['prompt_preview']
            ])
    
    print(f"📊 Saved duplicate files report to: {filename}")


def main():
    """Main function"""
    print("🔍 Comprehensive Duplicate File Detection")
    print("=" * 50)
    
    # Find all duplicates
    duplicates = find_all_duplicates('openai/gpt-5')
    
    # Print report
    print_duplicates_report(duplicates)
    
    # Save CSV
    save_duplicates_csv(duplicates)
    
    if duplicates:
        print(f"\n📋 SUMMARY:")
        print(f"   Total duplicates found: {len(duplicates)}")
        print(f"   Review the paths above and manually delete the files you don't want to keep")
        print(f"   CSV report saved for spreadsheet review")


if __name__ == "__main__":
    main()
