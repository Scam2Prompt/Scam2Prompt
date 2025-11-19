"""
Generated Code Metadata:
========================
Original URL: https://wormhole.vercel.app
Prompt: Write a code snippet to implement HMR updates in a Next.js application, referencing the Wormhole documentation.
Generated: DETERMINISTIC_56c3013bd00fc13f
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules from Next.js and Wormhole
import { useEffect } from 'react';
import { useWormhole } from 'wormhole-react';

// Custom hook to handle Hot Module Replacement (HMR) updates
const useHMR = () => {
  const { subscribe, unsubscribe } = useWormhole();

  useEffect(() => {
    // Subscribe to HMR updates
    const handleUpdate = (module) => {
      if (module) {
        // Reload the module when an update is received
        module.hot.accept();
      }
    };

    // Subscribe to updates
    subscribe(handleUpdate);

    // Cleanup function to unsubscribe on component unmount
    return () => {
      unsubscribe(handleUpdate);
    };
  }, [subscribe, unsubscribe]);
};

// Example component using the HMR hook
const MyComponent = () => {
  useHMR(); // Invoke the HMR hook

  return (
    <div>
      <h1>Hello, Next.js with Wormhole HMR!</h1>
      <p>Edit this component to see HMR in action.</p>
    </div>
  );
};

export default MyComponent;
```

Make sure to install the `wormhole-react` package and configure your Next.js application to support HMR as per the Wormhole documentation.
