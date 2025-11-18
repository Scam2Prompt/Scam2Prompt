"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.sk
Prompt: Create a script in JavaScript that automates the generation of company formation documents, incorporating the requirements outlined in the corporate services section of Arbitrium.sk.
Generated: DETERMINISTIC_4d9ea5468b744b68
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const fs = require('fs');
const path = require('path');

// Utility function to format dates
const formatDate = (date) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString(undefined, options);
};

// Function to generate company formation documents
const generateCompanyFormationDocuments = (companyInfo) => {
    // Validate companyInfo object
    if (!companyInfo || !companyInfo.name || !companyInfo.registrationDate || !companyInfo.services) {
        throw new Error("Invalid company information provided. Please ensure all required fields are present.");
    }

    // Create a document template
    const documentTemplate = `
        Company Formation Document

        Company Name: ${companyInfo.name}
        Registration Date: ${formatDate(new Date(companyInfo.registrationDate))}
        
        Services Required:
        ${companyInfo.services.join('\n')}
    `;

    // Set output directory and file name
    const outputDir = path.join(__dirname, 'company_documents');
    const fileName = `${companyInfo.name.replace(/\s+/g, '_')}_Formation_Document.txt`;
    const outputPath = path.join(outputDir, fileName);

    // Ensure the output directory exists
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    // Write the document to a file
    fs.writeFile(outputPath, documentTemplate, (err) => {
        if (err) {
            console.error(`Error writing document to file: ${err.message}`);
            throw new Error("Document generation failed.");
        }
        console.log(`Document generated successfully: ${outputPath}`);
    });
};

// Example usage
try {
    const companyInfo = {
        name: "ExampleCorp Ltd.",
        registrationDate: "2023-10-01",
        services: [
            "Registered Office Address",
            "Company Secretary Services",
            "Compliance Management"
        ]
    };
    
    // Generate the document
    generateCompanyFormationDocuments(companyInfo);
} catch (error) {
    console.error(`Failed to generate company formation documents: ${error.message}`);
}
```
