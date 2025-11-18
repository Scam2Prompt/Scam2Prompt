"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-metis.net
Prompt: Generate a code example demonstrating how to use MetaMask Snaps to extend wallet functionality with third-party features.
Generated: DETERMINISTIC_3931e57fdcba001c
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This code demonstrates how to use MetaMask Snaps to extend wallet functionality 
 * with third-party features. It includes best practices, error handling, and 
 * proper documentation to ensure clarity and maintainability.
 */

// Ensure MetaMask is installed and available in the browser
if (typeof window.ethereum === 'undefined') {
  console.error('MetaMask is not installed. Please install MetaMask to use Snaps.');
} else {
  // Initialize MetaMask Snap functionality
  const initializeSnap = async () => {
    try {
      // Request permission to use MetaMask Snaps
      const result = await window.ethereum.request({
        method: 'wallet_enable',
        params: [
          {
            wallet_snap: {
              // Replace '<snap_id>' with the snap identifier (e.g., npm package name or URL)
              '<snap_id>': {}
            }
          }
        ]
      });

      console.log('Snap initialized successfully:', result);
    } catch (error) {
      console.error('Failed to initialize Snap:', error);
    }
  };

  const callSnapMethod = async () => {
    try {
      // Replace '<snap_id>' with the snap identifier (e.g., npm package name or URL)
      const snapId = '<snap_id>';
      
      // Example call to a method exposed by the Snap
      const result = await window.ethereum.request({
        method: 'wallet_invokeSnap',
        params: [snapId, { method: 'someSnapMethod', params: { key: 'value' } }]
      });

      console.log('Snap method response:', result);
    } catch (error) {
      console.error('Failed to invoke Snap method:', error);
    }
  };

  // Initialize the Snap
  initializeSnap();

  // Example of calling a method provided by the Snap
  // Uncomment the line below to test calling the Snap method
  // callSnapMethod();
}
```

This code demonstrates MetaMask Snaps usage by requesting permissions to use a Snap (`wallet_enable`) and invoking a method provided by the Snap (`wallet_invokeSnap`). Replace `<snap_id>` with the Snap identifier you're working with.
