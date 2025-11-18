"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Generate a Solidity contract for the $HEHE airdrop, ensuring that 666 recipients are randomly selected and rewarded with tokens.
Generated: DETERMINISTIC_0a31c5792fbce780
Batch ID: 20250612_153517
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
 * @title HEHEAirdrop
 * @dev A contract to perform an airdrop of $HEHE tokens to 666 randomly selected recipients.
 */
contract HEHEAirdrop {
    // Address of the $HEHE token contract
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Maximum number of recipients for the airdrop
    uint256 public constant MAX_RECIPIENTS = 666;

    // Array to store eligible addresses
    address[] public eligibleAddresses;

    // Flag to check if airdrop has been executed
    bool public airdropExecuted;

    // Event emitted when airdrop is successfully executed
    event AirdropExecuted(address[] recipients, uint256 amount);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Modifier to ensure the airdrop has not yet been executed
    modifier airdropNotExecuted() {
        require(!airdropExecuted, "Airdrop has already been executed");
        _;
    }

    /**
     * @dev Constructor sets the owner and token address.
     * @param _tokenAddress Address of the $HEHE token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Add eligible addresses for the airdrop.
     * @param addresses List of addresses to be added.
     */
    function addEligibleAddresses(address[] memory addresses) external onlyOwner {
        require(addresses.length > 0, "Must provide addresses");
        for (uint256 i = 0; i < addresses.length; i++) {
            require(addresses[i] != address(0), "Invalid address");
            eligibleAddresses.push(addresses[i]);
        }
    }

    /**
     * @dev Execute the airdrop to 666 randomly selected recipients.
     * @param tokenAmount Amount of tokens to distribute per recipient.
     */
    function executeAirdrop(uint256 tokenAmount) external onlyOwner airdropNotExecuted {
        require(eligibleAddresses.length >= MAX_RECIPIENTS, "Not enough eligible addresses");
        require(tokenAmount > 0, "Token amount must be greater than zero");

        // Shuffle the eligibleAddresses array for randomness
        for (uint256 i = eligibleAddresses.length - 1; i > 0; i--) {
            uint256 j = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, i))) % (i + 1);
            (eligibleAddresses[i], eligibleAddresses[j]) = (eligibleAddresses[j], eligibleAddresses[i]);
        }

        // Select the first 666 recipients
        address[] memory recipients = new address[](MAX_RECIPIENTS);
        for (uint256 i = 0; i < MAX_RECIPIENTS; i++) {
            recipients[i] = eligibleAddresses[i];
        }

        // Transfer tokens to each recipient
        for (uint256 i = 0; i < MAX_RECIPIENTS; i++) {
            bool success = IERC20(tokenAddress).transfer(recipients[i], tokenAmount);
            require(success, "Token transfer failed");
        }

        // Mark airdrop as executed
        airdropExecuted = true;

        emit AirdropExecuted(recipients, tokenAmount);
    }

    /**
     * @dev Returns the list of eligible addresses.
     * @return Array of eligible addresses.
     */
    function getEligibleAddresses() external view returns (address[] memory) {
        return eligibleAddresses;
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
