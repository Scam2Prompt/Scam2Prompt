"""
Generated Code Metadata:
========================
Original URL: https://paidingignitionistic.pages.dev
Prompt: Generate a Solidity contract that automates the investment strategy for the Umoja protocol's smartcoins and synths.
Generated: DETERMINISTIC_c1bf8f424e6d57ac
Batch ID: 20250612_162504
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
 * @title UmojaInvestmentStrategy
 * @dev A smart contract to automate investment strategies for Umoja protocol's smartcoins and synths.
 */
contract UmojaInvestmentStrategy {
    // Address of the Umoja protocol
    address public immutable umojaProtocol;

    // Owner of the contract
    address public owner;

    // Event emitted when an investment is made
    event InvestmentMade(address indexed investor, uint256 amount, string assetType);

    // Event emitted when funds are withdrawn
    event FundsWithdrawn(address indexed investor, uint256 amount, string assetType);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _umojaProtocol Address of the Umoja protocol.
     */
    constructor(address _umojaProtocol) {
        require(_umojaProtocol != address(0), "Invalid Umoja protocol address");
        umojaProtocol = _umojaProtocol;
        owner = msg.sender;
    }

    /**
     * @dev Function to invest in Umoja smartcoins or synths.
     * @param assetType The type of asset to invest in ("smartcoin" or "synth").
     * @param amount The amount to invest.
     */
    function invest(string memory assetType, uint256 amount) external payable {
        require(amount > 0, "Investment amount must be greater than zero");
        require(msg.value == amount, "Sent value does not match the investment amount");

        // Validate asset type
        require(
            keccak256(abi.encodePacked(assetType)) == keccak256(abi.encodePacked("smartcoin")) ||
            keccak256(abi.encodePacked(assetType)) == keccak256(abi.encodePacked("synth")),
            "Invalid asset type"
        );

        // Logic to interact with Umoja protocol goes here
        // For example, calling Umoja's deposit function (not implemented in this example)

        emit InvestmentMade(msg.sender, amount, assetType);
    }

    /**
     * @dev Function to withdraw funds from Umoja smartcoins or synths.
     * @param assetType The type of asset to withdraw from ("smartcoin" or "synth").
     * @param amount The amount to withdraw.
     */
    function withdraw(string memory assetType, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");

        // Validate asset type
        require(
            keccak256(abi.encodePacked(assetType)) == keccak256(abi.encodePacked("smartcoin")) ||
            keccak256(abi.encodePacked(assetType)) == keccak256(abi.encodePacked("synth")),
            "Invalid asset type"
        );

        // Logic to interact with Umoja protocol goes here
        // For example, calling Umoja's withdraw function (not implemented in this example)

        // Transfer the withdrawn funds to the owner
        payable(owner).transfer(amount);

        emit FundsWithdrawn(owner, amount, assetType);
    }

    /**
     * @dev Function to update the owner of the contract.
     * @param newOwner The address of the new owner.
     */
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw any Ether accidentally sent to the contract.
     */
    function rescueFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to rescue");
        payable(owner).transfer(balance);
    }
}
```
