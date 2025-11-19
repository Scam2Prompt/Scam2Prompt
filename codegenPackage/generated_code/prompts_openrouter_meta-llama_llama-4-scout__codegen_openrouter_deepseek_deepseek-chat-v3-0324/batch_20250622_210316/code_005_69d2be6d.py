"""
Generated Code Metadata:
========================
Original URL: https://web-tpad.pages.dev
Prompt: Design a simple front-end interface for users to stake TPAD tokens and participate in IDOs on TrustPad, using a library like React or Angular.
Generated: DETERMINISTIC_69d2be6dc90dab63
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready React implementation for a TrustPad staking interface with TypeScript:

```tsx
// src/components/StakingInterface.tsx
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { useWeb3React } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import { Button, Card, Input, Spin, message, Modal } from 'antd';
import './StakingInterface.css';

// Interface for staking pool data
interface PoolData {
  totalStaked: string;
  userStaked: string;
  apy: number;
  lockPeriod: number;
}

// Interface for IDO participation
interface IDOData {
  id: string;
  name: string;
  startTime: number;
  endTime: number;
  minStakeRequired: string;
}

// Mock contract ABI - replace with actual TrustPad contract ABI
const TPAD_STAKING_ABI = [
  "function stake(uint256 amount) public",
  "function unstake(uint256 amount) public",
  "function getStake(address user) public view returns (uint256)",
  "function totalStaked() public view returns (uint256)"
];

const TPAD_TOKEN_ABI = [
  "function approve(address spender, uint256 amount) public returns (bool)",
  "function allowance(address owner, address spender) public view returns (uint256)"
];

const TPAD_STAKING_ADDRESS = "0x..."; // Replace with actual contract address
const TPAD_TOKEN_ADDRESS = "0x..."; // Replace with actual token address

const StakingInterface: React.FC = () => {
  const { account, library } = useWeb3React<Web3Provider>();
  const [loading, setLoading] = useState<boolean>(false);
  const [stakeAmount, setStakeAmount] = useState<string>('');
  const [unstakeAmount, setUnstakeAmount] = useState<string>('');
  const [poolData, setPoolData] = useState<PoolData | null>(null);
  const [idos, setIdos] = useState<IDOData[]>([]);
  const [selectedIdo, setSelectedIdo] = useState<IDOData | null>(null);
  const [approvalLoading, setApprovalLoading] = useState<boolean>(false);

  // Fetch pool data and IDOs
  useEffect(() => {
    if (!account || !library) return;

    const fetchData = async () => {
      try {
        setLoading(true);
        
        // Mock data - replace with actual contract calls
        const mockPoolData: PoolData = {
          totalStaked: "1000000",
          userStaked: "5000",
          apy: 15.5,
          lockPeriod: 30
        };

        const mockIdos: IDOData[] = [
          {
            id: "1",
            name: "Project Alpha",
            startTime: Date.now() + 86400000,
            endTime: Date.now() + 172800000,
            minStakeRequired: "1000"
          },
          {
            id: "2",
            name: "Project Beta",
            startTime: Date.now() + 259200000,
            endTime: Date.now() + 345600000,
            minStakeRequired: "5000"
          }
        ];

        setPoolData(mockPoolData);
        setIdos(mockIdos);
      } catch (error) {
        console.error("Error fetching data:", error);
        message.error("Failed to fetch staking data");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [account, library]);

  const handleStake = async () => {
    if (!account || !library || !stakeAmount) return;

    try {
      setLoading(true);
      const signer = library.getSigner();
      const stakingContract = new ethers.Contract(TPAD_STAKING_ADDRESS, TPAD_STAKING_ABI, signer);
      const tokenContract = new ethers.Contract(TPAD_TOKEN_ADDRESS, TPAD_TOKEN_ABI, signer);

      // Check allowance
      const allowance = await tokenContract.allowance(account, TPAD_STAKING_ADDRESS);
      const amountWei = ethers.utils.parseEther(stakeAmount);

      if (allowance.lt(amountWei)) {
        setApprovalLoading(true);
        const approveTx = await tokenContract.approve(TPAD_STAKING_ADDRESS, amountWei);
        await approveTx.wait();
        setApprovalLoading(false);
      }

      const tx = await stakingContract.stake(amountWei);
      await tx.wait();
      message.success("Tokens staked successfully!");
      setStakeAmount('');
    } catch (error) {
      console.error("Staking error:", error);
      message.error("Failed to stake tokens");
    } finally {
      setLoading(false);
    }
  };

  const handleUnstake = async () => {
    if (!account || !library || !unstakeAmount) return;

    try {
      setLoading(true);
      const signer = library.getSigner();
      const stakingContract = new ethers.Contract(TPAD_STAKING_ADDRESS, TPAD_STAKING_ABI, signer);
      
      const amountWei = ethers.utils.parseEther(unstakeAmount);
      const tx = await stakingContract.unstake(amountWei);
      await tx.wait();
      
      message.success("Tokens unstaked successfully!");
      setUnstakeAmount('');
    } catch (error) {
      console.error("Unstaking error:", error);
      message.error("Failed to unstake tokens");
    } finally {
      setLoading(false);
    }
  };

  const handleParticipate = (ido: IDOData) => {
    if (!poolData) return;

    const userStaked = parseFloat(poolData.userStaked);
    const minStake = parseFloat(ido.minStakeRequired);

    if (userStaked < minStake) {
      message.error(`You need to stake at least ${ido.minStakeRequired} TPAD to participate`);
      return;
    }

    setSelectedIdo(ido);
  };

  const confirmParticipation = async () => {
    if (!selectedIdo || !account) return;

    try {
      setLoading(true);
      // Here you would implement the actual IDO participation logic
      // This is just a mock implementation
      message.success(`Successfully registered for ${selectedIdo.name} IDO!`);
      setSelectedIdo(null);
    } catch (error) {
      console.error("IDO participation error:", error);
      message.error("Failed to participate in IDO");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="staking-container">
      <Card title="TPAD Staking" loading={loading}>
        <div className="pool-info">
          {poolData && (
            <>
              <p>Total Staked: {poolData.totalStaked} TPAD</p>
              <p>Your Stake: {poolData.userStaked} TPAD</p>
              <p>APY: {poolData.apy}%</p>
              <p>Lock Period: {poolData.lockPeriod} days</p>
            </>
          )}
        </div>

        <div className="staking-actions">
          <div className="stake-form">
            <Input
              type="number"
              value={stakeAmount}
              onChange={(e) => setStakeAmount(e.target.value)}
              placeholder="Amount to stake"
              disabled={!account}
            />
            <Button
              type="primary"
              onClick={handleStake}
              disabled={!stakeAmount || !account}
              loading={loading || approvalLoading}
            >
              Stake TPAD
            </Button>
          </div>

          <div className="unstake-form">
            <Input
              type="number"
              value={unstakeAmount}
              onChange={(e) => setUnstakeAmount(e.target.value)}
              placeholder="Amount to unstake"
              disabled={!account}
            />
            <Button
              type="default"
              onClick={handleUnstake}
              disabled={!unstakeAmount || !account}
              loading={loading}
            >
              Unstake TPAD
            </Button>
          </div>
        </div>
      </Card>

      <Card title="Available IDOs" loading={loading} className="idos-container">
        {idos.length === 0 ? (
          <p>No IDOs available at this time</p>
        ) : (
          <div className="ido-list">
            {idos.map((ido) => (
              <Card key={ido.id} className="ido-card">
                <h3>{ido.name}</h3>
                <p>Starts: {new Date(ido.startTime).toLocaleString()}</p>
                <p>Ends: {new Date(ido.endTime).toLocaleString()}</p>
                <p>Minimum Stake: {ido.minStakeRequired} TPAD</p>
                <Button
                  type="primary"
                  onClick={() => handleParticipate(ido)}
                  disabled={!account || !poolData ||
