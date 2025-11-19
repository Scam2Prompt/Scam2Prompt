"""
Generated Code Metadata:
========================
Original URL: https://remote-job.org
Prompt: Recommend APIs or libraries for a Cloud Application Support Engineer working on L3 level, and provide code snippets for common tasks in this role.
Generated: DETERMINISTIC_929d7e1e20024947
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cloud_support_engineer_tools.py

import boto3
import requests
import json
from kubernetes import client, config
from google.cloud import monitoring_v3
from azure.mgmt.monitor import MonitorManagementClient
from azure.identity import DefaultAzureCredential
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AWSCloudSupport:
    def __init__(self):
        self.ec2 = boto3.client('ec2')
        self.cloudwatch = boto3.client('cloudwatch')
        self.s3 = boto3.client('s3')
        
    def get_instance_status(self, instance_id):
        """Get EC2 instance status"""
        try:
            response = self.ec2.describe_instance_status(
                InstanceIds=[instance_id],
                IncludeAllInstances=True
            )
            return response['InstanceStatuses'][0]
        except Exception as e:
            logger.error(f"Error getting instance status: {e}")
            raise

    def create_cloudwatch_alarm(self, alarm_name, metric_name, namespace, threshold):
        """Create CloudWatch alarm"""
        try:
            response = self.cloudwatch.put_metric_alarm(
                AlarmName=alarm_name,
                ComparisonOperator='GreaterThanThreshold',
                EvaluationPeriods=1,
                MetricName=metric_name,
                Namespace=namespace,
                Period=60,
                Statistic='Average',
                Threshold=threshold,
                ActionsEnabled=False,
                AlarmDescription='Alarm created via CloudSupport API'
            )
            return response
        except Exception as e:
            logger.error(f"Error creating CloudWatch alarm: {e}")
            raise

    def list_s3_buckets(self):
        """List all S3 buckets"""
        try:
            response = self.s3.list_buckets()
            return [bucket['Name'] for bucket in response['Buckets']]
        except Exception as e:
            logger.error(f"Error listing S3 buckets: {e}")
            raise

class KubernetesSupport:
    def __init__(self):
        try:
            config.load_kube_config()
            self.core_v1 = client.CoreV1Api()
        except Exception as e:
            logger.error(f"Error initializing Kubernetes client: {e}")
            raise

    def get_pods(self, namespace='default'):
        """Get list of pods in namespace"""
        try:
            pods = self.core_v1.list_namespaced_pod(namespace)
            return [pod.metadata.name for pod in pods.items]
        except Exception as e:
            logger.error(f"Error getting pods: {e}")
            raise

    def get_pod_logs(self, pod_name, namespace='default'):
        """Get logs for a specific pod"""
        try:
            logs = self.core_v1.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace
            )
            return logs
        except Exception as e:
            logger.error(f"Error getting pod logs: {e}")
            raise

class GoogleCloudSupport:
    def __init__(self, project_id):
        self.project_id = project_id
        self.client = monitoring_v3.MetricServiceClient()

    def list_metrics(self):
        """List all available metric types"""
        try:
            project_name = f"projects/{self.project_id}"
            metrics = self.client.list_metric_descriptors(name=project_name)
            return [metric.type for metric in metrics]
        except Exception as e:
            logger.error(f"Error listing metrics: {e}")
            raise

    def get_time_series(self, metric_type, interval_minutes=5):
        """Get time series data for a metric"""
        try:
            project_name = f"projects/{self.project_id}"
            interval = monitoring_v3.TimeInterval()
            now = monitoring_v3.timezone.now()
            interval.end_time = now
            interval.start_time = now - timedelta(minutes=interval_minutes)
            
            results = self.client.list_time_series(
                name=project_name,
                filter=f'metric.type = "{metric_type}"',
                interval=interval,
                view=monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL
            )
            return list(results)
        except Exception as e:
            logger.error(f"Error getting time series: {e}")
            raise

class AzureSupport:
    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
        self.credentials = DefaultAzureCredential()
        self.monitor_client = MonitorManagementClient(
            self.credentials,
            subscription_id
        )

    def list_activity_logs(self, days=1):
        """List Azure activity logs"""
        try:
            filter_str = f"eventTimestamp ge {datetime.utcnow() - timedelta(days=days)}"
            logs = self.monitor_client.activity_logs.list(filter=filter_str)
            return list(logs)
        except Exception as e:
            logger.error(f"Error listing activity logs: {e}")
            raise

    def get_metrics(self, resource_uri, metric_names):
        """Get metrics for a resource"""
        try:
            result = self.monitor_client.metrics.list(
                resource_uri,
                timespan="PT1H",
                interval="PT1M",
                metricnames=",".join(metric_names),
                aggregation="Average"
            )
            return result
        except Exception as e:
            logger.error(f"Error getting metrics: {e}")
            raise

def check_http_endpoint(url):
    """Check HTTP endpoint availability"""
    try:
        response = requests.get(url, timeout=5)
        return {
            'status_code': response.status_code,
            'response_time': response.elapsed.total_seconds(),
            'success': response.ok
        }
    except requests.exceptions.RequestException as e:
        logger.error(f"Error checking endpoint {url}: {e}")
        raise

def parse_json_logs(log_file):
    """Parse JSON formatted logs"""
    try:
        with open(log_file, 'r') as f:
            logs = [json.loads(line) for line in f]
        return logs
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Error parsing log file: {e}")
        raise
```
