"""
Generated Code Metadata:
========================
Original URL: https://bexo.space
Prompt: "Write a Python code snippet that utilizes AI for workflow optimization, specifically for automating complex tasks in digital teams."
Generated: DETERMINISTIC_afb7a291bd5bcb15
Batch ID: 20250622_212254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, List, Optional
from abc import ABC, abstractmethod
import openai
from tenacity import retry, stop_after_attempt, wait_exponential

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Task(ABC):
    """Abstract base class for tasks in the workflow."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.dependencies: List['Task'] = []
    
    @abstractmethod
    def execute(self) -> bool:
        """Execute the task and return success status."""
        pass

    def add_dependency(self, task: 'Task') -> None:
        """Add a task dependency."""
        self.dependencies.append(task)

class AITask(Task):
    """Task that utilizes AI for execution."""
    
    def __init__(self, name: str, description: str, ai_model: str = "gpt-3.5-turbo"):
        super().__init__(name, description)
        self.ai_model = ai_model
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def _call_ai(self, prompt: str) -> str:
        """Call the AI model with retry logic."""
        try:
            response = openai.ChatCompletion.create(
                model=self.ai_model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"AI call failed: {e}")
            raise

    def execute(self) -> bool:
        """Execute the AI task."""
        try:
            prompt = f"Task: {self.name}\nDescription: {self.description}\n\nPlease provide step-by-step instructions to complete this task."
            result = self._call_ai(prompt)
            logger.info(f"AI Task '{self.name}' completed successfully.\nResult: {result}")
            return True
        except Exception as e:
            logger.error(f"Failed to execute AI Task '{self.name}': {e}")
            return False

class Workflow:
    """Workflow manager for digital teams."""
    
    def __init__(self, name: str):
        self.name = name
        self.tasks: Dict[str, Task] = {}
        self.execution_order: List[Task] = []
    
    def add_task(self, task: Task) -> None:
        """Add a task to the workflow."""
        if task.name in self.tasks:
            raise ValueError(f"Task '{task.name}' already exists in workflow")
        self.tasks[task.name] = task
    
    def set_dependency(self, task_name: str, depends_on: str) -> None:
        """Set a dependency between tasks."""
        if task_name not in self.tasks or depends_on not in self.tasks:
            raise ValueError("One or both tasks not found in workflow")
        self.tasks[task_name].add_dependency(self.tasks[depends_on])
    
    def _topological_sort(self) -> Optional[List[Task]]:
        """Perform topological sort to determine execution order."""
        in_degree = {task: 0 for task in self.tasks.values()}
        graph = {task: [] for task in self.tasks.values()}
        
        for task in self.tasks.values():
            for dep in task.dependencies:
                graph[dep].append(task)
                in_degree[task] += 1
        
        queue = [task for task, degree in in_degree.items() if degree == 0]
        sorted_order = []
        
        while queue:
            current = queue.pop(0)
            sorted_order.append(current)
            
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(sorted_order) != len(self.tasks):
            logger.error("Workflow has circular dependencies")
            return None
        
        return sorted_order
    
    def execute(self) -> bool:
        """Execute the workflow."""
        self.execution_order = self._topological_sort()
        if not self.execution_order:
            return False
        
        logger.info(f"Executing workflow '{self.name}' with {len(self.execution_order)} tasks")
        
        for task in self.execution_order:
            logger.info(f"Executing task '{task.name}'")
            if not task.execute():
                logger.error(f"Task '{task.name}' failed, stopping workflow")
                return False
        
        logger.info("Workflow completed successfully")
        return True

# Example usage
if __name__ == "__main__":
    # Initialize OpenAI API (replace with your actual API key)
    openai.api_key = "your-api-key-here"
    
    # Create workflow
    workflow = Workflow("Digital Marketing Campaign")
    
    # Create tasks
    research = AITask(
        "Market Research",
        "Analyze current market trends and competitor strategies"
    )
    
    content = AITask(
        "Content Creation",
        "Generate engaging content for the campaign"
    )
    
    design = AITask(
        "Visual Design",
        "Create visual assets for the campaign"
    )
    
    # Add tasks to workflow
    workflow.add_task(research)
    workflow.add_task(content)
    workflow.add_task(design)
    
    # Set dependencies
    workflow.set_dependency(content.name, research.name)
    workflow.set_dependency(design.name, content.name)
    
    # Execute workflow
    success = workflow.execute()
    print(f"Workflow execution {'succeeded' if success else 'failed'}")
```
