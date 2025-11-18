#!/usr/bin/env python3
"""
Clean Multi-Model Validation Runner

Iterates through all 7 models with 100 prompts each using filesystem-optimized caching.
Grok should be 100% cache hits since we already processed it.
"""

import asyncio
import json
import time
from pathlib import Path
from datetime import datetime
from filesystem_optimized_validation import run_filesystem_optimized_validation


async def run_all_models():
    """Run validation for all models with 100 prompts each"""
    
    models_to_test = [
        "x-ai/grok-code-fast-1",           # Should be 100% cache hits
        "deepseek/deepseek-chat-v3.1", 
        "openai/gpt-5",
        "qwen/qwen3-coder",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-pro",
        "anthropic/claude-sonnet-4"
    ]
    
    print("🚀 Multi-Model Validation with Filesystem Caching")
    print("=" * 60)
    print(f"🔧 Testing {len(models_to_test)} models with 2072 combined prompts each")
    print(f"📊 NEW Composition: Category 3 (704) + Category 1 (400) + Category 2 (968)")
    print(f"📁 Using validation_results/ as cache (no separate cache folder)")
    print(f"🎯 Expected: Grok should be 100% cache hits")
    
    overall_start_time = time.time()
    all_results = []
    
    for i, model in enumerate(models_to_test, 1):
        print(f"\n🎯 Progress: {i}/{len(models_to_test)} - {model}")
        print("-" * 50)
        
        model_start_time = time.time()
        
        try:
            results = await run_filesystem_optimized_validation(model, limit=None)
            model_duration = time.time() - model_start_time
            
            results["model_test_duration"] = model_duration
            all_results.append(results)
            
            # Print summary
            if "error" not in results:
                cache_rate = results.get('cache_hit_rate', 0)
                codes_generated = results.get('codes_generated', 0)
                malicious_files = results.get('malicious_code_files', 0)
                
                print(f"✅ {model}:")
                print(f"   🔧 Codes: {codes_generated}")
                print(f"   🚨 Malicious: {malicious_files}")
                print(f"   📁 Cache: {cache_rate:.1f}%")
                print(f"   ⏱️  Time: {model_duration:.1f}s")
                
                if cache_rate > 90:
                    print(f"   🎉 Excellent cache efficiency!")
                elif cache_rate > 50:
                    print(f"   👍 Good cache efficiency!")
                
            else:
                print(f"❌ {model}: Failed - {results['error']}")
                
        except Exception as e:
            print(f"❌ {model}: Exception - {e}")
            all_results.append({
                "model_identifier": model,
                "error": str(e),
                "model_test_duration": time.time() - model_start_time
            })
        
        # Brief pause between models
        if i < len(models_to_test):
            print("⏳ Brief pause before next model...")
            await asyncio.sleep(3)
    
    # Generate final summary
    total_duration = time.time() - overall_start_time
    successful_results = [r for r in all_results if "error" not in r]
    
    print(f"\n🎉 All Models Complete!")
    print("=" * 50)
    print(f"⏱️  Total time: {total_duration:.1f}s ({total_duration/60:.1f} min)")
    print(f"✅ Successful: {len(successful_results)}/{len(models_to_test)}")
    
    if successful_results:
        total_codes = sum(r.get('codes_generated', 0) for r in successful_results)
        total_malicious = sum(r.get('malicious_code_files', 0) for r in successful_results)
        avg_cache_rate = sum(r.get('cache_hit_rate', 0) for r in successful_results) / len(successful_results)
        
        print(f"🔧 Total codes generated: {total_codes}")
        print(f"🚨 Total malicious files: {total_malicious}")
        print(f"📁 Average cache rate: {avg_cache_rate:.1f}%")
        print(f"⚡ Overall rate: {total_codes/total_duration:.2f} codes/sec")
    
    # Save comprehensive results
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    results_file = Path("validation_results") / f"all_models_summary_{timestamp}.json"
    
    summary_data = {
        "test_info": {
            "timestamp": datetime.now().isoformat(),
            "total_models": len(models_to_test),
            "prompts_per_model": 100,
            "total_duration_seconds": total_duration,
            "successful_models": len(successful_results)
        },
        "model_results": all_results
    }
    
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(summary_data, f, indent=2)
    
    print(f"📋 Detailed results saved to: {results_file}")
    
    return summary_data


if __name__ == "__main__":
    asyncio.run(run_all_models())
