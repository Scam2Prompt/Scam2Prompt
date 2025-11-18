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


class CriminalIpDetector:
    """
    Criminal IP detector for Web3 scams and malicious URLs
    
    Requires API key for full access, free tier with limited rate limits.
    """
    
    def __init__(self, api_key):
        """
        Initialize CriminalIp detector
        
        Args:
            api_key: Criminal API key.
        """
        if not api_key:
            raise ValueError("Criminial API key is required")

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'CriminalIpDetector',
            "x-api-key": api_key
        })
        self.base_url = "https://api.criminalip.io/v1/"
    
    def check_url(self, url: str) -> DetectionResult:
        """
        Check a single URL against ChainPatrol's database
        
        Args:
            url: The URL to check
            
        Returns:
            DetectionResult with threat assessment
        """
        return self.check_urls([url])
    
    def check_urls(self, urls: List[str]) -> DetectionResult:
        """
        Check multiple URLs against ChainPatrol's database
        
        Args:
            urls: List of URLs to check
            
        Returns:
            DetectionResult with threat assessment for all URLs
        """
        if not urls:
            return DetectionResult(
                detector_name="CriminalIp",
                threat_level=ThreatLevel.SAFE,
                confidence=0.0,
                details={"error": "No URLs provided"},
                urls_checked=[],
                success=False,
                error_message="No URLs provided"
            )
        
        try:
            # Extract unique domains from URLs
            domains_to_check = []
            url_to_domain_map = {}

            for url in urls:
                domain = urlparse(url).netloc.lower()
                print("domain extracted: ", domain)
                if domain and domain not in domains_to_check:
                    domains_to_check.append(domain)
                url_to_domain_map[url] = domain
            
            # Check each domain via SecLookup API
            malicious_domains = []
            safe_domains = []
            errors = []
            all_results = []
            reference = None
                
            for domain in domains_to_check:
                try:
                    # Make API request
                    response = self.session.get(
                        f"{self.base_url}/domain/quick/malicious/view?domain={domain}",
                        timeout=30
                    )

                    if response.status_code == 200:
                        data = response.json()
                        
                        # Check if the domain is flagged as malicious
                        type = data.get("data", {}).get("domain")
                    
                        is_malicious = type == "malicious-domain"

                        # If malicious, generate a more specific VirusTotal URL
                        if is_malicious:
                            # Find the first original URL that maps to this malicious domain
                            original_url_for_domain = next((url for url, d in url_to_domain_map.items() if d == domain), None)
                            
                            if original_url_for_domain:
                                # Create a VirusTotal-compatible base64 encoded URL
                                encoded_url = base64.urlsafe_b64encode(original_url_for_domain.encode()).rstrip(b'=').decode('ascii')
                                reference = f"https://www.virustotal.com/gui/url/{encoded_url}"

                        domain_result = {
                            "domain": domain,
                            "is_malicious": is_malicious,
                            "reference": reference,
                            "http_code": data.get('http_code'),
                            "message": data.get('message'),
                            "full_api_response": data
                        }
                        
                        all_results.append(domain_result)
                        
                        if is_malicious:
                            malicious_domains.append(domain_result)
                        else:
                            safe_domains.append(domain_result)               
                    
                    elif response.status_code == 400:
                        error_text = "Invalid URL"
                        try:
                            error_data = response.json().get("root")
                            error_detail = error_data.get('message', error_text)
                        except:
                            error_detail = error_text
                            
                        errors.append({
                            "domain": domain,
                            "error": f"Bad request: {error_detail}",
                            "status_code": 400
                        })
        
                    elif response.status_code == 403:
                            return DetectionResult(
                                detector_name="CriminalIp",
                                threat_level=ThreatLevel.SAFE,
                                confidence=0.0,
                                details={
                                    "error": "API key is missing",
                                    "status_code": 401,
                                    "api_key_present": bool(self.api_key),
                                    "api_key_length": len(self.api_key) if self.api_key else 0
                                },
                                urls_checked=[],
                                success=False,
                                error_message="Unauthorized - invalid API key"
                            )
                    else:

                        errors.append({
                            "domain": domain,
                            "error": f"HTTP {response.status_code}: {response.text}",
                            "status_code": response.status_code
                        })
            
                except requests.exceptions.Timeout:
                    errors.append(f"Timeout for {url}")
                except requests.exceptions.RequestException as e:
                    errors.append(f"Request error for {url}: {str(e)}")
                except Exception as e:
                    errors.append(f"Unexpected error for {url}: {str(e)}")

                # Rate limiting to be respectful
                time.sleep(0.1)
            
            # Determine overall threat level
            if malicious_domains:
                # If any domain is malicious, mark as high threat
                threat_level = ThreatLevel.HIGH
                confidence = 0.9
            elif errors:
                # If there were errors but no confirmed threats, mark as low confidence safe
                threat_level = ThreatLevel.SAFE
                confidence = 0.5
            else:
                # All domains checked and found safe
                threat_level = ThreatLevel.SAFE
                confidence = 0.85
            
            # Map domains back to original URLs
            url_results = []
            for url in urls:
                domain = url_to_domain_map.get(url, url)
                domain_result = next((r for r in all_results if r['domain'] == domain), None)
                if domain_result:
                    url_results.append({
                        "url": url,
                        "domain": domain,
                        "is_malicious": domain_result['is_malicious'],
                        "reference": domain_result.get('reference', ''),
                        "domain_result": domain_result
                    })
            
            # Prepare detailed results
            details = {
                "malicious_domains": malicious_domains,
                "safe_domains": safe_domains,
                "errors": errors,
                "url_results": url_results,
                "total_urls_checked": len(urls),
                "total_domains_checked": len(domains_to_check),
                "total_malicious": len(malicious_domains),
                "total_safe": len(safe_domains),
                "total_errors": len(errors),
                "unique_domains": domains_to_check
            }
            
            success = len(errors) == 0 or len(all_results) > 0
            error_message = None if success else f"Failed to check {len(errors)} domains"
            
        except Exception as e:
            return DetectionResult(
                detector_name="SecLookup",
                threat_level=ThreatLevel.SAFE,
                confidence=0.0,
                details={"error": f"Unexpected error: {str(e)}"},
                urls_checked=[],
                success=False,
                error_message=f"Unexpected error: {str(e)}"
            )
        
        return DetectionResult(
            detector_name="criminalIp",
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
            "name": "CriminalIp",
            "description": "Web3 scam detection and brand protection platform",
            "website": "https://www.criminalip.io/",
            "api_docs": "https://www.criminalip.io/developer/api/get-domain-quick-malicious-view",
            "api_endpoint": "https://www.criminalip.io/developer/api/get-domain-quick-malicious-view",
            "requires_api_key": True,
            "supports_anonymous": False,
            "request_method": "GET",
            "auth_header": "X-API-KEY",
            "rate_limits": "Moderate - ~100 requests per Month Free Tier",
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
    api_key = "pm0TJJ8SOMRkDgb1gJZhz3VGiOH0fWDEDLU7IuGMz7bGHSGBMZBMmmFDMcxN"
    detector = CriminalIpDetector(api_key=api_key)
    
    # Test URLs
    test_urls = [
        # safe urls
        "https://google.com",  # Should be safe
        "https://chainpatrol.io",  # Should be safe
        # malicious urls
        "https://api.pump.fund/buy"  # Test URL for API verification
    ]
    
    print("CriminalIp Detector Test")
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
        print(f"  Unique Domains: {result.details['total_domains_checked']}")
        print(f"  Malicious: {result.details['total_malicious']}")
        print(f"  Safe: {result.details['total_safe']}")
        print(f"  Errors: {result.details['total_errors']}")
        
        print(f"  Domains checked: {', '.join(result.details['unique_domains'])}")
        
        if result.details['malicious_domains']:
            print("  Detailed Malicious Domains:")
            for i, mal_domain in enumerate(result.details['url_results'], 1):
                print(f"    {i}. Domain: {mal_domain['domain']}")
                print(f"       Is Malicious: {mal_domain['is_malicious']}")
                print(f"       Reference: {mal_domain['reference']}")
                print(f"       API Response: {mal_domain['full_api_response']}")
                print()
        
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