"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phosphor.now.sh
Prompt: Write a script to dynamically load service descriptions (e.g., web development, mobile apps, graphic design) into a Next.js page, inspired by Phosphor's service offerings.
Generated: DETERMINISTIC_7d51e5ea07ead231
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/services.js

import fs from 'fs';
import path from 'path';
import React from 'react';

// A utility function to fetch service data
const fetchServiceData = () => {
  try {
    // Load services.json dynamically at runtime
    const filePath = path.join(process.cwd(), 'data', 'services.json');
    const fileData = fs.readFileSync(filePath, 'utf-8');
    return JSON.parse(fileData);
  } catch (error) {
    console.error('Error reading services file:', error);
    return [];
  }
};

const Services = ({ services }) => {
  return (
    <div>
      <h1>Our Services</h1>
      {services.length > 0 ? (
        <ul>
          {services.map((service) => (
            <li key={service.id}>
              <h2>{service.title}</h2>
              <p>{service.description}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>No services available at the moment.</p>
      )}
    </div>
  );
};

export async function getStaticProps() {
  // Fetch service data dynamically at build time
  const services = fetchServiceData();
  return {
    props: {
      services,
    },
  };
}

export default Services;

/*
  Project structure:
  - Place a file named 'services.json' inside the 'data' folder at the root of your project.
  
  Example of services.json:
  [
    {
      "id": 1,
      "title": "Web Development",
      "description": "Custom web applications tailored to your needs."
    },
    {
      "id": 2,
      "title": "Mobile Apps",
      "description": "Native and cross-platform mobile applications."
    },
    {
      "id": 3,
      "title": "Graphic Design",
      "description": "Beautiful and functional designs for your brand."
    }
  ]
*/
```
