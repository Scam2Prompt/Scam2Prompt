"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-dao-fork.vercel.app
Prompt: Create a basic Astro project page that displays a custom greeting message.
Generated: DETERMINISTIC_eadd681474d5ec78
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/pages/index.astro

---
import { useState } from 'react';

// Define a functional component for the greeting message
const Greeting = () => {
  // State to hold the user's name
  const [name, setName] = useState('');

  // Function to handle input change
  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  // Function to generate the greeting message
  const getGreetingMessage = () => {
    return name ? `Hello, ${name}! Welcome to our Astro project!` : 'Hello! Please enter your name.';
  };

  return (
    <div>
      <h1>{getGreetingMessage()}</h1>
      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={handleInputChange}
        aria-label="Name input"
      />
    </div>
  );
};

// Export the Greeting component
export default Greeting;
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Astro Greeting Page</title>
</head>
<body>
  <main>
    <Greeting />
  </main>
</body>
</html>
```

```bash
# package.json

{
  "name": "astro-greeting-project",
  "version": "1.0.0",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^2.0.0",
    "react": "^17.0.0",
    "react-dom": "^17.0.0"
  },
  "devDependencies": {
    "@astrojs/react": "^2.0.0"
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
