"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: "Implement a filtering system in React for an automotive parts website, allowing users to filter by tire size, vehicle type, and service type."
Generated: DETERMINISTIC_d5437c1f49774c2d
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';

// Sample data for automotive parts
const partsData = [
  { id: 1, name: 'All-Season Tire', size: '205/55R16', vehicleType: 'Sedan', serviceType: 'Installation' },
  { id: 2, name: 'Off-Road Tire', size: '265/70R17', vehicleType: 'SUV', serviceType: 'Installation' },
  { id: 3, name: 'Performance Tire', size: '225/40R18', vehicleType: 'Coupe', serviceType: 'Balancing' },
  { id: 4, name: 'Winter Tire', size: '195/65R15', vehicleType: 'Sedan', serviceType: 'Installation' },
  // Add more parts as needed
];

// Main component for the filtering system
const FilterablePartsList = () => {
  const [sizeFilter, setSizeFilter] = useState('');
  const [vehicleTypeFilter, setVehicleTypeFilter] = useState('');
  const [serviceTypeFilter, setServiceTypeFilter] = useState('');

  // Function to handle filter changes
  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    switch (name) {
      case 'size':
        setSizeFilter(value);
        break;
      case 'vehicleType':
        setVehicleTypeFilter(value);
        break;
      case 'serviceType':
        setServiceTypeFilter(value);
        break;
      default:
        break;
    }
  };

  // Function to filter parts based on selected criteria
  const filteredParts = partsData.filter(part => {
    return (
      (sizeFilter ? part.size.includes(sizeFilter) : true) &&
      (vehicleTypeFilter ? part.vehicleType === vehicleTypeFilter : true) &&
      (serviceTypeFilter ? part.serviceType === serviceTypeFilter : true)
    );
  });

  return (
    <div>
      <h1>Automotive Parts Filter</h1>
      
      {/* Filter Inputs */}
      <div>
        <label>
          Tire Size:
          <input
            type="text"
            name="size"
            value={sizeFilter}
            onChange={handleFilterChange}
            placeholder="e.g. 205/55R16"
          />
        </label>
        
        <label>
          Vehicle Type:
          <select
            name="vehicleType"
            value={vehicleTypeFilter}
            onChange={handleFilterChange}
          >
            <option value="">All</option>
            <option value="Sedan">Sedan</option>
            <option value="SUV">SUV</option>
            <option value="Coupe">Coupe</option>
          </select>
        </label>
        
        <label>
          Service Type:
          <select
            name="serviceType"
            value={serviceTypeFilter}
            onChange={handleFilterChange}
          >
            <option value="">All</option>
            <option value="Installation">Installation</option>
            <option value="Balancing">Balancing</option>
          </select>
        </label>
      </div>

      {/* Displaying filtered parts */}
      <h2>Available Parts</h2>
      <ul>
        {filteredParts.length > 0 ? (
          filteredParts.map(part => (
            <li key={part.id}>
              {part.name} - {part.size} - {part.vehicleType} - {part.serviceType}
            </li>
          ))
        ) : (
          <li>No parts found matching the selected filters.</li>
        )}
      </ul>
    </div>
  );
};

export default FilterablePartsList;
```
