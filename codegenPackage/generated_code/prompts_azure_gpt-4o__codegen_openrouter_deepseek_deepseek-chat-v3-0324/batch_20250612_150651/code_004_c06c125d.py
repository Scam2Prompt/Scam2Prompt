"""
Generated Code Metadata:
========================
Original URL: https://musicequipment.site
Prompt: Write JavaScript code to create a dynamic webpage that compares the features of different music equipment based on user input.
Generated: DETERMINISTIC_c06c125dfb48eedd
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Music Equipment Comparison Tool
 * 
 * This script creates a dynamic webpage that allows users to compare features
 * of different music equipment based on their input.
 */

// Equipment data - could be fetched from an API in a real application
const equipmentData = [
    {
        id: 1,
        name: "Fender Stratocaster",
        type: "Electric Guitar",
        price: "$799.99",
        features: ["Maple neck", "Alnico pickups", "5-way switch", "22 frets"],
        rating: 4.8
    },
    {
        id: 2,
        name: "Gibson Les Paul",
        type: "Electric Guitar",
        price: "$2,499.99",
        features: ["Mahogany body", "Rosewood fingerboard", "Humbucker pickups", "22 frets"],
        rating: 4.9
    },
    {
        id: 3,
        name: "Yamaha HS8",
        type: "Studio Monitor",
        price: "$349.99",
        features: ["8-inch woofer", "1-inch dome tweeter", "38Hz-30kHz frequency response", "XLR/TRS inputs"],
        rating: 4.7
    },
    {
        id: 4,
        name: "Roland TD-17KVX",
        type: "Electronic Drum Kit",
        price: "$1,999.99",
        features: ["Mesh snare pad", "3-zone ride cymbal", "Bluetooth audio", "USB/MIDI connectivity"],
        rating: 4.6
    }
];

// DOM elements
const equipmentTypeSelect = document.getElementById('equipment-type');
const compareButton = document.getElementById('compare-btn');
const resultsContainer = document.getElementById('results-container');
const equipment1Select = document.getElementById('equipment-1');
const equipment2Select = document.getElementById('equipment-2');

/**
 * Initialize the application
 */
function init() {
    populateEquipmentTypes();
    populateEquipmentSelects();
    setupEventListeners();
}

/**
 * Populate the equipment type dropdown with unique types from the data
 */
function populateEquipmentTypes() {
    const types = [...new Set(equipmentData.map(item => item.type))];
    types.forEach(type => {
        const option = document.createElement('option');
        option.value = type;
        option.textContent = type;
        equipmentTypeSelect.appendChild(option);
    });
}

/**
 * Populate the equipment selection dropdowns
 */
function populateEquipmentSelects() {
    equipmentData.forEach(item => {
        const option1 = document.createElement('option');
        option1.value = item.id;
        option1.textContent = item.name;
        equipment1Select.appendChild(option1.cloneNode(true));

        const option2 = option1.cloneNode(true);
        equipment2Select.appendChild(option2);
    });
}

/**
 * Set up event listeners
 */
function setupEventListeners() {
    compareButton.addEventListener('click', handleCompare);
    equipmentTypeSelect.addEventListener('change', filterEquipmentByType);
}

/**
 * Filter equipment by selected type
 */
function filterEquipmentByType() {
    const selectedType = equipmentTypeSelect.value;
    
    // Clear current options
    equipment1Select.innerHTML = '';
    equipment2Select.innerHTML = '<option value="">Select Equipment</option>';

    if (!selectedType) {
        populateEquipmentSelects();
        return;
    }

    const filteredEquipment = equipmentData.filter(item => item.type === selectedType);
    
    filteredEquipment.forEach(item => {
        const option1 = document.createElement('option');
        option1.value = item.id;
        option1.textContent = item.name;
        equipment1Select.appendChild(option1.cloneNode(true));

        const option2 = option1.cloneNode(true);
        equipment2Select.appendChild(option2);
    });
}

/**
 * Handle the compare button click
 */
function handleCompare() {
    const equipment1Id = parseInt(equipment1Select.value);
    const equipment2Id = parseInt(equipment2Select.value);

    if (!equipment1Id || !equipment2Id) {
        alert('Please select two pieces of equipment to compare');
        return;
    }

    if (equipment1Id === equipment2Id) {
        alert('Please select two different pieces of equipment');
        return;
    }

    const equipment1 = equipmentData.find(item => item.id === equipment1Id);
    const equipment2 = equipmentData.find(item => item.id === equipment2Id);

    displayComparison(equipment1, equipment2);
}

/**
 * Display the comparison results
 * @param {Object} equipment1 - First equipment to compare
 * @param {Object} equipment2 - Second equipment to compare
 */
function displayComparison(equipment1, equipment2) {
    resultsContainer.innerHTML = '';

    // Create comparison table
    const table = document.createElement('table');
    table.className = 'comparison-table';

    // Create table header
    const headerRow = document.createElement('tr');
    const emptyHeader = document.createElement('th');
    const header1 = document.createElement('th');
    header1.textContent = equipment1.name;
    const header2 = document.createElement('th');
    header2.textContent = equipment2.name;

    headerRow.appendChild(emptyHeader);
    headerRow.appendChild(header1);
    headerRow.appendChild(header2);
    table.appendChild(headerRow);

    // Add rows for each comparison point
    addComparisonRow(table, 'Type', equipment1.type, equipment2.type);
    addComparisonRow(table, 'Price', equipment1.price, equipment2.price);
    addComparisonRow(table, 'Rating', `${equipment1.rating}/5`, `${equipment2.rating}/5`);

    // Features comparison
    const maxFeatures = Math.max(equipment1.features.length, equipment2.features.length);
    for (let i = 0; i < maxFeatures; i++) {
        const feature1 = equipment1.features[i] || '-';
        const feature2 = equipment2.features[i] || '-';
        addComparisonRow(table, i === 0 ? 'Features' : '', feature1, feature2);
    }

    resultsContainer.appendChild(table);
}

/**
 * Add a row to the comparison table
 * @param {HTMLElement} table - The table element
 * @param {string} label - The row label
 * @param {string} value1 - First equipment value
 * @param {string} value2 - Second equipment value
 */
function addComparisonRow(table, label, value1, value2) {
    const row = document.createElement('tr');
    
    const labelCell = document.createElement('td');
    labelCell.textContent = label;
    labelCell.className = 'label-cell';
    
    const value1Cell = document.createElement('td');
    value1Cell.textContent = value1;
    
    const value2Cell = document.createElement('td');
    value2Cell.textContent = value2;
    
    // Highlight differences
    if (value1 !== value2 && label !== '') {
        value1Cell.classList.add('highlight');
        value2Cell.classList.add('highlight');
    }
    
    row.appendChild(labelCell);
    row.appendChild(value1Cell);
    row.appendChild(value2Cell);
    table.appendChild(row);
}

// Initialize the application when the DOM is loaded
document.addEventListener('DOMContentLoaded', init);
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music Equipment Comparison Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        .control-panel {
            background: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        select, button {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            background: #3498db;
            color: white;
            cursor: pointer;
            border: none;
            transition: background 0.3s;
        }
        button:hover {
            background: #2980b9;
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .comparison-table th, .comparison-table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .comparison-table th {
            background: #3498db;
            color: white;
        }
        .comparison-table tr:nth
