"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefi.finance
Prompt: How can I integrate Beefi Finance's tools into a smart contract for automated staking?
Generated: DETERMINISTIC_7c6442829521b4ce
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

// Importing the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Beefi Finance staking functions
interface IBeefiStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function earned(address account) external view returns (uint256);
}

contract BeefiIntegration is Ownable {
    // State variables
    IERC20 public token; // Token to be staked
    IBeefiStaking public beefiStaking; // Address of the Beefi staking contract

    // Event emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token and Beefi staking address
    constructor(address _token, address _beefiStaking) {
        require(_token != address(0), "Token address cannot be zero");
        require(_beefiStaking != address(0), "Beefi staking address cannot be zero");

        token = IERC20(_token);
        beefiStaking = IBeefiStaking(_beefiStaking);
    }

    // Function to stake tokens in Beefi Finance
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Approve Beefi staking contract to spend the tokens
        token.approve(address(beefiStaking), amount);
        
        // Stake the tokens in Beefi Finance
        beefiStaking.stake(amount);

        emit TokensStaked(msg.sender, amount);
    }

    // Function to withdraw tokens from Beefi Finance
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");

        // Withdraw tokens from Beefi Finance
        beefiStaking.withdraw(amount);
        
        // Transfer the withdrawn tokens to the contract owner
        token.transfer(msg.sender, amount);

        emit TokensWithdrawn(msg.sender, amount);
    }

    // Function to check the earned rewards for a user
    function getEarnedRewards() external view returns (uint256) {
        return beefiStaking.earned(msg.sender);
    }
}
```
