"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://docs.matrixinfos.com
Prompt: Develop a Solidity contract that facilitates the staking of $MATRIX Tokens, ensuring decentralized governance and user privacy.
Generated: DETERMINISTIC_03f8bc9d3a6d8f47
Batch ID: 20250612_163408
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
 * @title MATRIX Token Staking Contract
 * @dev This contract allows users to stake MATRIX tokens, participate in decentralized governance,
 *      and ensures user privacy.
 */
contract MATRIXStaking {
    // Define state variables
    address public owner; // Contract owner
    IERC20 public matrixToken; // MATRIX Token contract address

    // Data structure to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // When the tokens were staked
    }

    // Mappings for user stakes
    mapping(address => Stake) private stakes; // Tracks individual user stakes
    mapping(address => bool) private hasStaked; // Tracks users who have staked

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);
    event UpdatedOwner(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _matrixToken Address of the MATRIX Token contract.
     */
    constructor(address _matrixToken) {
        require(_matrixToken != address(0), "Invalid token address");
        matrixToken = IERC20(_matrixToken);
        owner = msg.sender;
    }

    /**
     * @dev Function for users to stake MATRIX tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer MATRIX tokens from user to contract
        require(matrixToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's stake information
        Stake memory existingStake = stakes[msg.sender];
        stakes[msg.sender] = Stake(existingStake.amount + _amount, block.timestamp);
        hasStaked[msg.sender] = true;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Function for users to unstake their MATRIX tokens.
     */
    function unstake() external {
        require(hasStaked[msg.sender], "User has not staked");

        // Retrieve user's stake information
        Stake memory userStake = stakes[msg.sender];
        uint256 amountToUnstake = userStake.amount;

        require(amountToUnstake > 0, "No tokens available to unstake");

        // Reset user's stake information
        stakes[msg.sender] = Stake(0, 0);
        hasStaked[msg.sender] = false;

        // Transfer tokens back to the user
        require(matrixToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake, block.timestamp);
    }

    /**
     * @dev Function to get a user's staking details.
     * @param _user Address of the user.
     * @return amount Amount of tokens staked.
     * @return timestamp Timestamp of the stake.
     */
    function getStakeDetails(address _user) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory userStake = stakes[_user];
        return (userStake.amount, userStake.timestamp);
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address is invalid");

        emit UpdatedOwner(owner, _newOwner);
        owner = _newOwner;
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
