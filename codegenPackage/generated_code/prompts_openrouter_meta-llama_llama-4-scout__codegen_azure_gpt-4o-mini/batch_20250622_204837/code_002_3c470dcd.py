"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: "Develop a Solidity smart contract code for the CRUDO token, including its utility, tokenomics, and distribution phases as described in the Crudo Protocol's whitepaper."
Generated: DETERMINISTIC_3c470dcd9f62480f
Batch ID: 20250622_204837
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CRUDO Token
 * @dev Implementation of the CRUDO token as per the Crudo Protocol's whitepaper.
 * This token follows the ERC20 standard and includes features for tokenomics and distribution.
 */
contract CRUDO is ERC20, Ownable {
    // Total supply of the CRUDO token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 billion tokens

    // Distribution phases
    enum DistributionPhase { PreSale, PublicSale, Liquidity, Team, Reserve }
    DistributionPhase public currentPhase;

    // Mapping to track the amount allocated for each phase
    mapping(DistributionPhase => uint256) public phaseAllocations;

    // Events for logging
    event TokensDistributed(DistributionPhase phase, address recipient, uint256 amount);

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * It also sets the initial distribution allocations.
     */
    constructor() ERC20("CRUDO Token", "CRUDO") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Set initial allocations for each distribution phase
        phaseAllocations[DistributionPhase.PreSale] = 200_000_000 * 10 ** decimals(); // 20%
        phaseAllocations[DistributionPhase.PublicSale] = 300_000_000 * 10 ** decimals(); // 30%
        phaseAllocations[DistributionPhase.Liquidity] = 200_000_000 * 10 ** decimals(); // 20%
        phaseAllocations[DistributionPhase.Team] = 150_000_000 * 10 ** decimals(); // 15%
        phaseAllocations[DistributionPhase.Reserve] = 150_000_000 * 10 ** decimals(); // 15%

        // Set the initial distribution phase
        currentPhase = DistributionPhase.PreSale;
    }

    /**
     * @dev Function to change the current distribution phase.
     * @param _newPhase The new distribution phase to set.
     */
    function setDistributionPhase(DistributionPhase _newPhase) external onlyOwner {
        currentPhase = _newPhase;
    }

    /**
     * @dev Function to distribute tokens to a recipient.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to distribute.
     */
    function distributeTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(phaseAllocations[currentPhase] >= amount, "Insufficient allocation for current phase");

        // Transfer tokens to the recipient
        _transfer(msg.sender, recipient, amount);
        phaseAllocations[currentPhase] -= amount;

        emit TokensDistributed(currentPhase, recipient, amount);
    }

    /**
     * @dev Function to retrieve the remaining allocation for the current distribution phase.
     * @return The remaining allocation for the current phase.
     */
    function remainingAllocation() external view returns (uint256) {
        return phaseAllocations[currentPhase];
    }

    /**
     * @dev Function to withdraw any accidentally sent Ether to the contract.
     */
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
