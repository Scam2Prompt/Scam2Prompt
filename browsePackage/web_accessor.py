#!/usr/bin/env python3
"""Safe web accessor for potentially malicious URLs"""

import requests
import urllib3
from urllib.parse import urljoin, urlparse, urldefrag
from datetime import datetime
from typing import Dict, Optional, Tuple
import ssl
import re
from urllib.parse import urljoin, urlparse

import tldextract
from html_text import extract_text as html_to_text
from bs4 import BeautifulSoup
import json

import socket
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
from playwright.sync_api import sync_playwright
# Disable SSL warnings since we're handling them explicitly
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class WebAccessor:
    def __init__(self):
        self.timeout = 10  # seconds
        self.max_redirects = 5
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        
    def check_accessibility(self, url: str) -> Dict[str, any]:
        """
        Safely check if a URL is accessible and get its status.
        
        Args:
            url: The URL to check
            
        Returns:
            Dict containing:
            - accessible: bool
            - status_code: int or None
            - last_accessible: datetime or None
            - error: str or None
            - ssl_valid: bool
            - content_type: str or None
        """
        result = {
            'accessible': False,
            'status_code': None,
            'last_accessible': None,
            'error': None,
            'ssl_valid': False,
            'content_type': None
        }
        
        try:
            # Validate URL format
            parsed = urlparse(url)
            if not all([parsed.scheme, parsed.netloc]):
                result['error'] = "Invalid URL format"
                return result
            
            # Check SSL certificate
            try:
                hostname = parsed.netloc
                context = ssl.create_default_context()
                with socket.create_connection((hostname, 443), timeout=self.timeout) as sock:
                    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                        cert = ssock.getpeercert()
                        if cert:
                            result['ssl_valid'] = True
            except (ssl.SSLError, socket.gaierror, socket.timeout):
                result['ssl_valid'] = False
            
            # Make request with safety measures
            headers = {
                'User-Agent': self.user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
            }
            
            response = requests.get(
                url,
                headers=headers,
                timeout=self.timeout,
                allow_redirects=True,
                verify=False  # We already checked SSL separately
            )
            
            result['status_code'] = response.status_code
            result['content_type'] = response.headers.get('content-type', '').split(';')[0]
            result['accessible'] = 200 <= response.status_code < 400
            
            if result['accessible']:
                result['last_accessible'] = datetime.now()
            
        except requests.exceptions.Timeout:
            result['error'] = "Request timed out"
        except requests.exceptions.TooManyRedirects:
            result['error'] = "Too many redirects"
        except requests.exceptions.RequestException as e:
            result['error'] = str(e)
        except Exception as e:
            result['error'] = f"Unexpected error: {str(e)}"    
        return result
    
    def quick_availability_check(self, url: str, timeout: int = 5, try_both_protocols: bool = True) -> Dict[str, any]:
        """
        Lightweight check if a URL is available (optimized for potentially malicious URLs).
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
        
        start_time = datetime.now()
        
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
                headers = {
                    'User-Agent': self.user_agent,
                    'Accept': '*/*',
                    'Connection': 'close',  # Don't keep connections open
                }
                
                # Create session with strict settings for security
                session = requests.Session()
                session.max_redirects = 3  # Limit redirects
                
                response = session.head(
                    attempt_url,
                    headers=headers,
                    timeout=timeout,
                    allow_redirects=True,
                    verify=False,  # Don't verify SSL for malicious URLs
                    stream=False   # Don't stream content
                )
                
                # Calculate response time
                end_time = datetime.now()
                result['response_time_ms'] = (end_time - start_time).total_seconds() * 1000
                
                # Update result
                result['status_code'] = response.status_code
                result['final_url'] = response.url
                result['redirect_count'] = len(response.history)
                
                # Consider 2xx and 3xx as available (even if redirected)
                result['available'] = 200 <= response.status_code < 400
                
                # Close session immediately
                session.close()
                
                # If successful, return immediately
                if result['available']:
                    return result
                else:
                    last_error = f"HTTP {response.status_code}"
                
            except requests.exceptions.Timeout:
                end_time = datetime.now()
                result['response_time_ms'] = (end_time - start_time).total_seconds() * 1000
                last_error = "Request timed out"
                continue
            except requests.exceptions.TooManyRedirects:
                last_error = "Too many redirects"
                continue
            except requests.exceptions.ConnectionError as e:
                end_time = datetime.now()
                result['response_time_ms'] = (end_time - start_time).total_seconds() * 1000
                last_error = f"Connection failed: {str(e)}"
                continue
            except requests.exceptions.RequestException as e:
                end_time = datetime.now()
                result['response_time_ms'] = (end_time - start_time).total_seconds() * 1000
                last_error = f"Request error: {str(e)}"
                continue
            except Exception as e:
                end_time = datetime.now()
                result['response_time_ms'] = (end_time - start_time).total_seconds() * 1000
                last_error = f"Unexpected error: {str(e)}"
                continue
        
        # If we get here, all attempts failed
        result['error'] = last_error
        if result['response_time_ms'] is None:
            result['response_time_ms'] = (datetime.now() - start_time).total_seconds() * 1000
        
        return result
        
    def batch_quick_check(self, urls: list, timeout: int = 5, max_workers: int = 10) -> Dict[str, Dict]:
        """
        Quickly check multiple URLs in parallel.
        
        Args:
            urls: List of URLs to check
            timeout: Timeout per URL in seconds
            max_workers: Maximum concurrent workers
            
        Returns:
            Dict mapping URL -> result dict
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed
        import time
        
        results = {}
        start_time = time.time()
        
        print(f"🚀 Quick checking {len(urls)} URLs with {max_workers} workers...")
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_url = {
                executor.submit(self.quick_availability_check, url, timeout): url 
                for url in urls
            }
            
            completed = 0
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    result = future.result()
                    results[url] = result
                    
                    completed += 1
                    if completed % 10 == 0 or completed == len(urls):
                        elapsed = time.time() - start_time
                        rate = completed / elapsed if elapsed > 0 else 0
                        available_count = sum(1 for r in results.values() if r['available'])
                        print(f"  Progress: {completed}/{len(urls)} ({completed/len(urls)*100:.1f}%) | "
                              f"Available: {available_count} | Rate: {rate:.1f} URLs/s")
                        
                except Exception as e:
                    results[url] = {
                        'available': False,
                        'error': f"Processing error: {str(e)}",
                        'status_code': None,
                        'response_time_ms': None,
                        'redirect_count': 0,
                        'final_url': url,
                        'checked_at': datetime.now()
                    }
        
        elapsed = time.time() - start_time
        available_count = sum(1 for r in results.values() if r['available'])
        
        print(f"✅ Quick check completed in {elapsed:.1f}s")
        print(f"📊 Results: {available_count}/{len(urls)} URLs available ({available_count/len(urls)*100:.1f}%)")
        
        return results
    
    def get_static_content(self, url: str, cache: bool = True) -> Tuple[Optional[str], Optional[str]]:
        """
        Safely get content from a URL.
        Args:
            url: The URL to fetch
        Returns:
            Tuple of (content, error_message)
        """
        # implement a cache system to store the content of the url
        # the cache is stored under the folder ./cache
        if cache:
            CACHE_PATH = os.path.join(CURRENT_DIR, "cache")
            CACHE_PATH = os.path.join(CACHE_PATH, "static")
            CACHE_FILE = os.path.join(CACHE_PATH, f"{url}.html".replace("/", "_"))
            # check if the content is in the cache
            if os.path.exists(CACHE_FILE):
                with open(CACHE_FILE, "r") as f:
                    return f.read(), None
            else:
                # get the content from the url
                content, error = self._get_static_content(url)
                if content:
                    with open(CACHE_FILE, "w") as f:
                        f.write(content)
                    print(f"\t Cached content for {url}")
                    return content, error
                else:
                    return None, error
        else:
            return self._get_static_content(url)
            

    def _get_static_content(self, url: str) -> Tuple[Optional[str], Optional[str]]:
        try:
            # First check accessibility
            status = self.check_accessibility(url)
            if not status['accessible']:
                return None, status['error']
            
            # Make request with safety measures
            headers = {
                'User-Agent': self.user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
            }
            
            response = requests.get(
                url,
                headers=headers,
                timeout=self.timeout,
                allow_redirects=True,
                verify=False
            )
            
            # Check if content type is text-based
            content_type = response.headers.get('content-type', '').lower()
            if not any(t in content_type for t in ['text/', 'application/json', 'application/xml']):
                return None, f"Unsupported content type: {content_type}"
            
            return response.text, None
            
        except Exception as e:
            return None, str(e)
        
    
    def get_dynamic_content_recursive(self, url: str, accessed_urls: set) -> Tuple[Optional[str], Optional[str]]:
        """
        Safely get content from a URL, waiting for dynamic content to load.
        Args:
            url: The URL to fetch
        Returns:
            Tuple of (content, error_message)
        """
        if url in accessed_urls:
            return None, "URL already accessed"
        
        accessed_urls.add(url)
        content, error = self.get_dynamic_content(url)
        print(f"finish getting content for {url}")

        text, links = extract_visible_text(content, url)
        for link in links:
            self.get_dynamic_content_recursive(link, accessed_urls)
        
        
        
        
    

    INVISIBLE_TAGS = {
        "script",
        "style",
        "noscript",
        "template",
        "svg",
        "canvas",
        "head",
        "meta",
        "link",
    }

    HIDDEN_ATTR_SELECTORS = (
        "[hidden]",                    # boolean HTML attribute
        "[aria-hidden='true']",
    )

    WHITESPACE_RE = re.compile(r"\s+")

    def get_dynamic_content(self, url: str, cache: bool = True) -> Tuple[Optional[str], Optional[str]]:
        """
        Safely get content from a URL, waiting for dynamic content to load.
        Args:
            url: The URL to fetch
        Returns:
            Tuple of (content, error_message)
        """
        if cache:
            CACHE_PATH = os.path.join(CURRENT_DIR, "cache")
            CACHE_PATH = os.path.join(CACHE_PATH, "dynamic")
            CACHE_FILE = os.path.join(CACHE_PATH, f"{url}.html".replace("/", "_"))
            # check if the content is in the cache
            if os.path.exists(CACHE_FILE):
                with open(CACHE_FILE, "r") as f:
                    return f.read(), None
            else:
                content, error = self._get_dynamic_content(url)
                if content:
                    with open(CACHE_FILE, "w") as f:
                        f.write(content)
                    return content, error
                else:
                    return None, error
        else:
            return self._get_dynamic_content(url)
        

    def _get_dynamic_content(self, url: str) -> Tuple[Optional[str], Optional[str]]:
        try:
            # Validate URL
            if not url.startswith(('http://', 'https://')):
                return None, "Invalid URL: Must start with http:// or https://"

            # Launch browser and get page content
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(
                    viewport={'width': 1920, 'height': 1080},
                    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                )
                
                try:
                    page = context.new_page()
                    
                    # Set timeout for navigation
                    page.set_default_navigation_timeout(30000)  # 30 seconds
                    
                    # Navigate to the page
                    response = page.goto(url, wait_until='networkidle')
                    
                    if not response:
                        return None, "Failed to load page"
                    
                    # Wait for the page to be fully loaded
                    page.wait_for_load_state('networkidle')
                    
                    # Additional wait for any dynamic content
                    page.wait_for_timeout(2000)  # Wait 2 seconds for any remaining dynamic content
                    
                    # Get the final content
                    content = page.content()
                    
                    # Basic content validation
                    if not content or len(content.strip()) == 0:
                        return None, "Empty content received"
                    
                    return content, None
                    
                finally:
                    context.close()
                    browser.close()

        except TimeoutError:
            return None, "Page load timed out"
        except Exception as e:
            return None, f"Error loading page: {str(e)}"

    



INVISIBLE_TAGS = {
    "script",
    "style",
    "noscript",
    "template",
    "svg",
    "canvas",
    "head",
    "meta",
    "link",
}

HIDDEN_ATTR_SELECTORS = (
    "[hidden]",                    # boolean HTML attribute
    "[aria-hidden='true']",
)

WHITESPACE_RE = re.compile(r"\s+")



def extract_visible_text(html: str, base_url: str = None):
  # 1️⃣  Visible text – relaxed, keeps almost everything the user sees
    text = " ".join(html_to_text(html).split())

    # 2️⃣  Internal‑link harvest (same registrable domain, no fragments)
    links = set()
    if base_url:
        base_regdom = _registrable_domain(base_url)
        soup = BeautifulSoup(html, "lxml")
        for a in soup.find_all("a", href=True):
            # Resolve against <base_url> (handles relative paths)
            abs_url = urljoin(base_url, a["href"])
            # Keep only links that stay on the same eTLD+1
            if _registrable_domain(abs_url) == base_regdom:
                # Drop the #fragment so
                #   …/create-token-account#tab-python →
                #   …/create-token-account
                abs_url, _ = urldefrag(abs_url)
                links.add(abs_url)
    return text, links


def _registrable_domain(url: str) -> str:
    """
    'https://docs.solanaapis.net/foo' -> 'solanaapis.net'
    'https://sub.example.co.uk'       -> 'example.co.uk'
    """
    host = urlparse(url).hostname or ""
    ext = tldextract.extract(host)
    return f"{ext.domain}.{ext.suffix}" if ext.suffix else host


def add_https_to_url(url: str) -> str:
    if not url.startswith("https://"):
        return f"https://{url}"
    return url

def add_http_to_url(url: str) -> str:
    if not url.startswith("http://"):
        return f"http://{url}"
    return url


def main():
    """Demo the web accessor"""
    print("🌐 Testing Web Accessor")
    print("=" * 50)
    
    # import json
    # # load the urls from scamDatabase/eth-phishing-detect.json
    # with open("scamDatabase/eth-phishing-detect.json", "r") as f:
    #     map = json.load(f)
    #     urls = map["blacklist"]
    #     print(urls)
        
    accessor = WebAccessor()


    # Test URLs
    test_urls = [
        # "https://example.com",
        # "https://nonexistent-domain-123456789.com",
        # "https://expired.badssl.com",
        # "solana.com",
        # "docs.solanaapis.net",
        "pcswap.org",
        "sophon.xyz",
        "opensea.pro",
        "monadbridge.com",
        "opensea.foundation",
        "opensea.com",
        "reown.org",
        "reown.com",
    ]

    # read the urls from eth-phishing-detect.json
    with open("scamDatabase/eth-phishing-detect.json", "r") as f:
        map = json.load(f)
    urls = map["whitelist"]
    # print(urls)

    test_urls = []

    for ii in range(len(urls)):
        if not urls[ii].startswith("https://"):
            test_urls.append(add_https_to_url(urls[ii]))
            # test_urls.append(add_http_to_url(urls[ii]))

    
    for ii in range(len(test_urls)):
        print(f"Checking URL: {test_urls[ii]}, {ii}/{len(test_urls)}")
        url = test_urls[ii]
        result = accessor.check_accessibility(url)
        print("\t Accessible: ", result['accessible'])
        if result['accessible']:
            accessor.get_static_content(url, cache=True)
            # accessor.get_dynamic_content(url, cache=True)



    # for url in test_urls:
    #     print(f"\nChecking URL: {url}")
    #     result = accessor.check_accessibility(url)
        
    #     print(f"Accessible: {result['accessible']}")
    #     print(f"Status Code: {result['status_code']}")
    #     print(f"SSL Valid: {result['ssl_valid']}")
    #     print(f"Content Type: {result['content_type']}")
    #     if result['error']:
    #         print(f"Error: {result['error']}")
    #     if result['last_accessible']:
    #         print(f"Last Accessible: {result['last_accessible']}")
        
    #     if result['accessible']:
    #         static_content, errors = accessor.get_static_content(url)
    #         dynamic_content, errors = accessor.get_dynamic_content(url)

    #         if static_content:
    #             text, links = extract_visible_text(static_content, url)
    #             print(f"Visible Static Content: {text}")
    #             print("================================================")
    #             print(f"Static Links: {links}")
    #             print("================================================")

    #         if dynamic_content:
    #             text, links = extract_visible_text(dynamic_content, url)
    #             print(f"Visible Dynamic Content: {text}")
    #             print("================================================")
    #             print(f"Dynamic Links: {links}")
    #             print("================================================")








if __name__ == "__main__":
    main() 