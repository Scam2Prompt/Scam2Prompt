"""
Generated Code Metadata:
========================
Original URL: https://freedumfighert.pages.dev
Prompt: Write a Solidity function to implement the staking mechanism for $DUM tokens, ensuring secure and efficient transactions on a decentralized exchange.
Generated: DETERMINISTIC_a96bbecb7c9d51db
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DUMTokenStaking
 * @dev A smart contract for staking $DUM tokens securely and efficiently.
 */
contract DUMTokenStaking {
    IERC20 public dumToken; // Interface for the $DUM token
    address public owner; // Owner of the staking contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when the stake was created
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No active stake found for this user");
        _;
    }

    constructor(address _dumTokenAddress) {
        require(_dumTokenAddress != address(0), "Invalid token address");
        dumToken = IERC20(_dumTokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake $DUM tokens.
     * @param _amount The amount of $DUM tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(
            dumToken.balanceOf(msg.sender) >= _amount,
            "Insufficient token balance"
        );
        require(
            dumToken.allowance(msg.sender, address(this)) >= _amount,
            "Token allowance too low"
        );

        // Transfer tokens from the user to the contract
        bool success = dumToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update the total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows users to unstake their $DUM tokens.
     */
    function unstake() external hasStake(msg.sender) {
        uint256 stakedAmount = stakes[msg.sender].amount;

        // Reset the user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Update the total staked amount
        totalStaked -= stakedAmount;

        // Transfer tokens back to the user
        bool success = dumToken.transfer(msg.sender, stakedAmount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, block.timestamp);
    }

    /**
     * @dev Allows the owner to withdraw any accidentally sent tokens (excluding staked $DUM tokens).
     * @param _tokenAddress The address of the token to withdraw.
     * @param _amount The amount of tokens to withdraw.
     */
    function recoverTokens(address _tokenAddress, uint256 _amount)
        external
        onlyOwner
    {
        require(_tokenAddress != address(dumToken), "Cannot recover staked tokens");
        IERC20 token = IERC20(_tokenAddress);
        bool success = token.transfer(owner, _amount);
        require(success, "Token recovery failed");
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);

    function allowance(address owner, address spender)
        external
        view
        returns (uint256);
}
```
