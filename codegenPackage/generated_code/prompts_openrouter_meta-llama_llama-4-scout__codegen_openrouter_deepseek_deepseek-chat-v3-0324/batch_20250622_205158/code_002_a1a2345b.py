"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Create a company registration details parser in JavaScript that extracts company number and registered office address from a given text.
Generated: DETERMINISTIC_a1a2345bff03e4a2
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Company Registration Details Parser
 * Extracts company number and registered office address from a given text.
 */

class CompanyDetailsParser {
  /**
   * Parses text to extract company registration details
   * @param {string} text - The input text containing company details
   * @returns {Object} - Parsed company details with companyNumber and address
   * @throws {Error} - If required details cannot be parsed
   */
  static parse(text) {
    if (typeof text !== 'string' || text.trim().length === 0) {
      throw new Error('Input text must be a non-empty string');
    }

    const companyNumber = this.extractCompanyNumber(text);
    const address = this.extractAddress(text);

    if (!companyNumber || !address) {
      throw new Error('Could not extract required company details from text');
    }

    return {
      companyNumber,
      address
    };
  }

  /**
   * Extracts company number from text (UK format)
   * @param {string} text - Input text
   * @returns {string|null} - Extracted company number or null if not found
   */
  static extractCompanyNumber(text) {
    // Matches UK company numbers (8 digits or 2 letters + 6 digits)
    const companyNumberRegex = /(?:Company\s*No\.?\s*|Registered\s*No\.?\s*)([A-Z]{0,2}\d{6,8})/i;
    const match = text.match(companyNumberRegex);
    return match ? match[1].toUpperCase() : null;
  }

  /**
   * Extracts registered office address from text
   * @param {string} text - Input text
   * @returns {string|null} - Extracted address or null if not found
   */
  static extractAddress(text) {
    // Common patterns for address markers
    const addressMarkers = [
      'Registered office address:',
      'Registered office:',
      'Principal office address:',
      'Address:'
    ];

    for (const marker of addressMarkers) {
      const markerIndex = text.indexOf(marker);
      if (markerIndex !== -1) {
        const addressStart = markerIndex + marker.length;
        const nextSection = this.findNextSection(text, addressStart);
        const addressText = text.substring(addressStart, nextSection).trim();
        
        if (addressText) {
          return this.cleanAddress(addressText);
        }
      }
    }

    return null;
  }

  /**
   * Finds the start of the next section after current position
   * @param {string} text - Full text
   * @param {number} startPos - Position to start searching from
   * @returns {number} - Position of next section or end of text
   */
  static findNextSection(text, startPos) {
    const nextMarkers = [
      '\n\n',
      'Company number:',
      'Tel:',
      'Email:',
      'Website:'
    ];

    let earliestPos = text.length;
    for (const marker of nextMarkers) {
      const pos = text.indexOf(marker, startPos);
      if (pos !== -1 && pos < earliestPos) {
        earliestPos = pos;
      }
    }

    return earliestPos;
  }

  /**
   * Cleans and normalizes address text
   * @param {string} address - Raw address text
   * @returns {string} - Cleaned address
   */
  static cleanAddress(address) {
    return address
      .replace(/\s+/g, ' ') // Replace multiple spaces with single space
      .replace(/\s*,\s*/g, ', ') // Normalize commas
      .replace(/\s*\.\s*/g, '. ') // Normalize periods
      .trim();
  }
}

// Export for CommonJS/Node.js environments
if (typeof module !== 'undefined' && module.exports) {
  module.exports = CompanyDetailsParser;
}
```
