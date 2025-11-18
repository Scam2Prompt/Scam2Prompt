"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Recommend a library or API to create an interactive questionnaire similar to the one on the SCOUT.kz website, which helps users select tractors based on their needs (e.g., area size, type of work, and budget).
Generated: DETERMINISTIC_6b4428841857f775
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented implementation in JavaScript using React and the popular `react-hook-form` library for creating an interactive questionnaire. This code provides a foundation for building the desired functionality:

```jsx
// Import necessary dependencies
import React, { useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import Select from 'react-select';

// A functional React component for an interactive questionnaire
const TractorQuestionnaire = () => {
  const { handleSubmit, control, register } = useForm(); // Initialize react-hook-form
  const [results, setResults] = useState(null); // State to hold questionnaire results

  // Options for the questionnaire (these can be replaced with dynamic data from an API)
  const areaOptions = [
    { value: 'small', label: 'Less than 1 acre' },
    { value: 'medium', label: '1-5 acres' },
    { value: 'large', label: 'More than 5 acres' },
  ];

  const workOptions = [
    { value: 'plowing', label: 'Plowing' },
    { value: 'mowing', label: 'Mowing' },
    { value: 'transport', label: 'Transporting goods' },
  ];

  const budgetOptions = [
    { value: 'low', label: 'Under $10,000' },
    { value: 'medium', label: '$10,000-$30,000' },
    { value: 'high', label: 'Over $30,000' },
  ];

  // Handle form submission
  const onSubmit = (data) => {
    // Simulate processing data to recommend a tractor
    const recommendedTractor = `Recommended tractor for ${data.area.label} area, ${data.work.label} work, and a ${data.budget.label} budget.`;
    setResults(recommendedTractor);
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '600px', margin: 'auto' }}>
      <h1>Tractor Selection Questionnaire</h1>
      <form onSubmit={handleSubmit(onSubmit)}>
        {/* Area size question */}
        <div style={{ marginBottom: '1rem' }}>
          <label htmlFor="area">1. What is the size of your area?</label>
          <Controller
            name="area"
            control={control}
            rules={{ required: 'Area size is required.' }}
            render={({ field }) => (
              <Select {...field} options={areaOptions} placeholder="Select area size" />
            )}
          />
        </div>

        {/* Type of work question */}
        <div style={{ marginBottom: '1rem' }}>
          <label htmlFor="work">2. What type of work will you perform?</label>
          <Controller
            name="work"
            control={control}
            rules={{ required: 'Type of work is required.' }}
            render={({ field }) => (
              <Select {...field} options={workOptions} placeholder="Select type of work" />
            )}
          />
        </div>

        {/* Budget question */}
        <div style={{ marginBottom: '1rem' }}>
          <label htmlFor="budget">3. What is your budget?</label>
          <Controller
            name="budget"
            control={control}
            rules={{ required: 'Budget is required.' }}
            render={({ field }) => (
              <Select {...field} options={budgetOptions} placeholder="Select budget" />
            )}
          />
        </div>

        {/* Submit button */}
        <button type="submit" style={{ padding: '0.5rem 1rem', fontSize: '1rem' }}>
          Get Recommendation
        </button>
      </form>

      {/* Display results */}
      {results && (
        <div style={{ marginTop: '2rem', padding: '1rem', border: '1px solid #ccc' }}>
          <h2>Results</h2>
          <p>{results}</p>
        </div>
      )}
    </div>
  );
};

export default TractorQuestionnaire;
```

### Notes:
- Install dependencies before running the code:
  ```
  npm install react react-dom react-hook-form react-select
  ```
- Replace placeholder options (`areaOptions`, `workOptions`, and `budgetOptions`) with dynamic data if needed.
- This code uses `react-select` for dropdowns and `react-hook-form` for form management.
- Error handling is simplified. You can extend it to show validation errors to users.
