"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.oasishottubsep.com
Prompt: Suggest a library or framework to develop an interactive "Build & Price" tool for hot tubs, including options for Jacuzzi® Swim Spas and Hydropool Swim Spas, as seen on the Oasis Hot Tubs site.
Generated: DETERMINISTIC_bde72d5109b3b66e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is production-ready code for an interactive "Build & Price" tool using **React.js** with the **Material-UI** component library for UI elements and **Formik** for form handling. This solution is modular and extensible, allowing users to select options for Jacuzzi® Swim Spas and Hydropool Swim Spas.

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import { Container, Typography, Grid, Button, MenuItem, TextField } from '@mui/material';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';

// Validation schema for the form using Yup
const formValidationSchema = Yup.object().shape({
  brand: Yup.string().required('Please select a brand'),
  model: Yup.string().required('Please select a model'),
  features: Yup.array().of(Yup.string()).required('Select at least one feature'),
});

// Mock data for brands, models, and features
const spaOptions = {
  Jacuzzi: {
    models: ['Model A', 'Model B'],
    features: ['LED Lighting', 'Waterfall Jets', 'Bluetooth Speakers'],
  },
  Hydropool: {
    models: ['Model X', 'Model Y'],
    features: ['Self-Cleaning Technology', 'Hydrotherapy Jets', 'Energy Efficiency'],
  },
};

// Main Build & Price Tool Component
const BuildAndPriceTool = () => {
  const [formSubmitted, setFormSubmitted] = useState(false);
  const [submittedData, setSubmittedData] = useState(null);

  // Initial values for the form
  const initialValues = {
    brand: '',
    model: '',
    features: [],
  };

  // Form submission handler
  const handleSubmit = (values) => {
    setFormSubmitted(true);
    setSubmittedData(values);
  };

  return (
    <Container maxWidth="sm" sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Build & Price Your Hot Tub
      </Typography>
      {!formSubmitted ? (
        <Formik
          initialValues={initialValues}
          validationSchema={formValidationSchema}
          onSubmit={handleSubmit}
        >
          {({ values, errors, touched, handleChange, setFieldValue }) => (
            <Form>
              <Grid container spacing={2}>
                {/* Brand Selection */}
                <Grid item xs={12}>
                  <TextField
                    select
                    fullWidth
                    id="brand"
                    name="brand"
                    label="Select Brand"
                    value={values.brand}
                    onChange={handleChange}
                    error={touched.brand && Boolean(errors.brand)}
                    helperText={touched.brand && errors.brand}
                  >
                    {Object.keys(spaOptions).map((brand) => (
                      <MenuItem key={brand} value={brand}>
                        {brand}
                      </MenuItem>
                    ))}
                  </TextField>
                </Grid>

                {/* Model Selection */}
                <Grid item xs={12}>
                  <TextField
                    select
                    fullWidth
                    id="model"
                    name="model"
                    label="Select Model"
                    value={values.model}
                    onChange={handleChange}
                    error={touched.model && Boolean(errors.model)}
                    helperText={touched.model && errors.model}
                    disabled={!values.brand}
                  >
                    {values.brand &&
                      spaOptions[values.brand].models.map((model) => (
                        <MenuItem key={model} value={model}>
                          {model}
                        </MenuItem>
                      ))}
                  </TextField>
                </Grid>

                {/* Features Selection */}
                <Grid item xs={12}>
                  <Typography variant="subtitle1" gutterBottom>
                    Select Features:
                  </Typography>
                  {values.brand &&
                    spaOptions[values.brand].features.map((feature) => (
                      <div key={feature}>
                        <TextField
                          type="checkbox"
                          id={feature}
                          name="features"
                          value={feature}
                          checked={values.features.includes(feature)}
                          onChange={(e) => {
                            const newFeatures = values.features.includes(feature)
                              ? values.features.filter((f) => f !== feature)
                              : [...values.features, feature];
                            setFieldValue('features', newFeatures);
                          }}
                        />
                        <label htmlFor={feature}>{feature}</label>
                      </div>
                    ))}
                  {touched.features && errors.features && (
                    <Typography color="error">{errors.features}</Typography>
                  )}
                </Grid>

                {/* Submit Button */}
                <Grid item xs={12}>
                  <Button
                    type="submit"
                    variant="contained"
                    color="primary"
                    fullWidth
                  >
                    Submit
                  </Button>
                </Grid>
              </Grid>
            </Form>
          )}
        </Formik>
      ) : (
        <div>
          <Typography variant="h5" gutterBottom>
            Submission Successful!
          </Typography>
          <Typography>
            You selected the following options:
          </Typography>
          <pre>{JSON.stringify(submittedData, null, 2)}</pre>
          <Button
            variant="contained"
            color="secondary"
            onClick={() => setFormSubmitted(false)}
          >
            Reset
          </Button>
        </div>
      )}
    </Container>
  );
};

export default BuildAndPriceTool;
```

### Key Features of the Code:
1. **Formik** for form handling and validation.
2. **Material-UI** for UI components.
3. Modular data structure using mock `spaOptions`.
4. Error handling and validation through `Yup`.
5. Code adheres to React best practices.

To run this code:
- Ensure you have React, Material-UI, Formik, and Yup installed via npm (`npm install @mui/material formik yup`).
- Replace the mock data with actual options for hot tubs from your database/API.
