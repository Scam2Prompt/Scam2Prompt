"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-fraction-frontend.vercel.app
Prompt: Provide code to integrate a "Cancel" button in a Solana NFT fractionalizer frontend that resets all input fields for NFT creation.
Generated: DETERMINISTIC_14bd2b313172dddc
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CancelButton.js
import React from 'react';

/**
 * CancelButton component for resetting NFT creation input fields.
 * 
 * @param {object} props 
 * @param {function} props.onCancel - Callback function to handle cancel button click.
 * @param {object} props.formik - Formik instance for resetting form fields.
 */
const CancelButton = ({ onCancel, formik }) => {
  const handleCancel = () => {
    // Reset form fields using Formik's resetForm method
    formik.resetForm();
    // Call onCancel callback if provided
    if (onCancel) {
      onCancel();
    }
  };

  return (
    <button 
      type="button" 
      className="cancel-button" 
      onClick={handleCancel}
    >
      Cancel
    </button>
  );
};

export default CancelButton;
```

```javascript
// NFTForm.js
import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import CancelButton from './CancelButton';

/**
 * NFTForm component for creating new NFTs.
 */
const NFTForm = () => {
  const initialValues = {
    name: '',
    description: '',
    symbol: '',
    // Add other NFT fields as needed
  };

  const handleSubmit = (values, { setSubmitting }) => {
    try {
      // Call API to create NFT with provided values
      console.log('Creating NFT with values:', values);
      setSubmitting(false);
    } catch (error) {
      console.error('Error creating NFT:', error);
      setSubmitting(false);
    }
  };

  const handleCancel = () => {
    console.log('Cancel button clicked');
  };

  return (
    <div>
      <h1>Create NFT</h1>
      <Formik
        initialValues={initialValues}
        onSubmit={handleSubmit}
      >
        {({ isSubmitting, resetForm }) => (
          <Form>
            <Field type="text" name="name" placeholder="NFT Name" />
            <ErrorMessage name="name" component="div" />
            <Field type="text" name="description" placeholder="NFT Description" />
            <ErrorMessage name="description" component="div" />
            <Field type="text" name="symbol" placeholder="NFT Symbol" />
            <ErrorMessage name="symbol" component="div" />
            {/* Add other NFT fields as needed */}

            <button type="submit" disabled={isSubmitting}>
              Create NFT
            </button>
            <CancelButton 
              onCancel={handleCancel} 
              formik={{ resetForm }} 
            />
          </Form>
        )}
      </Formik>
    </div>
  );
};

export default NFTForm;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import NFTForm from './NFTForm';

ReactDOM.render(
  <React.StrictMode>
    <NFTForm />
  </React.StrictMode>,
  document.getElementById('root')
);
```
