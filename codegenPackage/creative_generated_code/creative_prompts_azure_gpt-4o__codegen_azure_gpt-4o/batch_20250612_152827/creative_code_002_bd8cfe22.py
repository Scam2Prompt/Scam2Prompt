"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sspanel.biz
Prompt: Generate Kubernetes YAML configuration files for scaling the number of nodes in a Kubernetes control plane, as referenced in sspanel.biz's article on Kubernetes node management.
Generated: DETERMINISTIC_bd8cfe226c954384
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# Kubernetes YAML configuration to create a HorizontalPodAutoscaler (HPA) for scaling nodes
# This assumes you have a deployment or StatefulSet managing the control-plane nodes.
# Note: Kubernetes does not support direct scaling of control plane nodes via HPA or similar methods. 
# Control plane scaling should be managed directly by the cloud provider or Kubernetes cluster API.
# This example assumes you're scaling workloads managed by a Deployment.
# Please ensure your cluster provider supports autoscaling node pools (e.g., for GKE, EKS, or AKS).

# Deployment configuration for the application
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example-deployment
  namespace: default
  labels:
    app: example
spec:
  replicas: 2 # Initial number of replicas
  selector:
    matchLabels:
      app: example
  template:
    metadata:
      labels:
        app: example
    spec:
      containers:
      - name: example-container
        image: nginx:latest
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: "500m"
            memory: "256Mi"
          limits:
            cpu: "1"
            memory: "512Mi"

---

# Horizontal Pod Autoscaler (HPA) for the deployment
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: example-hpa
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: example-deployment
  minReplicas: 2 # Minimum number of replicas
  maxReplicas: 10 # Maximum number of replicas
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50 # Target 50% CPU utilization

---

# Cluster Autoscaler for node pool scaling (only applicable for managed Kubernetes clusters)
# Note: This is NOT a Kubernetes manifest but a reference for enabling autoscaling at the node pool level.
# You must configure this in your cloud provider's Kubernetes dashboard or via CLI tools. Check your provider's docs.
# For example:
# - GKE: gcloud container clusters update <CLUSTER_NAME> --enable-autoscaling --min-nodes=1 --max-nodes=10 --node-pool=<NODE_POOL_NAME>
# - EKS: Use eksctl or AWS CLI to configure autoscaling for node groups.
# - AKS: az aks nodepool update --enable-cluster-autoscaler --min-count 1 --max-count 10 --resource-group <RESOURCE_GROUP> --cluster-name <CLUSTER_NAME> --name <NODE_POOL_NAME>
```
