"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad.seedify.de
Prompt: Provide an example of a Solidity function for distributing tokens to investors after a successful fundraising campaign on a launchpad.
Generated: DETERMINISTIC_7780174a8967426d
Batch ID: 20250612_151858
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
 * @title TokenDistributor
 * @dev A contract to distribute tokens to investors after a successful fundraising campaign.
 */
contract TokenDistributor {
    // Address of the token contract
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Mapping to store investor addresses and their allocated tokens
    mapping(address => uint256) public allocations;

    // Flag to ensure distribution happens only once
    bool public distributionComplete;

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token address and owner.
     * @param _tokenAddress Address of the token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to set token allocations for investors.
     * @param _investors Array of investor addresses.
     * @param _amounts Array of corresponding token amounts.
     */
    function setAllocations(address[] memory _investors, uint256[] memory _amounts) external onlyOwner {
        require(_investors.length == _amounts.length, "Investors and amounts arrays must have the same length");
        
        for (uint256 i = 0; i < _investors.length; i++) {
            require(_investors[i] != address(0), "Investor address cannot be zero");
            require(_amounts[i] > 0, "Allocated amount must be greater than zero");
            allocations[_investors[i]] = _amounts[i];
        }
    }

    /**
     * @dev Function to distribute tokens to all investors based on their allocations.
     * @notice Can only be called once.
     */
    function distributeTokens() external onlyOwner {
        require(!distributionComplete, "Tokens have already been distributed");
        
        for (address investor in allocations) {
            uint256 amount = allocations[investor];
            require(amount > 0, "No allocation for this investor");
            
            bool success = IERC20(tokenAddress).transfer(investor, amount);
            require(success, "Token transfer failed");
        }

        distributionComplete = true;
    }
}

/**
 * @dev Interface for ERC20 token standard
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
