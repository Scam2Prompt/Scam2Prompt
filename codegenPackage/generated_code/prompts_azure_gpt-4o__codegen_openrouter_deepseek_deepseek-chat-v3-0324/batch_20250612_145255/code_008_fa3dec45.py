"""
Generated Code Metadata:
========================
Original URL: https://salesstudios.com
Prompt: Write code to integrate ActiveCampaign with a website to capture visitor details and automate follow-up messaging, as described by Sales Studios.
Generated: DETERMINISTIC_fa3dec4549bc0e36
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ActiveCampaign Integration Script
// This script handles form submissions and sends data to ActiveCampaign
// for lead capture and automated follow-up messaging

class ActiveCampaignIntegration {
  constructor(apiUrl, apiKey) {
    if (!apiUrl || !apiKey) {
      throw new Error('API URL and API Key are required');
    }
    this.apiUrl = apiUrl;
    this.apiKey = apiKey;
    this.contactEndpoint = `${apiUrl}/api/3/contacts`;
    this.listEndpoint = `${apiUrl}/api/3/contactLists`;
    this.headers = {
      'Content-Type': 'application/json',
      'Api-Token': apiKey
    };
  }

  /**
   * Create or update a contact in ActiveCampaign
   * @param {Object} contactData - Contact information
   * @param {Array} listIds - Array of list IDs to add contact to
   * @returns {Promise} - Promise with API response
   */
  async syncContact(contactData, listIds = []) {
    try {
      if (!contactData.email) {
        throw new Error('Email is required');
      }

      // Check if contact exists
      const existingContact = await this._findContactByEmail(contactData.email);
      
      let contactId;
      if (existingContact) {
        // Update existing contact
        contactId = existingContact.id;
        await this._updateContact(contactId, contactData);
      } else {
        // Create new contact
        const newContact = await this._createContact(contactData);
        contactId = newContact.id;
      }

      // Add contact to lists
      if (listIds.length > 0) {
        await this._addContactToLists(contactId, listIds);
      }

      return { success: true, contactId };
    } catch (error) {
      console.error('Error syncing contact:', error);
      throw error;
    }
  }

  /**
   * Find contact by email
   * @param {string} email - Email address to search for
   * @returns {Promise} - Promise with contact data or null if not found
   */
  async _findContactByEmail(email) {
    try {
      const response = await fetch(`${this.contactEndpoint}?email=${encodeURIComponent(email)}`, {
        method: 'GET',
        headers: this.headers
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data.contacts.length > 0 ? data.contacts[0] : null;
    } catch (error) {
      console.error('Error finding contact:', error);
      throw error;
    }
  }

  /**
   * Create a new contact
   * @param {Object} contactData - Contact information
   * @returns {Promise} - Promise with created contact data
   */
  async _createContact(contactData) {
    try {
      const response = await fetch(this.contactEndpoint, {
        method: 'POST',
        headers: this.headers,
        body: JSON.stringify({
          contact: {
            email: contactData.email,
            firstName: contactData.firstName || '',
            lastName: contactData.lastName || '',
            phone: contactData.phone || '',
            fieldValues: this._prepareCustomFields(contactData)
          }
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json().contact;
    } catch (error) {
      console.error('Error creating contact:', error);
      throw error;
    }
  }

  /**
   * Update existing contact
   * @param {number} contactId - ActiveCampaign contact ID
   * @param {Object} contactData - Contact information
   * @returns {Promise} - Promise with API response
   */
  async _updateContact(contactId, contactData) {
    try {
      const response = await fetch(`${this.contactEndpoint}/${contactId}`, {
        method: 'PUT',
        headers: this.headers,
        body: JSON.stringify({
          contact: {
            email: contactData.email,
            firstName: contactData.firstName || '',
            lastName: contactData.lastName || '',
            phone: contactData.phone || '',
            fieldValues: this._prepareCustomFields(contactData)
          }
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error updating contact:', error);
      throw error;
    }
  }

  /**
   * Add contact to lists
   * @param {number} contactId - ActiveCampaign contact ID
   * @param {Array} listIds - Array of list IDs
   * @returns {Promise} - Promise with API response
   */
  async _addContactToLists(contactId, listIds) {
    try {
      const promises = listIds.map(listId => {
        return fetch(this.listEndpoint, {
          method: 'POST',
          headers: this.headers,
          body: JSON.stringify({
            contactList: {
              list: listId,
              contact: contactId,
              status: 1 // 1 = active, 2 = unsubscribed
            }
          })
        });
      });

      const responses = await Promise.all(promises);
      const errors = responses.filter(r => !r.ok);
      
      if (errors.length > 0) {
        throw new Error(`Failed to add contact to ${errors.length} lists`);
      }

      return responses;
    } catch (error) {
      console.error('Error adding contact to lists:', error);
      throw error;
    }
  }

  /**
   * Prepare custom field values for API
   * @param {Object} contactData - Contact information
   * @returns {Array} - Array of field value objects
   */
  _prepareCustomFields(contactData) {
    const fieldValues = [];
    
    // Add custom fields (excluding standard fields)
    const standardFields = ['email', 'firstName', 'lastName', 'phone'];
    for (const [key, value] of Object.entries(contactData)) {
      if (!standardFields.includes(key) && value) {
        fieldValues.push({
          field: key,
          value: value.toString()
        });
      }
    }

    return fieldValues;
  }
}

// Form Handler for Website Integration
class ActiveCampaignFormHandler {
  constructor(acIntegration, formSelector, listIds = []) {
    this.acIntegration = acIntegration;
    this.formSelector = formSelector;
    this.listIds = listIds;
    this.forms = document.querySelectorAll(formSelector);
    
    if (this.forms.length === 0) {
      console.warn(`No forms found with selector: ${formSelector}`);
      return;
    }
    
    this._initForms();
  }

  _initForms() {
    this.forms.forEach(form => {
      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        await this._handleFormSubmit(form);
      });
    });
  }

  async _handleFormSubmit(form) {
    try {
      const formData = this._extractFormData(form);
      const submitButton = form.querySelector('[type="submit"]');
      
      // Disable submit button to prevent duplicate submissions
      if (submitButton) {
        submitButton.disabled = true;
        submitButton.textContent = 'Processing...';
      }

      // Sync contact with ActiveCampaign
      const result = await this.acIntegration.syncContact(formData, this.listIds);
      
      // Show success message or redirect
      this._handleSuccess(form, result);
    } catch (error) {
      console.error('Form submission error:', error);
      this._handleError(form, error);
    }
  }

  _extractFormData(form) {
    const formData = {};
    const inputs = form.querySelectorAll('input, select, textarea');
    
    inputs.forEach(input => {
      if (input.name && input.value.trim()) {
        formData[input.name] = input.value.trim();
      }
    });

    return formData;
  }

  _handleSuccess(form, result) {
    const successMessage = form.querySelector('.success-message') || 
      document.createElement('div');
    
    if (!successMessage.classList.contains('success-message')) {
      successMessage.className = 'success-message';
      successMessage.style.color = 'green';
      successMessage.style.marginTop = '10px';
      form.appendChild(successMessage);
    }
    
    successMessage.textContent = 'Thank you! We\'ll be in touch soon.';
    
    // Reset form after successful submission
    form.reset();
    
    // Re-enable submit button
    const submitButton = form.querySelector('[type="submit"]');
    if (submitButton) {
      submitButton.disabled = false;
      submitButton.textContent = 'Submit';
    }
    
    // Track conversion if needed
    if (typeof gtag !== 'undefined') {
      gtag('event', 'conversion', {
        'send_to': 'AW-123456789/AbCdEfGhIjKlMnOpQrStUvWxYz'
      });
    }
  }

  _handleError(form, error) {
    const errorMessage = form.querySelector('.error-message
