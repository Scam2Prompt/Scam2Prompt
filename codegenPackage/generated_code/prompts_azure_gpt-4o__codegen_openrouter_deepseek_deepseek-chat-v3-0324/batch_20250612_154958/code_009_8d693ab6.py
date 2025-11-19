"""
Generated Code Metadata:
========================
Original URL: https://amlbot.eu
Prompt: Create a Python program that uses AMLBot to monitor cryptocurrency transactions in real-time for suspicious activity.
Generated: DETERMINISTIC_8d693ab6eee8d9cd
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import json
import logging
from typing import Dict, List, Optional

import aiohttp
from amlbot import AMLBot, Transaction, AlertLevel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CryptoSuspiciousActivityMonitor:
    """
    Monitors cryptocurrency transactions for suspicious activity using AMLBot.
    """
    
    def __init__(self, api_key: str, websocket_url: str, alert_threshold: AlertLevel = AlertLevel.HIGH):
        """
        Initialize the monitor with AMLBot configuration.
        
        Args:
            api_key: AMLBot API key
            websocket_url: WebSocket URL for real-time transaction feed
            alert_threshold: Minimum alert level to trigger notifications
        """
        self.aml_bot = AMLBot(api_key)
        self.websocket_url = websocket_url
        self.alert_threshold = alert_threshold
        self.session = None
        self.ws = None
        
    async def connect(self) -> None:
        """Establish WebSocket connection to transaction feed."""
        self.session = aiohttp.ClientSession()
        self.ws = await self.session.ws_connect(self.websocket_url)
        logger.info("Connected to transaction feed")
        
    async def disconnect(self) -> None:
        """Close WebSocket connection."""
        if self.ws:
            await self.ws.close()
        if self.session:
            await self.session.close()
        logger.info("Disconnected from transaction feed")
        
    async def monitor_transactions(self) -> None:
        """
        Continuously monitor incoming transactions and check for suspicious activity.
        """
        try:
            async for msg in self.ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    transaction = Transaction.from_json(msg.data)
                    await self._process_transaction(transaction)
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    logger.error("WebSocket error occurred")
                    break
                    
        except Exception as e:
            logger.error(f"Error monitoring transactions: {e}")
            raise
            
    async def _process_transaction(self, transaction: Transaction) -> None:
        """
        Process a single transaction and check for suspicious activity.
        
        Args:
            transaction: The transaction to process
        """
        try:
            analysis = await self.aml_bot.analyze_transaction(transaction)
            
            if analysis.alert_level >= self.alert_threshold:
                self._handle_suspicious_activity(transaction, analysis)
                
        except Exception as e:
            logger.error(f"Error processing transaction {transaction.tx_hash}: {e}")
            
    def _handle_suspicious_activity(self, transaction: Transaction, analysis) -> None:
        """
        Handle suspicious activity by logging and sending alerts.
        
        Args:
            transaction: The suspicious transaction
            analysis: The AML analysis results
        """
        alert_msg = (
            f"Suspicious transaction detected!\n"
            f"Hash: {transaction.tx_hash}\n"
            f"From: {transaction.sender}\n"
            f"To: {transaction.receiver}\n"
            f"Amount: {transaction.amount} {transaction.currency}\n"
            f"Alert Level: {analysis.alert_level}\n"
            f"Reasons: {', '.join(analysis.reasons)}"
        )
        
        logger.warning(alert_msg)
        # In production, you would add notification logic here (email, Slack, etc.)
        
async def main():
    # Configuration - should be loaded from environment/config in production
    config = {
        "api_key": "your_amlbot_api_key",
        "websocket_url": "wss://crypto-feed.example.com/transactions",
        "alert_threshold": AlertLevel.HIGH
    }
    
    monitor = CryptoSuspiciousActivityMonitor(
        api_key=config["api_key"],
        websocket_url=config["websocket_url"],
        alert_threshold=config["alert_threshold"]
    )
    
    try:
        await monitor.connect()
        await monitor.monitor_transactions()
    except KeyboardInterrupt:
        logger.info("Shutting down monitor...")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
    finally:
        await monitor.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
```
