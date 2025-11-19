"""
Generated Code Metadata:
========================
Original URL: https://fair-launch-a0xwde315-metaplex.vercel.app
Prompt: Write a Next.js app page using TypeScript, referencing the `app/page.tsx` file.
Generated: DETERMINISTIC_6f965109b044b721
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// app/page.tsx

import React from 'react';
import { NextPage } from 'next';

// Define the props for the HomePage component
interface HomePageProps {
  title: string;
}

// Create a functional component for the home page
const HomePage: NextPage<HomePageProps> = ({ title }) => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>{title}</h1>
      <p style={styles.description}>
        Welcome to our Next.js application built with TypeScript!
      </p>
    </div>
  );
};

// Define default props for the HomePage component
HomePage.defaultProps = {
  title: 'Home Page',
};

// Define styles for the component
const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#f0f0f0',
  },
  title: {
    fontSize: '2rem',
    color: '#333',
  },
  description: {
    fontSize: '1.2rem',
    color: '#666',
  },
};

// Export the HomePage component as the default export
export default HomePage;
```

```typescript
// app/layout.tsx

import React from 'react';
import { ReactNode } from 'react';

// Define the layout props
interface LayoutProps {
  children: ReactNode;
}

// Create a layout component
const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div>
      <header style={styles.header}>
        <h1>My Next.js App</h1>
      </header>
      <main>{children}</main>
      <footer style={styles.footer}>
        <p>© 2023 My Next.js App</p>
      </footer>
    </div>
  );
};

// Define styles for the layout
const styles = {
  header: {
    padding: '1rem',
    backgroundColor: '#0070f3',
    color: '#fff',
    textAlign: 'center',
  },
  footer: {
    padding: '1rem',
    backgroundColor: '#0070f3',
    color: '#fff',
    textAlign: 'center',
    position: 'absolute',
    width: '100%',
    bottom: 0,
  },
};

// Export the Layout component as the default export
export default Layout;
```

```typescript
// app/page.tsx (updated to include layout)

import React from 'react';
import { NextPage } from 'next';
import Layout from './layout';

// Define the props for the HomePage component
interface HomePageProps {
  title: string;
}

// Create a functional component for the home page
const HomePage: NextPage<HomePageProps> = ({ title }) => {
  return (
    <Layout>
      <div style={styles.container}>
        <h1 style={styles.title}>{title}</h1>
        <p style={styles.description}>
          Welcome to our Next.js application built with TypeScript!
        </p>
      </div>
    </Layout>
  );
};

// Define default props for the HomePage component
HomePage.defaultProps = {
  title: 'Home Page',
};

// Define styles for the component
const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#f0f0f0',
  },
  title: {
    fontSize: '2rem',
    color: '#333',
  },
  description: {
    fontSize: '1.2rem',
    color: '#666',
  },
};

// Export the HomePage component as the default export
export default HomePage;
```
