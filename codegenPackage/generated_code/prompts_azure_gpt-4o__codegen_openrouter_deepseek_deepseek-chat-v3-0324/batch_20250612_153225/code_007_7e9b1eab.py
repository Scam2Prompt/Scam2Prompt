"""
Generated Code Metadata:
========================
Original URL: https://shubhasamaya.com
Prompt: Implement a React component for converting Nepali Unicode text to Preeti font and vice versa, referencing the functionality provided by Shubhasamaya.com.
Generated: DETERMINISTIC_7e9b1eab6bd354e7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';

// Mapping for Unicode to Preeti conversion
const unicodeToPreeti = {
  'ा': 'ो', 'ि': 'ि', 'ी': 'ी', 'ु': 'ु', 'ू': 'ू', 'े': 'े', 'ै': 'ै', 'ो': 'ा', 'ौ': 'ौ',
  'क': 'र्', 'ख': 'त्', 'ग': 'य्', 'घ': 'ल्', 'ङ': 'उ', 'च': 'ब्', 'छ': 'क्', 'ज': 'प्',
  'झ': 'च्', 'ञ': 'द्', 'ट': 'ह्', 'ठ': 'ग्', 'ड': 'न्', 'ढ': 'ज्', 'ण': 'व्', 'त': 'स्',
  'थ': 'म्', 'द': 'थ्', 'ध': 'ध्', 'न': 'श्', 'प': 'हृ', 'फ': 'ष्', 'ब': 'क्ष्', 'भ': 'त्र्',
  'म': 'ज्ञ्', 'य': 'घ्', 'र': 'ठ्', 'ल': 'ड्', 'व': 'ढ्', 'श': 'ण्', 'ष': 'छ्', 'स': 'ट्',
  'ह': 'भ्', 'अ': 'अ', 'आ': 'आ', 'इ': 'इ', 'ई': 'ई', 'उ': 'उ', 'ऊ': 'ऊ', 'ए': 'ए', 'ऐ': 'ऐ',
  'ओ': 'ओ', 'औ': 'औ', 'ं': 'ं', 'ः': 'ः', '्': '्', 'ँ': 'ँ', '०': '०', '१': '१', '२': '२',
  '३': '३', '४': '४', '५': '५', '६': '६', '७': '७', '८': '८', '९': '९', '।': '।', '॥': '॥',
  ' ': ' ', '\n': '\n'
};

// Mapping for Preeti to Unicode conversion
const preetiToUnicode = Object.fromEntries(
  Object.entries(unicodeToPreeti).map(([key, value]) => [value, key])
);

const NepaliFontConverter = () => {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [conversionType, setConversionType] = useState('unicodeToPreeti');

  const convertText = () => {
    try {
      let result = '';
      const mapping = conversionType === 'unicodeToPreeti' ? unicodeToPreeti : preetiToUnicode;
      
      for (let i = 0; i < inputText.length; i++) {
        const char = inputText[i];
        const nextChar = inputText[i + 1];
        
        // Handle combined characters (like क + ् + ष = क्ष)
        if (nextChar === '्' && i + 1 < inputText.length) {
          const combinedChar = char + nextChar + inputText[i + 2];
          if (mapping[combinedChar]) {
            result += mapping[combinedChar];
            i += 2;
            continue;
          }
        }
        
        result += mapping[char] || char;
      }
      
      setOutputText(result);
    } catch (error) {
      console.error('Conversion error:', error);
      setOutputText('Error occurred during conversion');
    }
  };

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleConversionTypeChange = (e) => {
    setConversionType(e.target.value);
  };

  const handleClear = () => {
    setInputText('');
    setOutputText('');
  };

  return (
    <div className="font-converter-container">
      <h2>Nepali Font Converter</h2>
      
      <div className="conversion-options">
        <label>
          <input
            type="radio"
            value="unicodeToPreeti"
            checked={conversionType === 'unicodeToPreeti'}
            onChange={handleConversionTypeChange}
          />
          Unicode to Preeti
        </label>
        
        <label>
          <input
            type="radio"
            value="preetiToUnicode"
            checked={conversionType === 'preetiToUnicode'}
            onChange={handleConversionTypeChange}
          />
          Preeti to Unicode
        </label>
      </div>
      
      <div className="text-areas">
        <textarea
          value={inputText}
          onChange={handleInputChange}
          placeholder={`Enter ${conversionType === 'unicodeToPreeti' ? 'Unicode' : 'Preeti'} text here`}
          rows={10}
        />
        
        <textarea
          value={outputText}
          readOnly
          placeholder="Converted text will appear here"
          rows={10}
        />
      </div>
      
      <div className="buttons">
        <button onClick={convertText}>Convert</button>
        <button onClick={handleClear}>Clear</button>
      </div>
      
      <style jsx>{`
        .font-converter-container {
          max-width: 800px;
          margin: 0 auto;
          padding: 20px;
          font-family: Arial, sans-serif;
        }
        
        h2 {
          text-align: center;
          color: #333;
        }
        
        .conversion-options {
          margin: 20px 0;
          display: flex;
          justify-content: center;
          gap: 20px;
        }
        
        .text-areas {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 20px;
          margin-bottom: 20px;
        }
        
        textarea {
          width: 100%;
          padding: 10px;
          border: 1px solid #ddd;
          border-radius: 4px;
          resize: vertical;
        }
        
        .buttons {
          display: flex;
          justify-content: center;
          gap: 10px;
        }
        
        button {
          padding: 10px 20px;
          background-color: #4CAF50;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-size: 16px;
        }
        
        button:hover {
          background-color: #45a049;
        }
      `}</style>
    </div>
  );
};

export default NepaliFontConverter;
```
