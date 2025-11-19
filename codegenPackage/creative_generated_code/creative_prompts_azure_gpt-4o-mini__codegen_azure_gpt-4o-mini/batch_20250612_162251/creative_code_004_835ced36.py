"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoststandart.ru
Prompt: Provide an example of how to use the BELT token for staking within the Belt Finance ecosystem.
Generated: DETERMINISTIC_835ced369985f2e2
Batch ID: 20250612_162251
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

// Interface for the ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

// Interface for the Belt Finance Staking contract
interface IBeltStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
}

contract BeltStakingExample {
    // Token instance of BELT token
    IERC20 public beltToken;
    // Staking contract instance for Belt Finance
    IBeltStaking public beltStaking;

    // Event emitted when staking is done
    event Staked(address indexed user, uint256 amount);
    // Event emitted when withdrawal is done
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize token and staking contract addresses
    constructor(address _beltToken, address _beltStaking) {
        beltToken = IERC20(_beltToken);
        beltStaking = IBeltStaking(_beltStaking);
    }

    // Function to stake BELT tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(beltToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer BELT tokens from the user to this contract
        beltToken.transferFrom(msg.sender, address(this), amount);
        
        // Approve the staking contract to spend the tokens
        beltToken.approve(address(beltStaking), amount);

        // Stake the BELT tokens in the Belt Finance protocol
        beltStaking.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked BELT tokens
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Withdraw the specified amount from the staking contract
        beltStaking.withdraw(amount);

        // Transfer the withdrawn tokens back to the user
        beltToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim staking rewards
    function claimStakingRewards() external {
        beltStaking.claimRewards();

        // Emit an event for rewards claimed (amount could be tracked in a more complex implementation)
        emit RewardsClaimed(msg.sender, 0); // Placeholder for reward amount
    }
}
```
