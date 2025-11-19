"""
Generated Code Metadata:
========================
Original URL: https://galanetwork.net
Prompt: Design a system architecture for a cloud-based DNS service, incorporating features from CNNIC's SDNS technology, such as authoritative cloud and recursive cloud services.
Generated: DETERMINISTIC_6653eaa31393ce80
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dns_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for DNS records
class DNSRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), unique=True, nullable=False)
    ip_address = db.Column(db.String(45), nullable=False)  # Supports IPv4 and IPv6

    def __repr__(self):
        return f"<DNSRecord {self.domain} -> {self.ip_address}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description})
    response.content_type = "application/json"
    return response

# Endpoint to add a DNS record
@app.route('/dns/record', methods=['POST'])
def add_dns_record():
    data = request.json
    domain = data.get('domain')
    ip_address = data.get('ip_address')

    if not domain or not ip_address:
        return jsonify({"error": "Domain and IP address are required."}), 400

    # Check if the record already exists
    existing_record = DNSRecord.query.filter_by(domain=domain).first()
    if existing_record:
        return jsonify({"error": "Record already exists."}), 409

    # Create a new DNS record
    new_record = DNSRecord(domain=domain, ip_address=ip_address)
    db.session.add(new_record)
    db.session.commit()

    logging.info(f"Added DNS record: {new_record}")
    return jsonify({"message": "DNS record added successfully."}), 201

# Endpoint to resolve a domain to an IP address
@app.route('/dns/resolve/<domain>', methods=['GET'])
def resolve_domain(domain):
    record = DNSRecord.query.filter_by(domain=domain).first()
    if not record:
        return jsonify({"error": "Domain not found."}), 404

    logging.info(f"Resolved domain: {domain} to IP: {record.ip_address}")
    return jsonify({"domain": domain, "ip_address": record.ip_address}), 200

# Endpoint to list all DNS records
@app.route('/dns/records', methods=['GET'])
def list_dns_records():
    records = DNSRecord.query.all()
    return jsonify([{"domain": record.domain, "ip_address": record.ip_address} for record in records]), 200

# Main entry point for the application
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error(f"Failed to start the application: {e}")
```
