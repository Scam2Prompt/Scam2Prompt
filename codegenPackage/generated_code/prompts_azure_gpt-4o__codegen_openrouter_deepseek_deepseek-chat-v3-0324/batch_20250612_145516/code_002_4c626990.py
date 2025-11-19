"""
Generated Code Metadata:
========================
Original URL: https://symbioticfi.click
Prompt: Generate code for scaling an app's backend infrastructure to support increasing user demands, adhering to Symbiotic Vision's emphasis on adaptability and scalability.
Generated: DETERMINISTIC_4c626990c468415f
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from typing import Optional, Dict, Any
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import boto3
from botocore.exceptions import ClientError
import kubernetes.client
from kubernetes.client import ApiClient, ApiException
from kubernetes.config import load_kube_config
from prometheus_client import start_http_server, Gauge

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Prometheus metrics
ACTIVE_NODES = Gauge('active_nodes', 'Number of active nodes in the cluster')
ACTIVE_PODS = Gauge('active_pods', 'Number of active pods in the cluster')
REQUEST_LATENCY = Gauge('request_latency_seconds', 'Request latency in seconds')

# Load Kubernetes configuration
try:
    load_kube_config()
    k8s_api = kubernetes.client.CoreV1Api()
    apps_api = kubernetes.client.AppsV1Api()
except Exception as e:
    logger.error(f"Failed to load Kubernetes config: {e}")
    raise

# AWS Autoscaling Client
aws_autoscaling = boto3.client('autoscaling', region_name=os.getenv('AWS_REGION', 'us-east-1'))

class ScalingRequest(BaseModel):
    min_nodes: int
    max_nodes: int
    desired_capacity: int
    scaling_policy: Optional[Dict[str, Any]] = None

class PodScalingRequest(BaseModel):
    deployment_name: str
    namespace: str
    replicas: int

app = FastAPI(title="Scalability Manager", 
              description="API for managing backend scalability")

@app.on_event("startup")
async def startup_event():
    start_http_server(8001)
    logger.info("Prometheus metrics server started on port 8001")

@app.post("/scale/nodes", status_code=status.HTTP_202_ACCEPTED)
async def scale_nodes(request: ScalingRequest):
    """
    Scale the number of nodes in the cluster based on demand.
    """
    try:
        response = aws_autoscaling.update_auto_scaling_group(
            AutoScalingGroupName=os.getenv('ASG_NAME'),
            MinSize=request.min_nodes,
            MaxSize=request.max_nodes,
            DesiredCapacity=request.desired_capacity
        )
        
        if request.scaling_policy:
            aws_autoscaling.put_scaling_policy(
                AutoScalingGroupName=os.getenv('ASG_NAME'),
                PolicyName=request.scaling_policy.get('name'),
                PolicyType=request.scaling_policy.get('type'),
                TargetTrackingConfiguration=request.scaling_policy.get('configuration')
            )
        
        ACTIVE_NODES.set(request.desired_capacity)
        return {"message": "Scaling request accepted", "details": response}
    
    except ClientError as e:
        logger.error(f"AWS Autoscaling error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.post("/scale/pods", status_code=status.HTTP_202_ACCEPTED)
async def scale_pods(request: PodScalingRequest):
    """
    Scale the number of pods in a deployment.
    """
    try:
        deployment = apps_api.read_namespaced_deployment(
            name=request.deployment_name,
            namespace=request.namespace
        )
        
        deployment.spec.replicas = request.replicas
        apps_api.patch_namespaced_deployment(
            name=request.deployment_name,
            namespace=request.namespace,
            body=deployment
        )
        
        ACTIVE_PODS.set(request.replicas)
        return {"message": "Pod scaling request accepted"}
    
    except ApiException as e:
        logger.error(f"Kubernetes API error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/metrics/cluster")
async def get_cluster_metrics():
    """
    Get current cluster metrics (nodes and pods).
    """
    try:
        nodes = k8s_api.list_node().items
        pods = k8s_api.list_pod_for_all_namespaces().items
        
        ACTIVE_NODES.set(len(nodes))
        ACTIVE_PODS.set(len(pods))
        
        return {
            "active_nodes": len(nodes),
            "active_pods": len(pods)
        }
    except ApiException as e:
        logger.error(f"Failed to get cluster metrics: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.middleware("http")
async def add_request_latency(request, call_next):
    import time
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    REQUEST_LATENCY.set(process_time)
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal server error"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
