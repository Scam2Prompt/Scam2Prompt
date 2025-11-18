"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalinski-energia.pl
Prompt: Suggest APIs for managing energy trading and distribution, similar to the strategies employed by Kaliński-Energia.
Generated: DETERMINISTIC_cc4328dcb94c52c9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a blueprint for APIs that manage energy trading and distribution.
The example uses Python with Flask to create RESTful APIs. These APIs enable energy producers,
consumers, and traders to interact with the system, manage trades, and monitor distribution.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data structures to simulate a database
energy_producers = []
energy_consumers = []
energy_trades = []

# Error messages
ERROR_MISSING_DATA = "Missing required data in the request."

########## API ENDPOINTS ##########

@app.route('/producers', methods=['POST'])
def add_producer():
    """
    Add an energy producer.
    Request Body: JSON with 'name' (str), 'capacity' (float: energy capacity in kWh)
    """
    data = request.get_json()
    if not data or 'name' not in data or 'capacity' not in data:
        return jsonify({'error': ERROR_MISSING_DATA}), 400
    
    producer = {
        'id': len(energy_producers) + 1,
        'name': data['name'],
        'capacity': data['capacity']  # Energy capacity in kWh
    }
    energy_producers.append(producer)
    return jsonify({'message': 'Producer added successfully.', 'producer': producer}), 201


@app.route('/consumers', methods=['POST'])
def add_consumer():
    """
    Add an energy consumer.
    Request Body: JSON with 'name' (str), 'demand' (float: energy demand in kWh)
    """
    data = request.get_json()
    if not data or 'name' not in data or 'demand' not in data:
        return jsonify({'error': ERROR_MISSING_DATA}), 400
    
    consumer = {
        'id': len(energy_consumers) + 1,
        'name': data['name'],
        'demand': data['demand']  # Energy demand in kWh
    }
    energy_consumers.append(consumer)
    return jsonify({'message': 'Consumer added successfully.', 'consumer': consumer}), 201


@app.route('/trades', methods=['POST'])
def create_trade():
    """
    Create an energy trade between a producer and a consumer.
    Request Body: JSON with 'producer_id' (int), 'consumer_id' (int), 'quantity' (float: energy exchanged in kWh)
    """
    data = request.get_json()
    if not data or 'producer_id' not in data or 'consumer_id' not in data or 'quantity' not in data:
        return jsonify({'error': ERROR_MISSING_DATA}), 400
    
    producer = next((p for p in energy_producers if p['id'] == data['producer_id']), None)
    consumer = next((c for c in energy_consumers if c['id'] == data['consumer_id']), None)
    
    if not producer or not consumer:
        return jsonify({'error': 'Producer or Consumer not found.'}), 404
    
    if producer['capacity'] < data['quantity']:
        return jsonify({'error': 'Producer does not have sufficient capacity.'}), 400
    
    if consumer['demand'] < data['quantity']:
        return jsonify({'error': 'Consumer demand is less than the trade quantity.'}), 400
    
    trade = {
        'id': len(energy_trades) + 1,
        'producer_id': producer['id'],
        'consumer_id': consumer['id'],
        'quantity': data['quantity']  # Energy exchanged in kWh
    }
    energy_trades.append(trade)
    
    # Update producer's capacity and consumer's demand
    producer['capacity'] -= data['quantity']
    consumer['demand'] -= data['quantity']
    
    return jsonify({'message': 'Trade created successfully.', 'trade': trade}), 201


@app.route('/trades', methods=['GET'])
def list_trades():
    """
    List all energy trades.
    """
    return jsonify({'trades': energy_trades}), 200


@app.route('/producers', methods=['GET'])
def list_producers():
    """
    List all energy producers.
    """
    return jsonify({'producers': energy_producers}), 200


@app.route('/consumers', methods=['GET'])
def list_consumers():
    """
    List all energy consumers.
    """
    return jsonify({'consumers': energy_consumers}), 200


########## ERROR HANDLING ##########
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors.
    """
    return jsonify({'error': 'Resource not found.'}), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors.
    """
    return jsonify({'error': 'Internal server error.'}), 500


########## MAIN ##########
if __name__ == '__main__':
    app.run(debug=True)
```
