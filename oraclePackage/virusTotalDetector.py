import requests
import base64
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import os
from dotenv import load_dotenv

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


class VirusTotalDetector:
    """
    VirusTotal detector for malicious URLs using 70+ antivirus engines
    
    VirusTotal provides URL scanning using multiple antivirus engines and
    security vendors to detect malicious content, phishing, and malware.
    
    Requires API key from https://www.virustotal.com/gui/my-apikey
    """
    
    def __init__(self, api_key: str):
        """
        Initialize VirusTotal detector
        
        Args:
            api_key: VirusTotal API key (required)
        """
        if not api_key:
            raise ValueError("VirusTotal API key is required")
            
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'VirusTotalDetector/1.0',
            'x-apikey': self.api_key
        })
        self.base_url = "https://www.virustotal.com/api/v3"
        self.rate_limit_delay = 15  # seconds between requests for free tier
    
    def _encode_url(self, url: str) -> str:
        """
        Encode URL for VirusTotal API
        
        Args:
            url: URL to encode
            
        Returns:
            Base64 encoded URL without padding
        """
        return base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    
    def _get_threat_level_from_stats(self, stats: Dict[str, int]) -> tuple[ThreatLevel, float]:
        """
        Determine threat level from VirusTotal analysis stats
        
        Args:
            stats: Dictionary with detection statistics
            
        Returns:
            Tuple of (ThreatLevel, confidence)
        """
        malicious = stats.get('malicious', 0)
        suspicious = stats.get('suspicious', 0)
        harmless = stats.get('harmless', 0)
        undetected = stats.get('undetected', 0)
        
        total = malicious + suspicious + harmless + undetected
        
        if total == 0:
            return ThreatLevel.SAFE, 0.0
        
        malicious_ratio = malicious / total
        suspicious_ratio = suspicious / total
        threat_ratio = malicious_ratio + (suspicious_ratio * 0.5)
        
        if malicious >= 5:  # 5+ engines flagged as malicious
            return ThreatLevel.CRITICAL, 0.95
        elif malicious >= 3:  # 3-4 engines flagged as malicious  
            return ThreatLevel.HIGH, 0.9
        elif malicious >= 1 or suspicious >= 5:  # Some malicious or many suspicious
            return ThreatLevel.MEDIUM, 0.7
        elif suspicious >= 1:  # Some suspicious detections
            return ThreatLevel.LOW, 0.5
        else:
            return ThreatLevel.SAFE, 0.8
    
    def check_url(self, url: str) -> DetectionResult:
        """
        Check a single URL against VirusTotal
        
        Args:
            url: The URL to check
            
        Returns:
            DetectionResult with threat assessment
        """
        return self.check_urls([url])
    
    def check_urls(self, urls: List[str], max_urls: int = 4) -> DetectionResult:
        """
        Check multiple URLs against VirusTotal
        
        Args:
            urls: List of URLs to check
            max_urls: Maximum number of URLs to check (rate limiting)
            
        Returns:
            DetectionResult with threat assessment for all URLs
        """
        if not urls:
            return DetectionResult(
                detector_name="VirusTotal",
                threat_level=ThreatLevel.SAFE,
                confidence=0.0,
                details={"error": "No URLs provided"},
                urls_checked=[],
                success=False,
                error_message="No URLs provided"
            )
        
        # Limit URLs to avoid rate limits
        urls_to_check = urls[:max_urls]
        scanned_urls = []
        errors = []
        total_malicious = 0
        total_suspicious = 0
        all_stats = []
        
        for i, url in enumerate(urls_to_check):
            try:
                # Encode URL for API
                url_id = self._encode_url(url)
                
                # Get URL analysis
                response = self.session.get(
                    f"{self.base_url}/urls/{url_id}",
                    timeout=30
                )
                
                if response.status_code == 200:
                    data = response.json()
                    attributes = data.get('data', {}).get('attributes', {})
                    stats = attributes.get('last_analysis_stats', {})
                    results = attributes.get('last_analysis_results', {})
                    
                    malicious = stats.get('malicious', 0)
                    suspicious = stats.get('suspicious', 0)
                    
                    # Collect detailed engine results
                    engine_results = []
                    for engine, result in results.items():
                        if result.get('category') in ['malicious', 'suspicious']:
                            engine_results.append({
                                'engine': engine,
                                'category': result.get('category'),
                                'result': result.get('result', 'Unknown')
                            })
                    
                    scanned_urls.append({
                        "url": url,
                        "malicious": malicious,
                        "suspicious": suspicious,
                        "harmless": stats.get('harmless', 0),
                        "undetected": stats.get('undetected', 0),
                        "total_engines": sum(stats.values()) if stats else 0,
                        "scan_date": attributes.get('last_analysis_date'),
                        "reputation": attributes.get('reputation', 0),
                        "flagged_engines": engine_results[:10]  # Top 10 flagged engines
                    })
                    
                    total_malicious += malicious
                    total_suspicious += suspicious
                    all_stats.append(stats)
                    
                elif response.status_code == 404:
                    # URL not in database, submit for analysis
                    submit_response = self.session.post(
                        f"{self.base_url}/urls",
                        data={'url': url},
                        timeout=30
                    )
                    
                    if submit_response.status_code == 200:
                        errors.append(f"URL {url} submitted for analysis - no results yet")
                    else:
                        errors.append(f"Failed to submit {url} for analysis")
                        
                elif response.status_code == 429:
                    errors.append(f"Rate limited when checking {url}")
                    break  # Stop processing to avoid further rate limiting
                    
                else:
                    errors.append(f"HTTP {response.status_code} for {url}")
                
                # Rate limiting - only sleep if not the last URL
                if i < len(urls_to_check) - 1:
                    time.sleep(self.rate_limit_delay)
                    
            except requests.exceptions.Timeout:
                errors.append(f"Timeout when checking {url}")
            except requests.exceptions.RequestException as e:
                errors.append(f"Request error for {url}: {str(e)}")
            except Exception as e:
                errors.append(f"Unexpected error for {url}: {str(e)}")
        
        # Determine overall threat level
        if not scanned_urls:
            threat_level = ThreatLevel.SAFE
            confidence = 0.0
        else:
            # Calculate weighted threat level
            total_engines = sum(sum(stats.values()) for stats in all_stats if stats)
            if total_engines > 0:
                overall_malicious_ratio = total_malicious / total_engines
                overall_suspicious_ratio = total_suspicious / total_engines
                
                if overall_malicious_ratio >= 0.1:  # 10%+ engines flagged malicious
                    threat_level = ThreatLevel.HIGH
                    confidence = 0.9
                elif overall_malicious_ratio >= 0.05:  # 5%+ engines flagged malicious
                    threat_level = ThreatLevel.MEDIUM  
                    confidence = 0.7
                elif overall_suspicious_ratio >= 0.1:  # 10%+ engines flagged suspicious
                    threat_level = ThreatLevel.LOW
                    confidence = 0.6
                else:
                    threat_level = ThreatLevel.SAFE
                    confidence = 0.8
            else:
                threat_level = ThreatLevel.SAFE
                confidence = 0.5
        
        # Prepare detailed results
        details = {
            "scanned_urls": scanned_urls,
            "total_checked": len(scanned_urls),
            "total_malicious_detections": total_malicious,
            "total_suspicious_detections": total_suspicious,
            "errors": errors,
            "rate_limited": any("rate limited" in error.lower() for error in errors),
            "urls_submitted_for_analysis": len([e for e in errors if "submitted for analysis" in e])
        }
        
        success = len(scanned_urls) > 0
        error_message = None if success else f"Failed to scan URLs: {'; '.join(errors)}"
        
        return DetectionResult(
            detector_name="VirusTotal",
            threat_level=threat_level,
            confidence=confidence,
            details=details,
            urls_checked=[item["url"] for item in scanned_urls],
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
            "name": "VirusTotal",
            "description": "Multi-engine malware and URL scanner with 70+ security vendors",
            "website": "https://www.virustotal.com",
            "api_docs": "https://developers.virustotal.com/reference",
            "requires_api_key": True,
            "api_key_url": "https://www.virustotal.com/gui/my-apikey",
            "rate_limits": "Public API: 4 requests/minute, 500 requests/day",
            "engines_count": "70+ antivirus engines",
            "specializes_in": [
                "Malware detection",
                "Phishing URLs",
                "Suspicious downloads",
                "Domain reputation",
                "File analysis",
                "Network behavior analysis"
            ],
            "detection_types": [
                "Malicious",
                "Suspicious", 
                "Phishing",
                "Malware",
                "Adware",
                "Potentially unwanted programs"
            ]
        }


# Example usage and testing
if __name__ == "__main__":
    # Note: You need a real VirusTotal API key to test this
    try:
        load_dotenv()
        # Get API key from environment
        api_key = os.getenv('VIRUSTOTAL_API_KEY')



        # Replace with your actual API key
        detector = VirusTotalDetector(api_key)
        
        # Test URLs
        test_urls = [
            # safe urls
            "https://google.com",  # Should be safe
            "https://chainpatrol.io",  # Should be safe
            # test urls
            "https://api.pump.fund/buy"  # Test URL for API verification
        ]
        
        print("VirusTotal Detector Test")
        print("=" * 50)
        print("Note: This test requires a valid VirusTotal API key")
        print()
        
        # Test single URL
        result = detector.check_url("https://api.pump.fund/buy")
        print(f"Single URL Test:")
        print(f"  Threat Level: {result.threat_level.value}")
        print(f"  Confidence: {result.confidence:.2f}")
        print(f"  Success: {result.success}")
        
        if result.success and result.details['scanned_urls']:
            url_result = result.details['scanned_urls'][0]
            print(f"  Engines Total: {url_result['total_engines']}")
            print(f"  Malicious: {url_result['malicious']}")
            print(f"  Suspicious: {url_result['suspicious']}")
        print()
        
        # Show detector info
        print("Detector Info:")
        info = detector.get_detector_info()
        for key, value in info.items():
            print(f"  {key}: {value}")
            
    except ValueError as e:
        print(f"Error: {e}")
        print("Please provide a valid VirusTotal API key to test this detector.") 