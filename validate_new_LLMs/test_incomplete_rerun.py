#!/usr/bin/env python3
"""
Test Script for Incomplete Prompts Re-runner

This script tests the incomplete prompts re-runner functionality with a small subset
of data before running the full re-run.
"""

import asyncio
from pathlib import Path
from rerun_incomplete_prompts import IncompletePromptsReRunner, rerun_model_incomplete_prompts


async def test_incomplete_rerun(model_identifier: str = "deepseek/deepseek-chat-v3.1", limit: int = 3):
    """Test incomplete prompts re-run for a single model with limited prompts"""
    print(f"🧪 Testing incomplete prompts re-run for {model_identifier}")
    print("=" * 60)
    
    try:
        # Test the re-runner
        results = await rerun_model_incomplete_prompts(model_identifier, limit=limit)
        
        print(f"\n📊 Test Results:")
        print(f"   Model: {model_identifier}")
        print(f"   Total incomplete prompts: {results.get('total_incomplete_prompts', 0)}")
        print(f"   Prompts processed: {results.get('prompts_processed', 0)}")
        print(f"   Codes generated: {results.get('codes_generated', 0)}")
        print(f"   Files overwritten: {results.get('files_overwritten', 0)}")
        print(f"   Cache hits: {results.get('cache_hits', 0)}")
        print(f"   Cache misses: {results.get('cache_misses', 0)}")
        print(f"   Completion improvement: +{results.get('completion_improvement', 0)} files")
        print(f"   Execution time: {results.get('execution_time_seconds', 0):.2f}s")
        
        if "error" in results:
            print(f"   ❌ Error: {results['error']}")
            return False, results
        else:
            print(f"   ✅ Test completed successfully!")
            return True, results
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False, None


async def verify_collection_exists():
    """Verify that the incomplete prompts collection exists"""
    print(f"🔍 Checking for incomplete prompts collection...")
    
    current_dir = Path.cwd()
    collection_dirs = list(current_dir.glob("incomplete_prompts_collection_*"))
    
    if not collection_dirs:
        print(f"❌ No incomplete_prompts_collection directories found!")
        print(f"   Please run collect_incomplete_prompts.py first.")
        return False, None
    
    # Sort by timestamp (newest first)
    collection_dirs.sort(key=lambda x: x.name.split('_')[-1], reverse=True)
    latest_dir = collection_dirs[0]
    
    print(f"✅ Found collection directory: {latest_dir}")
    
    # Check if it has model directories
    model_dirs = [d for d in latest_dir.iterdir() if d.is_dir() and d.name != "collection_summary.json"]
    print(f"📁 Model directories found: {len(model_dirs)}")
    
    for model_dir in model_dirs[:3]:  # Show first 3
        prompts_file = model_dir / "prompts" / f"{model_dir.name}_incomplete_prompts.json"
        if prompts_file.exists():
            import json
            with open(prompts_file, 'r') as f:
                data = json.load(f)
            incomplete_count = len(data.get('incomplete_prompts', []))
            print(f"   - {model_dir.name}: {incomplete_count} incomplete prompts")
        else:
            print(f"   - {model_dir.name}: ❌ prompts file not found")
    
    if len(model_dirs) > 3:
        print(f"   ... and {len(model_dirs) - 3} more models")
    
    return True, str(latest_dir)


async def main():
    """Run all tests"""
    print("🚀 Starting Incomplete Prompts Re-runner Tests")
    print("=" * 80)
    
    # Test 1: Verify collection exists
    print("TEST 1: Collection Verification")
    collection_exists, collection_dir = await verify_collection_exists()
    
    if not collection_exists:
        print(f"\n❌ Tests FAILED - Collection not found!")
        print(f"   Please run: python3 collect_incomplete_prompts.py")
        return
    
    # Test 2: Single model re-run test
    print(f"\nTEST 2: Single Model Re-run Test")
    success, data = await test_incomplete_rerun("deepseek/deepseek-chat-v3.1", limit=3)
    
    if success and data:
        print(f"\n✅ Tests PASSED!")
        print(f"   Ready to run full incomplete prompts re-run")
        print(f"   Collection directory: {collection_dir}")
        
        # Show what would happen in full run
        print(f"\n📊 Full Run Preview:")
        print(f"   This would re-run ALL incomplete prompts for ALL models")
        print(f"   Expected to significantly improve completion rates")
        print(f"   Files will be overwritten with new 20k token results")
        
        # Ask user if they want to proceed with full re-run
        response = input(f"\n🤔 Run full incomplete prompts re-run for all models? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            print(f"\n🚀 Running full incomplete prompts re-run...")
            from rerun_incomplete_prompts import run_all_models_incomplete_experiment
            await run_all_models_incomplete_experiment(collection_dir)
            
            print(f"\n🎉 Full incomplete prompts re-run completed!")
        else:
            print(f"✋ Full re-run skipped by user")
            print(f"   You can run it later with: python3 rerun_incomplete_prompts.py")
    else:
        print(f"\n❌ Tests FAILED!")
        print(f"   Please check the implementation before running full re-run")


if __name__ == "__main__":
    asyncio.run(main())
