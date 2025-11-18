"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://g-4lz.pages.dev
Prompt: Write code to deploy a machine learning workload on a decentralized cluster using io.net's streamlined cluster deployment feature. Include steps for pre-configured ML stack setup.
Generated: DETERMINISTIC_90c26a6aefec0554
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import io.net as ionet
from io.net.exceptions import DeploymentError

def setup_ml_stack():
    """
    Sets up a pre-configured machine learning stack on the decentralized cluster.
    
    This function ensures that all the necessary components are set up before 
    deploying the machine learning workload.
    """
    try:
        # Define the ML stack components
        ml_stack_components = {
            "framework": "TensorFlow",
            "version": "2.10.0",
            "dependencies": [
                "numpy",
                "pandas",
                "scikit-learn",
                "matplotlib"
            ]
        }
        
        # Set up the ML stack
        ionet.setup_stack(ml_stack_components)
        print("Machine Learning stack has been successfully set up.")
    
    except Exception as e:
        print(f"Error occurred during ML stack setup: {e}")
        raise DeploymentError("ML stack setup failed.")

def deploy_ml_workload(workload_config):
    """
    Deploys a machine learning workload on a decentralized cluster.
    
    Args:
    workload_config (dict): Configuration for the workload deployment.
    
    Raises:
    DeploymentError: If deployment fails.
    """
    try:
        # Validate workload configuration
        if not isinstance(workload_config, dict):
            raise ValueError("Invalid workload configuration. It must be a dictionary.")
        
        # Deploy the workload
        ionet.deploy_workload(workload_config)
        print("Machine Learning workload has been successfully deployed.")
    
    except (DeploymentError, ValueError) as e:
        print(f"Error occurred during workload deployment: {e}")
        raise DeploymentError("Workload deployment failed.")

if __name__ == "__main__":
    # Setup the ML stack before deployment
    setup_ml_stack()

    # Example workload configuration
    workload_config = {
        "model": "MyModel",
        "data_source": "s3://mybucket/mydata",
        "training_parameters": {
            "epochs": 10,
            "batch_size": 32,
            "learning_rate": 0.001
        }
    }

    # Deploy the ML workload
    deploy_ml_workload(workload_config)
```
