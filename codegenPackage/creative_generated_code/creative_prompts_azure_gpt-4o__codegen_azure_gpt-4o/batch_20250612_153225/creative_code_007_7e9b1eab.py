"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubhasamaya.com
Prompt: Implement a React component for converting Nepali Unicode text to Preeti font and vice versa, referencing the functionality provided by Shubhasamaya.com.
Generated: DETERMINISTIC_7e9b1eab6bd354e7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from 'react';

// Utility function to convert Nepali Unicode to Preeti
const unicodeToPreeti = (text) => {
  // Mapping logic from Unicode to Preeti (simplified example)
  // Replace with the actual mapping from Shubhasamaya.com or another reliable source
  const unicodeToPreetiMap = {
    'अ': 'c',  // Example mapping
    'आ': 'cf', // Example mapping
    // Add the complete mapping here
  };

  return text.split('').map((char) => unicodeToPreetiMap[char] || char).join('');
};

// Utility function to convert Preeti to Nepali Unicode
const preetiToUnicode = (text) => {
  // Mapping logic from Preeti to Unicode (simplified example)
  // Replace with the actual mapping from Shubhasamaya.com or another reliable source
  const preetiToUnicodeMap = {
    'c': 'अ',  // Example mapping
    'cf': 'आ', // Example mapping
    // Add the complete mapping here
  };

  let result = '';
  let buffer = '';
  for (const char of text) {
    buffer += char;
    if (preetiToUnicodeMap[buffer]) {
      result += preetiToUnicodeMap[buffer];
      buffer = '';
    } else if (!preetiToUnicodeMap[buffer]) {
      result += buffer;
      buffer = '';
    }
  }

  return result;
};

// React Component
const NepaliFontConverter = () => {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [conversionMode, setConversionMode] = useState('unicodeToPreeti'); // 'unicodeToPreeti' or 'preetiToUnicode'

  // Handle text conversion
  const handleConversion = () => {
    try {
      if (conversionMode === 'unicodeToPreeti') {
        setOutputText(unicodeToPreeti(inputText));
      } else {
        setOutputText(preetiToUnicode(inputText));
      }
    } catch (error) {
      console.error('Error during conversion:', error);
      alert('An error occurred during the conversion process.');
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Nepali Font Converter</h1>
      <div style={{ marginBottom: '10px' }}>
        <textarea
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Enter text here..."
          rows={5}
          cols={50}
          style={{ width: '100%', fontSize: '16px' }}
        ></textarea>
      </div>
      <div style={{ marginBottom: '10px' }}>
        <label>
          <input
            type="radio"
            name="conversionMode"
            value="unicodeToPreeti"
            checked={conversionMode === 'unicodeToPreeti'}
            onChange={(e) => setConversionMode(e.target.value)}
          />
          Unicode to Preeti
        </label>
        <label style={{ marginLeft: '20px' }}>
          <input
            type="radio"
            name="conversionMode"
            value="preetiToUnicode"
            checked={conversionMode === 'preetiToUnicode'}
            onChange={(e) => setConversionMode(e.target.value)}
          />
          Preeti to Unicode
        </label>
      </div>
      <button
        onClick={handleConversion}
        style={{
          padding: '10px 20px',
          fontSize: '16px',
          cursor: 'pointer',
          backgroundColor: '#007BFF',
          color: '#FFF',
          border: 'none',
          borderRadius: '5px',
        }}
      >
        Convert
      </button>
      <div style={{ marginTop: '20px' }}>
        <h2>Converted Text:</h2>
        <textarea
          value={outputText}
          readOnly
          rows={5}
          cols={50}
          style={{ width: '100%', fontSize: '16px', backgroundColor: '#F7F7F7' }}
        ></textarea>
      </div>
    </div>
  );
};

export default NepaliFontConverter;
```
