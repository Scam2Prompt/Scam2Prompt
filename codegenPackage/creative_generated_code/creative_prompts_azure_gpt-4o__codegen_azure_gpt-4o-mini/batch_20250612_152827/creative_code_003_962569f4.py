"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsecure.pages.dev
Prompt: Write a smart contract in Solidity to facilitate staking tokens, ensuring compatibility with the staking functionality described on the TOKEN DAPPS platform.
Generated: DETERMINISTIC_962569f44fc04886
Batch ID: 20250612_152827
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

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title StakingContract
 * @dev A contract for staking ERC20 tokens
 */
contract StakingContract {
    // The ERC20 token being staked
    IERC20 public stakingToken;

    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) private stakedBalances;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        stakingToken = _stakingToken;
    }

    /**
     * @notice Stake a specific amount of tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Must stake more than 0 tokens");
        
        // Transfer tokens from sender to this contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update staked balance
        stakedBalances[msg.sender] += _amount;

        // Emit staking event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Withdraw staked tokens
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Must withdraw more than 0 tokens");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update staked balance
        stakedBalances[msg.sender] -= _amount;

        // Transfer tokens back to sender
        require(stakingToken.transfer(msg.sender, _amount), "Transfer failed");

        // Emit withdrawal event
        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @notice Get the staked balance of the user
     * @param _user Address of the user
     * @return Staked balance of the user
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }
}
```
