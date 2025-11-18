"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorealm.vercel.app
Prompt: Generate code for integrating a component into an app using Gorealm's CLI. Ensure the code aligns with the features described on the Gorealm site.
Generated: DETERMINISTIC_1708fc2779c99632
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# First, ensure that the Gorealm CLI is installed on your system.
# You can install it using Homebrew on macOS:
# brew install gorealm

# Create a new Realm app using the Gorealm CLI
realm-cli create app my-realm-app --org your-org-id --region your-region

# Navigate into your new app's directory
cd my-realm-app

# Initialize the app with a new Realm component
realm-cli init

# Create a new component for your app
realm-cli generate component my-component --type realm --description "A simple component to manage data"

# Navigate to the component directory
cd components/my-component

# Create a new file to define the component logic
cat > index.js <<EOL
// Import necessary libraries
const Realm = require('realm');

// Define the data model
const CarSchema = {
    name: 'Car',
    properties: {
        make: 'string',
        model: 'string',
        miles: 'int',
    },
};

// Initialize a Realm with the defined schema
const realm = new Realm({schema: [CarSchema]});

// Function to add a new car to the database
function addCar(make, model, miles) {
    // Error handling for invalid parameters
    if (!make || !model || miles < 0) {
        throw new Error('Invalid car data');
    }

    // Write to realm within a write transaction
    realm.write(() => {
        realm.create('Car', {make, model, miles});
    });
}

// Function to retrieve all cars from the database
function getCars() {
    return realm.objects('Car');
}

// Export the functions for external use
module.exports = { addCar, getCars };
EOL

# Create a test file to ensure the component works correctly
cat > test.js <<EOL
const { addCar, getCars } = require('./index');

try {
    addCar('Toyota', 'Camry', 12000);
    addCar('Honda', 'Civic', 8000);
    
    // Retrieve and log all cars
    console.log(getCars());
} catch (error) {
    console.error('Error occurred:', error.message);
}
EOL

# Run the test to ensure everything is working
node test.js
```
