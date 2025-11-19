"""
Generated Code Metadata:
========================
Original URL: https://farm-sophon.firebaseapp.com
Prompt: Design a user interface component for displaying user statistics, such as Total Users and Total Value Locked, on a farming platform similar to Sophon.
Generated: DETERMINISTIC_f7d34280a26f418c
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

// Styled components for the UI
const StatsContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin: 20px 0;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const StatCard = styled.div`
  flex: 1;
  min-width: 200px;
  padding: 15px;
  background: white;
  border-radius: 6px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
`;

const StatTitle = styled.h3`
  margin: 0 0 10px 0;
  font-size: 16px;
  color: #6c757d;
`;

const StatValue = styled.p`
  margin: 0;
  font-size: 24px;
  font-weight: bold;
  color: #212529;
`;

const LoadingMessage = styled.p`
  text-align: center;
  color: #6c757d;
`;

const ErrorMessage = styled.p`
  text-align: center;
  color: #dc3545;
`;

/**
 * UserStatistics Component
 * Displays key statistics like Total Users and Total Value Locked
 * 
 * @param {Object} props - Component props
 * @param {string} props.apiUrl - API endpoint to fetch statistics
 * @returns {JSX.Element} - Rendered statistics component
 */
const UserStatistics = ({ apiUrl }) => {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setStats(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, [apiUrl]);

  if (loading) {
    return <LoadingMessage>Loading statistics...</LoadingMessage>;
  }

  if (error) {
    return <ErrorMessage>Error: {error}</ErrorMessage>;
  }

  return (
    <StatsContainer>
      <StatCard>
        <StatTitle>Total Users</StatTitle>
        <StatValue>{stats?.totalUsers?.toLocaleString() || 'N/A'}</StatValue>
      </StatCard>
      <StatCard>
        <StatTitle>Total Value Locked</StatTitle>
        <StatValue>
          {stats?.totalValueLocked ? `$${stats.totalValueLocked.toLocaleString()}` : 'N/A'}
        </StatValue>
      </StatCard>
      <StatCard>
        <StatTitle>Active Farms</StatTitle>
        <StatValue>{stats?.activeFarms?.toLocaleString() || 'N/A'}</StatValue>
      </StatCard>
      <StatCard>
        <StatTitle>Average APY</StatTitle>
        <StatValue>{stats?.averageAPY ? `${stats.averageAPY}%` : 'N/A'}</StatValue>
      </StatCard>
    </StatsContainer>
  );
};

UserStatistics.propTypes = {
  apiUrl: PropTypes.string.isRequired,
};

export default UserStatistics;
```
