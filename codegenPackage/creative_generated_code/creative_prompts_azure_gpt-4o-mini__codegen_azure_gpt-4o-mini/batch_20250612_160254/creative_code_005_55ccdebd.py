"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dataonmatrix.com
Prompt: What are the steps to modernize an existing web application using AngularJS and MongoDB, following the guidelines from Data on Matrix?
Generated: DETERMINISTIC_55ccdebda442bf13
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Step 1: Initialize the AngularJS application
angular.module('modernApp', [])
    .controller('MainController', ['$scope', '$http', function($scope, $http) {
        // Controller to manage application data and functions
        
        // Initialize data array to hold records from MongoDB
        $scope.records = [];

        // Function to fetch records from the server
        $scope.fetchRecords = function() {
            // Make an HTTP GET request to the API endpoint
            $http.get('/api/records')
                .then(function(response) {
                    // On success, assign the fetched records to the scope variable
                    $scope.records = response.data;
                })
                .catch(function(error) {
                    // Handle errors appropriately
                    console.error('Error fetching records:', error);
                    alert('Failed to load records. Please try again later.');
                });
        };

        // Function to add a new record
        $scope.addRecord = function(newRecord) {
            // Ensure newRecord is not empty
            if (!newRecord || !newRecord.name) {
                alert('Please provide a valid record.');
                return;
            }

            // Make an HTTP POST request to add the new record
            $http.post('/api/records', newRecord)
                .then(function(response) {
                    // On success, push the new record to the records array
                    $scope.records.push(response.data);
                    // Reset newRecord for further entries
                    $scope.newRecord = {};
                })
                .catch(function(error) {
                    // Handle errors appropriately
                    console.error('Error adding record:', error);
                    alert('Failed to add record. Please try again.');
                });
        };

        // Initialize by fetching existing records
        $scope.fetchRecords();
    }]);

// Step 2: Set up the server with Express.js and MongoDB
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the express application
const app = express();
app.use(bodyParser.json()); // Middleware to parse JSON request bodies

// Step 3: Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/modernApp', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => {
        console.error('MongoDB connection error:', err);
        process.exit(1); // Exit process if unable to connect to the database
    });

// Step 4: Define a Mongoose model for records
const RecordSchema = new mongoose.Schema({
    name: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

const Record = mongoose.model('Record', RecordSchema);

// Step 5: Set up API endpoints
app.get('/api/records', async (req, res) => {
    try {
        // Fetch all records from the database
        const records = await Record.find();
        res.json(records);
    } catch (error) {
        // Handle errors appropriately
        console.error('Error fetching records:', error);
        res.status(500).send('Internal Server Error');
    }
});

app.post('/api/records', async (req, res) => {
    try {
        // Create a new record using request data
        const newRecord = new Record(req.body);
        // Save the record to the database
        await newRecord.save();
        res.status(201).json(newRecord);
    } catch (error) {
        // Handle errors appropriately
        console.error('Error adding record:', error);
        res.status(400).send('Bad Request');
    }
});

// Step 6: Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
