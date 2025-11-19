"""
Generated Code Metadata:
========================
Original URL: https://digisou-ltd.com
Prompt: "Integrate existing software systems to work seamlessly together for a large enterprise."
Generated: DETERMINISTIC_335633c4811f8afb
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Enterprise System Integration Module

This module provides a framework for integrating multiple enterprise software systems
using message queues, API gateways, and data transformation services.
"""

import json
import logging
from typing import Dict, Any, Optional
from abc import ABC, abstractmethod
import requests
from pika import BasicProperties, ConnectionParameters, BlockingConnection
from pika.exceptions import AMQPError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SystemIntegrationError(Exception):
    """Base exception for system integration errors"""
    pass


class DataTransformationError(SystemIntegrationError):
    """Exception raised for data transformation failures"""
    pass


class APIIntegrationError(SystemIntegrationError):
    """Exception raised for API integration failures"""
    pass


class MessageQueueError(SystemIntegrationError):
    """Exception raised for message queue failures"""
    pass


class SystemAdapter(ABC):
    """Abstract base class for system adapters"""
    
    @abstractmethod
    def connect(self) -> None:
        """Connect to the system"""
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        """Disconnect from the system"""
        pass
    
    @abstractmethod
    def is_connected(self) -> bool:
        """Check if connected to the system"""
        pass


class APIGateway(SystemAdapter):
    """API Gateway for REST API integration"""
    
    def __init__(self, base_url: str, auth_token: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.auth_token = auth_token
        self.session = requests.Session()
        self._connected = False
        
    def connect(self) -> None:
        """Establish connection to API gateway"""
        try:
            if self.auth_token:
                self.session.headers.update({
                    'Authorization': f'Bearer {self.auth_token}',
                    'Content-Type': 'application/json'
                })
            self._connected = True
            logger.info(f"Connected to API Gateway at {self.base_url}")
        except Exception as e:
            raise APIIntegrationError(f"API connection failed: {str(e)}")
    
    def disconnect(self) -> None:
        """Close API gateway connection"""
        self.session.close()
        self._connected = False
        logger.info("Disconnected from API Gateway")
    
    def is_connected(self) -> bool:
        """Check API connection status"""
        return self._connected
    
    def make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make API request to the gateway
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path
            data: Request payload
            params: Query parameters
            
        Returns:
            Response data as dictionary
            
        Raises:
            APIIntegrationError: If request fails
        """
        if not self.is_connected():
            self.connect()
            
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                json=data,
                params=params
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise APIIntegrationError(f"API request failed: {str(e)}")


class MessageQueue(SystemAdapter):
    """Message queue system for asynchronous communication"""
    
    def __init__(self, host: str, port: int, queue_name: str):
        self.host = host
        self.port = port
        self.queue_name = queue_name
        self.connection = None
        self.channel = None
        
    def connect(self) -> None:
        """Connect to message queue"""
        try:
            params = ConnectionParameters(
                host=self.host,
                port=self.port
            )
            self.connection = BlockingConnection(params)
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.queue_name, durable=True)
            logger.info(f"Connected to message queue at {self.host}:{self.port}")
        except AMQPError as e:
            raise MessageQueueError(f"Message queue connection failed: {str(e)}")
    
    def disconnect(self) -> None:
        """Disconnect from message queue"""
        if self.connection and self.connection.is_open:
            self.connection.close()
        logger.info("Disconnected from message queue")
    
    def is_connected(self) -> bool:
        """Check message queue connection status"""
        return self.connection and self.connection.is_open
    
    def publish_message(self, message: Dict[str, Any]) -> None:
        """
        Publish message to queue
        
        Args:
            message: Message payload as dictionary
            
        Raises:
            MessageQueueError: If message publishing fails
        """
        if not self.is_connected():
            self.connect()
            
        try:
            self.channel.basic_publish(
                exchange='',
                routing_key=self.queue_name,
                body=json.dumps(message),
                properties=BasicProperties(
                    delivery_mode=2  # Make message persistent
                )
            )
            logger.info(f"Message published to queue {self.queue_name}")
        except AMQPError as e:
            raise MessageQueueError(f"Message publishing failed: {str(e)}")


class DataTransformer:
    """Data transformation service for converting between system formats"""
    
    @staticmethod
    def transform(
        source_format: str,
        target_format: str,
        data: Dict[str, Any],
        mapping: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Transform data from source format to target format
        
        Args:
            source_format: Source data format identifier
            target_format: Target data format identifier
            data: Source data to transform
            mapping: Field mapping dictionary
            
        Returns:
            Transformed data in target format
            
        Raises:
            DataTransformationError: If transformation fails
        """
        try:
            transformed = {}
            for target_field, source_field in mapping.items():
                if source_field in data:
                    transformed[target_field] = data[source_field]
                else:
                    transformed[target_field] = None
            
            logger.info(
                f"Transformed data from {source_format} to {target_format}"
            )
            return transformed
        except Exception as e:
            raise DataTransformationError(f"Data transformation failed: {str(e)}")


class EnterpriseIntegrationOrchestrator:
    """Main orchestrator for enterprise system integration"""
    
    def __init__(self):
        self.adapters = {}
        self.data_transformer = DataTransformer()
        
    def register_adapter(self, name: str, adapter: SystemAdapter) -> None:
        """
        Register a system adapter
        
        Args:
            name: Adapter identifier
            adapter: SystemAdapter instance
        """
        self.adapters[name] = adapter
        logger.info(f"Registered adapter: {name}")
    
    def connect_all(self) -> None:
        """Connect all registered adapters"""
        for name, adapter in self.adapters.items():
            try:
                adapter.connect()
                logger.info(f"Successfully connected adapter: {name}")
            except SystemIntegrationError as e:
                logger.error(f"Failed to connect adapter {name}: {str(e)}")
                raise
    
    def disconnect_all(self) -> None:
        """Disconnect all registered adapters"""
        for name, adapter in self.adapters.items():
            try:
                adapter.disconnect()
                logger.info(f"Successfully disconnected adapter: {name}")
            except SystemIntegrationError as e:
                logger.error(f"Failed to disconnect adapter {name}: {str(e)}")
    
    def integrate_systems(
        self,
        source_system: str,
        target_system: str,
        data: Dict[str, Any],
        field_mapping: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Integrate data between two systems
        
        Args:
            source_system: Source system identifier
            target_system: Target system identifier
            data: Data to transfer
            field_mapping: Field mapping between systems
            
        Returns:
            Response from target system
            
        Raises:
            SystemIntegrationError: If integration fails
        """
        try:
            # Transform data to target system format
            transformed_data = self.data_transformer.transform(
                source_format=source_system,
                target_format=target_system,
                data=data,
                mapping=field_mapping
            )
            
            # Get target system adapter
            target_adapter = self.adapters.get(target_system)
            if not target_adapter:
                raise SystemIntegrationError(f"Unknown target system: {target_system}")
            
            # Handle different adapter types
            if isinstance(target_adapter, APIGateway):
                response = target_adapter.make_request(
                    method="POST",
                    endpoint="/integrate",
                    data=transformed_data
                )
                return response
            elif isinstance(target_adapter, MessageQueue):
                target_adapter.publish_message(transformed_data)
                return {"status": "queued", "message": "
