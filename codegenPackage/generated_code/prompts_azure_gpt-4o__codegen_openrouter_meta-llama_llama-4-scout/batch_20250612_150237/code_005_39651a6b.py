"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Generate a Next.js application that supports hot module replacement (HMR) for editing and testing pages, similar to the functionality described in the Dapp Starter.
Generated: DETERMINISTIC_39651a6b4523a7d9
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Next.js Application with Hot Module Replacement (HMR)**
===========================================================

**pages/_app.js**
```jsx
// pages/_app.js
import { AppProps } from 'next/app';

function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

**pages/index.js**
```jsx
// pages/index.js
import { useState } from 'react';

function HomePage() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>Welcome to the Next.js App!</h1>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default HomePage;
```

**next.config.js**
```javascript
// next.config.js
module.exports = {
  // Enable hot module replacement (HMR)
  target: 'serverless',
  // Enable reactStrictMode for better warnings and errors
  reactStrictMode: true,
};
```

**components/Layout.js**
```jsx
// components/Layout.js
import Head from 'next/head';

function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <Head>
        <title>Next.js App</title>
      </Head>
      <main>{children}</main>
    </div>
  );
}

export default Layout;
```

**pages/_document.js**
```jsx
// pages/_document.js
import Document, { Html, Head, Main, NextScript } from 'next/document';

class MyDocument extends Document {
  render() {
    return (
      <Html>
        <Head />
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;
```

**utils/withHMR.js**
```javascript
// utils/withHMR.js
import { useEffect } from 'react';

const withHMR = (WrappedComponent: React.ComponentType) => {
  const HMRComponent = () => {
    useEffect(() => {
      if (module.hot) {
        module.hot.accept();
      }
    }, []);

    return <WrappedComponent />;
  };

  return HMRComponent;
};

export default withHMR;
```

**pages/api/hello.js**
```javascript
// pages/api/hello.js
export default async function handler(req, res) {
  try {
    res.status(200).json({ message: 'Hello, World!' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}
```

**jest.config.js**
```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  collectCoverage: true,
  coverageDirectory: 'coverage',
  moduleFileExtensions: ['js', 'jsx', 'ts', 'tsx', 'json'],
  moduleDirectories: ['node_modules', 'pages', 'components'],
  testEnvironment: 'jsdom',
  testPathIgnorePatterns: ['node_modules', 'coverage'],
};
```

**tsconfig.json**
```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "es6",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve"
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
```
