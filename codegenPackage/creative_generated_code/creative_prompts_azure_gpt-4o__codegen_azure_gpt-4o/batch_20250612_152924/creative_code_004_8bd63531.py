"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: Develop a smart contract for the BlastUP token buy-back mechanism, using a percentage of funds raised by projects launched on the platform.
Generated: DETERMINISTIC_8bd635316a7da10d
Batch ID: 20250612_152924
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
 * @title BlastUP Token Buy-Back Mechanism
 * @dev This smart contract handles the buy-back mechanism for the BlastUP token by using a percentage
 *      of funds raised by projects launched on the platform.
 */
contract BlastUPBuyBack {

    // State variables
    address public owner;                       // Contract owner address
    address public blastUPToken;                // Address of the BlastUP token contract
    uint256 public buyBackPercentage;           // Percentage of funds allocated for buy-back (e.g., 10 for 10%)
    uint256 public totalFundsRaised;            // Total funds raised by projects on the platform

    // Events
    event FundsReceived(address indexed sender, uint256 amount);
    event TokensBoughtBack(uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the owner and token address.
     * @param _blastUPToken Address of the BlastUP token contract.
     * @param _buyBackPercentage Percentage of funds allocated for buy-back.
     */
    constructor(address _blastUPToken, uint256 _buyBackPercentage) {
        require(_blastUPToken != address(0), "Invalid token address");
        require(_buyBackPercentage > 0 && _buyBackPercentage <= 100, "Invalid buy-back percentage");

        owner = msg.sender;
        blastUPToken = _blastUPToken;
        buyBackPercentage = _buyBackPercentage;
    }

    /**
     * @dev Fallback function to receive funds.
     */
    receive() external payable {
        require(msg.value > 0, "Zero funds received");
        totalFundsRaised += msg.value;
        emit FundsReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function to perform the token buy-back using the allocated funds.
     */
    function buyBackTokens() external onlyOwner {
        // Calculate the amount allocated for buy-back
        uint256 buyBackAmount = (totalFundsRaised * buyBackPercentage) / 100;

        require(buyBackAmount <= address(this).balance, "Insufficient contract balance");

        // Transfer funds to the token contract for buy-back
        (bool success, ) = blastUPToken.call{value: buyBackAmount}("");
        require(success, "Buy-back transaction failed");

        // Log the buy-back event
        emit TokensBoughtBack(buyBackAmount);

        // Reduce the total funds raised
        totalFundsRaised -= buyBackAmount;
    }

    /**
     * @dev Function to update the buy-back percentage.
     * @param _buyBackPercentage New buy-back percentage.
     */
    function updateBuyBackPercentage(uint256 _buyBackPercentage) external onlyOwner {
        require(_buyBackPercentage > 0 && _buyBackPercentage <= 100, "Invalid buy-back percentage");
        buyBackPercentage = _buyBackPercentage;
    }

    /**
     * @dev Function to withdraw remaining funds from the contract.
     * @param _to Address to send the withdrawn funds.
     */
    function withdrawFunds(address payable _to) external onlyOwner {
        require(_to != address(0), "Invalid recipient address");

        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = _to.call{value: contractBalance}("");
        require(success, "Withdrawal transaction failed");
    }
}
```
