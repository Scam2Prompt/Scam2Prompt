"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pira.pages.dev
Prompt: Develop a script in Solidity to handle proportional token distribution for airdrops, similar to Avalaunch's distribution model based on XAVA staked during sales.
Generated: DETERMINISTIC_d4387085c70d0f2e
Batch ID: 20250612_151415
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
 * @title Proportional Token Distributor for Airdrops
 * @author Expert Programmer
 * @notice This contract distributes tokens proportionally based on stake weights.
 */
contract TokenDistributor {
    // State variables
    address public owner; // Contract owner
    IERC20 public token; // ERC20 token to distribute
    uint256 public totalStakeWeight; // Total weight of staked tokens

    mapping(address => uint256) public stakeWeights; // Weight of each participant
    mapping(address => bool) public hasClaimed; // Track if a participant has claimed their tokens

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Events
    event TokenDistributed(address indexed recipient, uint256 amount);
    event StakeWeightUpdated(address indexed participant, uint256 weight);

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token to distribute.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        owner = msg.sender;
        token = IERC20(_token);
    }

    /**
     * @dev Function to update the stake weight for a participant.
     * @param participant Address of the participant.
     * @param weight Stake weight for the participant.
     */
    function updateStakeWeight(address participant, uint256 weight) external onlyOwner {
        require(participant != address(0), "Participant address cannot be zero");
        require(weight > 0, "Weight must be greater than zero");

        // Adjust total weight
        totalStakeWeight = totalStakeWeight - stakeWeights[participant] + weight;
        stakeWeights[participant] = weight;

        emit StakeWeightUpdated(participant, weight);
    }

    /**
     * @dev Function for participants to claim their proportional share of tokens.
     */
    function claimTokens() external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(stakeWeights[msg.sender] > 0, "No stake weight assigned");

        // Calculate the proportional amount
        uint256 amountToClaim = (token.balanceOf(address(this)) * stakeWeights[msg.sender]) / totalStakeWeight;
        require(amountToClaim > 0, "No tokens to claim");

        // Mark as claimed and transfer tokens
        hasClaimed[msg.sender] = true;
        require(token.transfer(msg.sender, amountToClaim), "Token transfer failed");

        emit TokenDistributed(msg.sender, amountToClaim);
    }

    /**
     * @dev Function to withdraw remaining tokens back to the owner after distribution.
     */
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingBalance = token.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens left to withdraw");

        require(token.transfer(owner, remainingBalance), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
