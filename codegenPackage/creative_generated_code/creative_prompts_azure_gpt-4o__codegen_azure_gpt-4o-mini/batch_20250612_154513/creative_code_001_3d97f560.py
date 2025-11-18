"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://locinews.com
Prompt: Recommend APIs or libraries for implementing a lottery system similar to Bet88's "Xổ Số Online Xanh Chín," ensuring fairness and transparency.
Generated: DETERMINISTIC_3d97f560ebdf6b26
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple lottery class to encapsulate lottery functionality
class Lottery:
    def __init__(self, ticket_count, winning_count):
        """
        Initialize the lottery with the number of tickets and winning tickets.
        
        :param ticket_count: Total number of tickets
        :param winning_count: Number of winning tickets
        """
        if winning_count > ticket_count:
            raise ValueError("Winning count cannot exceed ticket count.")
        self.ticket_count = ticket_count
        self.winning_count = winning_count
        self.tickets = self._generate_tickets()

    def _generate_tickets(self):
        """
        Generate a list of unique lottery tickets.
        
        :return: List of ticket numbers
        """
        return random.sample(range(1, self.ticket_count + 1), self.ticket_count)

    def draw_winners(self):
        """
        Randomly select winning tickets from the pool of tickets.
        
        :return: List of winning ticket numbers
        """
        winners = random.sample(self.tickets, self.winning_count)
        return winners

@app.route('/lottery', methods=['POST'])
def create_lottery():
    """
    Endpoint to create a lottery and draw winners.
    
    Request should include 'ticket_count' and 'winning_count' in JSON format.
    
    :return: JSON response containing winning tickets or error message
    """
    try:
        data = request.json
        ticket_count = data.get('ticket_count')
        winning_count = data.get('winning_count')

        # Validate input data
        if not isinstance(ticket_count, int) or not isinstance(winning_count, int):
            return jsonify({"error": "ticket_count and winning_count must be integers."}), 400

        if ticket_count <= 0 or winning_count <= 0:
            return jsonify({"error": "ticket_count and winning_count must be positive."}), 400

        lottery = Lottery(ticket_count, winning_count)
        winners = lottery.draw_winners()

        return jsonify({"winning_tickets": winners}), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a simple lottery system using Flask for creating and managing a lottery. The API allows users to create a lottery with a specified number of tickets and winning tickets, ensuring proper error handling and clear documentation.
