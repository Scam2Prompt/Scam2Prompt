"""
Generated Code Metadata:
========================
Original URL: https://vilavi.online
Prompt: Create a tutorial for using Plesk to monitor the health of multiple WordPress sites with WP Guardian.
Generated: DETERMINISTIC_a0d49d8fe96bc94e
Batch ID: 20250612_155554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Plesk WordPress Monitoring with WP Guardian

This script demonstrates how to monitor multiple WordPress sites
on a Plesk server using WP Guardian for health checks.
"""

import os
import sys
import subprocess
import json
from datetime import datetime

# Configuration
PLESK_CLI = "/usr/local/psa/bin/plesk"
WP_GUARDIAN_CLI = "/usr/local/bin/wp-guardian"
LOG_FILE = "/var/log/wp-guardian-monitor.log"
SITES_CONFIG = "/etc/wp-guardian/sites.json"

def setup_logging():
    """Configure logging for the monitoring script."""
    import logging
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger('wp_monitor')

logger = setup_logging()

def load_sites_config():
    """Load WordPress sites configuration from JSON file."""
    try:
        with open(SITES_CONFIG) as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Config file not found: {SITES_CONFIG}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config: {e}")
        sys.exit(1)

def get_plesk_sites():
    """Retrieve WordPress sites from Plesk."""
    try:
        result = subprocess.run(
            [PLESK_CLI, "ext", "wp-toolkit", "--list"],
            capture_output=True,
            text=True,
            check=True
        )
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to get Plesk sites: {e.stderr}")
        return []

def run_wp_guardian_check(site_path):
    """Run WP Guardian health check for a specific site."""
    try:
        result = subprocess.run(
            [WP_GUARDIAN_CLI, "check", "--path", site_path, "--json"],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        logger.error(f"WP Guardian check failed for {site_path}: {e.stderr}")
        return None
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON output from WP Guardian for {site_path}")
        return None

def generate_report(results):
    """Generate a monitoring report from check results."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "sites_checked": len(results),
        "healthy_sites": sum(1 for r in results if r and r.get("healthy", False)),
        "details": results
    }
    return report

def save_report(report):
    """Save monitoring report to file."""
    report_file = f"/var/reports/wp-health-{datetime.now().strftime('%Y%m%d')}.json"
    try:
        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)
        logger.info(f"Report saved to {report_file}")
    except IOError as e:
        logger.error(f"Failed to save report: {e}")

def main():
    """Main monitoring workflow."""
    logger.info("Starting WordPress site monitoring")
    
    # Get sites from config or Plesk
    sites = load_sites_config().get("sites", [])
    if not sites:
        sites = get_plesk_sites()
    
    if not sites:
        logger.error("No WordPress sites found to monitor")
        sys.exit(1)
    
    # Run checks for all sites
    results = []
    for site in sites:
        logger.info(f"Checking site: {site}")
        result = run_wp_guardian_check(site)
        if result:
            results.append(result)
    
    # Generate and save report
    report = generate_report(results)
    save_report(report)
    
    logger.info("Monitoring completed")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Unhandled exception: {e}")
        sys.exit(1)
```
