"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-ia.pages.dev
Prompt: Write a smart contract in Solidity for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, ensuring compatibility with Ethereum Layer 2 standards.
Generated: DETERMINISTIC_e2c3c6390c335515
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title PEPU Staking Contract
 * @dev A smart contract for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain.
 */
contract PEPUStaking {
    // State variables
    IERC20 public pepuToken; // $PEPU token contract
    address public owner; // Contract owner

    // Staking data structure
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of staking
    }

    // Mapping of staker address to their staking details
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed staker, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed staker, uint256 amount, uint256 timestamp);
    event RewardsClaimed(address indexed staker, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor
    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid $PEPU token address");
        pepuToken = IERC20(_pepuToken);
        owner = msg.sender;
    }

    /**
     * @dev Staking function allowing users to stake $PEPU tokens.
     * @param _amount The amount of $PEPU tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer $PEPU tokens from the staker to the contract
        require(pepuToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Unstaking function allowing users to withdraw their staked $PEPU tokens.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 stakedAmount = userStake.amount;

        require(stakedAmount > 0, "No tokens staked");

        // Reset staking details
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer $PEPU tokens back to the staker
        require(pepuToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, block.timestamp);
    }

    /**
     * @dev Function to claim staking rewards (example: fixed rewards based on staking duration).
     * @return The amount of reward tokens claimed.
     */
    function claimRewards() external returns (uint256) {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Example reward calculation based on staking duration
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 rewards = (userStake.amount * stakingDuration) / (30 days); // Example reward formula

        // Transfer rewards to the staker
        require(pepuToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
        return rewards;
    }

    /**
     * @dev Emergency function for contract owner to withdraw tokens from the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(pepuToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        require(pepuToken.transfer(msg.sender, _amount), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
