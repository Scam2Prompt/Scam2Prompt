"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Create a JavaScript function to submit a transport inquiry form, ensuring it captures details for air, sea, and land transport as outlined by Portline Shipping.
Generated: DETERMINISTIC_a5222c518427058d
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Transport Inquiry Form Submission Function
 * =========================================
 * 
 * This function handles the submission of a transport inquiry form, 
 * capturing details for air, sea, and land transport as per Portline Shipping requirements.
 */

// Define the TransportInquiryForm class
class TransportInquiryForm {
  /**
   * Constructor to initialize the form data
   */
  constructor() {
    this.transportType = '';
    this.shipmentDetails = {};
  }

  /**
   * Validates the form data
   * @param {object} formData - The form data to be validated
   * @returns {boolean} True if the form data is valid, false otherwise
   */
  validateFormData(formData) {
    // Check if the transport type is selected
    if (!formData.transportType) {
      throw new Error('Transport type is required');
    }

    // Check if the shipment details are provided
    if (!formData.shipmentDetails) {
      throw new Error('Shipment details are required');
    }

    // Validate shipment details based on transport type
    switch (formData.transportType) {
      case 'air':
        if (!formData.shipmentDetails.airTransport) {
          throw new Error('Air transport details are required');
        }
        break;
      case 'sea':
        if (!formData.shipmentDetails.seaTransport) {
          throw new Error('Sea transport details are required');
        }
        break;
      case 'land':
        if (!formData.shipmentDetails.landTransport) {
          throw new Error('Land transport details are required');
        }
        break;
      default:
        throw new Error('Invalid transport type');
    }

    return true;
  }

  /**
   * Submits the transport inquiry form
   * @param {object} formData - The form data to be submitted
   * @returns {object} The response from the server
   */
  async submitForm(formData) {
    try {
      // Validate the form data
      this.validateFormData(formData);

      // Set the transport type and shipment details
      this.transportType = formData.transportType;
      this.shipmentDetails = formData.shipmentDetails;

      // Submit the form data to the server
      const response = await fetch('/api/transport-inquiry', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          transportType: this.transportType,
          shipmentDetails: this.shipmentDetails
        })
      });

      // Check if the response is OK
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Return the response from the server
      return await response.json();
    } catch (error) {
      // Log the error and rethrow it
      console.error('Error submitting transport inquiry form:', error);
      throw error;
    }
  }
}

// Example usage
const transportInquiryForm = new TransportInquiryForm();

// Air transport inquiry form data
const airTransportFormData = {
  transportType: 'air',
  shipmentDetails: {
    airTransport: {
      cargoType: 'Packages',
      weight: '100 kg',
      dimensions: '100x200x300 cm',
      origin: 'New York',
      destination: 'Los Angeles'
    }
  }
};

// Sea transport inquiry form data
const seaTransportFormData = {
  transportType: 'sea',
  shipmentDetails: {
    seaTransport: {
      cargoType: 'Containers',
      weight: '1000 kg',
      dimensions: '1000x2000x3000 cm',
      origin: 'Shanghai',
      destination: 'Rotterdam'
    }
  }
};

// Land transport inquiry form data
const landTransportFormData = {
  transportType: 'land',
  shipmentDetails: {
    landTransport: {
      cargoType: 'Trucks',
      weight: '5000 kg',
      dimensions: '5000x2000x3000 cm',
      origin: 'Chicago',
      destination: 'Houston'
    }
  }
};

// Submit the air transport inquiry form
transportInquiryForm.submitForm(airTransportFormData)
  .then(response => console.log('Air transport inquiry form submitted successfully:', response))
  .catch(error => console.error('Error submitting air transport inquiry form:', error));

// Submit the sea transport inquiry form
transportInquiryForm.submitForm(seaTransportFormData)
  .then(response => console.log('Sea transport inquiry form submitted successfully:', response))
  .catch(error => console.error('Error submitting sea transport inquiry form:', error));

// Submit the land transport inquiry form
transportInquiryForm.submitForm(landTransportFormData)
  .then(response => console.log('Land transport inquiry form submitted successfully:', response))
  .catch(error => console.error('Error submitting land transport inquiry form:', error));
```
