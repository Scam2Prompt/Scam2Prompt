import requests
import time
from typing import List, Dict, Any, Optional
from urllib.parse import urlparse
from dataclasses import dataclass
from enum import Enum
import xml.etree.ElementTree as ET


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


class URLVoidDetector:
    """
    URLVoid detector for domain reputation checking
    
    URLVoid checks domains against multiple blacklist engines and provides
    reputation information including domain age, country, and security vendor
    detections.
    
    Requires API key from URLVoid.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize URLVoid detector
        
        Args:
            api_key: URLVoid API key (required)
        """
        if not api_key:
            raise ValueError("URLVoid API key is required")
            
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'URLVoidDetector/1.0'
        })
        self.base_url = "http://api.urlvoid.com/v1/pay-as-you-go"
        self.rate_limit_delay = 1  # URLVoid has strict rate limits
    
    def _parse_xml_response(self, xml_content: str) -> Dict[str, Any]:
        """
        Parse URLVoid XML response
        
        Args:
            xml_content: XML response content
            
        Returns:
            Dictionary with parsed data
        """
        try:
            root = ET.fromstring(xml_content)
            
            # Extract basic info
            result = {
                "domain": root.find('.//host').text if root.find('.//host') is not None else 'Unknown',
                "detections": [],
                "engines_count": 0,
                "detection_ratio": "0/0"
            }
            
            # Extract detection engines
            detections_elem = root.find('.//detections')
            if detections_elem is not None:
                result["engines_count"] = int(detections_elem.get('count', 0))
                
                for engine in detections_elem.findall('engine'):
                    result["detections"].append({
                        'name': engine.text,
                        'detected': True
                    })
            
            # Extract engine count info
            engines_elem = root.find('.//engines')
            if engines_elem is not None:
                total_engines = int(engines_elem.get('count', 0))
                detection_count = len(result["detections"])
                result["detection_ratio"] = f"{detection_count}/{total_engines}"
                result["total_engines"] = total_engines
            
            # Extract domain info if available
            domain_info = {}
            if root.find('.//domain_1and1') is not None:
                domain_info["1and1"] = root.find('.//domain_1and1').text
            if root.find('.//domain_age') is not None:
                domain_info["age"] = root.find('.//domain_age').text
            if root.find('.//domain_country_code') is not None:
                domain_info["country"] = root.find('.//domain_country_code').text
                
            result["domain_info"] = domain_info
            
            return result
            
        except ET.ParseError as e:
            return {"error": f"XML parsing error: {str(e)}", "raw_content": xml_content[:500]}
        except Exception as e:
            return {"error": f"Parsing error: {str(e)}", "raw_content": xml_content[:500]}
    
    def check_url(self, url: str) -> DetectionResult:
        """
        Check a single URL against URLVoid
        
        Args:
            url: The URL to check
            
        Returns:
            DetectionResult with threat assessment
        """
        return self.check_urls([url])
    
    def check_urls(self, urls: List[str], max_urls: int = 3) -> DetectionResult:
        """
        Check multiple URLs against URLVoid
        
        Args:
            urls: List of URLs to check
            max_urls: Maximum number of URLs to check (rate limiting)
            
        Returns:
            DetectionResult with threat assessment for all URLs
        """
        if not urls:
            return DetectionResult(
                detector_name="URLVoid",
                threat_level=ThreatLevel.SAFE,
                confidence=0.0,
                details={"error": "No URLs provided"},
                urls_checked=[],
                success=False,
                error_message="No URLs provided"
            )
        
        # Limit URLs due to strict rate limits
        urls_to_check = urls[:max_urls]
        scan_results = []
        errors = []
        total_detections = 0
        total_engines = 0
        
        for i, url in enumerate(urls_to_check):
            try:
                # Extract domain from URL
                domain = urlparse(url).netloc.lower()
                if not domain:
                    errors.append(f"Could not extract domain from {url}")
                    continue
                
                # Make API request
                response = self.session.get(
                    f"{self.base_url}/?key={self.api_key}&host={domain}",
                    timeout=30
                )
                
                if response.status_code == 200:
                    # Parse XML response
                    parsed_data = self._parse_xml_response(response.text)
                    
                    if "error" in parsed_data:
                        errors.append(f"Parse error for {url}: {parsed_data['error']}")
                        continue
                    
                    detection_count = len(parsed_data.get("detections", []))
                    engines_count = parsed_data.get("total_engines", 0)
                    
                    scan_results.append({
                        "url": url,
                        "domain": domain,
                        "detections": parsed_data.get("detections", []),
                        "detection_count": detection_count,
                        "total_engines": engines_count,
                        "detection_ratio": parsed_data.get("detection_ratio", "0/0"),
                        "domain_info": parsed_data.get("domain_info", {})
                    })
                    
                    total_detections += detection_count
                    total_engines += engines_count
                    
                elif response.status_code == 429:
                    errors.append(f"Rate limited for {url}")
                    break  # Stop to avoid further rate limiting
                elif response.status_code == 400:
                    errors.append(f"Bad request for {url} - check domain format")
                else:
                    errors.append(f"HTTP {response.status_code} for {url}")
                
                # Rate limiting - sleep between requests except for last URL
                if i < len(urls_to_check) - 1:
                    time.sleep(self.rate_limit_delay)
                    
            except requests.exceptions.Timeout:
                errors.append(f"Timeout for {url}")
            except requests.exceptions.RequestException as e:
                errors.append(f"Request error for {url}: {str(e)}")
            except Exception as e:
                errors.append(f"Unexpected error for {url}: {str(e)}")
        
        # Determine threat level based on detection results
        if not scan_results:
            threat_level = ThreatLevel.SAFE
            confidence = 0.0
        else:
            # Calculate overall detection ratio
            if total_engines > 0:
                detection_ratio = total_detections / total_engines
                
                if detection_ratio >= 0.3:  # 30%+ engines detected threats
                    threat_level = ThreatLevel.HIGH
                    confidence = 0.8
                elif detection_ratio >= 0.15:  # 15%+ engines detected threats
                    threat_level = ThreatLevel.MEDIUM
                    confidence = 0.7
                elif detection_ratio >= 0.05:  # 5%+ engines detected threats
                    threat_level = ThreatLevel.LOW
                    confidence = 0.6
                else:
                    threat_level = ThreatLevel.SAFE
                    confidence = 0.75
            else:
                threat_level = ThreatLevel.SAFE
                confidence = 0.5
        
        # Prepare detailed results
        details = {
            "scan_results": scan_results,
            "total_checked": len(scan_results),
            "total_detections": total_detections,
            "total_engines_checked": total_engines,
            "overall_detection_ratio": f"{total_detections}/{total_engines}" if total_engines > 0 else "0/0",
            "errors": errors,
            "rate_limited": any("rate limited" in error.lower() for error in errors)
        }
        
        success = len(scan_results) > 0
        error_message = None if success else f"Failed to scan URLs: {'; '.join(errors)}"
        
        return DetectionResult(
            detector_name="URLVoid",
            threat_level=threat_level,
            confidence=confidence,
            details=details,
            urls_checked=[result["url"] for result in scan_results],
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
            "name": "URLVoid",
            "description": "Domain reputation checker using multiple blacklist engines",
            "website": "https://www.urlvoid.com",
            "api_docs": "https://www.urlvoid.com/api/",
            "api_endpoint": "http://api.urlvoid.com/v1/pay-as-you-go",
            "requires_api_key": True,
            "api_key_url": "https://www.urlvoid.com/api/",
            "request_method": "GET",
            "response_format": "XML",
            "rate_limits": "Very strict - 1 request per second recommended",
            "max_recommended_urls": 3,
            "checks_against": "Multiple blacklist engines and reputation databases",
            "provides_info": [
                "Domain reputation",
                "Blacklist engine detections",
                "Domain age and registration info",
                "Geographic location",
                "Detection ratio statistics"
            ],
            "specializes_in": [
                "Domain reputation analysis",
                "Blacklist database aggregation",
                "Suspicious domain detection",
                "Malware hosting identification",
                "Phishing site detection"
            ]
        }


# Example usage and testing
if __name__ == "__main__":
    # Note: You need a real URLVoid API key to test this
    try:
        # Replace with your actual API key
        detector = URLVoidDetector("your_urlvoid_api_key_here")
        
        # Test URLs - same as ChainPortal detector
        test_urls = [
            # safe urls
            "https://google.com",  # Should be safe
            "https://chainpatrol.io",  # Should be safe
            # test urls
            "https://api.pump.fund/buy"  # Test URL for API verification
        ]
        
        print("URLVoid Detector Test")
        print("=" * 50)
        print("Note: This test requires a valid URLVoid API key")
        print("Warning: URLVoid has strict rate limits - testing with limited URLs")
        print()
        
        # Test single URL
        result = detector.check_url("https://api.pump.fund/buy")
        print(f"Single URL Test:")
        print(f"  Threat Level: {result.threat_level.value}")
        print(f"  Confidence: {result.confidence:.2f}")
        print(f"  Success: {result.success}")
        
        if result.success and result.details['scan_results']:
            scan_result = result.details['scan_results'][0]
            print(f"  Domain: {scan_result['domain']}")
            print(f"  Detection Ratio: {scan_result['detection_ratio']}")
            print(f"  Detections: {scan_result['detection_count']}")
            
            if scan_result['detections']:
                print("  Detected by engines:")
                for detection in scan_result['detections'][:5]:  # Show first 5
                    print(f"    - {detection['name']}")
        elif not result.success:
            print(f"  Error: {result.error_message}")
        print()
        
        # Test multiple URLs (limited due to rate limits)
        limited_urls = test_urls[:2]  # Only test 2 URLs due to rate limits
        result = detector.check_urls(limited_urls)
        print(f"Multiple URLs Test (limited to {len(limited_urls)} URLs):")
        print(f"  Threat Level: {result.threat_level.value}")
        print(f"  Confidence: {result.confidence:.2f}")
        print(f"  Success: {result.success}")
        
        if result.success:
            print(f"  URLs Checked: {result.details['total_checked']}")
            print(f"  Total Detections: {result.details['total_detections']}")
            print(f"  Overall Ratio: {result.details['overall_detection_ratio']}")
            
            for scan_result in result.details['scan_results']:
                print(f"    {scan_result['domain']}: {scan_result['detection_ratio']}")
        elif not result.success:
            print(f"  Error: {result.error_message}")
        
        print()
        print("Detector Info:")
        info = detector.get_detector_info()
        for key, value in info.items():
            if key not in ['provides_info', 'specializes_in']:
                print(f"  {key}: {value}")
            
    except ValueError as e:
        print(f"Error: {e}")
        print("Please provide a valid URLVoid API key to test this detector.") 