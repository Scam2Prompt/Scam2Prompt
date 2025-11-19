"""
Generated Code Metadata:
========================
Original URL: https://etherfi.vercel.app
Prompt: Create a Next.js app page component that displays the current community allocation and countdown for Ether.fi Season 1, incorporating the provided allocation percentages.
Generated: DETERMINISTIC_60508ffa4f3adfbc
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// pages/season1.js
import Head from 'next/head';
import { useState, useEffect } from 'react';

const allocationPercentages = {
  lcath: 30,
  stader: 20,
  fig: 15,
  punks: 10,
  bluechip: 5,
  others: 20,
};

const Season1Page = () => {
  const [currentAllocation, setCurrentAllocation] = useState({});
  const [countdown, setCountdown] = useState(null);

  useEffect(() => {
    const fetchAllocationData = async () => {
      try {
        // Replace with actual API endpoint or data source
        const response = await fetch('/api/season1/allocation');
        const data = await response.json();
        setCurrentAllocation(data);
      } catch (error) {
        console.error('Error fetching allocation data:', error);
      }
    };

    fetchAllocationData();
  }, []);

  useEffect(() => {
    const calculateCountdown = () => {
      const season1EndDate = new Date('2024-09-16T00:00:00.000Z'); // Replace with actual end date
      const now = new Date();
      const timeLeft = season1EndDate.getTime() - now.getTime();

      if (timeLeft <= 0) {
        setCountdown('Season 1 has ended');
      } else {
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        setCountdown(`${days}d ${hours}h ${minutes}m ${seconds}s`);
      }
    };

    calculateCountdown();
    const intervalId = setInterval(calculateCountdown, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <Head>
        <title>Ether.fi Season 1</title>
      </Head>
      <h1>Ether.fi Season 1 Allocation and Countdown</h1>
      <section>
        <h2>Current Allocation</h2>
        <ul>
          {Object.keys(allocationPercentages).map((key) => (
            <li key={key}>
              {key}: {currentAllocation[key] || allocationPercentages[key]}%
            </li>
          ))}
        </ul>
      </section>
      <section>
        <h2>Countdown to Season 1 End</h2>
        <p>{countdown}</p>
      </section>
    </div>
  );
};

export default Season1Page;
```

```css
/* styles/globals.css */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

h1,
h2 {
  color: #333;
  margin-bottom: 1rem;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 0.5rem;
}
```

```javascript
// pages/api/season1/allocation.js
import { NextApiRequest, NextApiResponse } from 'next';

const allocationData = {
  lcath: 25,
  stader: 22,
  fig: 18,
  punks: 12,
  bluechip: 5,
  others: 18,
};

const handler = (req: NextApiRequest, res: NextApiResponse) => {
  if (req.method === 'GET') {
    return res.status(200).json(allocationData);
  }

  return res.status(405).json({ error: 'Method not allowed' });
};

export default handler;
```
