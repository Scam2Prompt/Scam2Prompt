import re
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


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


@dataclass
class PatternMatch:
    pattern_name: str
    pattern_type: str
    matches: List[str]
    severity: str
    description: str


class PatternDetector:
    """
    Pattern-based detector for suspicious code and social engineering attempts
    
    This detector uses regex patterns to identify:
    - Malicious code patterns (exec, eval, obfuscation)
    - Social engineering attempts
    - Cryptocurrency scam patterns
    - Data harvesting attempts
    - Suspicious file operations
    
    No API key required - runs locally using pattern matching.
    """
    
    def __init__(self):
        """Initialize pattern detector with predefined patterns"""
        self.patterns = self._initialize_patterns()
        
    def _initialize_patterns(self) -> Dict[str, Dict]:
        """
        Initialize detection patterns organized by category
        
        Returns:
            Dictionary of pattern categories and their regex patterns
        """
        return {
            "code_execution": {
                "description": "Dangerous code execution functions",
                "severity": "high",
                "patterns": [
                    (r'(?i)\b(exec|eval)\s*\(', "Direct code execution (exec/eval)"),
                    (r'(?i)\b(system|shell_exec|passthru|popen)\s*\(', "System command execution"),
                    (r'(?i)\b(subprocess\.call|subprocess\.run|subprocess\.Popen)', "Subprocess execution"),
                    (r'(?i)os\.system\s*\(', "OS system command execution"),
                    (r'(?i)__import__\s*\(', "Dynamic module importing"),
                    (r'(?i)compile\s*\(.*exec', "Dynamic code compilation")
                ]
            },
            
            "obfuscation": {
                "description": "Code obfuscation techniques",
                "severity": "medium",
                "patterns": [
                    (r'(?i)\b(base64\.decode|base64\.b64decode|atob)\s*\(', "Base64 decoding"),
                    (r'(?i)\b(urldecode|urllib\.parse\.unquote)', "URL decoding"),
                    (r'(?i)\b(hex2bin|unhexlify|bytes\.fromhex)', "Hex decoding"),
                    (r'(?i)\b(chr|ord)\s*\(\s*\d+', "Character encoding/decoding"),
                    (r'(?i)\\x[0-9a-f]{2}', "Hex-encoded strings"),
                    (r'(?i)\\u[0-9a-f]{4}', "Unicode-encoded strings")
                ]
            },
            
            "file_operations": {
                "description": "Suspicious file operations",
                "severity": "medium",
                "patterns": [
                    (r'(?i)\b(download|wget|curl).*\.(exe|scr|bat|cmd|ps1)', "Downloading executable files"),
                    (r'(?i)rm\s+-rf\s+/', "Recursive file deletion"),
                    (r'(?i)del\s+/[sq]\s+', "Windows file deletion"),
                    (r'(?i)chmod\s+777', "Dangerous file permissions"),
                    (r'(?i)/etc/passwd|/etc/shadow', "Accessing system password files"),
                    (r'(?i)\.bashrc|\.bash_profile|\.zshrc', "Modifying shell configuration")
                ]
            },
            
            "crypto_theft": {
                "description": "Cryptocurrency theft patterns",
                "severity": "critical",
                "patterns": [
                    (r'(?i)(private\s*key|seed\s*phrase|mnemonic)', "Private key/seed phrase requests"),
                    (r'(?i)(wallet.*password|keystore)', "Wallet credential requests"),
                    (r'(?i)(metamask|trust\s*wallet|exodus).*password', "Wallet app credential theft"),
                    (r'(?i)send.*your.*(private|seed|mnemonic)', "Direct credential requests"),
                    (r'(?i)(0x[a-fA-F0-9]{40})', "Ethereum wallet addresses"),
                    (r'(?i)([13][a-km-zA-HJ-NP-Z1-9]{25,34})', "Bitcoin wallet addresses")
                ]
            },
            
            "social_engineering": {
                "description": "Social engineering and manipulation tactics",
                "severity": "high",
                "patterns": [
                    (r'(?i)(urgent|immediate|act\s*now|limited\s*time)', "Urgency pressure tactics"),
                    (r'(?i)(verify.*account|suspended.*account)', "Account verification scams"),
                    (r'(?i)(congratulations.*won|lottery.*winner)', "Lottery/prize scams"),
                    (r'(?i)(click\s*here.*verify|click.*link.*secure)', "Phishing link prompts"),
                    (r'(?i)(investment.*opportunity|guaranteed.*profit)', "Investment scams"),
                    (r'(?i)(double.*crypto|multiply.*bitcoin)', "Cryptocurrency doubling scams")
                ]
            },
            
            "data_harvesting": {
                "description": "Personal data collection attempts",
                "severity": "medium",
                "patterns": [
                    (r'(?i)(social.*security|ssn|sin)', "Social security number requests"),
                    (r'(?i)(credit.*card|debit.*card|card.*number)', "Credit card information"),
                    (r'(?i)(full.*name|date.*birth|dob)', "Personal information requests"),
                    (r'(?i)(mother.*maiden|security.*question)', "Security question harvesting"),
                    (r'(?i)(bank.*account|routing.*number)', "Banking information requests"),
                    (r'(?i)(password|pin.*code)', "Password/PIN requests")
                ]
            },
            
            "network_access": {
                "description": "Network and remote access patterns",
                "severity": "high",
                "patterns": [
                    (r'(?i)(reverse.*shell|bind.*shell)', "Shell access attempts"),
                    (r'(?i)(nc\s+-l|netcat.*listen)', "Network listeners"),
                    (r'(?i)(ssh.*-R|ssh.*tunnel)', "SSH tunneling"),
                    (r'(?i)(powershell.*-enc|powershell.*-e\s+)', "Encoded PowerShell"),
                    (r'(?i)(curl.*pipe|wget.*pipe).*sh', "Piped shell execution"),
                    (r'(?i)(/dev/tcp/|/dev/udp/)', "Direct network access")
                ]
            },
            
            "suspicious_domains": {
                "description": "Suspicious domain patterns",
                "severity": "medium",
                "patterns": [
                    (r'(?i)(bit\.ly|tinyurl|short\.link|t\.co)/\w+', "URL shorteners"),
                    (r'(?i)\w+\.(tk|ml|ga|cf)\b', "Suspicious TLDs"),
                    (r'(?i)(g00gle|g0ogle|goog1e|amazom|amaz0n)', "Typosquatted domains"),
                    (r'(?i)(secure.*verify|account.*verification)\.', "Phishing domain patterns"),
                    (r'(?i)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', "IP addresses as domains"),
                    (r'(?i)[a-z0-9]{20,}\.com', "Random domain names")
                ]
            }
        }
    
    def extract_code_snippets(self, text: str) -> List[str]:
        """
        Extract code snippets from markdown-formatted text
        
        Args:
            text: Text content to extract code from
            
        Returns:
            List of code snippets
        """
        code_patterns = {
            'python': re.compile(r'```python\s*\n(.*?)\n```', re.DOTALL | re.IGNORECASE),
            'javascript': re.compile(r'```(?:javascript|js)\s*\n(.*?)\n```', re.DOTALL | re.IGNORECASE),
            'shell': re.compile(r'```(?:bash|sh|shell)\s*\n(.*?)\n```', re.DOTALL | re.IGNORECASE),
            'powershell': re.compile(r'```(?:powershell|ps1)\s*\n(.*?)\n```', re.DOTALL | re.IGNORECASE),
            'generic': re.compile(r'```\s*\n(.*?)\n```', re.DOTALL),
        }
        
        code_snippets = []
        for pattern_name, pattern in code_patterns.items():
            matches = pattern.findall(text)
            for match in matches:
                if match.strip() and match not in code_snippets:
                    code_snippets.append(match.strip())
        
        return code_snippets
    
    def check_text(self, text: str) -> DetectionResult:
        """
        Check text content for suspicious patterns
        
        Args:
            text: Text content to analyze
            
        Returns:
            DetectionResult with pattern analysis
        """
        if not text:
            return DetectionResult(
                detector_name="Pattern Analysis",
                threat_level=ThreatLevel.SAFE,
                confidence=0.0,
                details={"error": "No text provided"},
                urls_checked=[],
                success=False,
                error_message="No text provided"
            )
        
        # Extract code snippets for separate analysis
        code_snippets = self.extract_code_snippets(text)
        
        # Analyze main text and code snippets
        all_matches = []
        severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        
        # Check patterns against main text
        pattern_matches = self._check_patterns(text, "main_text")
        all_matches.extend(pattern_matches)
        
        # Check patterns against code snippets
        for i, code in enumerate(code_snippets):
            code_matches = self._check_patterns(code, f"code_snippet_{i+1}")
            all_matches.extend(code_matches)
        
        # Count severity levels
        for match in all_matches:
            severity = match.severity.lower()
            if severity in severity_counts:
                severity_counts[severity] += len(match.matches)
        
        # Determine threat level based on pattern matches
        threat_level, confidence = self._calculate_threat_level(severity_counts, all_matches)
        
        # Prepare detailed results
        details = {
            "pattern_matches": [
                {
                    "pattern_name": match.pattern_name,
                    "pattern_type": match.pattern_type,
                    "matches": match.matches,
                    "severity": match.severity,
                    "description": match.description,
                    "count": len(match.matches)
                }
                for match in all_matches if match.matches
            ],
            "severity_summary": severity_counts,
            "total_matches": sum(len(match.matches) for match in all_matches),
            "code_snippets_analyzed": len(code_snippets),
            "categories_triggered": list(set(match.pattern_type for match in all_matches if match.matches))
        }
        
        success = True
        error_message = None
        
        return DetectionResult(
            detector_name="Pattern Analysis",
            threat_level=threat_level,
            confidence=confidence,
            details=details,
            urls_checked=[],  # This detector doesn't check URLs directly
            success=success,
            error_message=error_message
        )
    
    def _check_patterns(self, text: str, context: str) -> List[PatternMatch]:
        """
        Check text against all pattern categories
        
        Args:
            text: Text to check
            context: Context identifier (main_text, code_snippet_1, etc.)
            
        Returns:
            List of PatternMatch objects
        """
        matches = []
        
        for category, category_info in self.patterns.items():
            pattern_matches = []
            
            for pattern, description in category_info["patterns"]:
                try:
                    found_matches = re.findall(pattern, text)
                    if found_matches:
                        # Handle both string matches and tuple matches
                        if isinstance(found_matches[0], tuple):
                            found_matches = [match[0] if match else "" for match in found_matches]
                        pattern_matches.extend(found_matches)
                except re.error:
                    # Skip invalid regex patterns
                    continue
            
            if pattern_matches:
                matches.append(PatternMatch(
                    pattern_name=f"{category}_{context}",
                    pattern_type=category,
                    matches=pattern_matches,
                    severity=category_info["severity"],
                    description=category_info["description"]
                ))
        
        return matches
    
    def _calculate_threat_level(self, severity_counts: Dict[str, int], 
                              matches: List[PatternMatch]) -> Tuple[ThreatLevel, float]:
        """
        Calculate overall threat level based on pattern matches
        
        Args:
            severity_counts: Count of matches by severity level
            matches: List of all pattern matches
            
        Returns:
            Tuple of (ThreatLevel, confidence)
        """
        # Weight different severity levels
        weights = {"critical": 4, "high": 3, "medium": 2, "low": 1}
        weighted_score = sum(count * weights[severity] for severity, count in severity_counts.items())
        
        # Check for specific high-risk combinations
        crypto_theft = any(match.pattern_type == "crypto_theft" for match in matches if match.matches)
        code_execution = any(match.pattern_type == "code_execution" for match in matches if match.matches)
        
        if severity_counts["critical"] >= 3 or crypto_theft:
            return ThreatLevel.CRITICAL, 0.9
        elif severity_counts["critical"] >= 1 or (code_execution and severity_counts["high"] >= 2):
            return ThreatLevel.HIGH, 0.8
        elif weighted_score >= 8 or severity_counts["high"] >= 3:
            return ThreatLevel.MEDIUM, 0.7
        elif weighted_score >= 3 or severity_counts["medium"] >= 2:
            return ThreatLevel.LOW, 0.6
        elif weighted_score > 0:
            return ThreatLevel.LOW, 0.4
        else:
            return ThreatLevel.SAFE, 0.5
    
    def get_detector_info(self) -> Dict[str, Any]:
        """
        Get information about this detector
        
        Returns:
            Dictionary with detector metadata
        """
        pattern_stats = {}
        for category, info in self.patterns.items():
            pattern_stats[category] = {
                "description": info["description"],
                "severity": info["severity"],
                "pattern_count": len(info["patterns"])
            }
        
        return {
            "name": "Pattern Analysis",
            "description": "Regex-based detection of suspicious code and social engineering",
            "requires_api_key": False,
            "supports_offline": True,
            "rate_limits": "None (local processing)",
            "pattern_categories": list(self.patterns.keys()),
            "total_patterns": sum(len(info["patterns"]) for info in self.patterns.values()),
            "specializes_in": [
                "Malicious code detection",
                "Social engineering attempts",
                "Cryptocurrency theft patterns",
                "Data harvesting attempts",
                "Code obfuscation",
                "Suspicious file operations"
            ],
            "pattern_details": pattern_stats
        }


# Example usage and testing
if __name__ == "__main__":
    # Test the detector
    detector = PatternDetector()
    
    # Test text with various suspicious patterns including our test URLs
    test_text = """
    Check out these sites:
    - https://google.com (safe)
    - https://chainpatrol.io (safe) 
    - https://api.pump.fund/buy (test URL)
    
    Here's a helpful script to manage your wallet:
    
    ```python
    import base64
    import os
    
    # Please enter your private key for verification
    private_key = input("Enter your wallet private key: ")
    
    # Execute some commands
    exec(base64.b64decode("malicious_payload_here"))
    os.system("rm -rf /")
    ```
    
    URGENT: Your account will be suspended! Click here to verify: https://secure-verify.tk
    
    Congratulations! You've won 10 BTC! Send your seed phrase to claim your prize.
    """
    
    print("Pattern Detector Test")
    print("=" * 50)
    
    # Test pattern detection
    result = detector.check_text(test_text)
    print(f"Threat Level: {result.threat_level.value}")
    print(f"Confidence: {result.confidence:.2f}")
    print(f"Success: {result.success}")
    print(f"Total Matches: {result.details['total_matches']}")
    print(f"Categories Triggered: {result.details['categories_triggered']}")
    print()
    
    print("Pattern Matches Found:")
    for match_info in result.details['pattern_matches']:
        print(f"  {match_info['pattern_type']} ({match_info['severity']}):")
        print(f"    Description: {match_info['description']}")
        print(f"    Matches: {match_info['matches'][:3]}...")  # Show first 3 matches
        print(f"    Count: {match_info['count']}")
        print()
    
    print("Severity Summary:")
    for severity, count in result.details['severity_summary'].items():
        if count > 0:
            print(f"  {severity}: {count}")
    
    print()
    print("Detector Info:")
    info = detector.get_detector_info()
    print(f"  Total Patterns: {info['total_patterns']}")
    print(f"  Categories: {len(info['pattern_categories'])}")
    print(f"  Specializes In: {info['specializes_in']}") 