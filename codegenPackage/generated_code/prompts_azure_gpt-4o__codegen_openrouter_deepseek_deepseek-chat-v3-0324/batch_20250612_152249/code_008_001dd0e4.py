"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Suggest an API for retrieving and visualizing patient feedback and testimonials from Dr. S. Nagendra Boopathy's website, focusing on treatments like Mitraclip and TAVR/TAVI.
Generated: DETERMINISTIC_001dd0e487f5bc01
Batch ID: 20250612_152249
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/chart.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Database setup
def init_db():
    conn = sqlite3.connect('patient_feedback.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            treatment_type TEXT NOT NULL,
            feedback_text TEXT NOT NULL,
            rating INTEGER CHECK (rating >= 1 AND rating <= 5),
            date_posted TEXT NOT NULL,
            approved BOOLEAN DEFAULT 0
        )
    ''')
    
    # Insert sample data if table is empty
    cursor.execute('SELECT COUNT(*) FROM feedback')
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ("John Doe", "Mitraclip", "Excellent treatment and care from Dr. Boopathy.", 5, "2023-05-15", 1),
            ("Jane Smith", "TAVR/TAVI", "Life-changing procedure with great results.", 4, "2023-06-20", 1),
            ("Robert Johnson", "Mitraclip", "Professional team and smooth experience.", 5, "2023-07-10", 1)
        ]
        cursor.executemany('''
            INSERT INTO feedback (patient_name, treatment_type, feedback_text, rating, date_posted, approved)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', sample_data)
    
    conn.commit()
    conn.close()

init_db()

# API Endpoints
@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    treatment_type = request.args.get('treatment_type')
    approved_only = request.args.get('approved_only', 'true').lower() == 'true'
    
    try:
        conn = sqlite3.connect('patient_feedback.db')
        cursor = conn.cursor()
        
        query = 'SELECT * FROM feedback'
        conditions = []
        params = []
        
        if treatment_type:
            conditions.append('treatment_type = ?')
            params.append(treatment_type)
        
        if approved_only:
            conditions.append('approved = 1')
        
        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)
        
        cursor.execute(query, params)
        feedback = cursor.fetchall()
        
        # Convert to list of dicts
        feedback_list = []
        for item in feedback:
            feedback_list.append({
                'id': item[0],
                'patient_name': item[1],
                'treatment_type': item[2],
                'feedback_text': item[3],
                'rating': item[4],
                'date_posted': item[5],
                'approved': bool(item[6])
            })
        
        return jsonify({'success': True, 'data': feedback_list})
    
    except sqlite3.Error as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    
    finally:
        conn.close()

@app.route('/api/feedback', methods=['POST'])
def add_feedback():
    data = request.get_json()
    
    required_fields = ['patient_name', 'treatment_type', 'feedback_text', 'rating']
    if not all(field in data for field in required_fields):
        return jsonify({'success': False, 'error': 'Missing required fields'}), 400
    
    try:
        rating = int(data['rating'])
        if rating < 1 or rating > 5:
            return jsonify({'success': False, 'error': 'Rating must be between 1 and 5'}), 400
        
        conn = sqlite3.connect('patient_feedback.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO feedback (patient_name, treatment_type, feedback_text, rating, date_posted)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            data['patient_name'],
            data['treatment_type'],
            data['feedback_text'],
            rating,
            datetime.now().strftime('%Y-%m-%d')
        ))
        
        conn.commit()
        return jsonify({'success': True, 'message': 'Feedback submitted for approval'})
    
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid rating format'}), 400
    except sqlite3.Error as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()

# Visualization Endpoint
@app.route('/feedback/visualization')
def visualization():
    return render_template('visualization.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/visualization.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Feedback Visualization</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .chart-container {
            margin: 30px 0;
        }
        .feedback-list {
            margin-top: 40px;
        }
        .feedback-item {
            border-bottom: 1px solid #eee;
            padding: 15px 0;
        }
        .treatment-filter {
            margin: 20px 0;
            text-align: center;
        }
        select {
            padding: 8px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Patient Feedback Analysis</h1>
        
        <div class="treatment-filter">
            <label for="treatment-select">Filter by Treatment:</label>
            <select id="treatment-select" onchange="loadData()">
                <option value="">All Treatments</option>
                <option value="Mitraclip">Mitraclip</option>
                <option value="TAVR/TAVI">TAVR/TAVI</option>
            </select>
        </div>
        
        <div class="chart-container">
            <canvas id="ratingChart"></canvas>
        </div>
        
        <div class="chart-container">
            <canvas id="feedbackTimeline"></canvas>
        </div>
        
        <div class="feedback-list">
            <h2>Recent Feedback</h2>
            <div id="feedback-items"></div>
        </div>
    </div>

    <script>
        let ratingChart;
        let timelineChart;
        
        function loadData(treatmentType = '') {
            const url = treatmentType 
                ? `/api/feedback?treatment_type=${treatmentType}` 
                : '/api/feedback';
            
            axios.get(url)
                .then(response => {
                    const feedbackData = response.data.data;
                    updateCharts(feedbackData);
                    renderFeedbackList(feedbackData);
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        }
        
        function updateCharts(data) {
            // Process data for rating distribution chart
            const ratingCounts = [0, 0, 0, 0, 0];
            data.forEach(item => {
                ratingCounts[item.rating - 1]++;
            });
            
            // Update or create rating chart
            const ratingCtx = document.getElementById('ratingChart').getContext('2d');
            if (ratingChart) {
                ratingChart.data.datasets[0].data = ratingCounts;
                ratingChart.update();
            } else {
                ratingChart = new Chart(ratingCtx, {
                    type: 'bar',
                    data: {
                        labels: ['1 Star', '2 Stars', '3 Stars', '4 Stars', '5 Stars'],
                        datasets: [{
                            label: 'Rating Distribution',
                            data: ratingCounts,
                            backgroundColor: 'rgba(54, 162, 235, 0.7)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: 'Number of Reviews'
                                }
                            },
                            x: {
                                title: {
                                    display: true,
                                    text: 'Rating'
                                }
                            }
                        }
                    }
                });
            }
            
            // Process data for timeline chart
            const monthlyData
