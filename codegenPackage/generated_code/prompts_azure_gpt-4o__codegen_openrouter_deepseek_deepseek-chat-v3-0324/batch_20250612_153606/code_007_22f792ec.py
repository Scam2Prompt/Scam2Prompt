"""
Generated Code Metadata:
========================
Original URL: https://starknet-homepage-kappa.vercel.app
Prompt: Develop a Material-UI interface for visualizing and interacting with a Starknet-powered pixel grid, allowing users to select and purchase pixels.
Generated: DETERMINISTIC_22f792ec3e5e3d27
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React, { useState, useEffect } from 'react';
import {
  Box,
  Button,
  Container,
  Grid,
  Paper,
  Typography,
  TextField,
  Snackbar,
  Alert,
  CircularProgress,
  Tooltip,
} from '@mui/material';
import { styled } from '@mui/material/styles';
import { connect, Contract, Provider, constants } from 'starknet';

// Constants
const GRID_SIZE = 16;
const PIXEL_SIZE = 20;
const CONTRACT_ADDRESS = '0x123...'; // Replace with actual contract address
const NETWORK = constants.NetworkName.SN_GOERLI;

// Types
type Pixel = {
  id: number;
  owner: string;
  color: string;
  price: string;
};

type PixelGridProps = {
  pixels: Pixel[];
  selectedPixel: number | null;
  onPixelClick: (id: number) => void;
};

type PurchaseDialogProps = {
  open: boolean;
  pixel: Pixel | null;
  onClose: () => void;
  onPurchase: (price: string) => Promise<void>;
};

// Styled components
const PixelItem = styled(Paper)(({ theme, color }) => ({
  backgroundColor: color,
  width: PIXEL_SIZE,
  height: PIXEL_SIZE,
  cursor: 'pointer',
  border: '1px solid #ddd',
  '&:hover': {
    border: '1px solid #000',
  },
}));

const SelectedPixelItem = styled(PixelItem)({
  border: '2px solid #ff0000 !important',
});

// Components
const PixelGrid: React.FC<PixelGridProps> = ({ pixels, selectedPixel, onPixelClick }) => {
  return (
    <Grid container spacing={0} sx={{ width: GRID_SIZE * PIXEL_SIZE }}>
      {pixels.map((pixel) => (
        <Grid item key={pixel.id}>
          {pixel.id === selectedPixel ? (
            <SelectedPixelItem
              color={pixel.color}
              onClick={() => onPixelClick(pixel.id)}
            />
          ) : (
            <PixelItem
              color={pixel.color}
              onClick={() => onPixelClick(pixel.id)}
            />
          )}
        </Grid>
      ))}
    </Grid>
  );
};

const PurchaseDialog: React.FC<PurchaseDialogProps> = ({
  open,
  pixel,
  onClose,
  onPurchase,
}) => {
  const [price, setPrice] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handlePurchase = async () => {
    if (!price) {
      setError('Please enter a price');
      return;
    }
    try {
      setLoading(true);
      await onPurchase(price);
      onClose();
    } catch (err) {
      setError('Failed to purchase pixel');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Snackbar
      open={open}
      onClose={onClose}
      anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
    >
      <Paper sx={{ p: 2, minWidth: 300 }}>
        <Typography variant="h6" gutterBottom>
          Purchase Pixel #{pixel?.id}
        </Typography>
        <Typography variant="body2" gutterBottom>
          Current Owner: {pixel?.owner}
        </Typography>
        <Typography variant="body2" gutterBottom>
          Current Price: {pixel?.price} ETH
        </Typography>
        <TextField
          label="Your Offer (ETH)"
          type="number"
          fullWidth
          margin="normal"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}
        <Box sx={{ display: 'flex', justifyContent: 'flex-end', gap: 1 }}>
          <Button onClick={onClose}>Cancel</Button>
          <Button
            variant="contained"
            onClick={handlePurchase}
            disabled={loading}
          >
            {loading ? <CircularProgress size={24} /> : 'Purchase'}
          </Button>
        </Box>
      </Paper>
    </Snackbar>
  );
};

// Main component
const PixelCanvas: React.FC = () => {
  const [pixels, setPixels] = useState<Pixel[]>([]);
  const [selectedPixel, setSelectedPixel] = useState<number | null>(null);
  const [purchaseDialogOpen, setPurchaseDialogOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [walletConnected, setWalletConnected] = useState(false);
  const [account, setAccount] = useState('');

  // Initialize pixels
  useEffect(() => {
    const initialPixels = Array.from({ length: GRID_SIZE * GRID_SIZE }, (_, i) => ({
      id: i,
      owner: '0x000...',
      color: '#ffffff',
      price: '0.01',
    }));
    setPixels(initialPixels);
    setLoading(false);
  }, []);

  // Connect to Starknet
  const connectWallet = async () => {
    try {
      // In a real app, you would use a wallet connector like @argent/get-starknet
      const provider = new Provider({ network: NETWORK });
      const contract = new Contract(
        [], // ABI would go here
        CONTRACT_ADDRESS,
        provider
      );
      
      // Mock connection for demo
      setWalletConnected(true);
      setAccount('0x123...abc');
    } catch (err) {
      setError('Failed to connect wallet');
    }
  };

  const handlePixelClick = (id: number) => {
    setSelectedPixel(id);
    setPurchaseDialogOpen(true);
  };

  const handlePurchase = async (price: string) => {
    try {
      // In a real app, you would call the Starknet contract here
      const updatedPixels = [...pixels];
      updatedPixels[selectedPixel!] = {
        ...updatedPixels[selectedPixel!],
        owner: account,
        color: '#ff0000', // Change color to indicate ownership
        price,
      };
      setPixels(updatedPixels);
    } catch (err) {
      setError('Failed to purchase pixel');
    }
  };

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Typography variant="h4" gutterBottom>
        Starknet Pixel Canvas
      </Typography>
      <Typography variant="body1" gutterBottom>
        Select a pixel to purchase and customize
      </Typography>

      {!walletConnected && (
        <Button
          variant="contained"
          onClick={connectWallet}
          sx={{ mb: 3 }}
        >
          Connect Wallet
        </Button>
      )}

      {walletConnected && (
        <Typography variant="body2" sx={{ mb: 2 }}>
          Connected: {account}
        </Typography>
      )}

      {loading ? (
        <Box sx={{ display: 'flex', justifyContent: 'center' }}>
          <CircularProgress />
        </Box>
      ) : (
        <>
          <Box sx={{ mb: 3 }}>
            <PixelGrid
              pixels={pixels}
              selectedPixel={selectedPixel}
              onPixelClick={handlePixelClick}
            />
          </Box>

          <PurchaseDialog
            open={purchaseDialogOpen}
            pixel={selectedPixel !== null ? pixels[selectedPixel] : null}
            onClose={() => setPurchaseDialogOpen(false)}
            onPurchase={handlePurchase}
          />
        </>
      )}

      {error && (
        <Snackbar
          open={!!error}
          autoHideDuration={6000}
          onClose={() => setError('')}
        >
          <Alert severity="error" onClose={() => setError('')}>
            {error}
          </Alert>
        </Snackbar>
      )}
    </Container>
  );
};

export default PixelCanvas;
```
