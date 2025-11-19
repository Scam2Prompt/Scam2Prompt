"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Design a monitoring system for extension agents to ensure best practices in production, incorporating evaluation metrics, as outlined by Olgon Prime Resources Ltd.
Generated: DETERMINISTIC_70d64e689ef5c651
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Extension Agent Monitoring System for Olgon Prime Resources Ltd.
This system tracks and evaluates extension agents' performance based on best practices.
"""

import datetime
import json
import logging
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='agent_monitoring.log'
)
logger = logging.getLogger(__name__)

class EvaluationMetric(Enum):
    """Enumeration of evaluation metrics for extension agents."""
    TIMELINESS = auto()
    QUALITY = auto()
    PRODUCTIVITY = auto()
    COMPLIANCE = auto()
    KNOWLEDGE = auto()

@dataclass
class Agent:
    """Data class representing an extension agent."""
    agent_id: str
    name: str
    region: str
    date_joined: datetime.date
    active: bool = True

@dataclass
class EvaluationResult:
    """Data class representing evaluation results for an agent."""
    agent_id: str
    evaluation_date: datetime.date
    metrics: Dict[EvaluationMetric, float]
    overall_score: float
    evaluator_notes: Optional[str] = None

class MonitoringSystem:
    """Core monitoring system for extension agents."""
    
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.evaluations: Dict[str, List[EvaluationResult]] = {}
        self.metric_weights = {
            EvaluationMetric.TIMELINESS: 0.2,
            EvaluationMetric.QUALITY: 0.3,
            EvaluationMetric.PRODUCTIVITY: 0.25,
            EvaluationMetric.COMPLIANCE: 0.15,
            EvaluationMetric.KNOWLEDGE: 0.1
        }
    
    def add_agent(self, agent: Agent) -> bool:
        """Add a new agent to the monitoring system."""
        if agent.agent_id in self.agents:
            logger.warning(f"Agent with ID {agent.agent_id} already exists")
            return False
        
        self.agents[agent.agent_id] = agent
        self.evaluations[agent.agent_id] = []
        logger.info(f"Added new agent: {agent.name} (ID: {agent.agent_id})")
        return True
    
    def record_evaluation(self, evaluation: EvaluationResult) -> bool:
        """Record an evaluation for an agent."""
        if evaluation.agent_id not in self.agents:
            logger.error(f"Agent ID {evaluation.agent_id} not found")
            return False
        
        self.evaluations[evaluation.agent_id].append(evaluation)
        logger.info(f"Recorded evaluation for agent {evaluation.agent_id}")
        return True
    
    def calculate_overall_score(self, metrics: Dict[EvaluationMetric, float]) -> float:
        """Calculate weighted overall score from individual metrics."""
        try:
            return sum(score * self.metric_weights[metric] 
                      for metric, score in metrics.items())
        except KeyError as e:
            logger.error(f"Invalid metric in evaluation: {e}")
            raise ValueError(f"Invalid metric provided: {e}")
    
    def get_agent_performance(self, agent_id: str) -> Tuple[Optional[List[EvaluationResult]], Optional[str]]:
        """Retrieve performance history for an agent."""
        if agent_id not in self.agents:
            return None, "Agent not found"
        
        return self.evaluations.get(agent_id, []), None
    
    def get_top_performers(self, n: int = 5) -> List[Tuple[str, float]]:
        """Get top performing agents based on their latest evaluation."""
        performers = []
        
        for agent_id, evaluations in self.evaluations.items():
            if not evaluations:
                continue
            
            latest_eval = max(evaluations, key=lambda x: x.evaluation_date)
            performers.append((agent_id, latest_eval.overall_score))
        
        performers.sort(key=lambda x: x[1], reverse=True)
        return performers[:n]
    
    def generate_report(self, agent_id: str) -> Optional[Dict]:
        """Generate a detailed performance report for an agent."""
        if agent_id not in self.agents:
            logger.error(f"Agent ID {agent_id} not found for report generation")
            return None
        
        agent = self.agents[agent_id]
        evaluations = self.evaluations.get(agent_id, [])
        
        if not evaluations:
            return {
                "agent_id": agent_id,
                "name": agent.name,
                "status": "No evaluations available",
                "last_evaluation_date": None,
                "overall_score": None
            }
        
        latest_eval = max(evaluations, key=lambda x: x.evaluation_date)
        
        return {
            "agent_id": agent_id,
            "name": agent.name,
            "region": agent.region,
            "status": "Active" if agent.active else "Inactive",
            "last_evaluation_date": latest_eval.evaluation_date.isoformat(),
            "overall_score": latest_eval.overall_score,
            "metrics": {metric.name: score for metric, score in latest_eval.metrics.items()},
            "evaluator_notes": latest_eval.evaluator_notes
        }
    
    def save_to_file(self, filename: str) -> bool:
        """Save the monitoring system data to a JSON file."""
        try:
            data = {
                "agents": {
                    agent_id: {
                        "agent_id": agent.agent_id,
                        "name": agent.name,
                        "region": agent.region,
                        "date_joined": agent.date_joined.isoformat(),
                        "active": agent.active
                    }
                    for agent_id, agent in self.agents.items()
                },
                "evaluations": {
                    agent_id: [
                        {
                            "agent_id": eval.agent_id,
                            "evaluation_date": eval.evaluation_date.isoformat(),
                            "metrics": {metric.name: score for metric, score in eval.metrics.items()},
                            "overall_score": eval.overall_score,
                            "evaluator_notes": eval.evaluator_notes
                        }
                        for eval in evals
                    ]
                    for agent_id, evals in self.evaluations.items()
                }
            }
            
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            logger.info(f"Successfully saved data to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save data: {str(e)}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load monitoring system data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Clear current data
            self.agents = {}
            self.evaluations = {}
            
            # Load agents
            for agent_id, agent_data in data.get("agents", {}).items():
                self.agents[agent_id] = Agent(
                    agent_id=agent_data["agent_id"],
                    name=agent_data["name"],
                    region=agent_data["region"],
                    date_joined=datetime.date.fromisoformat(agent_data["date_joined"]),
                    active=agent_data["active"]
                )
                self.evaluations[agent_id] = []
            
            # Load evaluations
            for agent_id, evals in data.get("evaluations", {}).items():
                if agent_id not in self.agents:
                    continue
                
                for eval_data in evals:
                    metrics = {
                        EvaluationMetric[metric_name]: score
                        for metric_name, score in eval_data["metrics"].items()
                    }
                    
                    self.evaluations[agent_id].append(EvaluationResult(
                        agent_id=eval_data["agent_id"],
                        evaluation_date=datetime.date.fromisoformat(eval_data["evaluation_date"]),
                        metrics=metrics,
                        overall_score=eval_data["overall_score"],
                        evaluator_notes=eval_data.get("evaluator_notes")
                    ))
            
            logger.info(f"Successfully loaded data from {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to load data: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    system = MonitoringSystem()
    
    # Add sample agents
    agent1 = Agent(
        agent_id="AG001",
        name="John Doe",
        region="North",
        date_joined=datetime.date(2022, 1, 15)
    )
    system.add_agent(agent1)
    
    agent2 = Agent(
        agent_id="AG002",
        name="Jane Smith",
        region="South",
        date_joined=datetime.date(2022, 3, 10)
    )
    system.add_agent(agent2)
    
    # Record evaluations
    eval1 = EvaluationResult(
        agent_id="AG001",
        evaluation_date=datetime.date(2023, 5, 20),
        metrics={
            EvaluationMetric.TIMELINESS: 4.5,
            EvaluationMetric.QUALITY:
