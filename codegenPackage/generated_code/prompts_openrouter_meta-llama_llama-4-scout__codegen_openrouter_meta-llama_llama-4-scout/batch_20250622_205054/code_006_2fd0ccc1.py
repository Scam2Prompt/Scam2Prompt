"""
Generated Code Metadata:
========================
Original URL: https://metreniuk.github.io
Prompt: How do I implement code splitting in a React app created with Create React App, and what are the benefits of using this feature?
Generated: DETERMINISTIC_2fd0ccc1ecbe02ca
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
import React, { Suspense, lazy } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

// Lazy loading components
const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));
const NotFound = lazy(() => import('./pages/NotFound'));

// App component
function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>Loading...</div>}>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/about" component={About} />
          <Route path="*" component={NotFound} />
        </Switch>
      </Suspense>
    </BrowserRouter>
  );
}

export default App;
```

```javascript
// pages/Home.js
import React from 'react';

function Home() {
  return <div>Welcome to the Home page</div>;
}

export default Home;
```

```javascript
// pages/About.js
import React from 'react';

function About() {
  return <div>About us</div>;
}

export default About;
```

```javascript
// pages/NotFound.js
import React from 'react';

function NotFound() {
  return <div>Page not found</div>;
}

export default NotFound;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```javascript
// webpack.config.js (ejected Create React App)
module.exports = {
  //...
  optimization: {
    splitChunks: {
      chunks: 'all',
      minSize: 10000,
      minChunks: 1,
      maxAsyncRequests: 30,
      maxInitialRequests: 30,
      enforceSizeThreshold: 50000,
      cacheGroups: {
        default: {
          minChunks: 2,
          priority: -20,
          reuseExistingChunk: true,
        },
      },
    },
  },
};
```
