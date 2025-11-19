"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-218--nervous-kare-6f3c45.netlify.app
Prompt: Suggest a suitable JavaScript framework for building a web application that provides refuse and recycling collection services, similar to the City of York's website.
Generated: DETERMINISTIC_47f4c096425ef2f8
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Framework Recommendation: React.js with Next.js for a refuse/recycling collection web app

// Sample Next.js page component for collection schedule lookup
import { useState } from 'react';
import Head from 'next/head';

export default function CollectionSchedule() {
  const [postcode, setPostcode] = useState('');
  const [schedule, setSchedule] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      // In a real app, this would call your API endpoint
      const response = await fetch(`/api/schedule?postcode=${encodeURIComponent(postcode)}`);
      const data = await response.json();
      
      if (!response.ok) throw new Error(data.message || 'Failed to fetch schedule');
      
      setSchedule(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <Head>
        <title>Refuse & Recycling Collection Schedule</title>
        <meta name="description" content="Check your collection schedule" />
      </Head>

      <main>
        <h1>Collection Schedule</h1>
        
        <form onSubmit={handleSubmit}>
          <label htmlFor="postcode">Enter your postcode:</label>
          <input
            id="postcode"
            type="text"
            value={postcode}
            onChange={(e) => setPostcode(e.target.value)}
            required
            pattern="[A-Za-z]{1,2}[0-9][A-Za-z0-9]? ?[0-9][A-Za-z]{2}"
            title="Please enter a valid UK postcode"
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Loading...' : 'Find Schedule'}
          </button>
        </form>

        {error && <div className="error">{error}</div>}

        {schedule && (
          <div className="schedule-results">
            <h2>Your Collection Schedule</h2>
            <ul>
              <li>Next collection: {schedule.nextCollection}</li>
              <li>Bin type: {schedule.binType}</li>
              <li>Collection day: {schedule.collectionDay}</li>
            </ul>
          </div>
        )}
      </main>

      <style jsx>{`
        .container {
          min-height: 100vh;
          padding: 0 2rem;
        }
        main {
          max-width: 800px;
          margin: 0 auto;
          padding: 2rem 0;
        }
        form {
          display: flex;
          flex-direction: column;
          gap: 1rem;
          margin: 2rem 0;
        }
        input {
          padding: 0.5rem;
          font-size: 1rem;
        }
        button {
          padding: 0.5rem 1rem;
          background: #0070f3;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }
        button:disabled {
          background: #ccc;
          cursor: not-allowed;
        }
        .error {
          color: red;
          margin: 1rem 0;
        }
      `}</style>
    </div>
  );
}

// Sample API route (pages/api/schedule.js)
export default async function handler(req, res) {
  const { postcode } = req.query;

  if (!postcode) {
    return res.status(400).json({ message: 'Postcode is required' });
  }

  try {
    // In a real app, this would query your database or external API
    const mockData = {
      nextCollection: '2023-11-15',
      binType: 'General Waste',
      collectionDay: 'Wednesday'
    };
    
    res.status(200).json(mockData);
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
}
```
