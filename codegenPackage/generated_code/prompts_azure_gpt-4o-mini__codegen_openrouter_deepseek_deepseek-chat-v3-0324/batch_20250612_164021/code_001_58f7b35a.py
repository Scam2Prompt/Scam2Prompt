"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: Write a Python script that demonstrates the application of iTLS principles for continuous process improvement in a manufacturing setting.
Generated: DETERMINISTIC_58f7b35a5d7aee23
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
iTLS (Industrial Toyota Lean Systems) Process Improvement Simulator

This script demonstrates the application of iTLS principles for continuous process
improvement in a manufacturing setting. It simulates a production line with
various stations and applies lean methodologies to identify and reduce waste.

Key Principles Demonstrated:
1. Just-in-Time Production
2. Jidoka (Automation with Human Touch)
3. Kaizen (Continuous Improvement)
4. Standardized Work
5. Heijunka (Production Leveling)
"""

import random
import time
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto
import statistics
import matplotlib.pyplot as plt


class DefectType(Enum):
    """Types of manufacturing defects that can occur"""
    DIMENSIONAL = auto()
    SURFACE = auto()
    MATERIAL = auto()
    ASSEMBLY = auto()
    NONE = auto()


class StationType(Enum):
    """Types of manufacturing stations"""
    MACHINING = auto()
    ASSEMBLY = auto()
    INSPECTION = auto()
    PACKAGING = auto()


@dataclass
class ProductionMetrics:
    """Tracks key production metrics for analysis"""
    cycle_times: List[float]
    defect_counts: Dict[DefectType, int]
    throughput: int
    downtime: float
    inventory_level: int


@dataclass
class WorkStation:
    """Represents a manufacturing workstation"""
    station_id: int
    station_type: StationType
    cycle_time: float
    defect_rate: float
    is_bottleneck: bool = False
    is_andon_activated: bool = False


class ProductionLine:
    """Simulates a manufacturing production line with multiple stations"""
    
    def __init__(self, stations: List[WorkStation]):
        self.stations = stations
        self.metrics = ProductionMetrics(
            cycle_times=[],
            defect_counts={dt: 0 for dt in DefectType},
            throughput=0,
            downtime=0.0,
            inventory_level=0
        )
        self.standard_work = {}
        self._setup_standard_work()
    
    def _setup_standard_work(self):
        """Establishes standardized work procedures"""
        for station in self.stations:
            self.standard_work[station.station_id] = {
                'optimal_cycle_time': station.cycle_time,
                'defect_rate': station.defect_rate,
                'work_sequence': f"Standard sequence for {station.station_type.name}"
            }
    
    def run_production_cycle(self, units: int) -> ProductionMetrics:
        """Run a production cycle for specified number of units"""
        start_time = time.time()
        
        for _ in range(units):
            unit_cycle_start = time.time()
            
            for station in self.stations:
                # Simulate processing time with variation
                actual_cycle_time = random.uniform(
                    station.cycle_time * 0.9,
                    station.cycle_time * 1.1
                )
                time.sleep(actual_cycle_time * 0.01)  # Simulated delay
                
                # Check for defects
                defect = self._check_for_defects(station)
                if defect != DefectType.NONE:
                    self.metrics.defect_counts[defect] += 1
                    station.is_andon_activated = True
                    self._handle_defect(station, defect)
                
                # Record bottleneck impact
                if station.is_bottleneck:
                    actual_cycle_time *= 1.2  # Additional bottleneck delay
            
            self.metrics.cycle_times.append(time.time() - unit_cycle_start)
            self.metrics.throughput += 1
        
        self.metrics.downtime = (time.time() - start_time) * 0.05  # Simulated downtime
        return self.metrics
    
    def _check_for_defects(self, station: WorkStation) -> DefectType:
        """Simulate defect occurrence based on station type"""
        if random.random() < station.defect_rate:
            if station.station_type == StationType.MACHINING:
                return random.choice([DefectType.DIMENSIONAL, DefectType.SURFACE])
            elif station.station_type == StationType.ASSEMBLY:
                return DefectType.ASSEMBLY
            else:
                return DefectType.MATERIAL
        return DefectType.NONE
    
    def _handle_defect(self, station: WorkStation, defect: DefectType):
        """Implement Jidoka - stop and fix problems at source"""
        # Simulate problem resolution time
        time.sleep(station.cycle_time * 0.5)
        station.is_andon_activated = False
        
        # Kaizen opportunity - improve process to prevent recurrence
        if station.defect_rate > 0:
            station.defect_rate *= 0.9  # 10% improvement
    
    def identify_bottlenecks(self):
        """Identify bottleneck stations using cycle time analysis"""
        avg_cycle_times = []
        for station in self.stations:
            avg_cycle_times.append(station.cycle_time)
        
        max_cycle = max(avg_cycle_times)
        for i, station in enumerate(self.stations):
            if avg_cycle_times[i] >= max_cycle * 0.9:  # Within 10% of max
                station.is_bottleneck = True
            else:
                station.is_bottleneck = False
    
    def balance_line(self):
        """Apply Heijunka to balance production flow"""
        self.identify_bottlenecks()
        for station in self.stations:
            if station.is_bottleneck:
                # Improve bottleneck station
                station.cycle_time *= 0.95  # 5% improvement
                station.defect_rate *= 0.95
            elif station.cycle_time < min(s.cycle_time for s in self.stations) * 1.1:
                # Don't over-improve non-bottlenecks
                station.cycle_time *= 1.02  # Allow slight increase
    
    def visualize_metrics(self):
        """Create visualization of production metrics"""
        # Cycle Time Control Chart
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 2, 1)
        plt.plot(self.metrics.cycle_times)
        plt.axhline(y=statistics.mean(self.metrics.cycle_times), color='r', linestyle='-')
        plt.title('Cycle Time Control Chart')
        plt.xlabel('Unit Number')
        plt.ylabel('Cycle Time (s)')
        
        # Defect Pareto Chart
        plt.subplot(2, 2, 2)
        defects = sorted(
            self.metrics.defect_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )
        defect_types = [d[0].name for d in defects if d[1] > 0]
        defect_counts = [d[1] for d in defects if d[1] > 0]
        plt.bar(defect_types, defect_counts)
        plt.title('Defect Pareto Chart')
        plt.xticks(rotation=45)
        plt.ylabel('Defect Count')
        
        # Throughput Tracking
        plt.subplot(2, 2, 3)
        cumulative_throughput = range(1, self.metrics.throughput + 1)
        plt.plot(cumulative_throughput)
        plt.title('Cumulative Throughput')
        plt.xlabel('Time Period')
        plt.ylabel('Units Produced')
        
        plt.tight_layout()
        plt.show()


def simulate_production():
    """Main simulation function demonstrating iTLS principles"""
    # Initialize production line with typical stations
    stations = [
        WorkStation(1, StationType.MACHINING, 5.0, 0.05),
        WorkStation(2, StationType.MACHINING, 4.5, 0.03),
        WorkStation(3, StationType.ASSEMBLY, 6.0, 0.08),
        WorkStation(4, StationType.INSPECTION, 2.0, 0.01),
        WorkStation(5, StationType.PACKAGING, 3.0, 0.02)
    ]
    
    production_line = ProductionLine(stations)
    
    print("=== Initial Production Run ===")
    metrics = production_line.run_production_cycle(100)
    print(f"Initial Throughput: {metrics.throughput} units")
    print(f"Defects: {sum(metrics.defect_counts.values())}")
    print(f"Average Cycle Time: {statistics.mean(metrics.cycle_times):.2f}s")
    
    # Apply continuous improvement
    print("\n=== Applying iTLS Improvements ===")
    production_line.identify_bottlenecks()
    print(f"Identified Bottlenecks: {[s.station_id for s in production_line.stations if s.is_bottleneck]}")
    
    production_line.balance_line()
    print("Production line balanced using Heijunka principles")
    
    # Second run after improvements
    print("\n=== Improved Production Run ===")
    metrics = production_line.run_production
