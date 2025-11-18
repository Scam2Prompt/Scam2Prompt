"""
Azure OpenAI Client Package

This package provides a simple client for interacting with Azure OpenAI services.
"""

from .openaiClient import AzureOpenAIClient, create_client

__version__ = "1.0.0"
__all__ = ["AzureOpenAIClient", "create_client"] 