"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Provide an example of using daisyUI components in a DApp built with Next.js.
Generated: DETERMINISTIC_7057e5b1305195cb
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/_app.js
import '../styles/globals.css';
import { useEffect } from 'react';
import { useRouter } from 'next/router';

function MyApp({ Component, pageProps }) {
  const router = useRouter();

  useEffect(() => {
    // Handle route changes for analytics or other purposes
    const handleRouteChange = (url) => {
      console.log('App is changing to: ', url);
    };
    router.events.on('routeChangeComplete', handleRouteChange);
    return () => {
      router.events.off('routeChangeComplete', handleRouteChange);
    };
  }, [router.events]);

  return <Component {...pageProps} />;
}

export default MyApp;
```

```javascript
// pages/index.js
import Head from 'next/head';
import { useState } from 'react';
import { Button, Card, Input } from 'daisyui';

export default function Home() {
  const [inputValue, setInputValue] = useState('');
  const [message, setMessage] = useState('');

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Basic validation
    if (!inputValue) {
      setMessage('Input cannot be empty');
      return;
    }
    setMessage(`Submitted: ${inputValue}`);
    setInputValue('');
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <Head>
        <title>DApp with DaisyUI</title>
        <meta name="description" content="A simple DApp using DaisyUI components" />
      </Head>
      <Card className="w-96 shadow-lg">
        <Card.Body>
          <h2 className="text-lg font-bold">DApp Input Form</h2>
          <form onSubmit={handleSubmit}>
            <Input
              type="text"
              placeholder="Enter something..."
              value={inputValue}
              onChange={handleInputChange}
              className="mb-4"
            />
            <Button type="submit" className="w-full">Submit</Button>
          </form>
          {message && <p className="mt-4 text-red-500">{message}</p>}
        </Card.Body>
      </Card>
    </div>
  );
}
```

```css
/* styles/globals.css */
@import 'daisyui/dist/full.css';

/* Custom global styles can be added here */
body {
  font-family: 'Arial', sans-serif;
}
```

```json
// package.json
{
  "name": "dapp-with-daisyui",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "daisyui": "^1.14.0",
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  }
}
```

```bash
# Install dependencies
npm install
```

```bash
# Start the development server
npm run dev
```

```bash
# Build for production
npm run build
```

```bash
# Start the production server
npm start
```
