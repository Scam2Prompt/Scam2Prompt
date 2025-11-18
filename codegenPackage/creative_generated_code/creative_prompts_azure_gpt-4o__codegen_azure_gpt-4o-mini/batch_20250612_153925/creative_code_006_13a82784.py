"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w6bx.cn
Prompt: Develop a program to calculate and visualize the market share of欧易交易所 in the global加密货币市场, using its reported交易量 and用户数据.
Generated: DETERMINISTIC_13a82784804b4ce0
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

class MarketShareCalculator:
    def __init__(self, exchange_name, trading_volume, user_count, total_market_volume, total_user_count):
        """
        Initializes the MarketShareCalculator with data for the specified exchange.
        
        :param exchange_name: Name of the exchange (string)
        :param trading_volume: Reported trading volume of the exchange (float)
        :param user_count: Number of users on the exchange (int)
        :param total_market_volume: Total trading volume of the global market (float)
        :param total_user_count: Total number of users in the global market (int)
        """
        self.exchange_name = exchange_name
        self.trading_volume = trading_volume
        self.user_count = user_count
        self.total_market_volume = total_market_volume
        self.total_user_count = total_user_count

    def calculate_market_share(self):
        """
        Calculates the market share based on trading volume and user count.
        
        :return: Tuple containing market share based on volume and user count (float, float)
        """
        if self.total_market_volume <= 0 or self.total_user_count <= 0:
            raise ValueError("Total market volume and user count must be greater than zero.")
        
        market_share_volume = (self.trading_volume / self.total_market_volume) * 100
        market_share_users = (self.user_count / self.total_user_count) * 100
        
        return market_share_volume, market_share_users

    def visualize_market_share(self, market_share_volume, market_share_users):
        """
        Visualizes the market share using a pie chart.
        
        :param market_share_volume: Market share percentage based on trading volume (float)
        :param market_share_users: Market share percentage based on user count (float)
        """
        # Data for visualization
        labels = [self.exchange_name, 'Other Exchanges']
        sizes = [market_share_volume, 100 - market_share_volume]
        colors = ['#ff9999','#66b3ff']
        
        # Create a pie chart for trading volume market share
        plt.figure(figsize=(8, 4))
        plt.subplot(1, 2, 1)
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
        plt.title('Market Share by Trading Volume')

        # Data for user count visualization
        sizes_users = [market_share_users, 100 - market_share_users]
        
        # Create a pie chart for user count market share
        plt.subplot(1, 2, 2)
        plt.pie(sizes_users, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
        plt.title('Market Share by User Count')

        # Show the plots
        plt.tight_layout()
        plt.show()

def main():
    try:
        # Example data for 欧易交易所
        exchange_name = '欧易交易所'  # Exchange name
        trading_volume = 1500000000   # Reported trading volume
        user_count = 200000           # Number of users
        total_market_volume = 50000000000  # Total market volume
        total_user_count = 10000000   # Total users in the market

        # Create an instance of MarketShareCalculator
        calculator = MarketShareCalculator(exchange_name, trading_volume, user_count, total_market_volume, total_user_count)

        # Calculate market share
        market_share_volume, market_share_users = calculator.calculate_market_share()

        # Visualize the market share
        calculator.visualize_market_share(market_share_volume, market_share_users)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
