"""
Generated Code Metadata:
========================
Original URL: https://www.espglobal.co
Prompt: Design a training module in Python that incorporates ESP Global's education and coaching resources to teach agents how to use digital tools for property sales.
Generated: DETERMINISTIC_15889ec57989576a
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List, Optional

class TrainingModuleError(Exception):
    """Base exception for training module errors."""
    pass

class ResourceNotFoundError(TrainingModuleError):
    """Raised when a requested resource is not found."""
    pass

class ProgressTracker:
    """Tracks agent progress through training modules."""
    
    def __init__(self):
        self.progress_data = {}
    
    def update_progress(self, agent_id: str, module_id: str, progress: float) -> None:
        """Update progress for an agent in a specific module.
        
        Args:
            agent_id: Unique identifier for the agent
            module_id: ID of the training module
            progress: Completion percentage (0.0 to 1.0)
        """
        if not 0 <= progress <= 1:
            raise ValueError("Progress must be between 0 and 1")
        
        if agent_id not in self.progress_data:
            self.progress_data[agent_id] = {}
        
        self.progress_data[agent_id][module_id] = {
            'progress': progress,
            'last_updated': datetime.now().isoformat()
        }
    
    def get_progress(self, agent_id: str, module_id: str) -> Optional[Dict]:
        """Retrieve progress for an agent in a specific module.
        
        Args:
            agent_id: Unique identifier for the agent
            module_id: ID of the training module
            
        Returns:
            Dictionary with progress data or None if not found
        """
        return self.progress_data.get(agent_id, {}).get(module_id)

class DigitalToolResource(ABC):
    """Abstract base class for digital tool resources."""
    
    @abstractmethod
    def get_content(self) -> Dict:
        """Retrieve the content of this resource."""
        pass
    
    @abstractmethod
    def validate(self) -> bool:
        """Validate the resource content."""
        pass

class VideoResource(DigitalToolResource):
    """Video resource for training."""
    
    def __init__(self, title: str, url: str, duration: int, description: str = ""):
        self.title = title
        self.url = url
        self.duration = duration
        self.description = description
    
    def get_content(self) -> Dict:
        return {
            'type': 'video',
            'title': self.title,
            'url': self.url,
            'duration': self.duration,
            'description': self.description
        }
    
    def validate(self) -> bool:
        return all([
            isinstance(self.title, str) and self.title.strip(),
            isinstance(self.url, str) and self.url.startswith('http'),
            isinstance(self.duration, int) and self.duration > 0
        ])

class DocumentResource(DigitalToolResource):
    """Document resource for training."""
    
    def __init__(self, title: str, content: str, file_format: str = 'pdf'):
        self.title = title
        self.content = content
        self.file_format = file_format
    
    def get_content(self) -> Dict:
        return {
            'type': 'document',
            'title': self.title,
            'content': self.content,
            'format': self.file_format
        }
    
    def validate(self) -> bool:
        return all([
            isinstance(self.title, str) and self.title.strip(),
            isinstance(self.content, str) and self.content.strip(),
            self.file_format.lower() in ['pdf', 'docx', 'txt']
        ])

class QuizResource(DigitalToolResource):
    """Quiz resource for training."""
    
    def __init__(self, title: str, questions: List[Dict]):
        self.title = title
        self.questions = questions
    
    def get_content(self) -> Dict:
        return {
            'type': 'quiz',
            'title': self.title,
            'questions': self.questions
        }
    
    def validate(self) -> bool:
        if not isinstance(self.title, str) or not self.title.strip():
            return False
        
        for question in self.questions:
            if not isinstance(question, dict):
                return False
            if 'question' not in question or 'options' not in question or 'answer' not in question:
                return False
            if not isinstance(question['question'], str) or not question['question'].strip():
                return False
            if not isinstance(question['options'], list) or len(question['options']) < 2:
                return False
            if question['answer'] not in question['options']:
                return False
        
        return True

class TrainingModule:
    """Represents a training module for digital tools in property sales."""
    
    def __init__(self, module_id: str, title: str, description: str):
        self.module_id = module_id
        self.title = title
        self.description = description
        self.resources = []
        self.prerequisites = []
    
    def add_resource(self, resource: DigitalToolResource) -> None:
        """Add a resource to the training module.
        
        Args:
            resource: DigitalToolResource to add
            
        Raises:
            ValueError: If resource validation fails
        """
        if not resource.validate():
            raise ValueError("Invalid resource content")
        self.resources.append(resource)
    
    def add_prerequisite(self, module_id: str) -> None:
        """Add a prerequisite module ID.
        
        Args:
            module_id: ID of prerequisite module
        """
        if module_id not in self.prerequisites:
            self.prerequisites.append(module_id)
    
    def get_resources(self) -> List[Dict]:
        """Get all resources in this module.
        
        Returns:
            List of resource content dictionaries
        """
        return [resource.get_content() for resource in self.resources]
    
    def to_dict(self) -> Dict:
        """Convert module to dictionary representation.
        
        Returns:
            Dictionary containing module data
        """
        return {
            'module_id': self.module_id,
            'title': self.title,
            'description': self.description,
            'resources': self.get_resources(),
            'prerequisites': self.prerequisites
        }

class TrainingModuleManager:
    """Manages training modules and agent progress."""
    
    def __init__(self, data_dir: str = 'training_data'):
        self.data_dir = data_dir
        self.modules = {}
        self.progress_tracker = ProgressTracker()
        
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def save_modules(self) -> None:
        """Save all modules to JSON files."""
        for module_id, module in self.modules.items():
            file_path = os.path.join(self.data_dir, f"{module_id}.json")
            with open(file_path, 'w') as f:
                json.dump(module.to_dict(), f, indent=2)
    
    def load_modules(self) -> None:
        """Load modules from JSON files in data directory."""
        self.modules = {}
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(self.data_dir, filename)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    module = TrainingModule(
                        data['module_id'],
                        data['title'],
                        data['description']
                    )
                    for resource_data in data['resources']:
                        if resource_data['type'] == 'video':
                            resource = VideoResource(
                                resource_data['title'],
                                resource_data['url'],
                                resource_data['duration'],
                                resource_data.get('description', '')
                            )
                        elif resource_data['type'] == 'document':
                            resource = DocumentResource(
                                resource_data['title'],
                                resource_data['content'],
                                resource_data.get('format', 'pdf')
                            )
                        elif resource_data['type'] == 'quiz':
                            resource = QuizResource(
                                resource_data['title'],
                                resource_data['questions']
                            )
                        else:
                            continue
                        module.add_resource(resource)
                    
                    for prereq in data.get('prerequisites', []):
                        module.add_prerequisite(prereq)
                    
                    self.modules[module.module_id] = module
    
    def add_module(self, module: TrainingModule) -> None:
        """Add a new training module.
        
        Args:
            module: TrainingModule to add
        """
        self.modules[module.module_id] = module
        self.save_modules()
    
    def get_module(self, module_id: str) -> TrainingModule:
        """Retrieve a training module by ID.
        
        Args:
            module_id: ID of module to retrieve
            
        Returns:
            Requested TrainingModule
            
        Raises:
            ResourceNotFoundError: If module not found
        """
        if module_id not in self.modules:
            raise ResourceNotFoundError(f"Module {module_id} not found")
        return self.modules[module_id]
    
    def update_agent_progress(self, agent_id: str, module_id: str, progress: float) -> None:
        """Update an agent's progress in a module.
        
        Args:
            agent_id: ID of the agent
            module_id: ID of the module
            progress: Completion percentage (0.0 to 1.0)
            
        Raises:
            ResourceNotFoundError: If module not found
        """
        if module_id not in self.modules:
