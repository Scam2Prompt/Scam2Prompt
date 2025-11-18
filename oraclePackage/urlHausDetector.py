# API keys: 34157caaa65e3cc8cece93a578eabd6f76734d29e15bb0a1 (Xun)
# Sample Python Script
# #!/usr/bin/python3
# import sys
# import requests
# import json

# auth_key1 = "34157caaa65e3cc8cece93a578eabd6f76734d29e15bb0a1"
# url1 = "https://api.pump.fund"

# def query_urlhaus(auth_key, url):
#     # Construct the HTTP request
#     data = {
#         'url' : url
#     }
#     # Set the Authentication header
#     headers = {
#         "Auth-Key"      :   auth_key
#     }
#     response = requests.post('https://urlhaus-api.abuse.ch/v1/url/', data, headers=headers)
#     # Parse the response from the API
#     json_response = response.json()
#     if json_response['query_status'] == 'ok':
#         print(json.dumps(json_response, indent=4, sort_keys=False))
#     elif json_response['query_status'] == 'no_results':
#         print("No results")
#     else:
#         print(json_response['query_status'])


# query_urlhaus(auth_key1, url1)

import requests
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
from urllib.parse import urlparse


class ThreatLevel(Enum):
    SAFE = "safe"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class DetectionResult:
    detector_name: str
    threat_level: ThreatLevel
    confidence: float
    details: Dict[str, Any]
    urls_checked: List[str]
    success: bool = True
    error_message: Optional[str] = None


class UrlHausDetector:
    """
    UrlHaus detector for Web3 scams and malicious URLs
    
    Requires API key for full access, free tier with limited rate limits.
    """
    
    def __init__(self, api_key):
        """
        Initialize UrlHaus detector

        Args:
            api_key: UrlHaus API key.
        """
        if not api_key:
            raise ValueError("UrlHaus API key is required")

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'UrlHausDetector',
            "Auth-Key": api_key
        })
        self.base_url = "https://urlhaus-api.abuse.ch/v1/url/"
    
    def check_url(self, url: str) -> DetectionResult:
        """
        Check a single URL against UrlHaus's database
        
        Args:
            url: The URL to check
            
        Returns:
            DetectionResult with threat assessment
        """
        return self.check_urls([url])
    
    def check_urls(self, urls: List[str]) -> DetectionResult:
        """
        Check multiple URLs against UrlHaus's database

        Args:
            urls: List of URLs to check
            
        Returns:
            DetectionResult with threat assessment for all URLs
        """
        if not urls:
            return DetectionResult(
                detector_name="UrlHaus",
                threat_level=ThreatLevel.SAFE,
                confidence=0.0,
                details={"error": "No URLs provided"},
                urls_checked=[],
                success=False,
                error_message="No URLs provided"
            )
        
        try:
            malicious_urls = []
            safe_urls = []
            errors = []
            url_results = []
            reference = None
            for url in urls:
                try:
                    # Make API request
                    data = {'url': url}
                    response = self.session.post(
                        'https://urlhaus-api.abuse.ch/v1/url/',
                        data=data,
                        timeout=15
                    )

                    if response.status_code == 200:
                        json_response = response.json()
                        query_status = json_response.get("query_status")

                        if query_status == "ok":
                            malicious_urls.append({
                                "url": url,
                                "full_api_response": json_response
                            })
                            encoded_url = base64.urlsafe_b64encode(url.encode()).rstrip(b'=').decode('ascii')
                            url_results.append({
                                "url": url,
                                "is_malicious": True,
                                "reference": f"https://www.virustotal.com/gui/url/{encoded_url}",
                                "api_response": json_response
                            })
                        elif query_status == "no_results":
                            safe_urls.append({
                                "url": url,
                                "full_api_response": json_response
                            })
                            url_results.append({
                                "url": url,
                                "is_malicious": False,
                                "reference": "",
                                "api_response": json_response
                            })
                        else:
                            errors.append({
                                "url": url,
                                "error": f"Unexpected status: {query_status}",
                                "status_code": response.status_code
                            })
                    else:
                        errors.append({
                            "url": url,
                            "error": f"HTTP {response.status_code}: {response.text}",
                            "status_code": response.status_code
                        })

                except requests.exceptions.Timeout:
                    errors.append({"url": url, "error": "Timeout"})
                except requests.exceptions.RequestException as e:
                    errors.append({"url": url, "error": f"Request exception: {str(e)}"})
                except Exception as e:
                    errors.append({"url": url, "error": f"Unexpected exception: {str(e)}"})

                time.sleep(0.1)

            if malicious_urls:
                threat_level = ThreatLevel.HIGH
                confidence = 0.9
            elif errors:
                threat_level = ThreatLevel.SAFE
                confidence = 0.5
            else:
                threat_level = ThreatLevel.SAFE
                confidence = 0.85

            success = len(errors) == 0 or len(url_results) > 0
            error_message = None if success else f"Failed to check {len(errors)} URLs"

            details = {
                "malicious_urls": malicious_urls,
                "safe_urls": safe_urls,
                "errors": errors,
                "url_results": url_results,
                "total_urls_checked": len(urls),
                "total_malicious": len(malicious_urls),
                "total_safe": len(safe_urls),
                "total_errors": len(errors)
            }

        except Exception as e:
            return DetectionResult(
                detector_name="UrlHaus",
                threat_level=ThreatLevel.SAFE,
                confidence=0.0,
                details={"error": f"Unexpected error: {str(e)}"},
                urls_checked=[],
                success=False,
                error_message=str(e)
            )

        return DetectionResult(
            detector_name="UrlHaus",
            threat_level=threat_level,
            confidence=confidence,
            details=details,
            urls_checked=urls,
            success=success,
            error_message=error_message
        )
    
    def get_detector_info(self) -> Dict[str, Any]:
        """
        Get information about this detector
        
        Returns:
            Dictionary with detector metadata
        """
        return {
            "name": "UrlHaus Detector",
            "description": "Web3 scam detection and brand protection platform",
            "website": "https://urlhaus.abuse.ch/",
            "api_docs": "https://urlhaus.abuse.ch/api/",
            "api_endpoint": "https://urlhaus-api.abuse.ch/v1/url/",
            "requires_api_key": True,
            "supports_anonymous": False,
            "request_method": "POST",
            "auth_header": "Auth-Key",
            "rate_limits": "Unknown",
            "aggregates_sources": True,
            # not updated
            "known_sources": [
                "chainpatrol",
                "eth-phishing-detect", 
                "phishfort"
            ],
            # not updated
            "detection_logic": "URL flagged as malicious if ANY source reports BLOCKED status",
            # not updated
            "specializes_in": [
                "Web3 scams",
                "Cryptocurrency phishing",
                "NFT scams", 
                "DeFi protocol impersonation",
                "Wallet address verification"
            ]
        }


# Example usage and testing
if __name__ == "__main__":
    # Test with anonymous access (no API key)
    api_key = "34157caaa65e3cc8cece93a578eabd6f76734d29e15bb0a1"
    detector = UrlHausDetector(api_key=api_key)

    # Test URLs
    test_urls = [
        # safe urls
        "https://google.com",  # Should be safe
        "https://chainpatrol.io",  # Should be safe
        # malicious urls
        "https://api.pump.fund/buy"  # Test URL for API verification
    ]

    print("UrlHaus Detector Test")
    print("=" * 50)
    
    # Test single URL
    result = detector.check_url("https://api.pump.fund/buy")
    print(f"Single URL Test:")
    print(f"  Threat Level: {result.threat_level.value}")
    print(f"  Confidence: {result.confidence:.2f}")
    print(f"  Success: {result.success}")
    print(f"  Details: {result.details}")
    print()
    
    #Test multiple URLs
    result = detector.check_urls(test_urls)
    print(f"Multiple URLs Test:")
    print(f"  Threat Level: {result.threat_level.value}")
    print(f"  Confidence: {result.confidence:.2f}")
    print(f"  URLs Checked: {len(result.urls_checked)}")
    print(f"  Malicious Found: {result.details['total_malicious']}")
    print(f"  Success: {result.success}")
    
    if result.success:
        print(f"  URLs Checked: {result.details['total_urls_checked']}")
        print(f"  Unique Domains: No Domains Checked")
        print(f"  Malicious: {result.details['total_malicious']}")
        print(f"  Safe: {result.details['total_safe']}")
        print(f"  Errors: {result.details['total_errors']}")
        
        print("  Domains checked: None")
        
        if result.details['malicious_urls']:
            print("  Detailed Malicious urls:")
            for i, mal_url in enumerate(result.details['url_results'], 1):
                print(f"    {i}. URL: {mal_url['url']}")
                print(f"       Is Malicious: {mal_url['is_malicious']}")
                print(f"       Reference: {mal_url['reference']}")
                print(f"       API Response: {mal_url['full_api_response']}")

        
        if result.details['errors']:
            print("  Errors encountered:")
            for error in result.details['errors']:
                print(f"    - Domain: {error['domain']}")
                print(f"      Error: {error['error']}")
                print()
        else:
            print(f"  Error: {result.error_message}")
    
    print()
    print("Detector Info:")
    info = detector.get_detector_info()
    for key, value in info.items():
        print(f"  {key}: {value}") 
