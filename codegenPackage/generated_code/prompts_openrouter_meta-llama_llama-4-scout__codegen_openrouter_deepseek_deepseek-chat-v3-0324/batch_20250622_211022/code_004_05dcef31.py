"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-fraction-frontend.vercel.app
Prompt: Design a frontend interface for creating NFT tokens on Solana with image upload and metadata input.
Generated: DETERMINISTIC_05dcef31db676721
Batch ID: 20250622_211022
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React, { useState, useCallback } from 'react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { useWallet } from '@solana/wallet-adapter-react';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';
import {
  Button,
  TextField,
  Typography,
  Container,
  Paper,
  Grid,
  CircularProgress,
  InputLabel,
  FormControl,
} from '@material-ui/core';
import { FileUploader } from 'react-drag-drop-files';

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      padding: theme.spacing(4),
    },
    form: {
      marginTop: theme.spacing(3),
    },
    submit: {
      margin: theme.spacing(3, 0, 2),
    },
    fileUpload: {
      padding: theme.spacing(3),
      border: '2px dashed #ccc',
      borderRadius: theme.shape.borderRadius,
      textAlign: 'center',
      cursor: 'pointer',
    },
    preview: {
      maxWidth: '100%',
      maxHeight: '300px',
      marginTop: theme.spacing(2),
    },
  })
);

interface NFTMetadata {
  name: string;
  symbol: string;
  description: string;
  image: File | null;
  externalUrl?: string;
  attributes?: Array<{
    trait_type: string;
    value: string;
  }>;
}

const CreateNFT: React.FC = () => {
  const classes = useStyles();
  const { publicKey, connected } = useWallet();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [metadata, setMetadata] = useState<NFTMetadata>({
    name: '',
    symbol: '',
    description: '',
    image: null,
    externalUrl: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setMetadata((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleFileChange = (file: File) => {
    setMetadata((prev) => ({
      ...prev,
      image: file,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setSuccess(null);

    try {
      if (!connected || !publicKey) {
        throw new Error('Wallet not connected');
      }

      if (!metadata.image) {
        throw new Error('Please upload an image');
      }

      // Here you would typically:
      // 1. Upload image to IPFS/Arweave
      // 2. Create metadata JSON
      // 3. Upload metadata to IPFS/Arweave
      // 4. Create NFT on Solana blockchain
      // This is a placeholder for actual implementation

      // Simulate processing delay
      await new Promise((resolve) => setTimeout(resolve, 2000));

      setSuccess('NFT created successfully!');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unknown error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="md" className={classes.root}>
      <Paper elevation={3}>
        <Typography variant="h4" align="center" gutterBottom>
          Create NFT on Solana
        </Typography>

        {error && (
          <Typography color="error" align="center">
            {error}
          </Typography>
        )}

        {success && (
          <Typography color="primary" align="center">
            {success}
          </Typography>
        )}

        <form onSubmit={handleSubmit} className={classes.form}>
          <Grid container spacing={3}>
            <Grid item xs={12}>
              <TextField
                required
                fullWidth
                label="NFT Name"
                name="name"
                value={metadata.name}
                onChange={handleChange}
                variant="outlined"
              />
            </Grid>

            <Grid item xs={12} sm={6}>
              <TextField
                required
                fullWidth
                label="Symbol"
                name="symbol"
                value={metadata.symbol}
                onChange={handleChange}
                variant="outlined"
              />
            </Grid>

            <Grid item xs={12} sm={6}>
              <TextField
                fullWidth
                label="External URL (optional)"
                name="externalUrl"
                value={metadata.externalUrl}
                onChange={handleChange}
                variant="outlined"
              />
            </Grid>

            <Grid item xs={12}>
              <TextField
                required
                fullWidth
                multiline
                rows={4}
                label="Description"
                name="description"
                value={metadata.description}
                onChange={handleChange}
                variant="outlined"
              />
            </Grid>

            <Grid item xs={12}>
              <FormControl fullWidth>
                <InputLabel shrink>NFT Image</InputLabel>
                <FileUploader
                  handleChange={handleFileChange}
                  name="image"
                  types={['JPG', 'PNG', 'GIF', 'JPEG', 'WEBP']}
                  classes={classes.fileUpload}
                >
                  <Typography>
                    {metadata.image
                      ? metadata.image.name
                      : 'Drag & drop your image here or click to browse'}
                  </Typography>
                </FileUploader>
              </FormControl>

              {metadata.image && (
                <img
                  src={URL.createObjectURL(metadata.image)}
                  alt="Preview"
                  className={classes.preview}
                />
              )}
            </Grid>

            <Grid item xs={12}>
              <Button
                type="submit"
                fullWidth
                variant="contained"
                color="primary"
                className={classes.submit}
                disabled={loading || !connected}
              >
                {loading ? (
                  <CircularProgress size={24} color="inherit" />
                ) : (
                  'Create NFT'
                )}
              </Button>
            </Grid>
          </Grid>
        </form>
      </Paper>
    </Container>
  );
};

export default CreateNFT;
```
