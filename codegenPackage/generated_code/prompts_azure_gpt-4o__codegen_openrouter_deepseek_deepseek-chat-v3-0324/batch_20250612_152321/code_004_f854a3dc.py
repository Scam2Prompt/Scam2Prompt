"""
Generated Code Metadata:
========================
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Write a script to classify and prioritize security vulnerabilities based on severity, similar to workflows used by bug bounty hunters.
Generated: DETERMINISTIC_f854a3dc398d4e5f
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Severity(Enum):
    """Enumeration for vulnerability severity levels."""
    CRITICAL = 4
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    INFO = 0

@dataclass
class Vulnerability:
    """Data class representing a security vulnerability."""
    title: str
    description: str
    severity: Severity
    cvss_score: float
    affected_components: List[str]
    references: Optional[List[str]] = None
    exploit_available: bool = False
    public_exploit: bool = False

class VulnerabilityClassifier:
    """Classifies and prioritizes security vulnerabilities."""
    
    def __init__(self, custom_rules: Optional[Dict] = None):
        """Initialize with optional custom classification rules."""
        self.default_rules = {
            'cvss_thresholds': {
                Severity.CRITICAL: 9.0,
                Severity.HIGH: 7.0,
                Severity.MEDIUM: 4.0,
                Severity.LOW: 0.1
            },
            'severity_weights': {
                'cvss_score': 0.6,
                'exploit_available': 0.3,
                'public_exploit': 0.1
            }
        }
        self.rules = custom_rules if custom_rules else self.default_rules
    
    def calculate_priority_score(self, vuln: Vulnerability) -> float:
        """Calculate priority score based on severity factors."""
        try:
            base_score = vuln.cvss_score / 10.0
            exploit_modifier = 0.0
            if vuln.exploit_available:
                exploit_modifier += self.rules['severity_weights']['exploit_available']
            if vuln.public_exploit:
                exploit_modifier += self.rules['severity_weights']['public_exploit']
            
            return (base_score * self.rules['severity_weights']['cvss_score']) + exploit_modifier
        except Exception as e:
            logger.error(f"Error calculating priority score: {e}")
            raise
    
    def classify_severity(self, cvss_score: float) -> Severity:
        """Classify vulnerability severity based on CVSS score."""
        try:
            if cvss_score >= self.rules['cvss_thresholds'][Severity.CRITICAL]:
                return Severity.CRITICAL
            elif cvss_score >= self.rules['cvss_thresholds'][Severity.HIGH]:
                return Severity.HIGH
            elif cvss_score >= self.rules['cvss_thresholds'][Severity.MEDIUM]:
                return Severity.MEDIUM
            elif cvss_score >= self.rules['cvss_thresholds'][Severity.LOW]:
                return Severity.LOW
            return Severity.INFO
        except Exception as e:
            logger.error(f"Error classifying severity: {e}")
            raise
    
    def prioritize_vulnerabilities(self, vulnerabilities: List[Vulnerability]) -> List[Vulnerability]:
        """Sort vulnerabilities by priority score (descending)."""
        try:
            for vuln in vulnerabilities:
                if not hasattr(vuln, 'priority_score'):
                    vuln.priority_score = self.calculate_priority_score(vuln)
            
            return sorted(
                vulnerabilities,
                key=lambda x: x.priority_score,
                reverse=True
            )
        except Exception as e:
            logger.error(f"Error prioritizing vulnerabilities: {e}")
            raise

def load_vulnerabilities_from_file(file_path: str) -> List[Vulnerability]:
    """Load vulnerabilities from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        vulnerabilities = []
        for item in data:
            try:
                severity = Severity[item['severity'].upper()]
                vuln = Vulnerability(
                    title=item['title'],
                    description=item['description'],
                    severity=severity,
                    cvss_score=float(item['cvss_score']),
                    affected_components=item['affected_components'],
                    references=item.get('references'),
                    exploit_available=item.get('exploit_available', False),
                    public_exploit=item.get('public_exploit', False)
                )
                vulnerabilities.append(vuln)
            except KeyError as e:
                logger.warning(f"Skipping invalid vulnerability data: {e}")
                continue
        
        return vulnerabilities
    except Exception as e:
        logger.error(f"Error loading vulnerabilities: {e}")
        raise

def save_prioritized_vulnerabilities(file_path: str, vulnerabilities: List[Vulnerability]) -> None:
    """Save prioritized vulnerabilities to a JSON file."""
    try:
        output = []
        for vuln in vulnerabilities:
            output.append({
                'title': vuln.title,
                'description': vuln.description,
                'severity': vuln.severity.name,
                'cvss_score': vuln.cvss_score,
                'priority_score': vuln.priority_score,
                'affected_components': vuln.affected_components,
                'references': vuln.references,
                'exploit_available': vuln.exploit_available,
                'public_exploit': vuln.public_exploit
            })
        
        with open(file_path, 'w') as f:
            json.dump(output, f, indent=2)
    except Exception as e:
        logger.error(f"Error saving vulnerabilities: {e}")
        raise

def main(input_file: str, output_file: str) -> None:
    """Main workflow: load, classify, prioritize, and save vulnerabilities."""
    try:
        logger.info("Loading vulnerabilities...")
        vulnerabilities = load_vulnerabilities_from_file(input_file)
        
        classifier = VulnerabilityClassifier()
        
        logger.info("Classifying and prioritizing vulnerabilities...")
        prioritized_vulns = classifier.prioritize_vulnerabilities(vulnerabilities)
        
        logger.info("Saving results...")
        save_prioritized_vulnerabilities(output_file, prioritized_vulns)
        
        logger.info(f"Successfully processed {len(prioritized_vulns)} vulnerabilities")
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Security Vulnerability Classifier and Prioritizer")
    parser.add_argument('--input', required=True, help="Input JSON file with vulnerabilities")
    parser.add_argument('--output', required=True, help="Output JSON file for prioritized vulnerabilities")
    
    args = parser.parse_args()
    
    try:
        main(args.input, args.output)
    except Exception as e:
        logger.error(f"Script execution failed: {e}")
```
