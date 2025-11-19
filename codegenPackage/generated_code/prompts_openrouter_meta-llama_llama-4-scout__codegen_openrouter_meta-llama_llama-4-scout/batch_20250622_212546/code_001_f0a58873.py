"""
Generated Code Metadata:
========================
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: Develop a Vercel app using React and JavaScript
Generated: DETERMINISTIC_f0a58873766ebd81
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required dependencies
import Head from 'next/head';
import { useState, useEffect } from 'react';

// Home page component
function Home() {
  // Initialize state
  const [count, setCount] = useState(0);

  // Increment count on button click
  const handleIncrement = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <Head>
        <title>Vercel App</title>
      </Head>
      <h1>Vercel App with React and JavaScript</h1>
      <p>Count: {count}</p>
      <button onClick={handleIncrement}>Increment</button>
    </div>
  );
}

// Error boundary component
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // You can also log the error to an error reporting service
    console.error('Error Info:', errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // You can render any custom fallback UI
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}

// Main application component
function App() {
  return (
    <ErrorBoundary>
      <Home />
    </ErrorBoundary>
  );
}

export default App;
```

```javascript
// pages/_app.js
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

```javascript
// pages/index.js
import Home from '../components/Home';

export default Home;
```

```javascript
// next.config.js
module.exports = {
  reactStrictMode: true,
};
```

```css
/* styles/globals.css */
body {
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

h1 {
  text-align: center;
  margin-top: 20px;
}

button {
  margin-top: 10px;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}
```
