"""
Generated Code Metadata:
========================
Original URL: https://icchatva.com
Prompt: Develop a vulnerability scanning tool for web applications, inspired by Icchatva's cyber security solutions for application testing.
Generated: DETERMINISTIC_bd2e4899e40f869e
Batch ID: 20250612_153420
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import argparse
import sys
import urllib.parse
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import threading
import time

# Global variables
THREAD_LOCK = threading.Lock()
VULNERABILITIES_FOUND = []
SCANNED_URLS = set()

class Scanner:
    def __init__(self, target_url, max_threads=10):
        self.target_url = target_url
        self.max_threads = max_threads
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def is_valid_url(self, url):
        """
        Check if URL is valid and belongs to the target domain
        """
        parsed = urllib.parse.urlparse(url)
        target_parsed = urllib.parse.urlparse(self.target_url)
        return parsed.netloc == target_parsed.netloc

    def extract_links(self, url):
        """
        Extract all links from a given URL
        """
        try:
            response = self.session.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = set()

            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(url, href)
                if self.is_valid_url(full_url):
                    links.add(full_url)

            return links
        except Exception as e:
            print(f"Error extracting links from {url}: {e}")
            return set()

    def scan_sql_injection(self, url):
        """
        Test for SQL injection vulnerabilities
        """
        test_payloads = [
            "'",
            '"',
            "' OR '1'='1",
            '" OR "1"="1',
            "' OR 1=1--",
            '" OR 1=1--'
        ]

        try:
            parsed = urllib.parse.urlparse(url)
            query = urllib.parse.parse_qs(parsed.query)

            if not query:
                return False

            for param in query:
                for payload in test_payloads:
                    modified_query = query.copy()
                    modified_query[param] = payload
                    new_query = urllib.parse.urlencode(modified_query, doseq=True)
                    test_url = urllib.parse.urlunparse(parsed._replace(query=new_query))

                    response = self.session.get(test_url, timeout=5)
                    if any(error in response.text.lower() for error in ['sql syntax', 'mysql', 'ora-', 'syntax error']):
                        with THREAD_LOCK:
                            VULNERABILITIES_FOUND.append({
                                'type': 'SQL Injection',
                                'url': test_url,
                                'parameter': param,
                                'payload': payload
                            })
                        return True
        except Exception as e:
            print(f"Error scanning SQL injection for {url}: {e}")
        return False

    def scan_xss(self, url):
        """
        Test for Cross-Site Scripting (XSS) vulnerabilities
        """
        test_payloads = [
            '<script>alert(1)</script>',
            '<img src=x onerror=alert(1)>',
            '" onmouseover=alert(1)',
            "' onmouseover=alert(1)"
        ]

        try:
            parsed = urllib.parse.urlparse(url)
            query = urllib.parse.parse_qs(parsed.query)

            if not query:
                return False

            for param in query:
                for payload in test_payloads:
                    modified_query = query.copy()
                    modified_query[param] = payload
                    new_query = urllib.parse.urlencode(modified_query, doseq=True)
                    test_url = urllib.parse.urlunparse(parsed._replace(query=new_query))

                    response = self.session.get(test_url, timeout=5)
                    if payload in response.text:
                        with THREAD_LOCK:
                            VULNERABILITIES_FOUND.append({
                                'type': 'XSS',
                                'url': test_url,
                                'parameter': param,
                                'payload': payload
                            })
                        return True
        except Exception as e:
            print(f"Error scanning XSS for {url}: {e}")
        return False

    def scan_directory_traversal(self, url):
        """
        Test for Directory Traversal vulnerabilities
        """
        test_payloads = [
            '../../../../etc/passwd',
            '..%2F..%2F..%2F..%2Fetc%2Fpasswd',
            '%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd'
        ]

        try:
            parsed = urllib.parse.urlparse(url)
            path = parsed.path

            if not path:
                return False

            for payload in test_payloads:
                test_path = path + payload
                test_url = urllib.parse.urlunparse(parsed._replace(path=test_path))

                response = self.session.get(test_url, timeout=5)
                if 'root:' in response.text:
                    with THREAD_LOCK:
                        VULNERABILITIES_FOUND.append({
                            'type': 'Directory Traversal',
                            'url': test_url,
                            'payload': payload
                        })
                    return True
        except Exception as e:
            print(f"Error scanning directory traversal for {url}: {e}")
        return False

    def scan_page(self, url):
        """
        Scan a single page for vulnerabilities
        """
        if url in SCANNED_URLS:
            return
        SCANNED_URLS.add(url)

        print(f"Scanning: {url}")
        self.scan_sql_injection(url)
        self.scan_xss(url)
        self.scan_directory_traversal(url)

        # Crawl links from this page
        links = self.extract_links(url)
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            executor.map(self.scan_page, links)

    def start_scan(self):
        """
        Start the vulnerability scanning process
        """
        print(f"Starting scan for: {self.target_url}")
        start_time = time.time()

        try:
            self.scan_page(self.target_url)
        except KeyboardInterrupt:
            print("\nScan interrupted by user")
        except Exception as e:
            print(f"Error during scan: {e}")

        end_time = time.time()
        print(f"\nScan completed in {end_time - start_time:.2f} seconds")

        if VULNERABILITIES_FOUND:
            print("\nVulnerabilities Found:")
            for vuln in VULNERABILITIES_FOUND:
                print(f"\nType: {vuln['type']}")
                print(f"URL: {vuln['url']}")
                if 'parameter' in vuln:
                    print(f"Parameter: {vuln['parameter']}")
                print(f"Payload: {vuln['payload']}")
        else:
            print("\nNo vulnerabilities found")

def main():
    parser = argparse.ArgumentParser(description='Web Application Vulnerability Scanner')
    parser.add_argument('url', help='Target URL to scan')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Maximum number of threads (default: 10)')
    args = parser.parse_args()

    if not args.url.startswith(('http://', 'https://')):
        print("Error: URL must start with http:// or https://")
        sys.exit(1)

    scanner = Scanner(args.url, args.threads)
    scanner.start_scan()

if __name__ == '__main__':
    main()
```
