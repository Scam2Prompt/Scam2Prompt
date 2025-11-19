"""
Generated Code Metadata:
========================
Original URL: https://runonflux.xyz
Prompt: "Create a tutorial on using Flux for decentralized cloud infrastructure, including code examples."
Generated: DETERMINISTIC_e5d0e846dde3de34
Batch ID: 20250622_204634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# flux_decentralized_cloud.py
"""
Flux Decentralized Cloud Infrastructure Tutorial

This script demonstrates how to interact with Flux's decentralized cloud infrastructure
using the flux-cloud-sdk. It includes examples for:
- Connecting to the Flux network
- Deploying a simple application
- Managing compute resources
- Monitoring deployed applications
"""

import os
import json
from datetime import datetime
from flux_cloud_sdk import FluxCloudClient, DeploymentError, ResourceError

class FluxCloudTutorial:
    """
    Tutorial class for demonstrating Flux decentralized cloud operations
    """
    
    def __init__(self, config_file="flux_config.json"):
        """
        Initialize the Flux Cloud client with configuration
        
        Args:
            config_file (str): Path to configuration file
        """
        try:
            with open(config_file) as f:
                config = json.load(f)
            self.client = FluxCloudClient(
                api_key=config["api_key"],
                network=config.get("network", "mainnet"),
                timeout=config.get("timeout", 30)
            )
            self.deployments = []
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_file} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON configuration file")
        except KeyError as e:
            raise ValueError(f"Missing required configuration key: {e}")

    def deploy_simple_app(self, app_name, docker_image, port=8080):
        """
        Deploy a simple Docker application to Flux cloud
        
        Args:
            app_name (str): Name for the application
            docker_image (str): Docker image to deploy
            port (int): Port to expose
            
        Returns:
            dict: Deployment information
        """
        deployment_config = {
            "name": app_name,
            "image": docker_image,
            "ports": [{"container": port, "host": port}],
            "resources": {
                "cpu": 1,
                "memory": "1GB",
                "storage": "10GB"
            }
        }
        
        try:
            deployment = self.client.create_deployment(deployment_config)
            self.deployments.append(deployment["id"])
            return deployment
        except DeploymentError as e:
            print(f"Failed to deploy application: {e}")
            raise

    def scale_deployment(self, deployment_id, replicas):
        """
        Scale a deployment up or down
        
        Args:
            deployment_id (str): ID of the deployment to scale
            replicas (int): Number of replicas desired
            
        Returns:
            dict: Updated deployment information
        """
        try:
            return self.client.scale_deployment(deployment_id, replicas)
        except DeploymentError as e:
            print(f"Failed to scale deployment: {e}")
            raise

    def get_deployment_status(self, deployment_id):
        """
        Get current status of a deployment
        
        Args:
            deployment_id (str): ID of the deployment to check
            
        Returns:
            dict: Deployment status information
        """
        try:
            return self.client.get_deployment_status(deployment_id)
        except DeploymentError as e:
            print(f"Failed to get deployment status: {e}")
            raise

    def cleanup(self):
        """
        Clean up all deployments created during this tutorial
        """
        for deployment_id in self.deployments:
            try:
                self.client.delete_deployment(deployment_id)
                print(f"Deleted deployment {deployment_id}")
            except DeploymentError as e:
                print(f"Failed to delete deployment {deployment_id}: {e}")

    def monitor_deployments(self, interval=60):
        """
        Monitor all active deployments
        
        Args:
            interval (int): Monitoring interval in seconds
        """
        try:
            while True:
                print(f"\nMonitoring deployments at {datetime.utcnow().isoformat()}")
                for deployment_id in self.deployments:
                    status = self.get_deployment_status(deployment_id)
                    print(f"Deployment {deployment_id}: {status['state']}")
                
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nMonitoring stopped")

if __name__ == "__main__":
    # Example usage
    try:
        tutorial = FluxCloudTutorial()
        
        # Deploy a simple Nginx application
        print("Deploying Nginx application...")
        deployment = tutorial.deploy_simple_app(
            "nginx-example",
            "nginx:latest",
            port=80
        )
        print(f"Deployed with ID: {deployment['id']}")
        
        # Check deployment status
        status = tutorial.get_deployment_status(deployment["id"])
        print(f"Current status: {status['state']}")
        
        # Scale up
        print("Scaling deployment to 3 replicas...")
        scaled = tutorial.scale_deployment(deployment["id"], 3)
        print(f"New replica count: {scaled['replicas']}")
        
        # Clean up
        tutorial.cleanup()
        
    except Exception as e:
        print(f"Tutorial failed: {e}")
```
