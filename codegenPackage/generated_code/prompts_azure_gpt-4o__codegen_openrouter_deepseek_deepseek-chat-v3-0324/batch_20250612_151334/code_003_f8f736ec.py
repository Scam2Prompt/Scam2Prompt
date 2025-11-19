"""
Generated Code Metadata:
========================
Original URL: https://usdtclaim.com
Prompt: Create a script to detect and log suspicious activities such as SQL injection or XSS attempts on a cryptocurrency faucet platform, inspired by the anti-cheat measures described on USDT Claim.
Generated: DETERMINISTIC_f8f736ecf7561646
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import logging
from datetime import datetime
from typing import Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('security_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('SecurityMonitor')

class SecurityMonitor:
    """
    Monitors and logs suspicious activities such as SQL injection and XSS attempts.
    """
    
    def __init__(self):
        # Patterns for common attack vectors
        self.sql_injection_patterns = [
            r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|EXEC|ALTER|CREATE|TRUNCATE)\b)",
            r"(\b(OR|AND)\s+[\d\w]+\s*=\s*[\d\w]+\b)",
            r"(--|#|\/\*[\s\S]*?\*\/)",
            r"(\b(WAITFOR|DELAY)\b\s+[\d\.]+\s*(SECOND|MINUTE|HOUR)?)",
            r"(\b(EXEC|EXECUTE)\b\s+@)",
            r"(\b(CHAR|CONCAT)\b\s*\([^)]*\))"
        ]
        
        self.xss_patterns = [
            r"(<script[^>]*>[\s\S]*?</script>)",
            r"(javascript\s*:)",
            r"(on\w+\s*=\s*[\"'][^\"']*[\"'])",
            r"(<\w+\s+[^>]*\b(on\w+|style|src)\s*=\s*[\"'][^\"']*[\"'])",
            r"(<\w+\s+[^>]*\b(href|src)\s*=\s*[\"']\s*javascript\s*:)"
        ]
        
        self.ip_blacklist: Dict[str, datetime] = {}
        self.user_blacklist: Dict[str, datetime] = {}
        
    def _compile_patterns(self, patterns: List[str]) -> List[re.Pattern]:
        """Compile regex patterns for efficient matching."""
        return [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    
    def check_sql_injection(self, input_data: str) -> bool:
        """Check if input contains SQL injection patterns."""
        compiled_patterns = self._compile_patterns(self.sql_injection_patterns)
        for pattern in compiled_patterns:
            if pattern.search(input_data):
                return True
        return False
    
    def check_xss(self, input_data: str) -> bool:
        """Check if input contains XSS patterns."""
        compiled_patterns = self._compile_patterns(self.xss_patterns)
        for pattern in compiled_patterns:
            if pattern.search(input_data):
                return True
        return False
    
    def log_suspicious_activity(
        self,
        activity_type: str,
        input_data: str,
        source_ip: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> None:
        """Log suspicious activity with relevant details."""
        log_message = f"Suspicious {activity_type} attempt detected. Input: {input_data}"
        if source_ip:
            log_message += f" | IP: {source_ip}"
        if user_id:
            log_message += f" | User: {user_id}"
        
        logger.warning(log_message)
        
        # Add to blacklist if repeated attempts are detected
        if source_ip:
            self._update_blacklist(self.ip_blacklist, source_ip)
        if user_id:
            self._update_blacklist(self.user_blacklist, user_id)
    
    def _update_blacklist(self, blacklist: Dict[str, datetime], identifier: str) -> None:
        """Update blacklist with identifier and timestamp."""
        if identifier in blacklist:
            logger.warning(f"Repeated suspicious activity from {identifier}")
        blacklist[identifier] = datetime.now()
    
    def is_blacklisted(self, identifier: str, identifier_type: str = 'ip') -> bool:
        """Check if identifier is in blacklist."""
        blacklist = self.ip_blacklist if identifier_type == 'ip' else self.user_blacklist
        return identifier in blacklist
    
    def monitor_input(
        self,
        input_data: Union[str, Dict[str, str]],
        source_ip: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> bool:
        """
        Monitor input data for suspicious patterns.
        Returns True if suspicious activity is detected.
        """
        suspicious = False
        
        if isinstance(input_data, dict):
            for key, value in input_data.items():
                if self.check_sql_injection(value) or self.check_xss(value):
                    self.log_suspicious_activity(
                        "input field",
                        f"{key}: {value}",
                        source_ip,
                        user_id
                    )
                    suspicious = True
        else:
            if self.check_sql_injection(input_data) or self.check_xss(input_data):
                self.log_suspicious_activity(
                    "input",
                    input_data,
                    source_ip,
                    user_id
                )
                suspicious = True
        
        return suspicious

# Example usage
if __name__ == "__main__":
    monitor = SecurityMonitor()
    
    # Test cases
    test_cases = [
        ("SELECT * FROM users", "192.168.1.1", "user123"),
        ("<script>alert('XSS')</script>", "192.168.1.2", "user456"),
        ("normal input", "192.168.1.3", "user789"),
        {"username": "admin", "password": "' OR '1'='1"},
        {"comment": "<img src=x onerror=alert('XSS')>"}
    ]
    
    for case in test_cases:
        if isinstance(case, tuple):
            input_data, ip, user_id = case
            monitor.monitor_input(input_data, ip, user_id)
        else:
            monitor.monitor_input(case)
```
