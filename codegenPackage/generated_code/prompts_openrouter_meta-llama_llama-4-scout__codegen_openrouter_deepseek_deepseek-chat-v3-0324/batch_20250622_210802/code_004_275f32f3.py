"""
Generated Code Metadata:
========================
Original URL: https://singularity2.pages.dev
Prompt: "Develop a code example for leveraging AI functions and exchanging input/output data between AI agents in the SingularityNET platform's self-organizing network."
Generated: DETERMINISTIC_275f32f34e045ce3
Batch ID: 20250622_210802
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://agent2.singularitynet.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://agent1.singularitynet.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
import requests
from typing import Dict, Any, Optional
from uuid import uuid4

class AIAgentClient:
    """
    Client for interacting with AI agents on the SingularityNET platform.
    Handles authentication, request formatting, and response processing.
    """
    
    def __init__(self, service_url: str, api_key: str):
        """
        Initialize the AI agent client.
        
        Args:
            service_url: Base URL of the AI service endpoint
            api_key: API key for authentication
        """
        self.service_url = service_url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        })
    
    def call_ai_function(self, 
                       function_name: str, 
                       params: Dict[str, Any], 
                       agent_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Call an AI function on a specified agent.
        
        Args:
            function_name: Name of the AI function to call
            params: Input parameters for the function
            agent_id: Optional specific agent ID to target
            
        Returns:
            Dictionary containing the function response
            
        Raises:
            ValueError: If input validation fails
            requests.exceptions.RequestException: For network/API errors
        """
        if not function_name:
            raise ValueError("Function name cannot be empty")
        
        if not isinstance(params, dict):
            raise ValueError("Params must be a dictionary")
        
        payload = {
            "jsonrpc": "2.0",
            "method": function_name,
            "params": params,
            "id": str(uuid4())
        }
        
        if agent_id:
            payload["agent_id"] = agent_id
        
        try:
            response = self.session.post(
                f"{self.service_url}/api/v1/execute",
                data=json.dumps(payload)
            )
            response.raise_for_status()
            
            result = response.json()
            if 'error' in result:
                raise ValueError(f"AI Function Error: {result['error']}")
                
            return result.get('result', {})
            
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Network error occurred: {str(e)}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON response from server")

class AgentCoordinator:
    """
    Coordinates communication between multiple AI agents.
    """
    
    def __init__(self, agents: Dict[str, AIAgentClient]):
        """
        Initialize with a dictionary of configured agents.
        
        Args:
            agents: Dictionary of {agent_name: AIAgentClient}
        """
        self.agents = agents
    
    def orchestrate_workflow(self, 
                           workflow: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a multi-agent workflow.
        
        Args:
            workflow: Dictionary defining the workflow steps
            
        Returns:
            Combined results from all steps
            
        Raises:
            ValueError: If workflow definition is invalid
        """
        if not workflow.get('steps'):
            raise ValueError("Workflow must contain 'steps'")
        
        results = {}
        context = {}
        
        for step in workflow['steps']:
            agent_name = step.get('agent')
            if not agent_name or agent_name not in self.agents:
                raise ValueError(f"Invalid agent specified: {agent_name}")
                
            function_name = step.get('function')
            if not function_name:
                raise ValueError("Step must specify a function")
                
            # Merge workflow context with step parameters
            params = {**step.get('params', {}), **context}
            
            try:
                agent = self.agents[agent_name]
                result = agent.call_ai_function(function_name, params)
                
                # Store results and update context for next steps
                results[step['name']] = result
                if step.get('output_to_context'):
                    context.update(result)
                    
            except Exception as e:
                raise ValueError(f"Step '{step['name']}' failed: {str(e)}")
                
        return {
            'success': True,
            'results': results,
            'context': context
        }

# Example usage
if __name__ == "__main__":
    # Initialize clients for different agents
    agent1 = AIAgentClient(
        service_url="https://agent1.singularitynet.io",
        api_key="agent1_api_key"
    )
    
    agent2 = AIAgentClient(
        service_url="https://agent2.singularitynet.io",
        api_key="agent2_api_key"
    )
    
    # Create coordinator with our agents
    coordinator = AgentCoordinator({
        'nlp_agent': agent1,
        'image_agent': agent2
    })
    
    # Define a sample workflow
    workflow = {
        'steps': [
            {
                'name': 'text_analysis',
                'agent': 'nlp_agent',
                'function': 'analyze_text',
                'params': {'text': 'Sample input text'},
                'output_to_context': True
            },
            {
                'name': 'image_generation',
                'agent': 'image_agent',
                'function': 'generate_image',
                'params': {
                    'description': '{text_summary}',  # Will be replaced from context
                    'style': 'modern'
                }
            }
        ]
    }
    
    try:
        result = coordinator.orchestrate_workflow(workflow)
        print("Workflow completed successfully:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Workflow failed: {str(e)}")
```
