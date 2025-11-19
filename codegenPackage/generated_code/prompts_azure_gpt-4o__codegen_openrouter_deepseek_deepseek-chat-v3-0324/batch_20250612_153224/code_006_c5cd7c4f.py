"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: Develop code to simulate and evaluate organizational safety culture practices, inspired by GESEC's "Cultura de Seguridad" initiative.
Generated: DETERMINISTIC_c5cd7c4f28c1b954
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Organizational Safety Culture Simulation

This module simulates and evaluates safety culture practices within an organization,
inspired by GESEC's "Cultura de Seguridad" initiative. It includes metrics for
assessing safety culture, simulation of organizational behavior, and evaluation
of safety practices.

Key components:
- SafetyCulture class: Main simulation class
- SafetyMetrics: Enum for safety metrics
- SafetyPractice: Dataclass for safety practices
- SimulationError: Custom exception class
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Dict, Optional
import random
import math
import statistics


class SimulationError(Exception):
    """Custom exception for simulation errors."""
    pass


class SafetyMetrics(Enum):
    """Enumeration of safety culture metrics."""
    LEADERSHIP_COMMITMENT = auto()
    RISK_PERCEPTION = auto()
    REPORTING_CULTURE = auto()
    LEARNING_CULTURE = auto()
    SAFETY_RESOURCES = auto()
    WORKER_ENGAGEMENT = auto()
    COMMUNICATION = auto()
    PROCEDURAL_COMPLIANCE = auto()


@dataclass
class SafetyPractice:
    """Represents a safety practice with its impact on various metrics."""
    name: str
    description: str
    metric_impacts: Dict[SafetyMetrics, float]
    implementation_cost: float
    implementation_difficulty: float  # 1-10 scale


class SafetyCulture:
    """
    Simulates and evaluates organizational safety culture.

    Attributes:
        practices (List[SafetyPractice]): Available safety practices
        current_metrics (Dict[SafetyMetrics, float]): Current metric scores (0-100)
        budget (float): Available budget for safety initiatives
        history (List[Dict]): History of metric changes
    """

    def __init__(self, initial_metrics: Optional[Dict[SafetyMetrics, float]] = None,
                 budget: float = 100000.0):
        """
        Initialize the safety culture simulation.

        Args:
            initial_metrics: Initial scores for safety metrics (0-100 scale)
            budget: Initial budget for safety initiatives
        """
        self.practices = self._initialize_practices()
        self.current_metrics = initial_metrics or self._default_metrics()
        self.budget = budget
        self.history = [{"metrics": self.current_metrics.copy(), "budget": self.budget}]

    def _default_metrics(self) -> Dict[SafetyMetrics, float]:
        """Return default metric scores (50/100 for all metrics)."""
        return {metric: 50.0 for metric in SafetyMetrics}

    def _initialize_practices(self) -> List[SafetyPractice]:
        """Initialize a set of standard safety practices."""
        practices = [
            SafetyPractice(
                name="Safety Leadership Training",
                description="Training for managers on safety leadership",
                metric_impacts={
                    SafetyMetrics.LEADERSHIP_COMMITMENT: 15,
                    SafetyMetrics.COMMUNICATION: 5,
                    SafetyMetrics.WORKER_ENGAGEMENT: 5
                },
                implementation_cost=10000,
                implementation_difficulty=4
            ),
            SafetyPractice(
                name="Near-Miss Reporting System",
                description="System for reporting near-miss incidents",
                metric_impacts={
                    SafetyMetrics.REPORTING_CULTURE: 20,
                    SafetyMetrics.LEARNING_CULTURE: 10,
                    SafetyMetrics.RISK_PERCEPTION: 5
                },
                implementation_cost=15000,
                implementation_difficulty=6
            ),
            SafetyPractice(
                name="Safety Equipment Upgrade",
                description="Upgrade of personal protective equipment",
                metric_impacts={
                    SafetyMetrics.SAFETY_RESOURCES: 25,
                    SafetyMetrics.PROCEDURAL_COMPLIANCE: 10
                },
                implementation_cost=25000,
                implementation_difficulty=3
            ),
            SafetyPractice(
                name="Safety Culture Survey",
                description="Organization-wide safety culture assessment",
                metric_impacts={
                    SafetyMetrics.LEARNING_CULTURE: 10,
                    SafetyMetrics.COMMUNICATION: 10,
                    SafetyMetrics.WORKER_ENGAGEMENT: 10
                },
                implementation_cost=8000,
                implementation_difficulty=2
            ),
            SafetyPractice(
                name="Safety Procedure Review",
                description="Comprehensive review of safety procedures",
                metric_impacts={
                    SafetyMetrics.PROCEDURAL_COMPLIANCE: 20,
                    SafetyMetrics.LEADERSHIP_COMMITMENT: 5,
                    SafetyMetrics.RISK_PERCEPTION: 5
                },
                implementation_cost=12000,
                implementation_difficulty=7
            )
        ]
        return practices

    def implement_practice(self, practice_name: str) -> None:
        """
        Implement a safety practice and update metrics.

        Args:
            practice_name: Name of the practice to implement

        Raises:
            SimulationError: If practice not found or insufficient budget
        """
        practice = next((p for p in self.practices if p.name == practice_name), None)
        if not practice:
            raise SimulationError(f"Practice '{practice_name}' not found")

        if self.budget < practice.implementation_cost:
            raise SimulationError("Insufficient budget for this practice")

        # Apply practice impacts with some randomness
        success_factor = random.uniform(0.8, 1.2) * (1 - practice.implementation_difficulty / 20)
        for metric, impact in practice.metric_impacts.items():
            self.current_metrics[metric] = min(100, self.current_metrics[metric] + impact * success_factor)

        # Deduct cost
        self.budget -= practice.implementation_cost

        # Record in history
        self.history.append({
            "metrics": self.current_metrics.copy(),
            "budget": self.budget,
            "practice": practice_name
        })

    def natural_metric_change(self) -> None:
        """Simulate natural changes in metrics over time."""
        for metric in self.current_metrics:
            # Random change between -5 and +5, weighted by current score
            change = random.uniform(-5, 5) * (1 - self.current_metrics[metric] / 100)
            self.current_metrics[metric] = max(0, min(100, self.current_metrics[metric] + change))

        # Record in history
        self.history.append({
            "metrics": self.current_metrics.copy(),
            "budget": self.budget,
            "event": "natural_change"
        })

    def calculate_overall_score(self) -> float:
        """Calculate an overall safety culture score (0-100)."""
        # Weighted average with emphasis on leadership and reporting
        weights = {
            SafetyMetrics.LEADERSHIP_COMMITMENT: 1.5,
            SafetyMetrics.REPORTING_CULTURE: 1.3,
            SafetyMetrics.LEARNING_CULTURE: 1.2,
            SafetyMetrics.RISK_PERCEPTION: 1.0,
            SafetyMetrics.SAFETY_RESOURCES: 1.0,
            SafetyMetrics.WORKER_ENGAGEMENT: 1.1,
            SafetyMetrics.COMMUNICATION: 1.1,
            SafetyMetrics.PROCEDURAL_COMPLIANCE: 1.0
        }

        weighted_sum = sum(self.current_metrics[metric] * weights[metric] for metric in self.current_metrics)
        total_weight = sum(weights.values())
        return weighted_sum / total_weight

    def get_metric_trend(self, metric: SafetyMetrics) -> float:
        """
        Calculate the trend for a specific metric.

        Args:
            metric: Metric to analyze

        Returns:
            Slope of the trend line (positive = improving, negative = declining)
        """
        if len(self.history) < 2:
            return 0.0

        # Simple linear regression for trend
        x = list(range(len(self.history)))
        y = [entry["metrics"][metric] for entry in self.history]

        n = len(x)
        x_mean = sum(x) / n
        y_mean = sum(y) / n

        numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

        if denominator == 0:
            return 0.0

        return numerator / denominator

    def get_weakest_metrics(self, count: int = 3) -> List[SafetyMetrics]:
        """
        Identify the weakest metrics based on current scores.

        Args:
            count: Number of metrics to return

        Returns:
            List of weakest metrics
        """
        sorted_metrics = sorted(
            self.current_metrics.items(),
            key=lambda item: item[1]
        )
        return [metric for metric, score in sorted_metrics[:count]]

    def simulate_time_period(self, periods: int = 1) -> None:
        """
        Simulate the passage of time with random events.

        Args:
            periods: Number of time periods to simulate
        """
        for _ in range(periods):
            # Random chance of implementing a practice
            if random.random() < 0.3 and
