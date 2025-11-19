"""
Generated Code Metadata:
========================
Original URL: https://topwcftutorials.sharepointfordummies.net
Prompt: Generate code for consuming a WCF REST service using jQuery, as described in the "Consuming REST Service using jQuery" tutorial on the website.
Generated: DETERMINISTIC_1ce1f1653f5ec32b
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/RestServiceImpl.svc/GetEmployees": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// rest-client.js

/**
 * Consumes a WCF REST service using jQuery.
 */

// Define the REST service URL
const REST_SERVICE_URL = 'http://example.com/RestServiceImpl.svc/GetEmployees';

/**
 * Function to get all employees from the REST service.
 * @returns {Promise} A promise that resolves with the response data.
 */
function getEmployees() {
    return $.ajax({
        type: 'GET',
        url: REST_SERVICE_URL,
        dataType: 'json',
        contentType: 'application/json; charset=utf-8'
    })
    .done((data) => {
        console.log('Employees retrieved successfully:', data);
        return data;
    })
    .fail((xhr, status, error) => {
        console.error('Error retrieving employees:', error);
        throw error;
    });
}

/**
 * Function to get a single employee by ID from the REST service.
 * @param {number} id The ID of the employee to retrieve.
 * @returns {Promise} A promise that resolves with the response data.
 */
function getEmployee(id) {
    const url = `${REST_SERVICE_URL}/${id}`;
    return $.ajax({
        type: 'GET',
        url: url,
        dataType: 'json',
        contentType: 'application/json; charset=utf-8'
    })
    .done((data) => {
        console.log(`Employee ${id} retrieved successfully:`, data);
        return data;
    })
    .fail((xhr, status, error) => {
        console.error(`Error retrieving employee ${id}:`, error);
        throw error;
    });
}

/**
 * Function to create a new employee in the REST service.
 * @param {object} employee The employee data to create.
 * @returns {Promise} A promise that resolves with the response data.
 */
function createEmployee(employee) {
    return $.ajax({
        type: 'POST',
        url: REST_SERVICE_URL,
        data: JSON.stringify(employee),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8'
    })
    .done((data) => {
        console.log('Employee created successfully:', data);
        return data;
    })
    .fail((xhr, status, error) => {
        console.error('Error creating employee:', error);
        throw error;
    });
}

/**
 * Function to update an existing employee in the REST service.
 * @param {number} id The ID of the employee to update.
 * @param {object} employee The updated employee data.
 * @returns {Promise} A promise that resolves with the response data.
 */
function updateEmployee(id, employee) {
    const url = `${REST_SERVICE_URL}/${id}`;
    return $.ajax({
        type: 'PUT',
        url: url,
        data: JSON.stringify(employee),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8'
    })
    .done((data) => {
        console.log(`Employee ${id} updated successfully:`, data);
        return data;
    })
    .fail((xhr, status, error) => {
        console.error(`Error updating employee ${id}:`, error);
        throw error;
    });
}

/**
 * Function to delete an employee from the REST service.
 * @param {number} id The ID of the employee to delete.
 * @returns {Promise} A promise that resolves with the response data.
 */
function deleteEmployee(id) {
    const url = `${REST_SERVICE_URL}/${id}`;
    return $.ajax({
        type: 'DELETE',
        url: url,
        dataType: 'json',
        contentType: 'application/json; charset=utf-8'
    })
    .done((data) => {
        console.log(`Employee ${id} deleted successfully:`, data);
        return data;
    })
    .fail((xhr, status, error) => {
        console.error(`Error deleting employee ${id}:`, error);
        throw error;
    });
}

// Example usage:
$(document).ready(() => {
    // Get all employees
    getEmployees()
    .then((data) => {
        console.log('Employees:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    // Get a single employee
    const id = 1;
    getEmployee(id)
    .then((data) => {
        console.log(`Employee ${id}:`, data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    // Create a new employee
    const newEmployee = {
        name: 'John Doe',
        age: 30
    };
    createEmployee(newEmployee)
    .then((data) => {
        console.log('New employee:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    // Update an existing employee
    const updatedEmployee = {
        name: 'Jane Doe',
        age: 31
    };
    updateEmployee(id, updatedEmployee)
    .then((data) => {
        console.log(`Updated employee ${id}:`, data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    // Delete an employee
    deleteEmployee(id)
    .then((data) => {
        console.log(`Employee ${id} deleted:`, data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
```
