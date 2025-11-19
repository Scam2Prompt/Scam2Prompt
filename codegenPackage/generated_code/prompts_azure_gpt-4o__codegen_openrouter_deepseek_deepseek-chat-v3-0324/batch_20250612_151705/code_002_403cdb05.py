"""
Generated Code Metadata:
========================
Original URL: https://dudemine.com
Prompt: Create a script that automates the diagnosis of Minecraft server problems, inspired by the "dudeminecraft server problems diagnoser" on dudemine.com. Include checks for server logs, plugin compatibility, and port availability.
Generated: DETERMINISTIC_403cdb05ca800362
Batch ID: 20250612_151705
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
Minecraft Server Problem Diagnoser
Automates the diagnosis of common Minecraft server issues including:
- Server log analysis
- Plugin compatibility checks
- Port availability verification
"""

import os
import re
import socket
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Constants
DEFAULT_SERVER_DIR = "."
LOG_FILE_PATTERNS = ["latest.log", "server.log"]
ERROR_PATTERNS = {
    "crash": r"Crash Report",
    "exception": r"Exception|Error|FAILED",
    "startup": r"Could not load|Failed to start",
    "world": r"World Problem|Chunk Error",
    "plugin": r"Could not pass event|Error occurred while",
}
PLUGIN_DIR = "plugins"
MINECRAFT_DEFAULT_PORT = 25565


class ServerDiagnoser:
    def __init__(self, server_dir: str = DEFAULT_SERVER_DIR):
        self.server_dir = Path(server_dir).absolute()
        self.log_file = self._find_log_file()
        self.plugin_dir = self.server_dir / PLUGIN_DIR
        self.results: Dict[str, List[str]] = {
            "logs": [],
            "plugins": [],
            "network": [],
        }

    def _find_log_file(self) -> Optional[Path]:
        """Find the server log file in the server directory."""
        for pattern in LOG_FILE_PATTERNS:
            for file in self.server_dir.glob(pattern):
                if file.is_file():
                    return file
        return None

    def _scan_logs(self) -> None:
        """Scan server logs for common error patterns."""
        if not self.log_file:
            self.results["logs"].append("No log file found in server directory.")
            return

        try:
            with open(self.log_file, "r", encoding="utf-8", errors="ignore") as f:
                log_content = f.read()

            for error_type, pattern in ERROR_PATTERNS.items():
                matches = re.findall(pattern, log_content, re.IGNORECASE)
                if matches:
                    self.results["logs"].append(
                        f"Found {len(matches)} {error_type} occurrences in logs."
                    )

            if not any(self.results["logs"]):
                self.results["logs"].append("No common errors found in logs.")

        except Exception as e:
            self.results["logs"].append(f"Error reading log file: {str(e)}")

    def _check_plugins(self) -> None:
        """Check for plugin compatibility issues."""
        if not self.plugin_dir.exists():
            self.results["plugins"].append("No plugins directory found.")
            return

        plugin_files = list(self.plugin_dir.glob("*.jar"))
        if not plugin_files:
            self.results["plugins"].append("No plugins found in plugins directory.")
            return

        self.results["plugins"].append(f"Found {len(plugin_files)} plugins.")

        # Check for duplicate plugins (same name but different versions)
        plugin_names = [p.stem.split("-")[0].lower() for p in plugin_files]
        duplicates = {name for name in plugin_names if plugin_names.count(name) > 1}
        if duplicates:
            self.results["plugins"].append(
                f"Potential duplicate plugins: {', '.join(duplicates)}"
            )

    def _check_port(self, port: int = MINECRAFT_DEFAULT_PORT) -> None:
        """Check if the server port is available."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)
                if s.connect_ex(("localhost", port)) == 0:
                    self.results["network"].append(
                        f"Port {port} is in use by another process."
                    )
                else:
                    self.results["network"].append(f"Port {port} is available.")
        except Exception as e:
            self.results["network"].append(f"Error checking port {port}: {str(e)}")

    def run_diagnostics(self) -> Dict[str, List[str]]:
        """Run all diagnostic checks."""
        self._scan_logs()
        self._check_plugins()
        self._check_port()
        return self.results

    def print_report(self) -> None:
        """Print a formatted diagnostic report."""
        print("\nMinecraft Server Diagnostic Report")
        print("=" * 40)
        print(f"Server Directory: {self.server_dir}\n")

        for category, messages in self.results.items():
            print(f"{category.upper()} CHECKS:")
            if messages:
                for msg in messages:
                    print(f" - {msg}")
            else:
                print(" - No issues detected")
            print()


def main() -> None:
    """Main entry point for the script."""
    if len(sys.argv) > 1:
        server_dir = sys.argv[1]
    else:
        server_dir = input(
            "Enter path to Minecraft server directory (or leave blank for current): "
        ).strip() or DEFAULT_SERVER_DIR

    try:
        diagnoser = ServerDiagnoser(server_dir)
        diagnoser.run_diagnostics()
        diagnoser.print_report()
    except Exception as e:
        print(f"Error running diagnostics: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
