"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://627d8bea.soiletdemo.pages.dev
Prompt: Write a smart contract in Solidity for staking $MGMES tokens, ensuring compatibility with Web3Payments and Web3Toolkit technology as described in The Meme Games Token documentation.
Generated: DETERMINISTIC_87413aedfaa59fb2
Batch ID: 20250612_152321
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
 * @title StakingContract
 * @dev A smart contract for staking MGMES tokens with compatibility for Web3Payments and Web3Toolkit.
 */
contract StakingContract {
    // MGMES token interface
    IERC20 private mgmesToken;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakes;

    // Mapping to track timestamps of when users staked tokens
    mapping(address => uint256) public stakingTimestamps;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Owner of the contract
    address public owner;

    // Events for staking and withdrawing
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to set the MGMES token address and initialize the owner.
     * @param _mgmesToken The address of the MGMES token contract.
     */
    constructor(address _mgmesToken) {
        require(_mgmesToken != address(0), "Invalid token address");
        mgmesToken = IERC20(_mgmesToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to stake MGMES tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(mgmesToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(mgmesToken.allowance(msg.sender, address(this)) >= _amount, "Allowance too low");

        // Transfer tokens from the user to the contract
        bool success = mgmesToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update staking balance and timestamp
        stakes[msg.sender] += _amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        // Update total staked tokens
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw staked MGMES tokens.
     */
    function withdraw() external {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No tokens to withdraw");

        // Reset user's stake and timestamp
        stakes[msg.sender] = 0;
        stakingTimestamps[msg.sender] = 0;

        // Update total staked tokens
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to the user
        bool success = mgmesToken.transfer(msg.sender, stakedAmount);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Function to get the staked tokens of a user.
     * @param _user The address of the user.
     * @return The amount of staked tokens.
     */
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakes[_user];
    }

    /**
     * @dev Function to get the staking timestamp of a user.
     * @param _user The address of the user.
     * @return The timestamp when the user staked tokens.
     */
    function getStakingTimestamp(address _user) external view returns (uint256) {
        return stakingTimestamps[_user];
    }

    /**
     * @dev Function to withdraw accidentally sent tokens (other than MGMES) by the contract owner.
     * @param _tokenAddress The address of the token to withdraw.
     * @param _amount The amount of tokens to withdraw.
     */
    function recoverTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(mgmesToken), "Cannot withdraw MGMES tokens");
        IERC20 token = IERC20(_tokenAddress);
        require(token.balanceOf(address(this)) >= _amount, "Insufficient token balance");
        bool success = token.transfer(owner, _amount);
        require(success, "Token transfer failed");
    }
}

/**
 * @title IERC20
 * @dev Minimal ERC20 interface to interact with MGMES token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}
```
