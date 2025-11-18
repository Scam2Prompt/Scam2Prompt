#!/usr/bin/env python3
"""
Demo script for quick URL availability checking (optimized for malicious URLs)
"""

import asyncio
import json
import os
from web_accessor import WebAccessor
from async_web_accessor import AsyncWebAccessor

def analyze_results(results, test_name=""):
    """Analyze and validate the results against expectations"""
    print(f"\n📊 {test_name} RESULTS ANALYSIS:")
    print("=" * 60)
    
    # Categorize results
    available = []
    unavailable = []
    errors = []
    https_success = []
    http_fallback = []
    redirects = []
    
    for url, result in results.items():
        if result['available']:
            available.append((url, result))
            if result.get('protocol_used') == 'https':
                https_success.append(url)
            elif result.get('protocol_used') == 'http':
                http_fallback.append(url)
            
            if result['redirect_count'] > 0:
                redirects.append((url, result))
        else:
            unavailable.append((url, result))
            if result['error']:
                errors.append((url, result))
    
    # Summary statistics
    total = len(results)
    print(f"📈 Summary Statistics:")
    print(f"  Total URLs tested: {total}")
    print(f"  ✅ Available: {len(available)} ({len(available)/total*100:.1f}%)")
    print(f"  ❌ Unavailable: {len(unavailable)} ({len(unavailable)/total*100:.1f}%)")
    print(f"  ⚠️  With errors: {len(errors)} ({len(errors)/total*100:.1f}%)")
    print(f"  🔒 HTTPS success: {len(https_success)}")
    print(f"  🔓 HTTP fallback: {len(http_fallback)}")
    print(f"  🔄 With redirects: {len(redirects)}")
    
    # Expected vs Actual Analysis
    print(f"\n🎯 Expectation Validation:")
    
    # Expected available sites
    expected_available = [
        "https://example.com", "https://google.com", "https://github.com",
        "stackoverflow.com", "reddit.com", "wikipedia.org",
        "http://httpbin.org", "http://neverssl.com", "example.org"
    ]
    
    # Expected unavailable sites  
    expected_unavailable = [
        "https://nonexistent-domain-12345.com", "fake-domain-xyz-999.net",
        "this-domain-does-not-exist.com", "malicious-site.com", 
        "phishing-test.net", "fake-bank.org"
    ]
    
    # Expected redirects
    expected_redirects = ["bit.ly", "t.co"]
    
    # Validate expectations
    available_urls = [url for url, _ in available]
    unavailable_urls = [url for url, _ in unavailable]
    redirect_urls = [url for url, _ in redirects]
    
    correct_available = sum(1 for url in expected_available if url in available_urls)
    correct_unavailable = sum(1 for url in expected_unavailable if url in unavailable_urls)
    correct_redirects = sum(1 for url in expected_redirects if url in redirect_urls)
    
    print(f"  Expected available sites working: {correct_available}/{len(expected_available)}")
    print(f"  Expected unavailable sites failing: {correct_unavailable}/{len(expected_unavailable)}")
    print(f"  Expected redirects working: {correct_redirects}/{len(expected_redirects)}")
    
    # Show detailed results
    if available:
        print(f"\n✅ Available URLs ({len(available)}):")
        for url, result in available[:10]:  # Show first 10
            protocol = result.get('protocol_used', 'N/A')
            status = result['status_code']
            time_ms = result['response_time_ms']
            time_str = f"{time_ms:.0f}ms" if time_ms else "N/A"
            redirects_str = f" [{result['redirect_count']} redirects]" if result['redirect_count'] > 0 else ""
            print(f"    {url} → {status} [{protocol}] {time_str}{redirects_str}")
        
        if len(available) > 10:
            print(f"    ... and {len(available) - 10} more")
    
    if errors:
        print(f"\n❌ Error URLs ({len(errors)}):")
        for url, result in errors[:10]:  # Show first 10
            print(f"    {url} → {result['error']}")
        
        if len(errors) > 10:
            print(f"    ... and {len(errors) - 10} more")
    
    # Protocol analysis
    if https_success and http_fallback:
        print(f"\n🔐 Protocol Analysis:")
        print(f"  HTTPS worked for: {len(https_success)} URLs")
        print(f"  HTTP fallback for: {len(http_fallback)} URLs")
        if http_fallback:
            print(f"  HTTP fallback examples: {', '.join(http_fallback[:3])}")
    
    return {
        'total': total,
        'available': len(available),
        'unavailable': len(unavailable), 
        'errors': len(errors),
        'https_success': len(https_success),
        'http_fallback': len(http_fallback),
        'redirects': len(redirects)
    }

def demo_sync_quick_check():
    """Demo the synchronous quick check functions"""
    print("🔍 SYNCHRONOUS QUICK URL CHECK DEMO")
    print("=" * 50)
    
    # Comprehensive test URLs covering different scenarios
    test_urls = [
        # Valid HTTPS sites (should work)
        "https://example.com",
        "https://google.com",
        "https://github.com",
        
        # Valid sites without protocol (should auto-add https://)
        "stackoverflow.com",
        "reddit.com",
        "wikipedia.org",
        
        # HTTP-only sites (should fallback to HTTP)
        "http://httpbin.org",
        "http://neverssl.com",
        
        # Sites that might require HTTP fallback
        "httpforever.com",
        "example.org",
        
        # Non-existent domains (should fail)
        "https://nonexistent-domain-12345.com",
        "fake-domain-xyz-999.net",
        "this-domain-does-not-exist.com",
        
        # SSL/TLS test sites
        "expired.badssl.com",
        "wrong.host.badssl.com", 
        "self-signed.badssl.com",
        
        # Redirects (should follow)
        "bit.ly",
        "t.co",
        
        # Malicious-looking domains (for testing)
        "malicious-site.com",
        "phishing-test.net",
        "fake-bank.org"
    ]
    
    accessor = WebAccessor()
    
    # Single URL check for detailed analysis
    print("\n📋 Single URL Check (First 5 URLs):")
    for url in test_urls[:5]:
        print(f"\nChecking: {url}")
        result = accessor.quick_availability_check(url, timeout=5)
        
        print(f"  Available: {result['available']}")
        print(f"  Status: {result['status_code']}")
        response_time = result['response_time_ms']
        if response_time is not None:
            print(f"  Response Time: {response_time:.1f}ms")
        else:
            print(f"  Response Time: N/A")
        print(f"  Final URL: {result['final_url']}")
        print(f"  Protocol: {result.get('protocol_used', 'N/A')}")
        print(f"  Redirects: {result['redirect_count']}")
        if result['error']:
            print(f"  Error: {result['error']}")
    
    # Batch check
    print(f"\n📦 Batch Check ({len(test_urls)} URLs):")
    batch_results = accessor.batch_quick_check(test_urls, timeout=5, max_workers=10)
    
    # Analyze results and validate expectations
    sync_stats = analyze_results(batch_results, "SYNC")
    return batch_results, sync_stats

async def demo_async_quick_check():
    """Demo the asynchronous quick check functions"""
    print("\n\n🚀 ASYNCHRONOUS QUICK URL CHECK DEMO")
    print("=" * 50)
    
    # Use the same comprehensive test URLs as sync version
    test_urls = [
        # Valid HTTPS sites (should work)
        "https://example.com",
        "https://google.com",
        "https://github.com",
        
        # Valid sites without protocol (should auto-add https://)
        "stackoverflow.com",
        "reddit.com",
        "wikipedia.org",
        
        # HTTP-only sites (should fallback to HTTP)
        "http://httpbin.org",
        "http://neverssl.com",
        
        # Sites that might require HTTP fallback
        "httpforever.com",
        "example.org",
        
        # Non-existent domains (should fail)
        "https://nonexistent-domain-12345.com",
        "fake-domain-xyz-999.net",
        "this-domain-does-not-exist.com",
        
        # SSL/TLS test sites
        "expired.badssl.com",
        "wrong.host.badssl.com", 
        "self-signed.badssl.com",
        
        # Redirects (should follow)
        "bit.ly",
        "t.co",
        
        # Malicious-looking domains (for testing)
        "malicious-site.com",
        "phishing-test.net",
        "fake-bank.org"
    ]
    
    # Also test with some real phishing URLs if available
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "..", "scamDatabase", "phishingfort-lists.json")
    
    try:
        with open(json_path, "r") as f:
            scam_urls = json.load(f)
        # Add a small sample of real phishing URLs
        test_urls.extend(scam_urls[:10])  # First 10 URLs from phishing database
        print(f"📁 Added {len(scam_urls[:10])} URLs from phishing database")
    except FileNotFoundError:
        print(f"📁 Phishing database not found, using test URLs only")
    
    print(f"📋 Testing {len(test_urls)} URLs total")
    
    async with AsyncWebAccessor(max_concurrent=15, timeout=10) as accessor:
        # Single async URL check
        print(f"\n📋 Single Async URL Check:")
        sample_url = test_urls[0]
        print(f"Checking: {sample_url}")
        result = await accessor.quick_availability_check(sample_url, timeout=5)
        
        print(f"  Available: {result['available']}")
        print(f"  Status: {result['status_code']}")
        response_time = result['response_time_ms']
        if response_time is not None:
            print(f"  Response Time: {response_time:.1f}ms")
        else:
            print(f"  Response Time: N/A")
        print(f"  Final URL: {result['final_url']}")
        print(f"  Protocol: {result.get('protocol_used', 'N/A')}")
        if result['error']:
            print(f"  Error: {result['error']}")
        
        # Batch async check
        print(f"\n📦 Batch Async Check ({len(test_urls)} URLs):")
        batch_results = await accessor.batch_quick_check(
            test_urls, 
            timeout=5, 
            max_concurrent=15
        )
        
        # Analyze results with detailed validation
        async_stats = analyze_results(batch_results, "ASYNC")
        
        return batch_results, async_stats

def compare_methods():
    """Compare quick check vs regular check performance"""
    print("\n\n⚡ PERFORMANCE COMPARISON")
    print("=" * 50)
    
    test_urls = [
        "https://google.com",
        "https://github.com",
        "https://stackoverflow.com"
    ]
    
    accessor = WebAccessor()
    
    import time
    
    # Quick check timing
    print("🚀 Quick Check (HEAD requests):")
    start_time = time.time()
    quick_results = accessor.batch_quick_check(test_urls, timeout=5, max_workers=3)
    quick_time = time.time() - start_time
    
    # Regular check timing (for comparison)
    print(f"\n🐌 Regular Check (GET requests):")
    start_time = time.time()
    regular_results = {}
    for url in test_urls:
        result = accessor.check_accessibility(url)
        regular_results[url] = result
    regular_time = time.time() - start_time
    
    print(f"\n📊 Performance Comparison:")
    print(f"  Quick Check: {quick_time:.2f}s")
    print(f"  Regular Check: {regular_time:.2f}s")
    print(f"  Speed Improvement: {regular_time/quick_time:.1f}x faster")

def main():
    """Main demo function"""
    print("🌐 QUICK URL AVAILABILITY CHECKER DEMO")
    print("Optimized for checking potentially malicious URLs safely")
    print("=" * 60)
    
    # Run sync demo
    print("Starting synchronous tests...")
    sync_results, sync_stats = demo_sync_quick_check()
    
    # Run async demo
    print("\nStarting asynchronous tests...")
    async_results, async_stats = asyncio.run(demo_async_quick_check())
    
    # Compare sync vs async results
    print("\n" + "="*60)
    print("🔄 SYNC vs ASYNC COMPARISON")
    print("="*60)
    
    print(f"📊 Performance Comparison:")
    print(f"  Sync  - Available: {sync_stats['available']}/{sync_stats['total']} ({sync_stats['available']/sync_stats['total']*100:.1f}%)")
    print(f"  Async - Available: {async_stats['available']}/{async_stats['total']} ({async_stats['available']/async_stats['total']*100:.1f}%)")
    print(f"  Sync  - Errors: {sync_stats['errors']}")
    print(f"  Async - Errors: {async_stats['errors']}")
    print(f"  Sync  - HTTPS success: {sync_stats['https_success']}")
    print(f"  Async - HTTPS success: {async_stats['https_success']}")
    print(f"  Sync  - HTTP fallback: {sync_stats['http_fallback']}")
    print(f"  Async - HTTP fallback: {async_stats['http_fallback']}")
    
    # Compare performance
    compare_methods()
    
    print(f"\n🎉 Demo completed!")
    print(f"\n✅ VALIDATION SUMMARY:")
    
    # Check if results are consistent
    consistency_check = abs(sync_stats['available'] - async_stats['available']) <= 2  # Allow small variance
    print(f"  Sync/Async consistency: {'✅ PASSED' if consistency_check else '❌ FAILED'}")
    
    # Check if protocol fallback is working
    protocol_check = (sync_stats['http_fallback'] > 0) and (async_stats['http_fallback'] > 0)
    print(f"  HTTP fallback working: {'✅ PASSED' if protocol_check else '❌ FAILED'}")
    
    # Check if redirects are being followed
    redirect_check = (sync_stats['redirects'] > 0) and (async_stats['redirects'] > 0)
    print(f"  Redirect handling: {'✅ PASSED' if redirect_check else '❌ FAILED'}")
    
    # Check if error handling is working
    error_check = (sync_stats['errors'] > 0) and (async_stats['errors'] > 0)
    print(f"  Error detection: {'✅ PASSED' if error_check else '❌ FAILED'}")
    
    print(f"\n💡 Key Benefits Demonstrated:")
    print(f"  • ✅ Automatic protocol detection (https:// → http:// fallback)")
    print(f"  • ✅ Uses HEAD requests (minimal data transfer)")
    print(f"  • ✅ Short timeouts (5s default for quick checks)")
    print(f"  • ✅ No SSL verification (safer for malicious URLs)")
    print(f"  • ✅ Parallel processing support (sync & async)")
    print(f"  • ✅ Detailed timing and error information")
    print(f"  • ✅ Redirect following with count tracking")
    print(f"  • ✅ Protocol usage tracking (https/http)")

if __name__ == "__main__":
    main() 