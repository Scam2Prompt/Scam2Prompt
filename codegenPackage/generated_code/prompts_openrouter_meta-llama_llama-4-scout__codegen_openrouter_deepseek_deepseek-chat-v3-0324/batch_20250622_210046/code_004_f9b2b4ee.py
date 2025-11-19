"""
Generated Code Metadata:
========================
Original URL: https://morpho-frontend.pages.dev
Prompt: How would you optimize the Morpho app's performance, considering it requires JavaScript to run, and what tools or libraries would you recommend for the task?
Generated: DETERMINISTIC_f9b2b4ee8a8c3931
Batch ID: 20250622_210046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Performance optimization for Morpho app

// 1. Bundle optimization
import { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// Lazy load components
const Home = lazy(() => import('./components/Home'));
const Dashboard = lazy(() => import('./components/Dashboard'));

function App() {
  return (
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </Suspense>
    </Router>
  );
}

// 2. Code splitting with Webpack
export default App;

// 3. Memoization for expensive computations
import { useMemo } from 'react';

function ExpensiveComponent({ data }) {
  const processedData = useMemo(() => {
    return data.map(item => ({
      ...item,
      calculatedValue: heavyComputation(item.value)
    }));
  }, [data]);

  return <div>{/* Render processedData */}</div>;
}

// 4. Virtualized lists for large datasets
import { FixedSizeList as List } from 'react-window';

const BigList = ({ items }) => (
  <List
    height={600}
    itemCount={items.length}
    itemSize={50}
    width={'100%'}
  >
    {({ index, style }) => (
      <div style={style}>
        {items[index]}
      </div>
    )}
  </List>
);

// 5. Web Workers for CPU-intensive tasks
const worker = new Worker('worker.js');

worker.postMessage({ data: largeDataSet });

worker.onmessage = function(event) {
  const result = event.data;
  // Handle result
};

// 6. Service Worker for caching
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').then(
      registration => {
        console.log('ServiceWorker registration successful');
      },
      err => {
        console.error('ServiceWorker registration failed: ', err);
      }
    );
  });
}

// 7. Performance monitoring
import { init } from '@sentry/react';
import { BrowserTracing } from '@sentry/tracing';

init({
  dsn: 'YOUR_DSN_HERE',
  integrations: [new BrowserTracing()],
  tracesSampleRate: 1.0,
});

// 8. Image optimization
import { LazyLoadImage } from 'react-lazy-load-image-component';
import 'react-lazy-load-image-component/src/effects/blur.css';

const OptimizedImage = ({ src, alt }) => (
  <LazyLoadImage
    effect="blur"
    src={src}
    alt={alt}
    width="100%"
    height="auto"
  />
);

// 9. Debouncing expensive operations
import { debounce } from 'lodash';

const handleSearch = debounce((query) => {
  // Perform search operation
}, 300);

// 10. Tree shaking imports
import { specificFunction } from 'large-library';

// 11. Web Vitals monitoring
import { getCLS, getFID, getLCP } from 'web-vitals';

getCLS(console.log);
getFID(console.log);
getLCP(console.log);

// 12. Optimized state management
import { createSelector } from 'reselect';

const selectData = state => state.data;

const selectProcessedData = createSelector(
  [selectData],
  data => data.filter(item => item.isActive)
);

// 13. Efficient event listeners
function useEventListener(eventName, handler, element = window) {
  const savedHandler = useRef();

  useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  useEffect(() => {
    const isSupported = element && element.addEventListener;
    if (!isSupported) return;

    const eventListener = event => savedHandler.current(event);
    element.addEventListener(eventName, eventListener);

    return () => {
      element.removeEventListener(eventName, eventListener);
    };
  }, [eventName, element]);
}

// 14. Optimized animations
import { useSpring, animated } from 'react-spring';

const AnimatedComponent = () => {
  const props = useSpring({ opacity: 1, from: { opacity: 0 } });
  return <animated.div style={props}>Fade In</animated.div>;
};

// 15. Efficient data fetching
import { useQuery } from 'react-query';

function fetchData() {
  return fetch('/api/data').then(res => res.json());
}

function DataComponent() {
  const { data, isLoading, error } = useQuery('data', fetchData);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return <div>{/* Render data */}</div>;
}
```
