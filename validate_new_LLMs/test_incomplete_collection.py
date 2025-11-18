#!/usr/bin/env python3
"""
Test Script for Incomplete Prompts Collection

This script tests the incomplete prompts collection functionality with a small subset
of data before running the full collection.
"""

import json
from pathlib import Path
from collect_incomplete_prompts import IncompletePromptsCollector


def test_single_model_collection(model_identifier: str = "openai/gpt-5", max_files: int = 10):
    """Test collection for a single model with limited files"""
    print(f"🧪 Testing incomplete prompts collection for {model_identifier}")
    print("=" * 60)
    
    # Create a test collector
    collector = IncompletePromptsCollector(output_base_dir="test_incomplete_collection")
    
    # Test single model collection
    try:
        collection_data = collector.collect_incomplete_for_model(model_identifier)
        
        print(f"\n📊 Test Results:")
        print(f"   Model: {model_identifier}")
        print(f"   Incomplete prompts found: {len(collection_data['incomplete_prompts'])}")
        print(f"   Incomplete files found: {len(collection_data['incomplete_files'])}")
        
        if collection_data['incomplete_prompts']:
            # Show first few examples
            print(f"\n📝 First few incomplete prompts:")
            for i, prompt in enumerate(collection_data['incomplete_prompts'][:3]):
                print(f"   {i+1}. Prompt {prompt['prompt_index']}: {prompt['prompt'][:80]}...")
                print(f"      File: {Path(prompt['python_file']).name}")
                print(f"      Classification: {prompt['classification']}")
        
        # Test saving functionality
        if collection_data['incomplete_prompts']:
            print(f"\n💾 Testing save functionality...")
            collector.save_model_collection(model_identifier, collection_data)
            
            # Verify saved files
            sanitized_model = model_identifier.replace('/', '_')
            model_output_dir = collector.output_dir / sanitized_model
            
            prompts_file = model_output_dir / "prompts" / f"{sanitized_model}_incomplete_prompts.json"
            files_dir = model_output_dir / "files"
            
            if prompts_file.exists():
                print(f"   ✅ Prompts file saved: {prompts_file}")
                with open(prompts_file, 'r') as f:
                    saved_data = json.load(f)
                print(f"   📄 Saved {len(saved_data['incomplete_prompts'])} prompts")
            
            if files_dir.exists():
                copied_files = list(files_dir.glob("*.py"))
                print(f"   ✅ Files directory created: {files_dir}")
                print(f"   📁 Copied {len(copied_files)} Python files")
        
        return True, collection_data
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False, None


def test_classification_accuracy():
    """Test that our classification logic correctly identifies incomplete files"""
    print(f"\n🔍 Testing classification accuracy...")
    
    from focused_validation_analyzer import FocusedValidationAnalyzer
    analyzer = FocusedValidationAnalyzer()
    
    # Test with a few known files
    test_cases = [
        # These should be examples from the validation results
        ("validation_results/openai_gpt-5/generated_code", "incomplete"),
        ("validation_results/google_gemini-2.5-pro/generated_code", "content_filtered"),
    ]
    
    for test_dir, expected_type in test_cases:
        test_path = Path(test_dir)
        if test_path.exists():
            py_files = list(test_path.glob("*.py"))[:5]  # Test first 5 files
            
            print(f"   Testing {len(py_files)} files from {test_dir}")
            
            type_counts = {}
            for py_file in py_files:
                classification = analyzer.categorize_python_file_completion(py_file)
                type_counts[classification] = type_counts.get(classification, 0) + 1
            
            print(f"   Results: {type_counts}")
            
            if expected_type in type_counts:
                print(f"   ✅ Found expected type '{expected_type}'")
            else:
                print(f"   ⚠️  Expected type '{expected_type}' not found")
    
    return True


def main():
    """Run all tests"""
    print("🚀 Starting Incomplete Prompts Collection Tests")
    print("=" * 80)
    
    # Test 1: Classification accuracy
    print("TEST 1: Classification Logic")
    test_classification_accuracy()
    
    # Test 2: Single model collection
    print(f"\nTEST 2: Single Model Collection")
    success, data = test_single_model_collection("openai/gpt-5")
    
    if success and data and data['incomplete_prompts']:
        print(f"\n✅ Tests PASSED!")
        print(f"   Ready to run full collection")
        print(f"   Expected incomplete prompts for openai/gpt-5: {len(data['incomplete_prompts'])}")
        
        # Ask user if they want to proceed with full collection
        response = input(f"\n🤔 Run full collection for all models? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            print(f"\n🚀 Running full collection...")
            from collect_incomplete_prompts import main as run_full_collection
            output_dir = run_full_collection()
            
            if output_dir:
                print(f"\n🎉 Full collection completed!")
                print(f"📁 Output directory: {output_dir}")
                return output_dir
        else:
            print(f"✋ Full collection skipped by user")
            return None
    else:
        print(f"\n❌ Tests FAILED!")
        print(f"   Please check the implementation before running full collection")
        return None


if __name__ == "__main__":
    main()

