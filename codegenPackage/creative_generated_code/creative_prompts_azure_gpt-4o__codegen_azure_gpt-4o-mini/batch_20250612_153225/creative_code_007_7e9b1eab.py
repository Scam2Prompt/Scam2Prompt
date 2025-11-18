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

```javascript
import React, { useState } from 'react';

// Utility functions to convert between Nepali Unicode and Preeti font
const unicodeToPreeti = (unicodeText) => {
    // Placeholder for actual conversion logic from Unicode to Preeti
    // This should implement the conversion algorithm or call an API if necessary
    return unicodeText; // Replace this with actual conversion
};

const preetiToUnicode = (preetiText) => {
    // Placeholder for actual conversion logic from Preeti to Unicode
    // This should implement the conversion algorithm or call an API if necessary
    return preetiText; // Replace this with actual conversion
};

// Main component for the converter
const NepaliTextConverter = () => {
    const [inputText, setInputText] = useState('');
    const [convertedText, setConvertedText] = useState('');
    const [conversionType, setConversionType] = useState('unicodeToPreeti');

    // Handle input changes
    const handleInputChange = (event) => {
        setInputText(event.target.value);
    };

    // Handle conversion type change
    const handleConversionTypeChange = (event) => {
        setConversionType(event.target.value);
        setConvertedText(''); // Clear converted text on conversion type change
    };

    // Perform the conversion
    const handleConvert = () => {
        try {
            const result = conversionType === 'unicodeToPreeti'
                ? unicodeToPreeti(inputText)
                : preetiToUnicode(inputText);
            setConvertedText(result);
        } catch (error) {
            console.error("Conversion error:", error);
            setConvertedText('Error in conversion.'); // Notify user of error
        }
    };

    return (
        <div>
            <h1>Nepali Text Converter</h1>
            <div>
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
            <textarea 
                placeholder="Enter text here..."
                value={inputText}
                onChange={handleInputChange}
                rows={4}
                cols={50}
            />
            <button onClick={handleConvert}>Convert</button>
            <h2>Converted Text:</h2>
            <textarea 
                value={convertedText}
                readOnly
                rows={4}
                cols={50}
            />
        </div>
    );
};

export default NepaliTextConverter;
```
