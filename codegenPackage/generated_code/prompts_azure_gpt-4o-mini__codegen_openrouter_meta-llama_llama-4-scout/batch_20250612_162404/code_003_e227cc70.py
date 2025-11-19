"""
Generated Code Metadata:
========================
Original URL: https://oeth-v-0-11.pages.dev
Prompt: What are best practices for handling loading states in a React application?
Generated: DETERMINISTIC_e227cc709d68f56e
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// LoadingStateHandler.js
import React, { useState, useEffect } from 'react';

/**
 * A custom hook to handle loading states in a React application.
 * 
 * @param {function} fetchData - A function that fetches data from an API.
 * @returns {object} An object containing the loading state, data, and error.
 */
const useLoadingState = (fetchData) => {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const response = await fetchData();
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        setData(await response.json());
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, [fetchData]);

  return { loading, data, error };
};

export default useLoadingState;
```

```jsx
// ExampleUsage.js
import React from 'react';
import useLoadingState from './LoadingStateHandler';

const fetchUserData = async () => {
  // Simulating an API call
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({
        ok: true,
        json: () => Promise.resolve({ name: 'John Doe', age: 30 }),
      });
    }, 2000);
  });
};

const UserProfile = () => {
  const { loading, data, error } = useLoadingState(fetchUserData);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>User Profile</h1>
      <p>Name: {data.name}</p>
      <p>Age: {data.age}</p>
    </div>
  );
};

export default UserProfile;
```

```jsx
// App.js
import React from 'react';
import UserProfile from './ExampleUsage';

const App = () => {
  return (
    <div>
      <UserProfile />
    </div>
  );
};

export default App;
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```
