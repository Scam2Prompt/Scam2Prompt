"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: What are the steps to edit the pages/index.tsx file for HMR updates in a Next.js project?
Generated: DETERMINISTIC_a860883e9b4e2b3f
Batch ID: 20250612_160245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// pages/index.tsx

import { useEffect, useState } from 'react';

// Define a functional component for the Home page
const Home: React.FC = () => {
  const [date, setDate] = useState<string>(new Date().toLocaleString());

  // Effect to update the date every second
  useEffect(() => {
    // Set up an interval to update the date
    const intervalId = setInterval(() => {
      setDate(new Date().toLocaleString());
    }, 1000);

    // Cleanup function to clear the interval on component unmount
    return () => {
      clearInterval(intervalId);
    };
  }, []);

  // Render the current date
  return (
    <div>
      <h1>Welcome to Next.js!</h1>
      <p>The current date and time is: {date}</p>
    </div>
  );
};

// Export the Home component
export default Home;

// Enable Hot Module Replacement (HMR) by default in Next.js
if (typeof window !== 'undefined' && module.hot) {
  module.hot.accept();
}
```
