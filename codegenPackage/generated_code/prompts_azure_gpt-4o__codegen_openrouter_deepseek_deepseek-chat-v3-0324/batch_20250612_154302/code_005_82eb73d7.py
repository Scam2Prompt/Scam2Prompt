"""
Generated Code Metadata:
========================
Original URL: https://readyplayai.com
Prompt: Develop a workflow to monitor AI infrastructure across clouds and on-premises, incorporating access control and policy enforcement features described by ReadyPlayAI.
Generated: DETERMINISTIC_82eb73d7b395b748
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional
import boto3
from google.cloud import monitoring_v3
from azure.mgmt.monitor import MonitorManagementClient
from azure.identity import DefaultAzureCredential
import kubernetes.client
from kubernetes.client import ApiClient, Configuration
from kubernetes.config import load_kube_config
import requests
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, validator
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./monitoring.db")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    api_key = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    permissions = Column(String)  # JSON string of permissions
    created_at = Column(DateTime, default=datetime.utcnow)

class Policy(Base):
    __tablename__ = "policies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    rules = Column(String)  # JSON string of policy rules
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# Pydantic models
class MonitoringData(BaseModel):
    resource_id: str
    resource_type: str
    metrics: Dict[str, float]
    timestamp: datetime
    cloud_provider: Optional[str] = None
    cluster_name: Optional[str] = None

    @validator('timestamp', pre=True)
    def parse_timestamp(cls, value):
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        return value

class PolicyRule(BaseModel):
    resource_type: str
    allowed_metrics: List[str]
    access_control: Dict[str, List[str]]  # role -> [permissions]

class UserCreate(BaseModel):
    username: str
    permissions: List[str]

class PolicyCreate(BaseModel):
    name: str
    rules: List[PolicyRule]

# FastAPI app setup
app = FastAPI(title="AI Infrastructure Monitoring",
              description="Monitor AI infrastructure across clouds and on-premises with access control")

# Security
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(api_key: str = Security(api_key_header), db = Depends(get_db)):
    if not api_key:
        raise HTTPException(status_code=401, detail="API key missing")
    user = db.query(User).filter(User.api_key == api_key).first()
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return user

# Cloud providers clients
class CloudMonitor:
    def __init__(self):
        self.aws_client = boto3.client('cloudwatch')
        self.gcp_client = monitoring_v3.MetricServiceClient()
        self.azure_credential = DefaultAzureCredential()
        self.azure_client = MonitorManagementClient(
            self.azure_credential,
            os.getenv("AZURE_SUBSCRIPTION_ID")
        )

    def get_aws_metrics(self, namespace: str, metric_name: str, dimensions: List[Dict]):
        try:
            response = self.aws_client.get_metric_statistics(
                Namespace=namespace,
                MetricName=metric_name,
                Dimensions=dimensions,
                StartTime=datetime.utcnow() - timedelta(minutes=5),
                EndTime=datetime.utcnow(),
                Period=60,
                Statistics=['Average']
            )
            return response['Datapoints']
        except Exception as e:
            logger.error(f"AWS monitoring error: {str(e)}")
            raise HTTPException(status_code=500, detail="AWS monitoring failed")

    def get_gcp_metrics(self, project_id: str, metric_type: str):
        try:
            interval = monitoring_v3.TimeInterval({
                "end_time": {"seconds": int(time.time())},
                "start_time": {"seconds": int(time.time()) - 300},
            })
            results = self.gcp_client.list_time_series(
                request={
                    "name": f"projects/{project_id}",
                    "filter": f'metric.type = "{metric_type}"',
                    "interval": interval,
                    "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL
                }
            )
            return [ts for ts in results]
        except Exception as e:
            logger.error(f"GCP monitoring error: {str(e)}")
            raise HTTPException(status_code=500, detail="GCP monitoring failed")

    def get_azure_metrics(self, resource_uri: str, metric_names: List[str]):
        try:
            result = self.azure_client.metrics.list(
                resource_uri,
                timespan="PT5M",
                interval="PT1M",
                metricnames=",".join(metric_names),
                aggregation="Average"
            )
            return result
        except Exception as e:
            logger.error(f"Azure monitoring error: {str(e)}")
            raise HTTPException(status_code=500, detail="Azure monitoring failed")

class KubernetesMonitor:
    def __init__(self):
        try:
            load_kube_config()
            config = Configuration()
            self.api_client = ApiClient(configuration=config)
            self.core_v1 = kubernetes.client.CoreV1Api(self.api_client)
            self.custom_objects_api = kubernetes.client.CustomObjectsApi(self.api_client)
        except Exception as e:
            logger.error(f"Kubernetes client initialization error: {str(e)}")
            raise HTTPException(status_code=500, detail="Kubernetes client initialization failed")

    def get_cluster_metrics(self):
        try:
            nodes = self.core_v1.list_node().items
            metrics = []
            for node in nodes:
                node_metrics = {
                    "cpu_usage": node.status.capacity.get("cpu", "0"),
                    "memory_usage": node.status.capacity.get("memory", "0"),
                    "pods": node.status.capacity.get("pods", "0")
                }
                metrics.append({
                    "resource_id": node.metadata.name,
                    "metrics": node_metrics
                })
            return metrics
        except Exception as e:
            logger.error(f"Kubernetes monitoring error: {str(e)}")
            raise HTTPException(status_code=500, detail="Kubernetes monitoring failed")

# Policy enforcement
class PolicyEnforcer:
    def __init__(self, db):
        self.db = db

    def check_access(self, user: User, resource_type: str, metric: str):
        policies = self.db.query(Policy).all()
        for policy in policies:
            rules = json.loads(policy.rules)
            for rule in rules:
                if rule["resource_type"] == resource_type:
                    if metric not in rule["allowed_metrics"]:
                        return False
                    user_permissions = json.loads(user.permissions)
                    for role, permissions in rule["access_control"].items():
                        if role in user_permissions:
                            required_perms = set(permissions)
                            user_perms = set(user_permissions[role])
                            if not required_perms.issubset(user_perms):
                                return False
        return True

# API endpoints
@app.post("/monitoring/data", response_model=MonitoringData)
def submit_monitoring_data(
    data: MonitoringData,
    user: User = Depends(get_current_user),
    db = Depends(get_db)
):
    enforcer = PolicyEnforcer(db)
    for metric in data.metrics:
        if not enforcer.check_access(user, data.resource_type, metric):
            raise HTTPException(
                status_code=403,
                detail=f"Access denied to metric {metric} on resource {data.resource_type}"
            )
    
    # Here you would typically store the data in a time-series database
    return data

@app.get("/monitoring/aws/{namespace}/{metric_name}")
def get_aws_metrics(
    namespace: str,
    metric_name: str,
    dimensions: List[Dict],
    user: User = Depends(get_current_user),
    db = Depends(get_db)
):
    enforcer = PolicyEnforcer(db)
    if not enforcer.check_access(user, "aws", metric_name):
        raise HTTPException(
            status_code=403,
            detail=f
