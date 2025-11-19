"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-claim.pages.dev
Prompt: Develop a sample Solidity contract that allows users to stake their $PEPU tokens and earn double rewards on the Pepe Unchained Layer 2 blockchain.
Generated: DETERMINISTIC_5b295d2ff558c6d7
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PEPU Staking Contract
 * @dev A contract that allows users to stake $PEPU tokens and earn double rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PEPUStaking {
    // Address of the $PEPU token contract
    IERC20 public pepuToken;

    // Mapping of user address to their staked balance
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to their reward balance
    mapping(address => uint256) public rewardBalances;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Rewards rate (double rewards) per staked token
    uint256 public constant REWARD_RATE = 2;

    // Address of the contract owner
    address public owner;

    // Event to log staking actions
    event Staked(address indexed user, uint256 amount);

    // Event to log withdrawal of staked tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event to log claim of rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the $PEPU token address.
     * @param _pepuTokenAddress Address of the $PEPU token contract.
     */
    constructor(address _pepuTokenAddress) {
        require(_pepuTokenAddress != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuTokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Function to allow users to stake their $PEPU tokens.
     * @param amount The amount of $PEPU tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer $PEPU tokens from the user to the contract
        require(pepuToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's staked balance
        stakedBalances[msg.sender] += amount;

        // Update total staked
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to allow users to withdraw their staked $PEPU tokens.
     */
    function withdraw() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens to withdraw");

        // Update user's staked balance
        stakedBalances[msg.sender] = 0;

        // Update total staked
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to the user
        require(pepuToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Emit withdrawal event
        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Function to allow users to claim their earned rewards (double rewards).
     */
    function claimRewards() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens for rewards");

        // Calculate rewards (double the staked amount)
        uint256 rewards = stakedAmount * REWARD_RATE;

        // Update reward balance
        rewardBalances[msg.sender] += rewards;

        // Transfer rewards to the user
        require(pepuToken.transfer(msg.sender, rewards), "Reward transfer failed");

        // Emit reward claim event
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to retrieve contract's $PEPU token balance for owner.
     * @return The $PEPU token balance of the contract.
     */
    function getContractBalance() external view onlyOwner returns (uint256) {
        return pepuToken.balanceOf(address(this));
    }

    /**
     * @dev Emergency function for the owner to withdraw all $PEPU tokens from the contract.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = pepuToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        // Transfer all $PEPU tokens to the contract owner
        require(pepuToken.transfer(owner, contractBalance), "Emergency withdraw failed");
    }
}
```
