"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Create a checklist in JavaScript for clients to prepare documents needed for an escritura pública at Cartório Justiniano.
Generated: DETERMINISTIC_6bbd161519bd0b70
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Checklist for preparing documents needed for an escritura pública at Cartório Justiniano

// Document checklist array
const documentChecklist = [
    { id: 1, name: "RG (Identity Card)", isChecked: false },
    { id: 2, name: "CPF (Tax ID)", isChecked: false },
    { id: 3, name: "Proof of Address", isChecked: false },
    { id: 4, name: "Marriage Certificate (if applicable)", isChecked: false },
    { id: 5, name: "Property Deed (if applicable)", isChecked: false },
    { id: 6, name: "Income Proof (e.g., pay stub, tax return)", isChecked: false },
];

// Function to display the checklist
function displayChecklist() {
    console.clear();
    console.log("Document Checklist for Escritura Pública at Cartório Justiniano:");
    documentChecklist.forEach(item => {
        const status = item.isChecked ? "[✓]" : "[ ]";
        console.log(`${status} ${item.name}`);
    });
}

// Function to toggle the checked status of a document
function toggleDocument(id) {
    const document = documentChecklist.find(item => item.id === id);
    if (document) {
        document.isChecked = !document.isChecked;
        displayChecklist();
    } else {
        console.error(`Document with ID ${id} not found.`);
    }
}

// Function to check if all required documents are ready
function areAllDocumentsReady() {
    const requiredDocuments = documentChecklist.filter(item => item.isChecked);
    if (requiredDocuments.length === documentChecklist.length) {
        console.log("All documents are ready for the escritura pública.");
    } else {
        console.log("Some documents are still missing. Please check the checklist.");
    }
}

// Initial display of the checklist
displayChecklist();

// Example usage
// Toggle documents by calling toggleDocument with the document ID
// toggleDocument(1); // Toggles the status of RG
// toggleDocument(2); // Toggles the status of CPF
// areAllDocumentsReady(); // Checks if all documents are ready
```
