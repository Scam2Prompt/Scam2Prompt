"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matmomomey.pages.dev
Prompt: Develop a smart contract that supports staking and unstaking tokens, ensuring compatibility with the ClaimTokens staking pool.
Generated: DETERMINISTIC_c767fad5770bf26e
Batch ID: 20250612_150226
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
 * @dev Smart contract for staking and unstaking tokens with ClaimTokens staking pool compatibility.
 */
contract StakingContract {
    // Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    IERC20 public stakingToken; // The token being staked
    address public owner; // Contract owner
    uint256 public totalStaked; // Total amount of tokens staked

    // Mapping to track staked balances and timestamps
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public stakingTimestamps;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staking contract.
     * @param _stakingToken Address of the staking token contract.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        owner = msg.sender;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the user to the contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update user staking balance and total staked amount
        stakedBalances[msg.sender] += _amount;
        stakingTimestamps[msg.sender] = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update user staking balance and total staked amount
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens from the contract back to the user
        bool success = stakingToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Get the total balance staked by a specific user.
     * @param _user Address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Get the total tokens staked in the contract.
     * @return The total staked amount.
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    /**
     * @dev Fallback function to prevent sending Ether directly to the contract.
     */
    fallback() external {
        revert("Ether not accepted");
    }

    /**
     * @dev Receive function to prevent sending Ether directly to the contract.
     */
    receive() external payable {
        revert("Ether not accepted");
    }
}
```
