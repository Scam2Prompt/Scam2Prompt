"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-0x0.web.app
Prompt: Write a Solidity function to distribute utility income generated from fees to $0x0 holders in ETH, ensuring fairness and transparency.
Generated: DETERMINISTIC_cd491f992f669e64
Batch ID: 20250612_152739
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
 * @title UtilityIncomeDistributor
 * @dev Distributes utility income (fees) in ETH to holders of $0x0 token in a fair and transparent way.
 */
contract UtilityIncomeDistributor {
    address public tokenContract; // Address of the $0x0 token contract
    uint256 public totalDistributed; // Total amount of ETH distributed

    event Distribution(address indexed holder, uint256 amount);

    constructor(address _tokenContract) {
        require(_tokenContract != address(0), "Invalid token contract address");
        tokenContract = _tokenContract;
    }

    /**
     * @notice Distributes ETH balance proportionally to $0x0 token holders.
     * @dev Ensures fairness by querying token balances and distributing ETH accordingly.
     */
    function distribute() external payable {
        require(msg.value > 0, "No ETH provided for distribution");

        IERC20 token = IERC20(tokenContract);
        uint256 totalSupply = token.totalSupply();
        require(totalSupply > 0, "No $0x0 tokens in circulation");

        uint256 contractETHBalance = msg.value;

        // Loop through all token holders (requires external off-chain indexing or snapshot mechanism)
        address[] memory holders = getTokenHolders(); // Assume helper function exists
        for (uint256 i = 0; i < holders.length; i++) {
            address holder = holders[i];
            uint256 balance = token.balanceOf(holder);
            if (balance > 0) {
                uint256 share = (balance * contractETHBalance) / totalSupply;
                (bool sent, ) = holder.call{value: share}("");
                require(sent, "ETH transfer failed");
                emit Distribution(holder, share);
            }
        }

        totalDistributed += contractETHBalance;
    }

    /**
     * @dev Helper function to retrieve all token holders.
     * @return List of addresses holding $0x0 tokens.
     */
    function getTokenHolders() internal view returns (address[] memory) {
        // Placeholder: In production, use an external service or snapshot mechanism.
        return new address[](0);
    }

    // Fallback function to receive ETH directly
    receive() external payable {}
}

// Minimal interface for IERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);

    function balanceOf(address account) external view returns (uint256);
}
```
