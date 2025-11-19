"""
Generated Code Metadata:
========================
Original URL: https://don.co.ke
Prompt: "Compare and contrast The Don's trading bots, such as Digit Match Bot and Digit Under-3 Bot, in terms of their performance and risk management on Deriv."
Generated: DETERMINISTIC_773cfbab233dcb8f
Batch ID: 20250622_212307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class TradingBot:
    """
    Base class for trading bots. Provides common functionality and structure.
    """
    def __init__(self, name):
        self.name = name
        self.total_trades = 0
        self.wins = 0
        self.losses = 0

    def trade(self):
        """
        Simulates a trade. Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the trade method.")

    def calculate_performance(self):
        """
        Calculates the win rate and loss rate of the bot.
        """
        if self.total_trades == 0:
            return {"win_rate": 0, "loss_rate": 0}
        win_rate = (self.wins / self.total_trades) * 100
        loss_rate = (self.losses / self.total_trades) * 100
        return {"win_rate": win_rate, "loss_rate": loss_rate}

    def __str__(self):
        """
        Returns a string representation of the bot's performance.
        """
        performance = self.calculate_performance()
        return (f"Bot Name: {self.name}\n"
                f"Total Trades: {self.total_trades}\n"
                f"Wins: {self.wins}\n"
                f"Losses: {self.losses}\n"
                f"Win Rate: {performance['win_rate']:.2f}%\n"
                f"Loss Rate: {performance['loss_rate']:.2f}%\n")


class DigitMatchBot(TradingBot):
    """
    A trading bot that wins if the last digit of a random number matches a target digit.
    """
    def __init__(self, target_digit):
        super().__init__("Digit Match Bot")
        self.target_digit = target_digit

    def trade(self):
        """
        Simulates a trade for the Digit Match Bot.
        """
        try:
            random_number = random.randint(0, 9)
            self.total_trades += 1
            if random_number == self.target_digit:
                self.wins += 1
            else:
                self.losses += 1
        except Exception as e:
            print(f"Error during trade: {e}")


class DigitUnder3Bot(TradingBot):
    """
    A trading bot that wins if the last digit of a random number is less than 3.
    """
    def __init__(self):
        super().__init__("Digit Under-3 Bot")

    def trade(self):
        """
        Simulates a trade for the Digit Under-3 Bot.
        """
        try:
            random_number = random.randint(0, 9)
            self.total_trades += 1
            if random_number < 3:
                self.wins += 1
            else:
                self.losses += 1
        except Exception as e:
            print(f"Error during trade: {e}")


def compare_bots(bot1, bot2, num_trades=100):
    """
    Compares the performance of two trading bots over a specified number of trades.

    Args:
        bot1 (TradingBot): The first trading bot.
        bot2 (TradingBot): The second trading bot.
        num_trades (int): The number of trades to simulate for each bot.

    Returns:
        None
    """
    try:
        # Simulate trades for bot1
        for _ in range(num_trades):
            bot1.trade()

        # Simulate trades for bot2
        for _ in range(num_trades):
            bot2.trade()

        # Print performance comparison
        print("Performance Comparison:")
        print(bot1)
        print(bot2)
    except Exception as e:
        print(f"Error during bot comparison: {e}")


if __name__ == "__main__":
    # Instantiate bots
    digit_match_bot = DigitMatchBot(target_digit=5)
    digit_under_3_bot = DigitUnder3Bot()

    # Compare bots
    compare_bots(digit_match_bot, digit_under_3_bot, num_trades=100)
```
