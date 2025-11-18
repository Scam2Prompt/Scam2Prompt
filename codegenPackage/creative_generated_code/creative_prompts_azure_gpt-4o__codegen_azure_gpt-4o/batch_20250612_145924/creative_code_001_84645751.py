"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-basemafia-com.pages.dev
Prompt: Generate code to implement a buy-back-and-burn mechanism for $MAFIA tokens, ensuring half of the tokens are added to a rewards pool and the other half are burned.
Generated: DETERMINISTIC_84645751aad3a44f
Batch ID: 20250612_145924
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
 * @title BuyBackAndBurn
 * @dev Implements a mechanism to buy back $MAFIA tokens, split them into a rewards pool, and burn the rest.
 */
contract BuyBackAndBurn {
    // Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
        function burn(uint256 amount) external;
    }

    IERC20 public mafiaToken; // $MAFIA token reference
    address public rewardsPool; // Address of the rewards pool
    address public owner; // Contract owner

    event TokensBoughtBack(uint256 amount);
    event TokensBurned(uint256 amount);
    event TokensAddedToRewardsPool(uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize contract parameters.
     * @param _mafiaToken Address of the $MAFIA token contract.
     * @param _rewardsPool Address of the rewards pool.
     */
    constructor(IERC20 _mafiaToken, address _rewardsPool) {
        require(address(_mafiaToken) != address(0), "Invalid $MAFIA token address");
        require(_rewardsPool != address(0), "Invalid rewards pool address");
        mafiaToken = _mafiaToken;
        rewardsPool = _rewardsPool;
        owner = msg.sender;
    }

    /**
     * @dev Buy back $MAFIA tokens from the sender, split them into rewards pool and burning.
     * @param amount Amount of tokens to buy back.
     */
    function buyBackAndBurn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 balance = mafiaToken.balanceOf(msg.sender);
        require(balance >= amount, "Insufficient token balance");

        // Transfer tokens from sender to this contract
        require(mafiaToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Split tokens: Half to rewards pool, half to burn
        uint256 halfAmount = amount / 2;
        uint256 remainingAmount = amount - halfAmount; // Handle odd amounts

        // Transfer half to rewards pool
        require(mafiaToken.transfer(rewardsPool, halfAmount), "Failed to transfer to rewards pool");
        emit TokensAddedToRewardsPool(halfAmount);

        // Burn the other half
        mafiaToken.burn(remainingAmount);
        emit TokensBurned(remainingAmount);

        emit TokensBoughtBack(amount);
    }

    /**
     * @dev Update the rewards pool address.
     * @param _rewardsPool New address of the rewards pool.
     */
    function updateRewardsPool(address _rewardsPool) external onlyOwner {
        require(_rewardsPool != address(0), "Invalid rewards pool address");
        rewardsPool = _rewardsPool;
    }
}
```
