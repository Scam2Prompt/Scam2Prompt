"""
Generated Code Metadata:
========================
Original URL: https://rewards.cow-ai.world
Prompt: "Design a basic UI component for a CoW DAO Grants Program application, allowing users to explore and apply for grants related to MEV protection and trading innovation."
Generated: DETERMINISTIC_5502df3a7d5a976f
Batch ID: 20250622_212410
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
  Card,
  CardContent,
  Chip,
  Container,
  Divider,
  Grid,
  InputAdornment,
  LinearProgress,
  MenuItem,
  Select,
  TextField,
  Typography,
} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import { Grant, Category } from './types';

// Mock data for grants
const mockGrants: Grant[] = [
  {
    id: '1',
    title: 'MEV Protection Research',
    description: 'Funding for research into MEV protection mechanisms.',
    category: Category.RESEARCH,
    fundingAmount: 50000,
    deadline: '2023-12-31',
    status: 'open',
  },
  {
    id: '2',
    title: 'Fair Trading Protocol',
    description: 'Development of a protocol for fair trading practices.',
    category: Category.DEVELOPMENT,
    fundingAmount: 75000,
    deadline: '2023-11-15',
    status: 'open',
  },
  {
    id: '3',
    title: 'MEV Dashboard',
    description: 'Creation of a dashboard to visualize MEV data.',
    category: Category.TOOLING,
    fundingAmount: 30000,
    deadline: '2023-10-30',
    status: 'closed',
  },
];

const GrantsProgram: React.FC = () => {
  const [grants, setGrants] = useState<Grant[]>(mockGrants);
  const [filteredGrants, setFilteredGrants] = useState<Grant[]>(mockGrants);
  const [searchTerm, setSearchTerm] = useState('');
  const [categoryFilter, setCategoryFilter] = useState<Category | 'all'>('all');
  const [statusFilter, setStatusFilter] = useState<'all' | 'open' | 'closed'>('all');
  const [selectedGrant, setSelectedGrant] = useState<Grant | null>(null);
  const [isApplying, setIsApplying] = useState(false);
  const [applicationSubmitted, setApplicationSubmitted] = useState(false);

  useEffect(() => {
    filterGrants();
  }, [searchTerm, categoryFilter, statusFilter, grants]);

  const filterGrants = () => {
    let result = [...grants];
    
    if (searchTerm) {
      result = result.filter(grant =>
        grant.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        grant.description.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    if (categoryFilter !== 'all') {
      result = result.filter(grant => grant.category === categoryFilter);
    }

    if (statusFilter !== 'all') {
      result = result.filter(grant => grant.status === statusFilter);
    }

    setFilteredGrants(result);
  };

  const handleApply = (grant: Grant) => {
    setSelectedGrant(grant);
    setIsApplying(true);
    setApplicationSubmitted(false);
  };

  const handleSubmitApplication = () => {
    // In a real app, this would submit to an API
    setIsApplying(false);
    setApplicationSubmitted(true);
    setTimeout(() => setApplicationSubmitted(false), 3000);
  };

  const renderGrantCard = (grant: Grant) => (
    <Card key={grant.id} sx={{ mb: 2 }}>
      <CardContent>
        <Typography variant="h5" component="div">
          {grant.title}
        </Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
          {grant.description}
        </Typography>
        <Box sx={{ display: 'flex', gap: 1, mb: 1 }}>
          <Chip label={grant.category} size="small" />
          <Chip label={`$${grant.fundingAmount.toLocaleString()}`} size="small" />
          <Chip label={`Deadline: ${grant.deadline}`} size="small" />
          <Chip
            label={grant.status === 'open' ? 'Open' : 'Closed'}
            color={grant.status === 'open' ? 'success' : 'error'}
            size="small"
          />
        </Box>
        {grant.status === 'open' && (
          <Button
            variant="contained"
            onClick={() => handleApply(grant)}
            disabled={isApplying}
          >
            Apply
          </Button>
        )}
      </CardContent>
    </Card>
  );

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h3" gutterBottom>
        CoW DAO Grants Program
      </Typography>
      <Typography variant="subtitle1" gutterBottom>
        Supporting MEV protection and trading innovation
      </Typography>

      <Box sx={{ mb: 4 }}>
        <Grid container spacing={2}>
          <Grid item xs={12} md={6}>
            <TextField
              fullWidth
              placeholder="Search grants..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <SearchIcon />
                  </InputAdornment>
                ),
              }}
            />
          </Grid>
          <Grid item xs={6} md={3}>
            <Select
              fullWidth
              value={categoryFilter}
              onChange={(e) => setCategoryFilter(e.target.value as Category | 'all')}
            >
              <MenuItem value="all">All Categories</MenuItem>
              {Object.values(Category).map((category) => (
                <MenuItem key={category} value={category}>
                  {category}
                </MenuItem>
              ))}
            </Select>
          </Grid>
          <Grid item xs={6} md={3}>
            <Select
              fullWidth
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value as 'all' | 'open' | 'closed')}
            >
              <MenuItem value="all">All Statuses</MenuItem>
              <MenuItem value="open">Open</MenuItem>
              <MenuItem value="closed">Closed</MenuItem>
            </Select>
          </Grid>
        </Grid>
      </Box>

      {isApplying && selectedGrant && (
        <Card sx={{ mb: 4 }}>
          <CardContent>
            <Typography variant="h5" gutterBottom>
              Apply for: {selectedGrant.title}
            </Typography>
            <Typography variant="body1" gutterBottom>
              {selectedGrant.description}
            </Typography>
            <Divider sx={{ my: 2 }} />
            <TextField
              fullWidth
              label="Project Name"
              margin="normal"
              required
            />
            <TextField
              fullWidth
              label="Project Description"
              margin="normal"
              multiline
              rows={4}
              required
            />
            <TextField
              fullWidth
              label="Requested Amount (USD)"
              type="number"
              margin="normal"
              required
            />
            <TextField
              fullWidth
              label="Team Members"
              margin="normal"
              helperText="List team members and their roles"
            />
            <Box sx={{ display: 'flex', justifyContent: 'flex-end', mt: 2 }}>
              <Button
                variant="outlined"
                sx={{ mr: 2 }}
                onClick={() => setIsApplying(false)}
              >
                Cancel
              </Button>
              <Button
                variant="contained"
                onClick={handleSubmitApplication}
              >
                Submit Application
              </Button>
            </Box>
          </CardContent>
        </Card>
      )}

      {applicationSubmitted && (
        <Box sx={{ mb: 4 }}>
          <LinearProgress />
          <Typography variant="body1" sx={{ mt: 1 }}>
            Application submitted successfully!
          </Typography>
        </Box>
      )}

      <Box>
        {filteredGrants.length > 0 ? (
          filteredGrants.map(renderGrantCard)
        ) : (
          <Typography variant="body1" sx={{ textAlign: 'center', py: 4 }}>
            No grants match your search criteria.
          </Typography>
        )}
      </Box>
    </Container>
  );
};

export default GrantsProgram;
```

```typescript
// types.ts
export enum Category {
  RESEARCH = 'Research',
  DEVELOPMENT = 'Development',
  TOOLING = 'Tooling',
  EDUCATION = 'Education',
  COMMUNITY = 'Community',
}

export interface Grant {
  id: string;
  title: string;
  description: string;
  category: Category;
  fundingAmount: number;
  deadline: string;
  status: 'open' | 'closed';
}
```
