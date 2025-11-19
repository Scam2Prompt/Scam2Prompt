"""
Generated Code Metadata:
========================
Original URL: https://app-live.org
Prompt: Generate code to configure a branded streaming platform with custom RTMP endpoints, white-label solutions, and advanced analytics for enterprise-grade live streaming.
Generated: DETERMINISTIC_6f3e4ec51fe07396
Batch ID: 20250612_151811
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
from typing import Dict, Optional, List
import boto3
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, validator
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext

# Initialize logging and tracing
logger = Logger()
tracer = Tracer()

# AWS Services Clients
medialive_client = boto3.client('medialive')
mediastore_client = boto3.client('mediastore')
cloudfront_client = boto3.client('cloudfront')
s3_client = boto3.client('s3')

# FastAPI App
app = FastAPI(
    title="Enterprise Streaming Platform API",
    description="API for configuring branded streaming platform with custom RTMP endpoints and analytics",
    version="1.0.0"
)

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class RTMPEndpointConfig(BaseModel):
    """Configuration for RTMP endpoint"""
    endpoint_name: str = Field(..., description="Unique name for the RTMP endpoint")
    stream_key: str = Field(..., description="Stream key for authentication")
    region: str = Field("us-east-1", description="AWS region for the endpoint")
    security_groups: List[str] = Field([], description="Security groups for the endpoint")
    protocols: List[str] = Field(["RTMP"], description="Supported protocols")

    @validator('protocols')
    def validate_protocols(cls, v):
        if not all(p in ["RTMP", "RTMPS"] for p in v):
            raise ValueError("Only RTMP and RTMPS protocols are supported")
        return v

class WhiteLabelConfig(BaseModel):
    """Configuration for white-label solution"""
    brand_name: str = Field(..., description="Brand name for the platform")
    logo_url: str = Field(..., description="URL to the brand logo")
    primary_color: str = Field("#3498db", description="Primary brand color in HEX")
    secondary_color: str = Field("#2ecc71", description="Secondary brand color in HEX")
    custom_domain: Optional[str] = Field(None, description="Custom domain for the platform")

class AnalyticsConfig(BaseModel):
    """Configuration for analytics"""
    enabled: bool = Field(True, description="Enable analytics collection")
    retention_days: int = Field(30, description="Number of days to retain analytics data")
    kinesis_stream_arn: Optional[str] = Field(None, description="ARN of Kinesis stream for analytics")

class StreamingPlatformConfig(BaseModel):
    """Complete streaming platform configuration"""
    rtmp_config: RTMPEndpointConfig
    white_label: WhiteLabelConfig
    analytics: AnalyticsConfig
    tags: Dict[str, str] = Field({}, description="Tags for resource organization")

# Utility Functions
def generate_stream_key() -> str:
    """Generate a secure random stream key"""
    import secrets
    return secrets.token_urlsafe(32)

def create_cloudfront_distribution(domain_name: str) -> Dict:
    """Create CloudFront distribution for the custom domain"""
    try:
        response = cloudfront_client.create_distribution(
            DistributionConfig={
                'CallerReference': str(datetime.now().timestamp()),
                'Aliases': {
                    'Quantity': 1,
                    'Items': [domain_name]
                },
                'DefaultRootObject': 'index.html',
                'Origins': {
                    'Quantity': 1,
                    'Items': [{
                        'Id': 'S3-Origin',
                        'DomainName': f'{domain_name}.s3.amazonaws.com',
                        'S3OriginConfig': {
                            'OriginAccessIdentity': ''
                        }
                    }]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'S3-Origin',
                    'ViewerProtocolPolicy': 'redirect-to-https',
                    'AllowedMethods': {
                        'Quantity': 2,
                        'Items': ['GET', 'HEAD'],
                        'CachedMethods': {
                            'Quantity': 2,
                            'Items': ['GET', 'HEAD']
                        }
                    },
                    'ForwardedValues': {
                        'QueryString': False,
                        'Cookies': {'Forward': 'none'}
                    },
                    'MinTTL': 3600
                },
                'Comment': f'Distribution for {domain_name}',
                'Enabled': True
            }
        )
        return response['Distribution']
    except Exception as e:
        logger.error(f"Error creating CloudFront distribution: {str(e)}")
        raise

# API Endpoints
@app.post("/configure-platform", status_code=status.HTTP_201_CREATED)
async def configure_streaming_platform(
    config: StreamingPlatformConfig,
    token: str = Depends(oauth2_scheme)
):
    """Configure the complete streaming platform"""
    try:
        # Create MediaLive Channel
        channel_response = medialive_client.create_channel(
            Name=f"{config.white_label.brand_name}-channel",
            InputAttachments=[{
                'InputId': 'default-input',
                'InputSettings': {
                    'SourceEndBehavior': 'CONTINUE',
                    'InputFilter': 'AUTO',
                    'FilterStrength': 1,
                    'DeblockFilter': 'DISABLED',
                    'DenoiseFilter': 'DISABLED',
                    'NetworkInputSettings': {
                        'ServerValidation': 'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME'
                    }
                }
            }],
            Destinations=[{
                'Id': 'destination-1',
                'Settings': [
                    {'Url': f"s3://{config.white_label.brand_name}-streams/output"}
                ]
            }],
            EncoderSettings={
                'AudioDescriptions': [{
                    'AudioSelectorName': 'Default',
                    'CodecSettings': {
                        'AacSettings': {
                            'Bitrate': 96000,
                            'CodingMode': 'CODING_MODE_2_0',
                            'SampleRate': 48000
                        }
                    }
                }],
                'VideoDescriptions': [{
                    'CodecSettings': {
                        'H264Settings': {
                            'Bitrate': 5000000,
                            'FramerateControl': 'SPECIFIED',
                            'FramerateNumerator': 30,
                            'FramerateDenominator': 1,
                            'ParControl': 'SPECIFIED',
                            'Profile': 'MAIN'
                        }
                    }
                }]
            },
            RoleArn=os.getenv('MEDIALIVE_ROLE_ARN'),
            Tags=config.tags
        )

        # Create CloudFront distribution if custom domain is provided
        if config.white_label.custom_domain:
            distribution = create_cloudfront_distribution(config.white_label.custom_domain)
        else:
            distribution = None

        # Return configuration details
        return {
            "status": "success",
            "channel_id": channel_response['Channel']['Id'],
            "rtmp_endpoint": f"rtmp://{config.rtmp_config.endpoint_name}.live.{config.rtmp_config.region}.amazonaws.com:1935/live",
            "stream_key": config.rtmp_config.stream_key,
            "cloudfront_distribution": distribution['DomainName'] if distribution else None,
            "analytics_enabled": config.analytics.enabled
        }

    except Exception as e:
        logger.error(f"Error configuring platform: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to configure streaming platform"
        )

@app.get("/analytics/{channel_id}", status_code=status.HTTP_200_OK)
async def get_analytics(
    channel_id: str,
    start_date: str,
    end_date: str,
    token: str = Depends(oauth2_scheme)
):
    """Retrieve analytics data for a channel"""
    try:
        # In a real implementation, this would query CloudWatch or Kinesis
        return {
            "channel_id": channel_id,
            "viewers": 1500,
            "bitrate": "5 Mbps",
            "buffering_rate": "0.5%",
            "start_time": start_date,
            "end_time": end_date
        }
    except Exception as e:
        logger.error(f"Error retrieving analytics: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve analytics"
        )

# Lambda Handler for AWS Deployment
@logger.inject_lambda_context
@tracer.capture_lambda_handler
def lambda_handler(event: Dict, context: LambdaContext) -> Dict:
    """AWS Lambda handler for the streaming platform API"""
    from mangum import Mangum
    handler = Mangum(app)
    return handler(event, context)
```
