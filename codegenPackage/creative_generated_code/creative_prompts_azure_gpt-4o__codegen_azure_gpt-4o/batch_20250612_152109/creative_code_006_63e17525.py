"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguins-gainsassociates.pages.dev
Prompt: Write a smart contract to enable users to purchase tokens from listed Web3 projects on the GAINS Associates platform, ensuring compliance with the platform's terms of service.
Generated: DETERMINISTIC_63e175254cfe88a1
Batch ID: 20250612_152109
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
 * @title GAINS Associates Token Purchase Smart Contract
 * @author Your Name
 * @notice This contract enables users to purchase tokens from listed Web3 projects on the GAINS Associates platform.
 * @dev Ensure compliance with the platform's terms of service.
 */
contract TokenPurchase {
    // Declare necessary state variables

    address public owner; // Owner of the contract
    uint256 public platformFee; // Fee collected by GAINS Associates (in percentage, e.g., 2 = 2%)
    mapping(address => bool) public listedProjects; // Mapping to track listed projects

    event ProjectListed(address indexed projectAddress);
    event ProjectDelisted(address indexed projectAddress);
    event TokensPurchased(address indexed projectAddress, address indexed buyer, uint256 amount, uint256 feePaid);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier onlyListedProject(address projectAddress) {
        require(listedProjects[projectAddress], "Project is not listed");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner and platform fee.
     * @param _platformFee Percentage fee charged by GAINS Associates on each purchase.
     */
    constructor(uint256 _platformFee) {
        owner = msg.sender;
        platformFee = _platformFee;
    }

    /**
     * @dev List a new Web3 project on the platform.
     * @param projectAddress Address of the project to list.
     */
    function listProject(address projectAddress) external onlyOwner {
        require(projectAddress != address(0), "Invalid project address");
        listedProjects[projectAddress] = true;
        emit ProjectListed(projectAddress);
    }

    /**
     * @dev Delist a Web3 project from the platform.
     * @param projectAddress Address of the project to delist.
     */
    function delistProject(address projectAddress) external onlyOwner {
        require(listedProjects[projectAddress], "Project is not listed");
        listedProjects[projectAddress] = false;
        emit ProjectDelisted(projectAddress);
    }

    /**
     * @dev Purchase tokens from a listed project.
     * @param projectAddress Address of the project.
     * @param tokenAmount Amount of tokens to purchase.
     */
    function purchaseTokens(address projectAddress, uint256 tokenAmount) external payable onlyListedProject(projectAddress) {
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(msg.value > 0, "Payment required");

        // Calculate platform fee
        uint256 fee = (msg.value * platformFee) / 100;
        uint256 paymentToProject = msg.value - fee;

        // Transfer fee to the platform owner
        (bool feeTransferSuccess, ) = owner.call{value: fee}("");
        require(feeTransferSuccess, "Fee transfer failed");

        // Transfer payment to the project
        (bool projectTransferSuccess, ) = projectAddress.call{value: paymentToProject}("");
        require(projectTransferSuccess, "Payment to project failed");

        emit TokensPurchased(projectAddress, msg.sender, tokenAmount, fee);
    }

    /**
     * @dev Withdraw contract balance (owner-only).
     */
    function withdrawBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance available to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to receive ETH directly.
     */
    receive() external payable {}

    /**
     * @dev Update platform fee (owner-only).
     * @param _newPlatformFee The new platform fee percentage.
     */
    function updatePlatformFee(uint256 _newPlatformFee) external onlyOwner {
        require(_newPlatformFee >= 0 && _newPlatformFee <= 100, "Invalid platform fee percentage");
        platformFee = _newPlatformFee;
    }
}
```
