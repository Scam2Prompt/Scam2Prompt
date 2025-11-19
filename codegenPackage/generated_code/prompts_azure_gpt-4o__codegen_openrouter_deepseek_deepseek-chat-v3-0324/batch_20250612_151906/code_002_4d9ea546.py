"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Create a script in JavaScript that automates the generation of company formation documents, incorporating the requirements outlined in the corporate services section of Arbitrium.sk.
Generated: DETERMINISTIC_4d9ea5468b744b68
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Company Formation Document Generator
 * Automates the generation of company formation documents based on Arbitrium.sk requirements
 */

const fs = require('fs');
const path = require('path');
const { PDFDocument, rgb } = require('pdf-lib');
const { v4: uuidv4 } = require('uuid');

// Document templates and configurations
const DOCUMENT_TEMPLATES = {
  ARTICLES_OF_ASSOCIATION: 'templates/articles_of_association.pdf',
  FOUNDATION_DEED: 'templates/foundation_deed.pdf',
  REGISTRATION_APPLICATION: 'templates/registration_application.pdf'
};

const COMPANY_TYPES = {
  SRO: 's.r.o.',
  AS: 'a.s.',
  KS: 'k.s.',
  VOS: 'v.o.s.'
};

class CompanyFormationGenerator {
  /**
   * Initialize the generator with output directory
   * @param {string} outputDir - Directory to save generated documents
   */
  constructor(outputDir = './output') {
    this.outputDir = outputDir;
    this.ensureOutputDirectory();
  }

  /**
   * Ensure output directory exists
   */
  ensureOutputDirectory() {
    if (!fs.existsSync(this.outputDir)) {
      fs.mkdirSync(this.outputDir, { recursive: true });
    }
  }

  /**
   * Generate all required documents for company formation
   * @param {Object} companyData - Company information
   * @returns {Promise<Object>} Generated document paths
   */
  async generateDocuments(companyData) {
    try {
      this.validateCompanyData(companyData);

      const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
      const companyId = `${companyData.name.toLowerCase().replace(/\s+/g, '-')}-${timestamp}`;
      const outputPaths = {};

      // Generate each document
      outputPaths.articlesOfAssociation = await this.generateArticlesOfAssociation(companyData, companyId);
      outputPaths.foundationDeed = await this.generateFoundationDeed(companyData, companyId);
      outputPaths.registrationApplication = await this.generateRegistrationApplication(companyData, companyId);

      return outputPaths;
    } catch (error) {
      console.error('Error generating documents:', error);
      throw error;
    }
  }

  /**
   * Validate company data before processing
   * @param {Object} companyData - Company information to validate
   */
  validateCompanyData(companyData) {
    const requiredFields = ['name', 'type', 'address', 'capital', 'founders'];
    const missingFields = requiredFields.filter(field => !companyData[field]);

    if (missingFields.length > 0) {
      throw new Error(`Missing required fields: ${missingFields.join(', ')}`);
    }

    if (!COMPANY_TYPES[companyData.type]) {
      throw new Error(`Invalid company type: ${companyData.type}`);
    }

    if (typeof companyData.capital !== 'number' || companyData.capital <= 0) {
      throw new Error('Company capital must be a positive number');
    }

    if (!Array.isArray(companyData.founders) || companyData.founders.length === 0) {
      throw new Error('At least one founder must be specified');
    }
  }

  /**
   * Generate Articles of Association document
   * @param {Object} companyData - Company information
   * @param {string} companyId - Unique identifier for the company
   * @returns {Promise<string>} Path to generated document
   */
  async generateArticlesOfAssociation(companyData, companyId) {
    const templatePath = DOCUMENT_TEMPLATES.ARTICLES_OF_ASSOCIATION;
    const outputPath = path.join(this.outputDir, `articles_of_association_${companyId}.pdf`);

    const pdfDoc = await PDFDocument.load(fs.readFileSync(templatePath));
    const form = pdfDoc.getForm();

    // Fill form fields
    form.getTextField('companyName').setText(companyData.name);
    form.getTextField('companyType').setText(COMPANY_TYPES[companyData.type]);
    form.getTextField('registeredAddress').setText(companyData.address);
    form.getTextField('capitalAmount').setText(companyData.capital.toString());
    form.getTextField('businessPurpose').setText(companyData.businessPurpose || 'General commercial activities');

    // Add founders
    companyData.founders.forEach((founder, index) => {
      if (index < 5) { // Template supports up to 5 founders
        form.getTextField(`founderName${index + 1}`).setText(founder.name);
        form.getTextField(`founderAddress${index + 1}`).setText(founder.address);
        form.getTextField(`founderShare${index + 1}`).setText(founder.share || '100%');
      }
    });

    // Save the filled PDF
    const pdfBytes = await pdfDoc.save();
    fs.writeFileSync(outputPath, pdfBytes);

    return outputPath;
  }

  /**
   * Generate Foundation Deed document
   * @param {Object} companyData - Company information
   * @param {string} companyId - Unique identifier for the company
   * @returns {Promise<string>} Path to generated document
   */
  async generateFoundationDeed(companyData, companyId) {
    const templatePath = DOCUMENT_TEMPLATES.FOUNDATION_DEED;
    const outputPath = path.join(this.outputDir, `foundation_deed_${companyId}.pdf`);

    const pdfDoc = await PDFDocument.load(fs.readFileSync(templatePath));
    const form = pdfDoc.getForm();

    // Fill form fields
    form.getTextField('companyName').setText(companyData.name);
    form.getTextField('companyType').setText(COMPANY_TYPES[companyData.type]);
    form.getTextField('registeredAddress').setText(companyData.address);
    form.getTextField('capitalAmount').setText(companyData.capital.toString());

    // Add notary information
    form.getTextField('notaryName').setText(companyData.notary?.name || 'Notary Public');
    form.getTextField('notaryLocation').setText(companyData.notary?.location || 'Bratislava');

    // Save the filled PDF
    const pdfBytes = await pdfDoc.save();
    fs.writeFileSync(outputPath, pdfBytes);

    return outputPath;
  }

  /**
   * Generate Registration Application document
   * @param {Object} companyData - Company information
   * @param {string} companyId - Unique identifier for the company
   * @returns {Promise<string>} Path to generated document
   */
  async generateRegistrationApplication(companyData, companyId) {
    const templatePath = DOCUMENT_TEMPLATES.REGISTRATION_APPLICATION;
    const outputPath = path.join(this.outputDir, `registration_application_${companyId}.pdf`);

    const pdfDoc = await PDFDocument.load(fs.readFileSync(templatePath));
    const form = pdfDoc.getForm();

    // Fill form fields
    form.getTextField('companyName').setText(companyData.name);
    form.getTextField('companyType').setText(COMPANY_TYPES[companyData.type]);
    form.getTextField('registeredAddress').setText(companyData.address);
    form.getTextField('capitalAmount').setText(companyData.capital.toString());
    form.getTextField('businessPurpose').setText(companyData.businessPurpose || 'General commercial activities');

    // Add statutory body members
    if (companyData.statutoryBody && companyData.statutoryBody.length > 0) {
      companyData.statutoryBody.forEach((member, index) => {
        if (index < 3) { // Template supports up to 3 members
          form.getTextField(`statutoryName${index + 1}`).setText(member.name);
          form.getTextField(`statutoryAddress${index + 1}`).setText(member.address);
          form.getTextField(`statutoryPosition${index + 1}`).setText(member.position || 'Director');
        }
      });
    }

    // Save the filled PDF
    const pdfBytes = await pdfDoc.save();
    fs.writeFileSync(outputPath, pdfBytes);

    return outputPath;
  }
}

// Example usage
/*
const generator = new CompanyFormationGenerator();

const companyData = {
  name: 'Example Company',
  type: 'SRO',
  address: 'Example Street 123, Bratislava',
  capital: 5000,
  businessPurpose: 'Software development and consulting',
  founders: [
    { name: 'John Doe', address: 'Main Street 1, Bratislava', share: '50%' },
    { name: 'Jane Smith', address: 'Second Street 2, Bratislava', share: '50%' }
  ],
  statutoryBody: [
    { name: 'John Doe', address: 'Main Street 1, Bratislava', position: 'CEO' }
  ],
  notary: {
    name: 'Dr. Notary',
    location: 'Bratislava'
  }
};

generator.generateDocuments(companyData)
  .then(docs => console.log('Generated documents:', docs))
  .catch(err => console.error('Error:',
