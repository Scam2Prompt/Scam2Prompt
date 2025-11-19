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
// renovation-contract-generator.js

/**
 * Generates a renovation contract based on user input.
 * 
 * @author [Your Name]
 */

// Import required modules
const fs = require('fs');
const readline = require('readline');

// Define contract template
const contractTemplate = {
  clientName: '',
  projectAddress: '',
  totalArea: 0,
  pricePerSquareMeter: 0,
  totalPrice: 0,
  guarantees: [],
  warrantyPeriod: ''
};

// Define guarantee types
const guaranteeTypes = [
  'structural',
  'waterproofing',
  'electrical',
  'plumbing'
];

// Function to get user input
function getUserInput() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  return new Promise((resolve, reject) => {
    rl.question('Enter client name: ', (clientName) => {
      rl.question('Enter project address: ', (projectAddress) => {
        rl.question('Enter total area (in square meters): ', (totalArea) => {
          rl.question('Enter price per square meter: ', (pricePerSquareMeter) => {
            rl.question('Enter warranty period: ', (warrantyPeriod) => {
              const guarantees = [];
              console.log('Select guarantee types:');
              guaranteeTypes.forEach((type, index) => {
                console.log(`${index + 1}. ${type}`);
              });
              rl.question('Enter guarantee type numbers (comma-separated): ', (guaranteeTypeNumbers) => {
                const numbers = guaranteeTypeNumbers.split(',').map(Number);
                numbers.forEach((number) => {
                  if (number > 0 && number <= guaranteeTypes.length) {
                    guarantees.push(guaranteeTypes[number - 1]);
                  }
                });
                rl.close();
                resolve({
                  clientName,
                  projectAddress,
                  totalArea: parseFloat(totalArea),
                  pricePerSquareMeter: parseFloat(pricePerSquareMeter),
                  guarantees,
                  warrantyPeriod
                });
              });
            });
          });
        });
      });
    });
  });
}

// Function to generate contract
function generateContract(data) {
  const contract = { ...contractTemplate, ...data };
  contract.totalPrice = contract.totalArea * contract.pricePerSquareMeter;
  return contract;
}

// Function to save contract to file
function saveContractToFile(contract, filename) {
  try {
    const contractJson = JSON.stringify(contract, null, 2);
    fs.writeFileSync(filename, contractJson);
    console.log(`Contract saved to ${filename}`);
  } catch (error) {
    console.error(`Error saving contract to file: ${error.message}`);
  }
}

// Main function
async function main() {
  try {
    const userInput = await getUserInput();
    const contract = generateContract(userInput);
    console.log('Generated Contract:');
    console.log(contract);
    saveContractToFile(contract, 'renovation_contract.json');
  } catch (error) {
    console.error(`Error generating contract: ${error.message}`);
  }
}

// Run main function
main();
```
