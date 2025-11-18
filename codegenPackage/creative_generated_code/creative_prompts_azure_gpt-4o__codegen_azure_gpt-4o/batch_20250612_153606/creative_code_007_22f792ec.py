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
// Importing necessary libraries and components
import React, { useState } from "react";
import { Grid, Button, Dialog, DialogTitle, DialogContent, TextField } from "@mui/material";
import { ethers } from "ethers"; // Ethereum library for interacting with Starknet
import { starknet } from "starknet"; // Starknet SDK

// Constants for grid size and pixel pricing
const GRID_SIZE = 10; // 10x10 pixel grid
const PIXEL_PRICE = 0.01; // Price per pixel in ETH

// Main PixelGrid Component
const PixelGrid = () => {
  // State to hold pixel ownership and selected pixel
  const [pixels, setPixels] = useState(Array(GRID_SIZE * GRID_SIZE).fill(null)); // Null means unowned
  const [selectedPixel, setSelectedPixel] = useState(null); // Pixel index
  const [purchaseDialogOpen, setPurchaseDialogOpen] = useState(false); // Dialog visibility
  const [walletAddress, setWalletAddress] = useState(""); // Wallet address

  // Function to handle pixel selection
  const handlePixelClick = (index) => {
    if (pixels[index]) {
      alert(`Pixel already owned by: ${pixels[index]}`); // Notify if owned
    } else {
      setSelectedPixel(index);
      setPurchaseDialogOpen(true);
    }
  };

  // Function to handle pixel purchase
  const handlePurchase = async () => {
    try {
      // Connect to wallet
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      await provider.send("eth_requestAccounts", []); // Request wallet connection
      const signer = provider.getSigner();

      // Starknet transaction for pixel purchase
      const tx = await starknet.invoke({
        contractAddress: "Your_Starknet_Contract_Address", // Replace with actual contract address
        entrypoint: "purchasePixel",
        calldata: [selectedPixel], // Pass the pixel index as calldata
      });

      // Wait for transaction confirmation
      await tx.wait();

      // Update pixel ownership and close dialog
      const address = await signer.getAddress();
      const updatedPixels = [...pixels];
      updatedPixels[selectedPixel] = address; // Assign ownership
      setPixels(updatedPixels);
      setPurchaseDialogOpen(false);
    } catch (error) {
      console.error("Error purchasing pixel:", error);
      alert("Transaction failed. Please try again.");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Starknet Pixel Grid</h1>
      <Grid container spacing={1}>
        {pixels.map((owner, index) => (
          <Grid item xs={1} key={index}>
            <Button
              variant="contained"
              color={owner ? "secondary" : "primary"}
              style={{ width: 50, height: 50 }}
              onClick={() => handlePixelClick(index)}
            >
              {owner ? "💰" : ""}
            </Button>
          </Grid>
        ))}
      </Grid>

      {/* Dialog for purchasing a pixel */}
      <Dialog open={purchaseDialogOpen} onClose={() => setPurchaseDialogOpen(false)}>
        <DialogTitle>Purchase Pixel</DialogTitle>
        <DialogContent>
          <TextField
            label="Wallet Address"
            fullWidth
            value={walletAddress}
            onChange={(e) => setWalletAddress(e.target.value)}
            margin="dense"
          />
          <p>Pixel Price: {PIXEL_PRICE} ETH</p>
          <Button variant="contained" color="primary" onClick={handlePurchase}>
            Confirm Purchase
          </Button>
        </DialogContent>
      </Dialog>
    </div>
  );
};

export default PixelGrid;
```
