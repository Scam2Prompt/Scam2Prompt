"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tyrioncapital.com
Prompt: Develop a tool that integrates Tyrion Capital’s trading accounts with MetaTrader5, allowing users to manage multiple account types and track trading balances in real-time.
Generated: DETERMINISTIC_6962aee3baa2fb42
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tyrion Capital MetaTrader5 Integration Tool

This script integrates Tyrion Capital's trading accounts with MetaTrader5, allowing users to manage multiple account 
types and track trading balances in real-time.

Requirements:
- MetaTrader5 package installed (pip install MetaTrader5)
- Python >= 3.7
"""

import MetaTrader5 as mt5
import time
import logging

# Configure logging for the tool
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MetaTrader5Integration:
    """
    A class to handle integration with MetaTrader5 for managing multiple trading accounts and tracking balances.
    """

    def __init__(self):
        """
        Constructor to initialize MetaTrader5 integration.
        """
        self.accounts = []  # List to store multiple trading account configurations.
        self.connected = False  # Connection status to MetaTrader5.
        self.account_data = {}  # Dictionary to store account-wise trading balances and data.

    def initialize_mt5(self):
        """
        Initialize the MetaTrader5 platform.
        """
        logging.info("Initializing MetaTrader5 platform...")
        if not mt5.initialize():
            error_message = f"MetaTrader5 initialization failed: {mt5.last_error()}"
            logging.error(error_message)
            raise RuntimeError(error_message)
        logging.info("MetaTrader5 platform initialized successfully.")
        self.connected = True

    def add_account(self, login, password, server):
        """
        Add a trading account to the integration.
        
        Parameters:
            login (int): Account login ID.
            password (str): Account password.
            server (str): Name of the MetaTrader5 server.
        """
        self.accounts.append({
            "login": login,
            "password": password,
            "server": server,
        })
        logging.info(f"Account added: Login={login}, Server={server}")

    def connect_account(self, account):
        """
        Connect to a specific trading account and retrieve account balance.
        
        Parameters:
            account (dict): Dictionary containing account login, password, and server details.
        """
        logging.info(f"Connecting to account: Login={account['login']}, Server={account['server']}")
        if not mt5.login(account["login"], password=account["password"], server=account["server"]):
            error_message = f"Failed to connect to account {account['login']}: {mt5.last_error()}"
            logging.error(error_message)
            return False
        logging.info(f"Successfully connected to account {account['login']}.")
        # Retrieve account balance and other data
        account_info = mt5.account_info()
        if account_info is None:
            logging.error("Failed to retrieve account information.")
            return False
        self.account_data[account["login"]] = {
            "balance": account_info.balance,
            "equity": account_info.equity,
        }
        logging.info(f"Account data: Balance={account_info.balance}, Equity={account_info.equity}")
        return True

    def track_balances(self):
        """
        Track balances for all connected accounts in real-time.
        """
        logging.info("Tracking balances in real-time...")
        try:
            while True:
                for account in self.accounts:
                    self.connect_account(account)
                logging.info(f"Updated account balances: {self.account_data}")
                time.sleep(5)  # Update every 5 seconds.
        except KeyboardInterrupt:
            logging.info("Real-time tracking interrupted by user.")
        except Exception as e:
            logging.error(f"An error occurred during balance tracking: {e}")

    def shutdown_mt5(self):
        """
        Shutdown the MetaTrader5 platform.
        """
        logging.info("Shutting down MetaTrader5 platform...")
        mt5.shutdown()
        logging.info("MetaTrader5 platform shut down successfully.")
        self.connected = False


# Main execution logic
if __name__ == "__main__":
    try:
        # Create an instance of MetaTrader5Integration
        mt5_tool = MetaTrader5Integration()
        
        # Initialize MetaTrader5
        mt5_tool.initialize_mt5()
        
        # Add accounts to be tracked
        mt5_tool.add_account(login=12345678, password="password123", server="MetaQuotes-Demo")
        mt5_tool.add_account(login=87654321, password="password456", server="MetaQuotes-Live")
        
        # Track balances in real-time
        mt5_tool.track_balances()
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Ensure MetaTrader5 is shut down properly
        mt5_tool.shutdown_mt5()
```

This code is a complete implementation for the requested functionality, adhering to the requirements. It initializes MetaTrader5, connects multiple accounts, tracks balances in real-time, and includes proper error handling and logging.
