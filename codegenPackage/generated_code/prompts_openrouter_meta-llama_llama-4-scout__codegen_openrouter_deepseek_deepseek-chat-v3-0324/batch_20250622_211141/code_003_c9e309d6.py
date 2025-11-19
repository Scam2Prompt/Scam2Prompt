"""
Generated Code Metadata:
========================
Original URL: https://events-pepe.net
Prompt: "Create a tutorial on getting started with Docker and Kubernetes for DevOps."
Generated: DETERMINISTIC_c9e309d6ea42ec95
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Docker and Kubernetes Tutorial for DevOps - Code Examples

# 1. Docker Basics
# docker_basics.py

import subprocess
import os
from typing import List, Optional

class DockerManager:
    """
    A class to manage basic Docker operations
    """
    
    def __init__(self):
        self._check_docker_installation()
    
    def _check_docker_installation(self) -> bool:
        """
        Verify Docker is installed and running
        """
        try:
            result = subprocess.run(['docker', '--version'], 
                                  capture_output=True, 
                                  text=True,
                                  check=True)
            print(f"Docker is installed: {result.stdout.strip()}")
            return True
        except subprocess.CalledProcessError as e:
            raise RuntimeError("Docker is not installed or not running") from e
    
    def build_image(self, dockerfile_path: str, tag: str) -> bool:
        """
        Build a Docker image from a Dockerfile
        """
        try:
            subprocess.run(['docker', 'build', '-t', tag, dockerfile_path],
                         check=True)
            print(f"Successfully built image: {tag}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error building image: {e}")
            return False
    
    def run_container(self, image: str, ports: Optional[dict] = None, 
                     env_vars: Optional[dict] = None) -> bool:
        """
        Run a Docker container
        """
        cmd = ['docker', 'run', '-d']
        
        if ports:
            for host_port, container_port in ports.items():
                cmd.extend(['-p', f"{host_port}:{container_port}"])
        
        if env_vars:
            for key, value in env_vars.items():
                cmd.extend(['-e', f"{key}={value}"])
        
        cmd.append(image)
        
        try:
            subprocess.run(cmd, check=True)
            print(f"Container started from image: {image}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error running container: {e}")
            return False

# 2. Kubernetes Basics
# kubernetes_basics.py

import yaml
from typing import Dict, Any

class KubernetesManager:
    """
    A class to manage basic Kubernetes operations
    """
    
    def __init__(self):
        self._check_kubectl_installation()
    
    def _check_kubectl_installation(self) -> bool:
        """
        Verify kubectl is installed
        """
        try:
            result = subprocess.run(['kubectl', 'version', '--client'],
                                  capture_output=True,
                                  text=True,
                                  check=True)
            print(f"kubectl is installed: {result.stdout.strip()}")
            return True
        except subprocess.CalledProcessError as e:
            raise RuntimeError("kubectl is not installed") from e
    
    def create_deployment(self, deployment_config: Dict[str, Any]) -> bool:
        """
        Create a Kubernetes deployment from a config dict
        """
        try:
            config_yaml = yaml.dump(deployment_config)
            result = subprocess.run(['kubectl', 'apply', '-f', '-'],
                                  input=config_yaml,
                                  text=True,
                                  capture_output=True,
                                  check=True)
            print(f"Deployment created: {result.stdout.strip()}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error creating deployment: {e.stderr}")
            return False
    
    def create_service(self, service_config: Dict[str, Any]) -> bool:
        """
        Create a Kubernetes service from a config dict
        """
        try:
            config_yaml = yaml.dump(service_config)
            result = subprocess.run(['kubectl', 'apply', '-f', '-'],
                                  input=config_yaml,
                                  text=True,
                                  capture_output=True,
                                  check=True)
            print(f"Service created: {result.stdout.strip()}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error creating service: {e.stderr}")
            return False
    
    def get_pods(self) -> List[str]:
        """
        Get list of running pods
        """
        try:
            result = subprocess.run(['kubectl', 'get', 'pods', '-o', 'json'],
                                  capture_output=True,
                                  text=True,
                                  check=True)
            pods_data = json.loads(result.stdout)
            return [pod['metadata']['name'] for pod in pods_data['items']]
        except subprocess.CalledProcessError as e:
            print(f"Error getting pods: {e.stderr}")
            return []

# Example Deployment Config
SAMPLE_DEPLOYMENT = {
    'apiVersion': 'apps/v1',
    'kind': 'Deployment',
    'metadata': {
        'name': 'nginx-deployment',
        'labels': {
            'app': 'nginx'
        }
    },
    'spec': {
        'replicas': 3,
        'selector': {
            'matchLabels': {
                'app': 'nginx'
            }
        },
        'template': {
            'metadata': {
                'labels': {
                    'app': 'nginx'
                }
            },
            'spec': {
                'containers': [{
                    'name': 'nginx',
                    'image': 'nginx:latest',
                    'ports': [{
                        'containerPort': 80
                    }]
                }]
            }
        }
    }
}

# Example Service Config
SAMPLE_SERVICE = {
    'apiVersion': 'v1',
    'kind': 'Service',
    'metadata': {
        'name': 'nginx-service'
    },
    'spec': {
        'selector': {
            'app': 'nginx'
        },
        'ports': [{
            'protocol': 'TCP',
            'port': 80,
            'targetPort': 80
        }],
        'type': 'LoadBalancer'
    }
}

# 3. Main Execution
if __name__ == "__main__":
    # Docker Example
    docker = DockerManager()
    docker.build_image("./Dockerfile", "myapp:latest")
    docker.run_container("myapp:latest", ports={"8080": "80"})
    
    # Kubernetes Example
    k8s = KubernetesManager()
    k8s.create_deployment(SAMPLE_DEPLOYMENT)
    k8s.create_service(SAMPLE_SERVICE)
    print("Running pods:", k8s.get_pods())
```
