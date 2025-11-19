"""
Generated Code Metadata:
========================
Original URL: https://unstaked-token.world
Prompt: Create a dashboard interface using React.js to display $UNSD token presale statistics, including stage progress, total tokens sold, and amount raised.
Generated: DETERMINISTIC_263263b854b8bb1d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { Box, Typography, LinearProgress, Card, CardContent, Grid } from '@mui/material';
import { styled } from '@mui/material/styles';
import CountUp from 'react-countup';

// Mock data for presale stages
const presaleStages = [
  { name: 'Stage 1', target: 1000000, sold: 750000, price: 0.05 },
  { name: 'Stage 2', target: 2000000, sold: 1200000, price: 0.075 },
  { name: 'Stage 3', target: 3000000, sold: 500000, price: 0.10 },
];

const DashboardCard = styled(Card)(({ theme }) => ({
  borderRadius: '12px',
  boxShadow: '0 4px 20px rgba(0, 0, 0, 0.1)',
  transition: 'transform 0.3s ease-in-out',
  '&:hover': {
    transform: 'translateY(-5px)',
  },
}));

const PresaleDashboard = () => {
  const [currentStage, setCurrentStage] = useState(0);
  const [totalRaised, setTotalRaised] = useState(0);
  const [totalSold, setTotalSold] = useState(0);

  useEffect(() => {
    // Calculate totals when component mounts
    let raised = 0;
    let sold = 0;
    
    presaleStages.forEach(stage => {
      raised += stage.sold * stage.price;
      sold += stage.sold;
    });

    setTotalRaised(raised);
    setTotalSold(sold);

    // Determine current stage (first incomplete stage)
    const incompleteStage = presaleStages.findIndex(stage => stage.sold < stage.target);
    setCurrentStage(incompleteStage >= 0 ? incompleteStage : presaleStages.length - 1);
  }, []);

  const calculateProgress = (sold, target) => {
    return (sold / target) * 100;
  };

  const formatCurrency = (amount) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    }).format(amount);
  };

  return (
    <Box sx={{ p: 4 }}>
      <Typography variant="h4" gutterBottom sx={{ fontWeight: 'bold', mb: 4 }}>
        $UNSD Token Presale Dashboard
      </Typography>

      <Grid container spacing={4} sx={{ mb: 4 }}>
        <Grid item xs={12} md={6}>
          <DashboardCard>
            <CardContent>
              <Typography variant="h6" color="text.secondary" gutterBottom>
                Total Tokens Sold
              </Typography>
              <Typography variant="h3" sx={{ fontWeight: 'bold' }}>
                <CountUp end={totalSold} separator="," duration={2} />
              </Typography>
            </CardContent>
          </DashboardCard>
        </Grid>
        <Grid item xs={12} md={6}>
          <DashboardCard>
            <CardContent>
              <Typography variant="h6" color="text.secondary" gutterBottom>
                Total Amount Raised
              </Typography>
              <Typography variant="h3" sx={{ fontWeight: 'bold' }}>
                <CountUp end={totalRaised} prefix="$" separator="," decimals={2} duration={2} />
              </Typography>
            </CardContent>
          </DashboardCard>
        </Grid>
      </Grid>

      <Typography variant="h5" sx={{ fontWeight: 'bold', mb: 3 }}>
        Current Stage: {presaleStages[currentStage]?.name || 'Completed'}
      </Typography>

      {presaleStages.map((stage, index) => (
        <DashboardCard key={index} sx={{ mb: 3 }}>
          <CardContent>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
              <Typography variant="h6">{stage.name}</Typography>
              <Typography variant="subtitle1">
                {formatCurrency(stage.price)} per token
              </Typography>
            </Box>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
              <Typography variant="body2">
                Sold: {stage.sold.toLocaleString()} / {stage.target.toLocaleString()}
              </Typography>
              <Typography variant="body2">
                {formatCurrency(stage.sold * stage.price)} raised
              </Typography>
            </Box>
            <LinearProgress
              variant="determinate"
              value={calculateProgress(stage.sold, stage.target)}
              sx={{
                height: 10,
                borderRadius: 5,
                backgroundColor: '#e0e0e0',
                '& .MuiLinearProgress-bar': {
                  borderRadius: 5,
                  backgroundColor: index === currentStage ? '#4caf50' : '#1976d2',
                },
              }}
            />
          </CardContent>
        </DashboardCard>
      ))}
    </Box>
  );
};

export default PresaleDashboard;
```
