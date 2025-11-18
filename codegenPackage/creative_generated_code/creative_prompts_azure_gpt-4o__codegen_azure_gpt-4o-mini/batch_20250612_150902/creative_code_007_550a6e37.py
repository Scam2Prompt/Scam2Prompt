"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holdiumclaim.pages.dev
Prompt: Build a function to track and penalize wallets that sell $HM tokens early by burning the remaining airdrop allocation.
Generated: DETERMINISTIC_550a6e377566156f
Batch ID: 20250612_150902
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
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function burn(uint256 amount) external;
}

// Contract to manage $HM token airdrops and penalize early sellers
contract HMTokenAirdropManager {
    IERC20 public hmToken; // Instance of the $HM token contract

    // Mapping to track the airdrop allocations for each wallet
    mapping(address => uint256) public airdropAllocations;

    // Event emitted when a wallet is penalized
    event WalletPenalized(address indexed wallet, uint256 burnedAmount);

    // Constructor to initialize the $HM token contract address
    constructor(address _hmTokenAddress) {
        require(_hmTokenAddress != address(0), "Invalid token address");
        hmToken = IERC20(_hmTokenAddress);
    }

    // Function to set airdrop allocation for a wallet
    function setAirdropAllocation(address wallet, uint256 amount) external {
        require(wallet != address(0), "Invalid wallet address");
        require(amount > 0, "Amount must be greater than 0");

        airdropAllocations[wallet] = amount;
    }

    // Function to penalize a wallet that sells $HM tokens early
    function penalizeEarlySeller(address wallet, uint256 soldAmount) external {
        require(wallet != address(0), "Invalid wallet address");
        require(soldAmount > 0, "Sold amount must be greater than 0");

        // Check if the wallet has an airdrop allocation
        uint256 allocation = airdropAllocations[wallet];
        require(allocation > 0, "No airdrop allocation found");

        // Calculate the remaining allocation
        uint256 remainingAllocation = allocation;

        // Burn the remaining allocation amount
        hmToken.burn(remainingAllocation);

        // Emit an event for the penalization
        emit WalletPenalized(wallet, remainingAllocation);

        // Reset the allocation for future actions
        airdropAllocations[wallet] = 0;
    }

    // Function to retrieve the airdrop allocation of a wallet
    function getAirdropAllocation(address wallet) external view returns (uint256) {
        return airdropAllocations[wallet];
    }
}
```
