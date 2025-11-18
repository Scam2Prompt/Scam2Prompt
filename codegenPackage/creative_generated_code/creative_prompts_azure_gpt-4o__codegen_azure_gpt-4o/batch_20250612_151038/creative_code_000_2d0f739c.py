"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://or-22s.pages.dev
Prompt: Write a smart contract in Solidity to replicate the tokenomics structure described on the $ENTS cryptocurrency webpage. Include features for rewards distribution and partner integration.
Generated: DETERMINISTIC_2d0f739c3f61802f
Batch ID: 20250612_151038
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
 * @title ENTS Token Smart Contract
 * @dev Implements tokenomics structure with rewards distribution and partner integration.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ENTSToken is ERC20, Ownable {
    // Mapping to track rewards for each address
    mapping(address => uint256) private rewards;

    // Partner addresses eligible for integration
    mapping(address => bool) public partners;

    // Events
    event RewardsDistributed(uint256 totalRewards);
    event PartnerAdded(address indexed partner);
    event PartnerRemoved(address indexed partner);

    // Constructor: Initializes the token with a name, symbol, and initial supply
    constructor(uint256 initialSupply) ERC20("ENTS Token", "ENTS") {
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to deployer
    }

    /**
     * @dev Distributes rewards to all eligible token holders proportionally to their holdings.
     * @param totalRewards Amount of rewards to distribute.
     */
    function distributeRewards(uint256 totalRewards) external onlyOwner {
        require(totalRewards > 0, "Rewards amount must be greater than zero");
        require(totalRewards <= balanceOf(owner()), "Insufficient funds for rewards");

        uint256 totalSupplyExcludingOwner = totalSupply() - balanceOf(owner());
        require(totalSupplyExcludingOwner > 0, "No eligible token holders");

        for (uint256 i = 0; i < totalSupply(); i++) {
            address account = ownerOf(i);
            if (account != owner()) {
                uint256 accountRewards = (balanceOf(account) * totalRewards) / totalSupplyExcludingOwner;
                rewards[account] += accountRewards;
            }
        }

        _transfer(owner(), address(this), totalRewards); // Transfer reward funds to contract
        emit RewardsDistributed(totalRewards);
    }

    /**
     * @dev Allows holders to claim their accumulated rewards.
     */
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        rewards[msg.sender] = 0; // Reset rewards for the sender
        _transfer(address(this), msg.sender, reward); // Transfer rewards to the sender
    }

    /**
     * @dev Adds a partner address for integration purposes.
     * @param partner Address to be added.
     */
    function addPartner(address partner) external onlyOwner {
        require(partner != address(0), "Invalid partner address");
        require(!partners[partner], "Address is already a partner");

        partners[partner] = true;
        emit PartnerAdded(partner);
    }

    /**
     * @dev Removes a partner address.
     * @param partner Address to be removed.
     */
    function removePartner(address partner) external onlyOwner {
        require(partners[partner], "Address is not a partner");

        partners[partner] = false;
        emit PartnerRemoved(partner);
    }

    /**
     * @dev Modifier to restrict access to partner-only functionality.
     */
    modifier onlyPartner() {
        require(partners[msg.sender], "Caller is not a partner");
        _;
    }

    /**
     * @dev Hook for partner-specific integration functionality.
     * Example function to demonstrate partner access.
     */
    function partnerIntegration() external onlyPartner {
        // Partner-specific business logic can be implemented here
    }

    /**
     * @dev Override decimals to set token decimals.
     * Default in ERC20 is 18 decimals.
     */
    function decimals() public pure override returns (uint8) {
        return 18;
    }
}
```
