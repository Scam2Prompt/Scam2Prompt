"""
Generated Code Metadata:
========================
Original URL: https://connect-moca.com
Prompt: Provide an example of how to use the MT5 API to implement a risk management tool that monitors account balance and prevents trades exceeding a defined risk threshold.
Generated: DETERMINISTIC_6a9a8d0ff012fb51
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import MetaTrader5 as mt5
import time
from datetime import datetime

class RiskManagementTool:
    """
    A risk management tool that monitors account balance and prevents trades exceeding a defined risk threshold.
    """
    
    def __init__(self, risk_percentage=1.0, max_retries=3, retry_delay=5):
        """
        Initialize the risk management tool.
        
        Args:
            risk_percentage (float): Maximum risk percentage per trade (default: 1.0%)
            max_retries (int): Maximum connection retries (default: 3)
            retry_delay (int): Delay between retries in seconds (default: 5)
        """
        self.risk_percentage = risk_percentage
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.connected = False
        
    def connect_to_mt5(self):
        """
        Establish connection to MetaTrader 5 terminal.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        retry_count = 0
        while retry_count < self.max_retries and not self.connected:
            try:
                if not mt5.initialize():
                    print(f"Initialize() failed, error code = {mt5.last_error()}")
                    retry_count += 1
                    time.sleep(self.retry_delay)
                else:
                    self.connected = True
                    return True
            except Exception as e:
                print(f"Connection error: {e}")
                retry_count += 1
                time.sleep(self.retry_delay)
        
        return False
    
    def disconnect_from_mt5(self):
        """Disconnect from MetaTrader 5 terminal."""
        if self.connected:
            mt5.shutdown()
            self.connected = False
    
    def get_account_info(self):
        """
        Get current account information.
        
        Returns:
            dict: Account information including balance, equity, margin, etc.
            None: If failed to get account info
        """
        if not self.connected:
            print("Not connected to MT5")
            return None
            
        try:
            account_info = mt5.account_info()
            if account_info is None:
                print(f"Failed to get account info, error code = {mt5.last_error()}")
                return None
                
            return {
                'balance': account_info.balance,
                'equity': account_info.equity,
                'margin': account_info.margin,
                'free_margin': account_info.margin_free,
                'margin_level': account_info.margin_level,
                'currency': account_info.currency,
                'leverage': account_info.leverage
            }
        except Exception as e:
            print(f"Error getting account info: {e}")
            return None
    
    def calculate_position_size(self, symbol, stop_loss_pips, risk_amount=None):
        """
        Calculate position size based on risk percentage and stop loss.
        
        Args:
            symbol (str): Trading symbol
            stop_loss_pips (float): Stop loss in pips
            risk_amount (float): Optional fixed risk amount (overrides percentage)
            
        Returns:
            float: Position size in lots
            None: If calculation fails
        """
        if not self.connected:
            print("Not connected to MT5")
            return None
            
        try:
            account_info = self.get_account_info()
            if account_info is None:
                return None
                
            if risk_amount is None:
                risk_amount = account_info['balance'] * (self.risk_percentage / 100)
                
            symbol_info = mt5.symbol_info(symbol)
            if symbol_info is None:
                print(f"Failed to get symbol info for {symbol}, error code = {mt5.last_error()}")
                return None
                
            tick_value = symbol_info.trade_tick_value
            tick_size = symbol_info.trade_tick_size
            contract_size = symbol_info.trade_contract_size
            
            if tick_value <= 0 or tick_size <= 0 or contract_size <= 0:
                print(f"Invalid symbol parameters for {symbol}")
                return None
                
            pip_value = (tick_value / tick_size) * 0.0001 if 'JPY' not in symbol else (tick_value / tick_size) * 0.01
            position_size = (risk_amount / (stop_loss_pips * pip_value)) / contract_size
            
            return round(position_size, 2)
            
        except Exception as e:
            print(f"Error calculating position size: {e}")
            return None
    
    def validate_trade_request(self, request):
        """
        Validate trade request against risk parameters.
        
        Args:
            request (dict): Trade request dictionary
            
        Returns:
            bool: True if trade is within risk limits, False otherwise
        """
        if not self.connected:
            print("Not connected to MT5")
            return False
            
        try:
            account_info = self.get_account_info()
            if account_info is None:
                return False
                
            if 'action' not in request or 'symbol' not in request or 'volume' not in request:
                print("Invalid trade request: missing required fields")
                return False
                
            # Check if volume exceeds calculated position size
            if 'sl' in request and request['sl'] > 0:
                stop_loss_pips = abs(request['price'] - request['sl']) / mt5.symbol_info(request['symbol']).point
                max_position_size = self.calculate_position_size(request['symbol'], stop_loss_pips)
                
                if max_position_size is None:
                    return False
                    
                if request['volume'] > max_position_size:
                    print(f"Trade rejected: volume {request['volume']} exceeds max position size {max_position_size}")
                    return False
                    
            # Check margin requirements
            required_margin = mt5.order_calc_margin(
                request['action'],
                request['symbol'],
                request['volume'],
                request['price'] if 'price' in request else mt5.symbol_info_tick(request['symbol']).ask
            )
            
            if required_margin is None:
                print(f"Failed to calculate margin, error code = {mt5.last_error()}")
                return False
                
            if required_margin > account_info['free_margin']:
                print(f"Trade rejected: insufficient margin. Required: {required_margin}, Available: {account_info['free_margin']}")
                return False
                
            return True
            
        except Exception as e:
            print(f"Error validating trade request: {e}")
            return False
    
    def execute_trade(self, request):
        """
        Execute trade if it passes risk validation.
        
        Args:
            request (dict): Trade request dictionary
            
        Returns:
            bool: True if trade executed successfully, False otherwise
        """
        if not self.validate_trade_request(request):
            return False
            
        try:
            result = mt5.order_send(request)
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                print(f"Trade failed, retcode={result.retcode}, comment={result.comment}")
                return False
                
            print(f"Trade executed successfully, order={result.order}")
            return True
            
        except Exception as e:
            print(f"Error executing trade: {e}")
            return False
    
    def monitor_account(self, interval=60):
        """
        Continuously monitor account balance and margin levels.
        
        Args:
            interval (int): Monitoring interval in seconds (default: 60)
        """
        try:
            while True:
                account_info = self.get_account_info()
                if account_info:
                    print(f"[{datetime.now()}] Account Monitor - "
                          f"Balance: {account_info['balance']} {account_info['currency']}, "
                          f"Equity: {account_info['equity']}, "
                          f"Margin Level: {account_info['margin_level']}%")
                    
                    # Alert if margin level is below 100%
                    if account_info['margin_level'] is not None and account_info['margin_level'] < 100:
                        print(f"WARNING: Margin level below 100% ({account_info['margin_level']}%)")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("Monitoring stopped by user")
        except Exception as e:
            print(f"Monitoring error: {e}")

# Example usage
if __name__ == "__main__":
    risk_tool = RiskManagementTool(risk_percentage=1.0)
    
    if risk_tool.connect_to_mt5():
        try:
            # Example trade request
            symbol = "EURUSD"
            symbol_info = mt5.symbol_info(symbol)
            if symbol_info is None:
                print(f"Symbol {symbol} not found")
            else:
                price = mt5.symbol_info_tick(symbol).ask
                stop_loss = price - 50 * symbol_info.point
                
                trade_request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": symbol,
                    "volume": 0.1,
                    "type": mt5.ORDER_TYPE_BUY,
                    "price": price,
                    "sl": stop_loss,
                    "deviation": 10,
                    "magic": 123456,
                    "comment": "python
