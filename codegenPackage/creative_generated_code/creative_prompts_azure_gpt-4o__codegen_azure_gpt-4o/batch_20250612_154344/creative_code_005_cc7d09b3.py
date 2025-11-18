"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jpegsfun.pages.dev
Prompt: Implement a smart contract that adheres to the no-presales, no-whitelists, and no-team-allocations policy described on jpegs.fun.
Generated: DETERMINISTIC_cc7d09b36de6167c
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Solidity smart contract implementing the requested policies:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleNFT
 * @dev An ERC721-compliant smart contract with no presales, no whitelists, and no team allocations.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SimpleNFT is ERC721, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Price per NFT (in wei)
    uint256 public constant PRICE = 0.05 ether;

    // Counter to keep track of minted NFTs
    uint256 public totalMinted;

    /**
     * @dev Constructor initializing the token name and symbol.
     */
    constructor() ERC721("SimpleNFT", "SNFT") {}

    /**
     * @dev Public function to mint an NFT.
     * @param quantity The number of NFTs to mint.
     */
    function mint(uint256 quantity) external payable {
        // Ensure the requested quantity does not exceed the maximum supply
        require(totalMinted + quantity <= MAX_SUPPLY, "Exceeds maximum supply");

        // Ensure the correct amount of ether is sent
        require(msg.value == PRICE * quantity, "Incorrect ETH amount");

        // Mint the requested quantity of NFTs
        for (uint256 i = 0; i < quantity; i++) {
            _mint(msg.sender, totalMinted + i);
        }

        // Update the total minted count
        totalMinted += quantity;
    }

    /**
     * @dev Function for withdrawing contract balance. Restricted to the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct payments not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct payments not allowed");
    }
}
```

### Key Features:
1. **No Presales:** The contract does not include any presale logic.
2. **No Whitelists:** There is no whitelist mechanism; anyone can mint as long as they meet the conditions.
3. **No Team Allocations:** No special allocation or pre-minting is done for the team or any privileged parties.
4. **Error Handling:** Fallback and receive functions prevent unintended ETH transfers. Proper `require` statements ensure minting conditions are met.
5. **Production-Ready:** Follows best practices, uses OpenZeppelin libraries, and is compliant with ERC721 standards.
