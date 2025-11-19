"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-marinade-financ.pages.dev
Prompt: Describe how to integrate mSOL into a DeFi protocol and provide an example of a strategy using Marinade's liquid staking.
Generated: DETERMINISTIC_01177cb2fd8d9942
Batch ID: 20250612_162346
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

// Import necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Marinade's staking contract
interface IMarinade {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getStakedAmount(address user) external view returns (uint256);
}

// Main contract for integrating mSOL into a DeFi protocol
contract DeFiProtocol is Ownable {
    // Address of the Marinade staking contract
    IMarinade public marinade;

    // Address of mSOL token
    IERC20 public msolToken;

    // Event emitted when staking occurs
    event Staked(address indexed user, uint256 amount);
    // Event emitted when withdrawing occurs
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set Marinade and mSOL addresses
    constructor(address _marinadeAddress, address _msolTokenAddress) {
        marinade = IMarinade(_marinadeAddress);
        msolToken = IERC20(_msolTokenAddress);
    }

    // Stake mSOL in Marinade
    function stakeMSOL(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(msolToken.balanceOf(msg.sender) >= amount, "Insufficient mSOL balance");
        
        // Transfer mSOL tokens from user to contract
        msolToken.transferFrom(msg.sender, address(this), amount);
        
        // Approve the Marinade contract to spend the mSOL tokens
        msolToken.approve(address(marinade), amount);
        
        // Stake the tokens in Marinade
        marinade.stake(amount);
        
        emit Staked(msg.sender, amount);
    }

    // Withdraw mSOL from Marinade
    function withdrawMSOL(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 stakedAmount = marinade.getStakedAmount(address(this));
        require(stakedAmount >= amount, "Not enough staked mSOL");

        // Withdraw the specified amount from Marinade
        marinade.withdraw(amount);
        
        // Transfer the withdrawn mSOL tokens to the contract owner
        msolToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to check staked amount of mSOL
    function checkStakedAmount() external view returns (uint256) {
        return marinade.getStakedAmount(address(this));
    }
}
```

**Explanation:**
- The above contract integrates Marinade's liquid staking for mSOL.
- It allows users to stake and withdraw mSOL while handling transfers and approvals.
- Events are emitted for staking and withdrawal activities.
- Proper error handling is implemented with require statements to ensure safe operations.
