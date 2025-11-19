"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Design a simple decentralized application (dApp) that utilizes the $HEHE token for staking and rewards, including a basic user interface.
Generated: DETERMINISTIC_6db165629aec1084
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is the code for a simple decentralized application (dApp) that utilizes the `$HEHE` token for staking and rewards. The code includes a smart contract written in Solidity and a basic user interface using React.js. 

---

### Smart Contract (`HEHEStaking.sol`)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title HEHE Staking Contract
 * @dev A simple staking contract for the HEHE token with rewards distribution.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract HEHEStaking {
    IERC20 public immutable heheToken; // HEHE token contract
    uint256 public rewardRate; // Reward rate per second
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastUpdated; // Last time the stake was updated
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    constructor(IERC20 _heheToken, uint256 _rewardRate) {
        heheToken = _heheToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake HEHE tokens to earn rewards.
     * @param amount Amount of HEHE tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer HEHE tokens from user to contract
        require(heheToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user stake
        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt += _calculateReward(msg.sender);
        userStake.amount += amount;
        userStake.lastUpdated = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake HEHE tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = _calculateReward(msg.sender) + userStake.rewardDebt;

        // Transfer staked tokens and rewards to user
        require(heheToken.transfer(msg.sender, userStake.amount), "Token transfer failed");
        require(heheToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Unstaked(msg.sender, userStake.amount);
        emit RewardClaimed(msg.sender, reward);

        // Reset user stake
        delete stakes[msg.sender];
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param user Address of the user.
     * @return Pending reward amount.
     */
    function _calculateReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        return userStake.amount * rewardRate * timeElapsed / 1e18;
    }

    /**
     * @dev Update reward rate (only owner).
     * @param newRate New reward rate per second.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```

---

### Frontend (`App.js`)

```jsx
import React, { useState, useEffect } from "react";
import Web3 from "web3";
import HEHEStakingABI from "./HEHEStakingABI.json"; // ABI of the staking contract

const App = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [contract, setContract] = useState(null);
  const [stakeAmount, setStakeAmount] = useState("");
  const [userStake, setUserStake] = useState(null);

  const contractAddress = "0xYourContractAddress"; // Replace with deployed contract address

  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
        setAccount(accounts[0]);

        const stakingContract = new web3Instance.eth.Contract(HEHEStakingABI, contractAddress);
        setContract(stakingContract);
      } else {
        alert("Please install MetaMask!");
      }
    };

    initWeb3();
  }, []);

  const handleStake = async () => {
    if (contract && account) {
      try {
        await contract.methods.stake(web3.utils.toWei(stakeAmount, "ether")).send({ from: account });
        alert("Staked successfully!");
        fetchUserStake();
      } catch (error) {
        console.error("Error staking:", error);
        alert("Failed to stake tokens.");
      }
    }
  };

  const handleUnstake = async () => {
    if (contract && account) {
      try {
        await contract.methods.unstake().send({ from: account });
        alert("Unstaked successfully!");
        fetchUserStake();
      } catch (error) {
        console.error("Error unstaking:", error);
        alert("Failed to unstake tokens.");
      }
    }
  };

  const fetchUserStake = async () => {
    if (contract && account) {
      try {
        const stake = await contract.methods.stakes(account).call();
        setUserStake({
          amount: web3.utils.fromWei(stake.amount, "ether"),
          rewardDebt: web3.utils.fromWei(stake.rewardDebt, "ether"),
        });
      } catch (error) {
        console.error("Error fetching stake:", error);
      }
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>HEHE Token Staking</h1>
      <p>Connected Account: {account}</p>

      <div>
        <h2>Stake Tokens</h2>
        <input
          type="number"
          placeholder="Amount to stake"
          value={stakeAmount}
          onChange={(e) => setStakeAmount(e.target.value)}
        />
        <button onClick={handleStake}>Stake</button>
      </div>

      <div>
        <h2>Unstake Tokens</h2>
        <button onClick={handleUnstake}>Unstake</button>
      </div>

      <div>
        <h2>Your Stake</h2>
        {userStake ? (
          <div>
            <p>Staked Amount: {userStake.amount} HEHE</p>
            <p>Reward Debt: {userStake.rewardDebt} HEHE</p>
          </div>
        ) : (
          <p>No tokens staked.</p>
        )}
      </div>
    </div>
  );
};

export default App;
```

---

### Notes:
1. Replace `0xYourContractAddress` with the actual deployed contract address.
2. Ensure the `HEHEStakingABI.json` file contains the ABI of the `HEHEStaking` contract.
3. Install dependencies for the frontend:
   ```bash
   npm install web3 react
   ```
4. Deploy the smart contract to an Ethereum-compatible network and test the dApp thoroughly.
