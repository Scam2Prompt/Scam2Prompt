"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: Write a script in Node.js to automate the generation of renovation contracts, including fixed pricing per square meter and guarantees, as described on the ПАНАМ website.
Generated: DETERMINISTIC_141dfcf1e089f56b
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const fs = require('fs');
const path = require('path');
const { v4: uuidv4 } = require('uuid');
const PDFDocument = require('pdfkit');

/**
 * Renovation Contract Generator
 * Automates the creation of renovation contracts with fixed pricing per square meter and guarantees.
 */
class RenovationContractGenerator {
  /**
   * @param {Object} options - Configuration options
   * @param {number} options.pricePerSquareMeter - Price per square meter in local currency
   * @param {number} options.guaranteePeriod - Guarantee period in months
   * @param {string} options.outputDir - Directory to save generated contracts
   */
  constructor(options) {
    this.pricePerSquareMeter = options.pricePerSquareMeter || 0;
    this.guaranteePeriod = options.guaranteePeriod || 12;
    this.outputDir = options.outputDir || './contracts';
    
    this._validateOptions();
    this._ensureOutputDirectory();
  }

  /**
   * Validate constructor options
   * @private
   */
  _validateOptions() {
    if (typeof this.pricePerSquareMeter !== 'number' || this.pricePerSquareMeter <= 0) {
      throw new Error('Invalid price per square meter. Must be a positive number.');
    }

    if (typeof this.guaranteePeriod !== 'number' || this.guaranteePeriod <= 0) {
      throw new Error('Invalid guarantee period. Must be a positive number.');
    }

    if (typeof this.outputDir !== 'string' || this.outputDir.trim() === '') {
      throw new Error('Invalid output directory path.');
    }
  }

  /**
   * Ensure output directory exists
   * @private
   */
  _ensureOutputDirectory() {
    if (!fs.existsSync(this.outputDir)) {
      fs.mkdirSync(this.outputDir, { recursive: true });
    }
  }

  /**
   * Generate a renovation contract
   * @param {Object} clientData - Client information
   * @param {string} clientData.clientName - Full name of the client
   * @param {string} clientData.clientAddress - Client's address
   * @param {string} clientData.clientPhone - Client's phone number
   * @param {number} clientData.area - Area to be renovated in square meters
   * @param {Date} clientData.startDate - Project start date
   * @param {Date} clientData.endDate - Project end date
   * @returns {Promise<string>} Path to the generated contract file
   */
  async generateContract(clientData) {
    this._validateClientData(clientData);

    const totalPrice = this._calculateTotalPrice(clientData.area);
    const contractId = uuidv4();
    const fileName = `contract_${contractId}.pdf`;
    const filePath = path.join(this.outputDir, fileName);

    const doc = new PDFDocument();
    const stream = fs.createWriteStream(filePath);
    doc.pipe(stream);

    // Generate contract content
    this._generateHeader(doc, contractId);
    this._generatePartiesSection(doc, clientData);
    this._generateProjectDetails(doc, clientData, totalPrice);
    this._generateTermsAndConditions(doc);
    this._generateSignatures(doc);

    doc.end();

    return new Promise((resolve, reject) => {
      stream.on('finish', () => resolve(filePath));
      stream.on('error', reject);
    });
  }

  /**
   * Validate client data
   * @private
   */
  _validateClientData(clientData) {
    if (!clientData || typeof clientData !== 'object') {
      throw new Error('Invalid client data. Must be an object.');
    }

    const requiredFields = ['clientName', 'clientAddress', 'clientPhone', 'area', 'startDate', 'endDate'];
    for (const field of requiredFields) {
      if (!clientData[field]) {
        throw new Error(`Missing required field: ${field}`);
      }
    }

    if (typeof clientData.area !== 'number' || clientData.area <= 0) {
      throw new Error('Invalid area. Must be a positive number.');
    }

    if (!(clientData.startDate instanceof Date) || !(clientData.endDate instanceof Date)) {
      throw new Error('Invalid dates. Must be Date objects.');
    }

    if (clientData.endDate <= clientData.startDate) {
      throw new Error('End date must be after start date.');
    }
  }

  /**
   * Calculate total price
   * @private
   */
  _calculateTotalPrice(area) {
    return area * this.pricePerSquareMeter;
  }

  /**
   * Generate contract header
   * @private
   */
  _generateHeader(doc, contractId) {
    doc.fontSize(18).text('RENOVATION CONTRACT', { align: 'center' });
    doc.moveDown();
    doc.fontSize(12).text(`Contract ID: ${contractId}`, { align: 'center' });
    doc.moveDown(2);
  }

  /**
   * Generate parties section
   * @private
   */
  _generatePartiesSection(doc, clientData) {
    doc.fontSize(14).text('PARTIES', { underline: true });
    doc.moveDown();
    
    doc.fontSize(12).text('Contractor: ПАНАМ Renovations', { indent: 20 });
    doc.moveDown();
    
    doc.fontSize(12).text('Client:', { indent: 20 });
    doc.text(`Name: ${clientData.clientName}`, { indent: 40 });
    doc.text(`Address: ${clientData.clientAddress}`, { indent: 40 });
    doc.text(`Phone: ${clientData.clientPhone}`, { indent: 40 });
    doc.moveDown(2);
  }

  /**
   * Generate project details section
   * @private
   */
  _generateProjectDetails(doc, clientData, totalPrice) {
    doc.fontSize(14).text('PROJECT DETAILS', { underline: true });
    doc.moveDown();
    
    doc.fontSize(12).text(`Area to be renovated: ${clientData.area} square meters`, { indent: 20 });
    doc.text(`Price per square meter: ${this.pricePerSquareMeter}`, { indent: 20 });
    doc.text(`Total price: ${totalPrice}`, { indent: 20 });
    doc.moveDown();
    
    doc.text(`Project start date: ${clientData.startDate.toLocaleDateString()}`, { indent: 20 });
    doc.text(`Project end date: ${clientData.endDate.toLocaleDateString()}`, { indent: 20 });
    doc.moveDown();
    
    doc.text(`Guarantee period: ${this.guaranteePeriod} months`, { indent: 20 });
    doc.moveDown(2);
  }

  /**
   * Generate terms and conditions section
   * @private
   */
  _generateTermsAndConditions(doc) {
    doc.fontSize(14).text('TERMS AND CONDITIONS', { underline: true });
    doc.moveDown();
    
    const terms = [
      '1. The contractor agrees to perform all renovation work according to industry standards.',
      '2. The client agrees to pay the total amount upon completion of the work.',
      '3. Any changes to the scope of work must be agreed upon in writing by both parties.',
      '4. The contractor provides a guarantee for all work performed for the specified period.',
      '5. In case of defects during the guarantee period, the contractor will repair them at no additional cost.'
    ];
    
    terms.forEach(term => {
      doc.fontSize(12).text(term, { indent: 20 });
      doc.moveDown(0.5);
    });
    
    doc.moveDown(2);
  }

  /**
   * Generate signatures section
   * @private
   */
  _generateSignatures(doc) {
    doc.fontSize(14).text('SIGNATURES', { underline: true });
    doc.moveDown(2);
    
    doc.text('Contractor Representative:', { indent: 20 });
    doc.moveDown(2);
    doc.text('___________________________', { indent: 20 });
    doc.moveDown();
    
    doc.text('Client:', { indent: 20 });
    doc.moveDown(2);
    doc.text('___________________________', { indent: 20 });
    doc.moveDown();
    
    doc.text('Date:', { indent: 20 });
    doc.moveDown(2);
    doc.text('___________________________', { indent: 20 });
  }
}

module.exports = RenovationContractGenerator;
```
