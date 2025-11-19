"""
Generated Code Metadata:
========================
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Design a user interface for the EarthMeta Wallet app, allowing users to track their token performance and rewards in real-time, as well as manage their digital assets.
Generated: DETERMINISTIC_d6b3506731232fb3
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a production-ready implementation of a user interface for the EarthMeta Wallet app using React.js and Material-UI. This code assumes you have a backend API to fetch token performance and rewards data.

```javascript
// App.js
import React, { useState, useEffect } from "react";
import { Container, Typography, Grid, Card, CardContent, Button, CircularProgress } from "@mui/material";
import axios from "axios";

// EarthMeta Wallet App Component
const EarthMetaWalletApp = () => {
  const [tokens, setTokens] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch token data from the backend API
  useEffect(() => {
    const fetchTokenData = async () => {
      try {
        const response = await axios.get("/api/tokens"); // Replace with your API endpoint
        setTokens(response.data);
        setLoading(false);
      } catch (err) {
        setError("Failed to fetch token data. Please try again later.");
        setLoading(false);
      }
    };

    fetchTokenData();
  }, []);

  // Handle asset management actions (placeholder function)
  const handleManageAssets = (tokenId) => {
    alert(`Manage assets for token ID: ${tokenId}`);
  };

  return (
    <Container maxWidth="lg" style={{ marginTop: "2rem" }}>
      <Typography variant="h4" gutterBottom>
        EarthMeta Wallet
      </Typography>
      <Typography variant="subtitle1" gutterBottom>
        Track your token performance and rewards in real-time, and manage your digital assets.
      </Typography>

      {loading ? (
        <CircularProgress />
      ) : error ? (
        <Typography color="error">{error}</Typography>
      ) : (
        <Grid container spacing={3}>
          {tokens.map((token) => (
            <Grid item xs={12} sm={6} md={4} key={token.id}>
              <Card>
                <CardContent>
                  <Typography variant="h6">{token.name}</Typography>
                  <Typography variant="body2" color="textSecondary">
                    Symbol: {token.symbol}
                  </Typography>
                  <Typography variant="body1">
                    Current Value: ${token.currentValue.toFixed(2)}
                  </Typography>
                  <Typography variant="body1">
                    Rewards: ${token.rewards.toFixed(2)}
                  </Typography>
                  <Button
                    variant="contained"
                    color="primary"
                    style={{ marginTop: "1rem" }}
                    onClick={() => handleManageAssets(token.id)}
                  >
                    Manage Assets
                  </Button>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}
    </Container>
  );
};

export default EarthMetaWalletApp;
```

### Notes:
1. **Dependencies**: Ensure you have the following installed:
   - React (`npm install react react-dom`)
   - Material-UI (`npm install @mui/material @emotion/react @emotion/styled`)
   - Axios (`npm install axios`)

2. **Backend API**: Replace `/api/tokens` with the actual endpoint of your backend API that provides token data in the format:
   ```json
   [
     {
       "id": 1,
       "name": "Token Name",
       "symbol": "TKN",
       "currentValue": 123.45,
       "rewards": 10.5
     },
     ...
   ]
   ```

3. **Error Handling**: The code includes basic error handling for failed API requests.

4. **Styling**: Material-UI is used for styling to ensure a clean and responsive design.
