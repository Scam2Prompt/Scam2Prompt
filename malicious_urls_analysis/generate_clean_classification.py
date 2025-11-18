#!/usr/bin/env python3
"""
Script to generate clean, model-organized classification results
"""

import json
import csv
import os
from collections import defaultdict
from typing import Dict, List

def load_final_classification():
    """Load the final classification results"""
    with open('classified_malicious_urls_final.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_entry(entry: Dict) -> Dict:
    """Clean entry to keep only essential information"""
    return {
        'original_url': entry.get('original_url', ''),
        'malicious_url': entry.get('malicious_url', ''),
        'prompt': entry.get('prompt', ''),
        'model_identifier': entry.get('model_identifier', ''),
        'classification': {
            'category': entry['classification']['category'],
            'category_description': entry['classification']['category_description']
        }
    }

def organize_by_model(classified_entries: List[Dict]) -> Dict[str, Dict[int, List[Dict]]]:
    """Organize entries by model and category"""
    model_data = defaultdict(lambda: defaultdict(list))
    
    for entry in classified_entries:
        cleaned_entry = clean_entry(entry)
        model = cleaned_entry['model_identifier']
        category = cleaned_entry['classification']['category']
        
        model_data[model][category].append(cleaned_entry)
    
    return model_data

def create_model_folders(model_data: Dict[str, Dict[int, List[Dict]]]):
    """Create folders and files for each model"""
    
    # Create models directory
    models_dir = 'models_classification'
    if os.path.exists(models_dir):
        import shutil
        shutil.rmtree(models_dir)
    os.makedirs(models_dir)
    
    category_descriptions = {
        1: "url_directly_mentioned",
        2: "platform_name_same_domain", 
        3: "platform_name_different_domain",
        4: "others"
    }
    
    overall_summary = {
        'total_entries': 0,
        'models': {}
    }
    
    for model, categories in model_data.items():
        # Clean model name for folder
        model_folder = model.replace('/', '_').replace(':', '_')
        model_path = os.path.join(models_dir, model_folder)
        os.makedirs(model_path)
        
        model_total = sum(len(entries) for entries in categories.values())
        overall_summary['total_entries'] += model_total
        
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
            
            # Create CSV summary for category
            csv_filename = f'category_{category}_{category_descriptions[category]}_summary.csv'
            csv_path = os.path.join(model_path, csv_filename)
            
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['original_url', 'malicious_url', 'prompt_preview'])
                
                for entry in entries[:500]:  # Limit to 500 for readability
                    prompt_preview = entry['prompt'][:100] + "..." if len(entry['prompt']) > 100 else entry['prompt']
                    writer.writerow([
                        entry['original_url'],
                        entry['malicious_url'],
                        prompt_preview
                    ])
            
            model_summary['categories'][f'category_{category}'] = {
                'description': category_descriptions[category],
                'count': count,
                'percentage': round(percentage, 1)
            }
        
        # Save model summary
        model_summary_path = os.path.join(model_path, 'model_summary.json')
        with open(model_summary_path, 'w', encoding='utf-8') as f:
            json.dump(model_summary, f, indent=2, ensure_ascii=False)
        
        # Create model overview CSV
        model_csv_path = os.path.join(model_path, 'model_overview.csv')
        with open(model_csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['category', 'description', 'count', 'percentage'])
            
            for category in [1, 2, 3, 4]:
                cat_info = model_summary['categories'][f'category_{category}']
                writer.writerow([
                    category,
                    cat_info['description'],
                    cat_info['count'],
                    cat_info['percentage']
                ])
        
        overall_summary['models'][model] = model_summary
    
    # Save overall summary
    overall_summary_path = os.path.join(models_dir, 'overall_summary.json')
    with open(overall_summary_path, 'w', encoding='utf-8') as f:
        json.dump(overall_summary, f, indent=2, ensure_ascii=False)
    
    return overall_summary

def create_consolidated_summaries(model_data: Dict[str, Dict[int, List[Dict]]]):
    """Create consolidated summary files"""
    
    # Create consolidated category comparison
    category_comparison = {
        'categories': {
            1: {'description': 'URL directly mentioned', 'models': {}},
            2: {'description': 'Platform name + same domain', 'models': {}},
            3: {'description': 'Platform name + different domain', 'models': {}},
            4: {'description': 'Others', 'models': {}}
        }
    }
    
    for model, categories in model_data.items():
        model_total = sum(len(entries) for entries in categories.values())
        
        for category in [1, 2, 3, 4]:
            count = len(categories.get(category, []))
            percentage = (count / model_total * 100) if model_total > 0 else 0
            
            category_comparison['categories'][category]['models'][model] = {
                'count': count,
                'percentage': round(percentage, 1)
            }
    
    with open('models_classification/category_comparison.json', 'w', encoding='utf-8') as f:
        json.dump(category_comparison, f, indent=2, ensure_ascii=False)
    
    # Create comparison CSV
    with open('models_classification/category_comparison.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        models = list(model_data.keys())
        header = ['category', 'description'] + [f'{model}_count' for model in models] + [f'{model}_percent' for model in models]
        writer.writerow(header)
        
        for category in [1, 2, 3, 4]:
            cat_info = category_comparison['categories'][category]
            row = [category, cat_info['description']]
            
            # Add counts
            for model in models:
                row.append(cat_info['models'][model]['count'])
            
            # Add percentages
            for model in models:
                row.append(f"{cat_info['models'][model]['percentage']}%")
            
            writer.writerow(row)

def cleanup_old_files():
    """Remove large unnecessary files"""
    files_to_remove = [
        'classified_malicious_urls_final.json',
        'classified_malicious_urls_initial.json',
        'category_1_url_directly_mentioned_final.json',
        'category_1_url_directly_mentioned_initial.json',
        'category_2_platform_name_same_domain_final.json',
        'category_2_platform_name_same_domain_initial.json',
        'category_3_platform_name_different_domain_final.json',
        'category_3_platform_name_different_domain_initial.json',
        'category_4_others_final.json',
        'category_4_others_initial.json',
        'uncertain_cases_for_gpt4o_mini.json'
    ]
    
    removed_count = 0
    for filename in files_to_remove:
        if os.path.exists(filename):
            os.remove(filename)
            removed_count += 1
    
    print(f"Removed {removed_count} large unnecessary files")

def main():
    print("Loading final classification results...")
    classified_entries = load_final_classification()
    print(f"Loaded {len(classified_entries)} classified entries")
    
    print("\nOrganizing entries by model...")
    model_data = organize_by_model(classified_entries)
    print(f"Found {len(model_data)} models")
    
    print("\nCreating model-specific folders and files...")
    overall_summary = create_model_folders(model_data)
    
    print("\nCreating consolidated summaries...")
    create_consolidated_summaries(model_data)
    
    print("\nCleaning up large unnecessary files...")
    cleanup_old_files()
    
    print("\n=== CLEAN CLASSIFICATION SUMMARY ===")
    print(f"Total entries: {overall_summary['total_entries']}")
    print(f"Models processed: {len(overall_summary['models'])}")
    
    print(f"\nModel breakdown:")
    for model, summary in overall_summary['models'].items():
        print(f"  {model}: {summary['total_urls']} URLs")
        for cat_key, cat_data in summary['categories'].items():
            if cat_data['count'] > 0:
                print(f"    {cat_data['description']}: {cat_data['count']} ({cat_data['percentage']}%)")
    
    print(f"\n📁 Generated structure:")
    print(f"  models_classification/")
    for model in overall_summary['models'].keys():
        model_folder = model.replace('/', '_').replace(':', '_')
        print(f"    {model_folder}/")
        print(f"      ├── category_1_url_directly_mentioned.json")
        print(f"      ├── category_2_platform_name_same_domain.json") 
        print(f"      ├── category_3_platform_name_different_domain.json")
        print(f"      ├── category_4_others.json")
        print(f"      ├── category_*_summary.csv (4 files)")
        print(f"      ├── model_summary.json")
        print(f"      └── model_overview.csv")
    
    print(f"    overall_summary.json")
    print(f"    category_comparison.json")
    print(f"    category_comparison.csv")

if __name__ == "__main__":
    main()
