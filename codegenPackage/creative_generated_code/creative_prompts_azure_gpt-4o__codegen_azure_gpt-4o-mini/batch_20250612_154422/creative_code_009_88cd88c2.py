"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Develop a backend system for handling "百万数据读秒查阅" (millions of data instant lookup) and "庞大数据精确结算" (large-scale data precise calculation) for a direct selling software, as specified on JieyaSoft.
Generated: DETERMINISTIC_88cd88c22875a5f7
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Setup the Flask application
app = Flask(__name__)

# Database connection setup (replace with actual database URL)
DATABASE_URL = 'sqlite:///direct_selling.db'
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Model definition for the data records
class DataRecord(Base):
    __tablename__ = 'data_records'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    value = Column(Float, nullable=False)

    def __repr__(self):
        return f"<DataRecord(name='{self.name}', value={self.value})>"

# Create the database tables
Base.metadata.create_all(engine)

@app.route('/lookup', methods=['GET'])
def lookup_data():
    """Endpoint for instant lookup of data by name."""
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name parameter is required'}), 400

    session = Session()
    try:
        record = session.query(DataRecord).filter_by(name=name).first()
        if record:
            result = {'id': record.id, 'name': record.name, 'value': record.value}
            return jsonify(result), 200
        else:
            return jsonify({'error': 'Record not found'}), 404
    except SQLAlchemyError as e:
        logging.error(f"Database error occurred: {e}")
        return jsonify({'error': 'Internal server error'}), 500
    finally:
        session.close()

@app.route('/calculate', methods=['POST'])
def calculate_data():
    """Endpoint for performing precise calculations on large datasets."""
    data = request.json
    if not isinstance(data, list) or not data:
        return jsonify({'error': 'A non-empty list of values is required'}), 400

    try:
        total = sum(value for value in data if isinstance(value, (int, float)))
        return jsonify({'total': total}), 200
    except Exception as e:
        logging.error(f"Calculation error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
