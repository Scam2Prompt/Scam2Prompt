"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-homepage-kappa.vercel.app
Prompt: Develop a Material-UI interface for visualizing and interacting with a Starknet-powered pixel grid, allowing users to select and purchase pixels.
Generated: DETERMINISTIC_22f792ec3e5e3d27
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components from Material-UI
import React, { useState, useEffect } from 'react';
import { Grid, Button, Typography, Snackbar, Alert } from '@mui/material';
import { ethers } from 'ethers';

// Define constants for pixel grid size and Starknet contract address
const GRID_SIZE = 10; // 10x10 grid
const CONTRACT_ADDRESS = '0xYourStarknetContractAddress'; // Replace with your Starknet contract address

// Main component for the Pixel Grid
const PixelGrid = () => {
  const [pixels, setPixels] = useState(Array(GRID_SIZE * GRID_SIZE).fill({ color: '#FFFFFF', owned: false }));
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');

  // Function to handle pixel click and purchase
  const handlePixelClick = (index) => {
    // Check if the pixel is already owned
    if (pixels[index].owned) {
      setSnackbarMessage('This pixel is already owned!');
      setSnackbarOpen(true);
      return;
    }

    // Call the purchase function (assumed to be defined elsewhere)
    purchasePixel(index)
      .then(response => {
        // Update pixel state on successful purchase
        const newPixels = [...pixels];
        newPixels[index] = { color: '#FF0000', owned: true }; // Example color for purchased pixel
        setPixels(newPixels);
        setSnackbarMessage('Pixel purchased successfully!');
      })
      .catch(error => {
        console.error("Purchase failed:", error);
        setSnackbarMessage('An error occurred while purchasing the pixel.');
      })
      .finally(() => {
        setSnackbarOpen(true);
      });
  };

  // Mock function to simulate purchasing a pixel (to be implemented with Starknet logic)
  const purchasePixel = async (index) => {
    // Here you would integrate with your Starknet smart contract
    // For example, using ethers.js to interact with the contract
    console.log(`Purchasing pixel at index ${index}`);
    return new Promise((resolve) => setTimeout(resolve, 1000)); // Simulating network request
  };

  // Function to close the snackbar
  const handleSnackbarClose = () => {
    setSnackbarOpen(false);
  };

  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Starknet Pixel Grid
      </Typography>
      <Grid container spacing={1}>
        {pixels.map((pixel, index) => (
          <Grid item xs={1.2} key={index}>
            <Button
              variant="contained"
              style={{ backgroundColor: pixel.color, width: '100%', height: '100px' }}
              onClick={() => handlePixelClick(index)}
            >
              {pixel.owned ? 'Owned' : 'Buy'}
            </Button>
          </Grid>
        ))}
      </Grid>
      <Snackbar open={snackbarOpen} autoHideDuration={6000} onClose={handleSnackbarClose}>
        <Alert onClose={handleSnackbarClose} severity="info">
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </div>
  );
};

export default PixelGrid;
```

Make sure to replace `'0xYourStarknetContractAddress'` with the actual address of your Starknet contract and implement the logic for purchasing pixels within the `purchasePixel` function according to your project requirements.
