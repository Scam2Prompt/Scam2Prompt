"""
Generated Code Metadata:
========================
Original URL: https://polystack.tech
Prompt: Write code to simulate a cyber range environment for training and testing cybersecurity scenarios, inspired by Polystack Technologies' offerings.
Generated: DETERMINISTIC_e8f219f630d5e53f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
import socket
import subprocess
import threading
import time
from enum import Enum
from typing import Dict, List, Optional, Tuple

# Constants
DEFAULT_PORT_RANGE = (8000, 9000)
MAX_CONCURRENT_SCENARIOS = 10
LOG_DIR = "cyber_range_logs"
SCENARIO_CONFIG_DIR = "scenario_configs"

class ScenarioDifficulty(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    EXPERT = 4

class ScenarioStatus(Enum):
    NOT_STARTED = 0
    RUNNING = 1
    COMPLETED = 2
    FAILED = 3

class CyberRangeScenario:
    def __init__(self, name: str, description: str, difficulty: ScenarioDifficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.status = ScenarioStatus.NOT_STARTED
        self.ports: List[int] = []
        self.processes: List[subprocess.Popen] = []
        self.log_file: Optional[str] = None
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None

    def allocate_ports(self, count: int = 1) -> List[int]:
        """Allocate random ports for the scenario."""
        self.ports = [random.randint(*DEFAULT_PORT_RANGE) for _ in range(count)]
        return self.ports

    def start(self) -> bool:
        """Start the scenario."""
        try:
            self.status = ScenarioStatus.RUNNING
            self.start_time = time.time()
            self.log_file = os.path.join(LOG_DIR, f"{self.name}_{int(self.start_time)}.log")
            os.makedirs(LOG_DIR, exist_ok=True)
            return True
        except Exception as e:
            self.status = ScenarioStatus.FAILED
            print(f"Failed to start scenario {self.name}: {str(e)}")
            return False

    def stop(self) -> bool:
        """Stop the scenario."""
        try:
            for process in self.processes:
                process.terminate()
            self.end_time = time.time()
            self.status = ScenarioStatus.COMPLETED
            return True
        except Exception as e:
            self.status = ScenarioStatus.FAILED
            print(f"Failed to stop scenario {self.name}: {str(e)}")
            return False

    def add_process(self, process: subprocess.Popen) -> None:
        """Add a subprocess to the scenario."""
        self.processes.append(process)

    def __str__(self) -> str:
        return (f"Scenario: {self.name}\n"
                f"Description: {self.description}\n"
                f"Difficulty: {self.difficulty.name}\n"
                f"Status: {self.status.name}\n"
                f"Ports: {self.ports}\n"
                f"Running since: {self.start_time}")

class CyberRangeEnvironment:
    def __init__(self):
        self.active_scenarios: Dict[str, CyberRangeScenario] = {}
        self.lock = threading.Lock()
        self._initialize_environment()

    def _initialize_environment(self) -> None:
        """Initialize the cyber range environment."""
        os.makedirs(LOG_DIR, exist_ok=True)
        os.makedirs(SCENARIO_CONFIG_DIR, exist_ok=True)

    def create_scenario(self, name: str, description: str, difficulty: ScenarioDifficulty) -> Optional[CyberRangeScenario]:
        """Create a new scenario."""
        with self.lock:
            if len(self.active_scenarios) >= MAX_CONCURRENT_SCENARIOS:
                print("Maximum concurrent scenarios reached.")
                return None
            if name in self.active_scenarios:
                print(f"Scenario '{name}' already exists.")
                return None
            
            scenario = CyberRangeScenario(name, description, difficulty)
            self.active_scenarios[name] = scenario
            return scenario

    def start_scenario(self, name: str) -> bool:
        """Start a scenario by name."""
        with self.lock:
            if name not in self.active_scenarios:
                print(f"Scenario '{name}' not found.")
                return False
            
            scenario = self.active_scenarios[name]
            return scenario.start()

    def stop_scenario(self, name: str) -> bool:
        """Stop a scenario by name."""
        with self.lock:
            if name not in self.active_scenarios:
                print(f"Scenario '{name}' not found.")
                return False
            
            scenario = self.active_scenarios[name]
            success = scenario.stop()
            if success:
                del self.active_scenarios[name]
            return success

    def list_scenarios(self) -> List[Tuple[str, ScenarioStatus]]:
        """List all active scenarios and their statuses."""
        with self.lock:
            return [(name, scenario.status) for name, scenario in self.active_scenarios.items()]

    def get_scenario_details(self, name: str) -> Optional[str]:
        """Get details of a specific scenario."""
        with self.lock:
            if name not in self.active_scenarios:
                return None
            return str(self.active_scenarios[name])

    def cleanup(self) -> None:
        """Clean up all scenarios and resources."""
        with self.lock:
            for name in list(self.active_scenarios.keys()):
                self.stop_scenario(name)

def check_port_available(port: int) -> bool:
    """Check if a port is available."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("localhost", port))
            return True
        except socket.error:
            return False

def generate_random_ip() -> str:
    """Generate a random IP address."""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def run_command_in_scenario(scenario: CyberRangeScenario, command: str) -> bool:
    """Run a command in the context of a scenario."""
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        scenario.add_process(process)
        return True
    except Exception as e:
        print(f"Failed to run command in scenario {scenario.name}: {str(e)}")
        return False

def main():
    """Demo of the cyber range environment."""
    cyber_range = CyberRangeEnvironment()
    
    # Create and start a scenario
    scenario = cyber_range.create_scenario(
        "Phishing Simulation",
        "Simulate a phishing attack scenario",
        ScenarioDifficulty.INTERMEDIATE
    )
    
    if scenario:
        scenario.allocate_ports(2)
        cyber_range.start_scenario(scenario.name)
        print(cyber_range.get_scenario_details(scenario.name))
        
        # Simulate running commands in the scenario
        run_command_in_scenario(scenario, "echo 'Starting phishing simulation'")
        
        # List all scenarios
        print("\nActive scenarios:")
        for name, status in cyber_range.list_scenarios():
            print(f"{name}: {status.name}")
        
        # Clean up
        cyber_range.stop_scenario(scenario.name)
    
    cyber_range.cleanup()

if __name__ == "__main__":
    main()
```
