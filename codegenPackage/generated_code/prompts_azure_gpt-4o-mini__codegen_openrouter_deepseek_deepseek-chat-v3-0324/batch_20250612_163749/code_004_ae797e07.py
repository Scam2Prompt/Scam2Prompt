"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Design a user interface component that allows users to search for tires by width and rim size, inspired by the filtering options on the dcpneus blog.
Generated: DETERMINISTIC_ae797e077c134b5d
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Tire Search Component

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * TireSearch Component
 * Allows users to search for tires by width and rim size
 * 
 * @param {Object} props - Component props
 * @param {function} props.onSearch - Callback function when search is performed
 * @param {number} props.minWidth - Minimum tire width in mm
 * @param {number} props.maxWidth - Maximum tire width in mm
 * @param {number} props.minRimSize - Minimum rim size in inches
 * @param {number} props.maxRimSize - Maximum rim size in inches
 */
const TireSearch = ({ 
  onSearch, 
  minWidth = 100, 
  maxWidth = 400, 
  minRimSize = 12, 
  maxRimSize = 22 
}) => {
  const [width, setWidth] = useState(Math.floor((minWidth + maxWidth) / 2));
  const [rimSize, setRimSize] = useState(Math.floor((minRimSize + maxRimSize) / 2));
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Validate props on component mount
  useEffect(() => {
    if (minWidth >= maxWidth) {
      setError('Invalid width range: minWidth must be less than maxWidth');
    } else if (minRimSize >= maxRimSize) {
      setError('Invalid rim size range: minRimSize must be less than maxRimSize');
    }
  }, [minWidth, maxWidth, minRimSize, maxRimSize]);

  const handleSearch = async (e) => {
    e.preventDefault();
    
    if (error) return;
    
    try {
      setIsLoading(true);
      await onSearch({ width, rimSize });
    } catch (err) {
      setError('Failed to perform search. Please try again.');
      console.error('Search error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleWidthChange = (e) => {
    const value = parseInt(e.target.value);
    if (!isNaN(value) && value >= minWidth && value <= maxWidth) {
      setWidth(value);
    }
  };

  const handleRimSizeChange = (e) => {
    const value = parseInt(e.target.value);
    if (!isNaN(value) && value >= minRimSize && value <= maxRimSize) {
      setRimSize(value);
    }
  };

  return (
    <div className="tire-search-container">
      {error && (
        <div className="error-message" role="alert">
          {error}
        </div>
      )}
      
      <form onSubmit={handleSearch} className="tire-search-form">
        <div className="form-group">
          <label htmlFor="tire-width">Tire Width (mm):</label>
          <input
            id="tire-width"
            type="number"
            min={minWidth}
            max={maxWidth}
            value={width}
            onChange={handleWidthChange}
            className="form-control"
            aria-label="Tire width in millimeters"
          />
          <div className="range-info">
            Range: {minWidth}mm - {maxWidth}mm
          </div>
        </div>

        <div className="form-group">
          <label htmlFor="rim-size">Rim Size (inches):</label>
          <input
            id="rim-size"
            type="number"
            min={minRimSize}
            max={maxRimSize}
            value={rimSize}
            onChange={handleRimSizeChange}
            className="form-control"
            aria-label="Rim size in inches"
          />
          <div className="range-info">
            Range: {minRimSize}" - {maxRimSize}"
          </div>
        </div>

        <button 
          type="submit" 
          className="search-button"
          disabled={isLoading || error}
          aria-busy={isLoading}
        >
          {isLoading ? 'Searching...' : 'Search Tires'}
        </button>
      </form>
    </div>
  );
};

TireSearch.propTypes = {
  onSearch: PropTypes.func.isRequired,
  minWidth: PropTypes.number,
  maxWidth: PropTypes.number,
  minRimSize: PropTypes.number,
  maxRimSize: PropTypes.number,
};

export default TireSearch;
```

```css
/* TireSearch.css */
.tire-search-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #e1e1e1;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.error-message {
  color: #d32f2f;
  background-color: #fde8e8;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 15px;
  font-size: 14px;
}

.tire-search-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.form-group label {
  font-weight: 600;
  color: #333;
}

.form-control {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.form-control:focus {
  outline: none;
  border-color: #4a90e2;
  box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2);
}

.range-info {
  font-size: 12px;
  color: #666;
}

.search-button {
  padding: 10px 15px;
  background-color: #4a90e2;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.2s;
}

.search-button:hover {
  background-color: #3a7bc8;
}

.search-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
```
