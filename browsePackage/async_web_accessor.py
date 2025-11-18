#!/usr/bin/env python3
"""Async web accessor for high-performance URL processing"""

import asyncio
import aiohttp
import time
from urllib.parse import urlparse, urljoin, urldefrag
from datetime import datetime
from typing import Dict, Optional, Tuple, List
import json
import os
from pathlib import Path
import hashlib
import gc

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    print("⚠️  Warning: psutil not available. Memory monitoring disabled.")
    print("   Install with: pip install psutil")


# add the current directory to the path
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# Import existing functions we'll reuse
from web_accessor import extract_visible_text, add_https_to_url, _registrable_domain
from optimized_cache import OptimizedHTMLCache

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class AsyncWebAccessor:
    def __init__(self, max_concurrent=50, timeout=10, use_cache=True):
        self.max_concurrent = max_concurrent
        self.timeout = timeout
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        
        # Initialize optimized HTML cache
        self.use_cache = use_cache
        if self.use_cache:
            self.static_cache = OptimizedHTMLCache("static")
            self.dynamic_cache = OptimizedHTMLCache("dynamic")
        
        # Connection pool settings
        self.connector = aiohttp.TCPConnector(
            limit=100,  # Total connection pool size
            limit_per_host=10,  # Max connections per host
            ttl_dns_cache=300,
            use_dns_cache=True,
            enable_cleanup_closed=True
        )
        
        # Rate limiting
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.last_request_time = {}
        self.rate_limit = 10  # requests per second per domain
        
    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession(
            connector=self.connector,
            timeout=aiohttp.ClientTimeout(total=self.timeout),
            headers={'User-Agent': self.user_agent}
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        await self.session.close()
        await self.connector.close()
    
    async def rate_limited_request(self, url: str):
        """Apply rate limiting per domain"""
        async with self.semaphore:
            domain = urlparse(url).netloc
            
            # Simple rate limiting per domain
            if domain in self.last_request_time:
                elapsed = time.time() - self.last_request_time[domain]
                min_interval = 1.0 / self.rate_limit
                if elapsed < min_interval:
                    await asyncio.sleep(min_interval - elapsed)
            
            self.last_request_time[domain] = time.time()
            return await self.fetch_url_content(url)
    
    async def fetch_url_content(self, url: str) -> Dict:
        """Fetch content from a single URL with error handling - OPTIMIZED VERSION"""
        result = {
            'url': url,
            'accessible': False,
            'status_code': None,
            'content': None,
            'error': None,
            'content_type': None,
            'ssl_valid': False,
            'timestamp': datetime.now()
        }
        
        try:
            # Validate URL format
            parsed = urlparse(url)
            if not all([parsed.scheme, parsed.netloc]):
                result['error'] = "Invalid URL format"
                return result
            
            # Single optimized request that gets ALL information at once
            async with self.session.get(url, allow_redirects=True) as response:
                result['status_code'] = response.status
                result['content_type'] = response.headers.get('content-type', '').split(';')[0]
                
                # SSL validation (quick check if HTTPS)
                if url.startswith('https://'):
                    # If we got a response, SSL worked
                    result['ssl_valid'] = True
                
                # Check if successful
                if 200 <= response.status < 400:
                    result['accessible'] = True
                    
                    # Check if content type is text-based
                    content_type = result['content_type'].lower()
                    if any(t in content_type for t in ['text/', 'application/json', 'application/xml']):
                        try:
                            # Get the content in one go
                            result['content'] = await response.text()
                            
                            # Basic content validation
                            if not result['content'] or len(result['content'].strip()) == 0:
                                result['error'] = "Empty content received"
                                result['accessible'] = False
                                result['content'] = None
                        except UnicodeDecodeError:
                            try:
                                result['content'] = await response.text(encoding='utf-8', errors='ignore')
                            except Exception as e:
                                result['error'] = f"Content encoding error: {str(e)}"
                                result['accessible'] = False
                        except Exception as e:
                            result['error'] = f"Content reading error: {str(e)}"
                            result['accessible'] = False
                    else:
                        result['error'] = f"Unsupported content type: {content_type}"
                        result['accessible'] = False
                else:
                    result['error'] = f"HTTP {response.status}"
                    
        except asyncio.TimeoutError:
            result['error'] = "Request timed out"
        except aiohttp.ClientConnectorError as e:
            result['error'] = f"Connection error: {str(e)}"
        except aiohttp.ClientSSLError as e:
            result['error'] = f"SSL error: {str(e)}"
            result['ssl_valid'] = False
        except aiohttp.ClientError as e:
            result['error'] = f"Client error: {str(e)}"
        except Exception as e:
            result['error'] = f"Unexpected error: {str(e)}"
        
        return result
    
    async def process_urls_batch(self, urls: List[str], progress_callback=None) -> List[Dict]:
        """Process a batch of URLs concurrently"""
        tasks = []
        
        for i, url in enumerate(urls):
            task = self.rate_limited_request(url)
            tasks.append(task)
        
        # Process with progress tracking
        results = []
        completed = 0
        
        for coro in asyncio.as_completed(tasks):
            result = await coro
            results.append(result)
            completed += 1
            
            if progress_callback:
                progress_callback(completed, len(urls))
        
        return results
    
    async def process_urls_in_chunks(self, urls: List[str], chunk_size: int = 1000, progress_callback=None) -> List[Dict]:
        """Process URLs in manageable chunks to avoid memory issues"""
        all_results = []
        total_chunks = (len(urls) + chunk_size - 1) // chunk_size
        total_processed = 0
        start_time = time.time()
        
        # Memory monitoring
        if PSUTIL_AVAILABLE:
            process = psutil.Process()
            initial_memory = process.memory_info().rss / 1024 / 1024  # MB
            print(f"📊 Initial memory usage: {initial_memory:.1f} MB")
        else:
            process = None
            initial_memory = 0
            print(f"📊 Memory monitoring disabled (psutil not available)")
        
        print(f"🚀 Starting processing of {len(urls)} URLs in {total_chunks} chunks")
        
        for chunk_num, i in enumerate(range(0, len(urls), chunk_size)):
            chunk = urls[i:i + chunk_size]
            chunk_start_time = time.time()
            
            print(f"\n📦 Processing chunk {chunk_num + 1}/{total_chunks} ({len(chunk)} URLs)")
            
            chunk_results = await self.process_urls_batch_with_cache(chunk, progress_callback)
            all_results.extend(chunk_results)
            
            # Update counters
            total_processed += len(chunk)
            chunk_duration = time.time() - chunk_start_time
            overall_duration = time.time() - start_time
            
            # Calculate performance metrics
            chunk_successful = sum(1 for r in chunk_results if r['accessible'])
            chunk_speed = len(chunk) / chunk_duration if chunk_duration > 0 else 0
            overall_speed = total_processed / overall_duration if overall_duration > 0 else 0
            
            # Memory tracking
            if PSUTIL_AVAILABLE:
                current_memory = process.memory_info().rss / 1024 / 1024  # MB
                memory_increase = current_memory - initial_memory
            else:
                memory_increase = 0
            
            # Progress summary
            print(f"✅ Chunk {chunk_num + 1} completed:")
            print(f"   📈 Successful: {chunk_successful}/{len(chunk)} ({chunk_successful/len(chunk)*100:.1f}%)")
            print(f"   ⏱️  Chunk time: {chunk_duration:.1f}s ({chunk_speed:.1f} URLs/s)")
            print(f"   🏃 Overall: {total_processed}/{len(urls)} ({total_processed/len(urls)*100:.1f}%) at {overall_speed:.1f} URLs/s")
            
            if PSUTIL_AVAILABLE:
                current_memory = process.memory_info().rss / 1024 / 1024  # MB
                memory_increase = current_memory - initial_memory
                print(f"   💾 Memory: {current_memory:.1f} MB (+{memory_increase:.1f} MB)")
            else:
                print(f"   💾 Memory: monitoring disabled")
            
            # Estimate remaining time
            if overall_speed > 0:
                remaining_urls = len(urls) - total_processed
                eta_seconds = remaining_urls / overall_speed
                eta_minutes = eta_seconds / 60
                if eta_minutes > 60:
                    print(f"   🕐 ETA: {eta_minutes/60:.1f} hours")
                else:
                    print(f"   🕐 ETA: {eta_minutes:.1f} minutes")
            
            # Garbage collection every 5 chunks or when memory usage increases significantly
            should_gc = (
                (chunk_num + 1) % 5 == 0 or  # Every 5 chunks
                memory_increase > 100 or      # Memory increased by >100MB
                (chunk_num + 1) % 10 == 0     # Every 10 chunks regardless
            )
            
            if should_gc:
                print(f"   🧹 Running garbage collection...")
                gc_start = time.time()
                
                # Force garbage collection
                collected = gc.collect()
                
                # Check memory after GC
                if PSUTIL_AVAILABLE:
                    gc_memory = process.memory_info().rss / 1024 / 1024  # MB
                    memory_freed = current_memory - gc_memory
                    gc_duration = time.time() - gc_start
                    
                    print(f"   🗑️  GC completed: freed {memory_freed:.1f} MB, collected {collected} objects in {gc_duration:.2f}s")
                    print(f"   💾 Memory after GC: {gc_memory:.1f} MB")
                else:
                    print(f"   🗑️  GC completed: no memory freed (psutil not available)")
            
            # Small delay between chunks to be nice to servers
            if chunk_num < total_chunks - 1:
                await asyncio.sleep(1)
        
        # Final summary
        total_duration = time.time() - start_time
        if PSUTIL_AVAILABLE:
            process = psutil.Process()
            final_memory = process.memory_info().rss / 1024 / 1024  # MB
        else:
            final_memory = 0
        
        print(f"\n🎉 Processing Complete!")
        print(f"📊 Final Stats:")
        print(f"   Total URLs: {len(urls)}")
        print(f"   Total time: {total_duration:.1f}s ({total_duration/60:.1f} minutes)")
        print(f"   Average speed: {len(urls)/total_duration:.1f} URLs/s")
        
        if PSUTIL_AVAILABLE:
            print(f"   Final memory: {final_memory:.1f} MB")
            print(f"   Memory change: {final_memory - initial_memory:+.1f} MB")
        else:
            print(f"   Memory monitoring: disabled")
        
        return all_results

    async def process_urls_batch_with_cache(self, urls: List[str], progress_callback=None) -> List[Dict]:
        """Process a batch of URLs with HTML cache support"""
        if not self.use_cache:
            return await self.process_urls_batch(urls, progress_callback)
        
        # Separate cached vs uncached URLs
        urls_to_fetch = []
        cached_results = []
        
        for url in urls:
            cached_content = self.static_cache.get_cached_content(url)
            if cached_content:
                # Convert cached content to result format
                cached_result = {
                    'url': url,
                    'accessible': True,
                    'status_code': 200,  # Assume success since it was cached
                    'content': cached_content,
                    'error': None,
                    'content_type': 'text/html',
                    'timestamp': None
                }
                cached_results.append(cached_result)
            else:
                urls_to_fetch.append(url)
        
        print(f"  Cache hits: {len(cached_results)}/{len(urls)} ({len(cached_results)/len(urls)*100:.1f}%)")
        print(f"  URLs to fetch: {len(urls_to_fetch)}")
        
        # Fetch uncached URLs
        if urls_to_fetch:
            fresh_results = await self.process_urls_batch(urls_to_fetch, progress_callback)
            
            # Cache the fresh results
            cached_count = 0
            for result in fresh_results:
                if result['accessible'] and result['content']:
                    success = self.static_cache.cache_content(result['url'], result['content'])
                    if success:
                        cached_count += 1
            
            print(f"  Cached {cached_count} new results")
        else:
            fresh_results = []
        
        # Combine cached and fresh results
        all_results = cached_results + fresh_results
        return all_results

    async def quick_availability_check(self, url: str, timeout: int = 5, try_both_protocols: bool = True) -> Dict:
        """
        Lightweight async check if a URL is available (optimized for potentially malicious URLs).
        Uses HEAD request to minimize data transfer and security risk.
        
        Args:
            url: The URL to check
            timeout: Timeout in seconds (default: 5 for quick checks)
            try_both_protocols: If True, try HTTP if HTTPS fails (default: True)
            
        Returns:
            Dict containing:
            - available: bool (True if URL responds with 2xx/3xx status)
            - status_code: int or None
            - response_time_ms: float (response time in milliseconds)
            - error: str or None
            - redirect_count: int (number of redirects followed)
            - final_url: str (final URL after redirects)
            - protocol_used: str (https or http)
        """
        result = {
            'available': False,
            'status_code': None,
            'response_time_ms': None,
            'error': None,
            'redirect_count': 0,
            'final_url': url,
            'protocol_used': None,
            'checked_at': datetime.now()
        }
        
        start_time = time.time()
        
        # Store original URL for fallback
        original_url = url
        urls_to_try = []
        
        # Prepare URLs to try
        if url.startswith(('http://', 'https://')):
            urls_to_try.append(url)
            if try_both_protocols:
                if url.startswith('https://'):
                    urls_to_try.append(url.replace('https://', 'http://'))
                else:
                    urls_to_try.append(url.replace('http://', 'https://'))
        else:
            # No protocol specified, try both
            if try_both_protocols:
                urls_to_try = [f"https://{url}", f"http://{url}"]
            else:
                urls_to_try = [f"https://{url}"]
        
        last_error = None
        
        for attempt_url in urls_to_try:
            try:
                result['final_url'] = attempt_url
                
                # Validate URL format
                parsed = urlparse(attempt_url)
                if not all([parsed.scheme, parsed.netloc]):
                    last_error = "Invalid URL format"
                    continue
                
                # Determine protocol used
                result['protocol_used'] = 'https' if attempt_url.startswith('https://') else 'http'
                
                # Use HEAD request for minimal data transfer (safer for malicious URLs)
                custom_timeout = aiohttp.ClientTimeout(total=timeout)
                
                async with self.session.head(
                    attempt_url,
                    timeout=custom_timeout,
                    allow_redirects=True,
                    ssl=False  # Don't verify SSL for malicious URLs
                ) as response:
                    
                    # Calculate response time
                    end_time = time.time()
                    result['response_time_ms'] = (end_time - start_time) * 1000
                    
                    # Update result
                    result['status_code'] = response.status
                    result['final_url'] = str(response.url)
                    result['redirect_count'] = len(response.history) if hasattr(response, 'history') else 0
                    
                    # Consider 2xx and 3xx as available (even if redirected)
                    result['available'] = 200 <= response.status < 400
                    
                    # If successful, return immediately
                    if result['available']:
                        return result
                    else:
                        last_error = f"HTTP {response.status}"
                
            except asyncio.TimeoutError:
                end_time = time.time()
                result['response_time_ms'] = (end_time - start_time) * 1000
                last_error = "Request timed out"
                continue
            except aiohttp.ClientConnectorError as e:
                end_time = time.time()
                result['response_time_ms'] = (end_time - start_time) * 1000
                last_error = f"Connection failed: {str(e)}"
                continue
            except aiohttp.ClientError as e:
                end_time = time.time()
                result['response_time_ms'] = (end_time - start_time) * 1000
                last_error = f"Client error: {str(e)}"
                continue
            except Exception as e:
                end_time = time.time()
                result['response_time_ms'] = (end_time - start_time) * 1000
                last_error = f"Unexpected error: {str(e)}"
                continue
        
        # If we get here, all attempts failed
        result['error'] = last_error
        if result['response_time_ms'] is None:
            result['response_time_ms'] = (time.time() - start_time) * 1000
        
        return result
    
    async def batch_quick_check(self, urls: List[str], timeout: int = 5, max_concurrent: int = 20) -> Dict[str, Dict]:
        """
        Quickly check multiple URLs in parallel using async.
        
        Args:
            urls: List of URLs to check
            timeout: Timeout per URL in seconds
            max_concurrent: Maximum concurrent requests
            
        Returns:
            Dict mapping URL -> result dict
        """
        results = {}
        start_time = time.time()
        
        print(f"🚀 Quick checking {len(urls)} URLs with {max_concurrent} concurrent requests...")
        
        # Create semaphore for concurrency control
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def check_with_semaphore(url):
            async with semaphore:
                return await self.quick_availability_check(url, timeout)
        
        # Create tasks for all URLs
        tasks = [check_with_semaphore(url) for url in urls]
        
        # Process with progress tracking
        completed = 0
        for coro in asyncio.as_completed(tasks):
            result = await coro
            url = result['final_url'] if 'final_url' in result else urls[completed]
            results[urls[completed]] = result
            
            completed += 1
            if completed % 10 == 0 or completed == len(urls):
                elapsed = time.time() - start_time
                rate = completed / elapsed if elapsed > 0 else 0
                available_count = sum(1 for r in results.values() if r['available'])
                print(f"  Progress: {completed}/{len(urls)} ({completed/len(urls)*100:.1f}%) | "
                      f"Available: {available_count} | Rate: {rate:.1f} URLs/s")
        
        elapsed = time.time() - start_time
        available_count = sum(1 for r in results.values() if r['available'])
        
        print(f"✅ Quick check completed in {elapsed:.1f}s")
        print(f"📊 Results: {available_count}/{len(urls)} URLs available ({available_count/len(urls)*100:.1f}%)")
        
        return results


def progress_printer(completed: int, total: int):
    """Enhanced progress callback with real-time updates"""
    percent = (completed / total) * 100
    bar_length = 25
    filled_length = int(bar_length * completed // total)
    bar = '█' * filled_length + '▒' * (bar_length - filled_length)
    
    # Calculate speed (this is approximate since we don't have time context here)
    status = f"   Progress: [{bar}] {completed:3d}/{total} ({percent:5.1f}%)"
    
    # Use \r to overwrite the same line
    print(f"\r{status}", end='', flush=True)
    
    # Print newline when complete
    if completed == total:
        print()  # New line after completion


async def main_async():
    """Async main function for testing"""
    print("🚀 Testing Async Web Accessor")
    print("=" * 50)
    
    # Load URLs from the JSON file
    # json_path = os.path.join(CURRENT_DIR, "..", "scamDatabase", "eth-phishing-detect.json")
    json_path = os.path.join(CURRENT_DIR, "..", "scamDatabase", "phishingfort-lists.json")
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
        # urls = data["blacklist"]
        urls = data
    except FileNotFoundError:
        # print("Warning: eth-phishing-detect.json not found, using test URLs")
        print("Warning: phishingfort-lists.json not found, using test URLs")
        sys.exit(1)
    
    # Add https:// prefix to URLs that need it
    test_urls = []
    for url in urls:
        if not url.startswith("https://"):
            test_urls.append(add_https_to_url(url))
        else:
            test_urls.append(url)
    
    print(f"Processing {len(test_urls)} URLs...")
    start_time = time.time()
    
    # Process URLs with async accessor
    async with AsyncWebAccessor(max_concurrent=20) as accessor:
        # Show initial cache stats
        if accessor.use_cache:
            initial_stats = accessor.static_cache.get_cache_stats()
            print(f"Initial cache stats: {initial_stats['total_files']} files, {initial_stats['total_size_mb']} MB")
        
        results = await accessor.process_urls_in_chunks(
            test_urls, 
            chunk_size=50,
            progress_callback=progress_printer
        )
        
        # Show final cache stats
        if accessor.use_cache:
            final_stats = accessor.static_cache.get_cache_stats()
            print(f"\nFinal cache stats:")
            for key, value in final_stats.items():
                print(f"  {key}: {value}")
    
    end_time = time.time()
    print(f"\n\nCompleted in {end_time - start_time:.2f} seconds")
    
    # Analyze results
    accessible_count = sum(1 for r in results if r['accessible'])
    error_count = sum(1 for r in results if r['error'])
    
    print(f"Results:")
    print(f"  Accessible: {accessible_count}/{len(results)}")
    print(f"  Errors: {error_count}")
    
    # Show sample results
    print(f"\nSample accessible URLs:")
    for result in results[:5]:
        if result['accessible']:
            content_length = len(result['content']) if result['content'] else 0
            print(f"  {result['url']} - {result['status_code']} - {content_length} chars")


def main():
    """Sync wrapper for the async main function"""
    asyncio.run(main_async())


if __name__ == "__main__":
    main() 