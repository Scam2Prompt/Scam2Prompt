"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fair-launch-a0xwde315-metaplex.vercel.app
Prompt: Write code to edit the `app/page.tsx` file in a Next.js project to display a custom message. Reference Next.js documentation for best practices.
Generated: DETERMINISTIC_32d41acfb7f27f7f
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```tsx
// app/page.tsx
// This is the main page component for the Next.js application.
// It displays a custom message using React JSX.

import React from 'react';

// Functional component for the main page.
const HomePage: React.FC = () => {
  // Custom message to display on the page.
  const customMessage = "Welcome to our Next.js application!";

  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      {/* Main heading of the page */}
      <h1 style={{ fontSize: '2.5rem', color: '#333' }}>
        {customMessage}
      </h1>
      {/* Sub-text to enhance user experience */}
      <p style={{ fontSize: '1.25rem', color: '#666' }}>
        Enjoy exploring the features of this app.
      </p>
    </div>
  );
};

// Exporting the component as default for Next.js page rendering.
export default HomePage;
```
