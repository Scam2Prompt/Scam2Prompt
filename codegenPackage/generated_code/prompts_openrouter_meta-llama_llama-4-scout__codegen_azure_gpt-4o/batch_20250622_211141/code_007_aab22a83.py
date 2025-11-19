"""
Generated Code Metadata:
========================
Original URL: https://polygon6d.com
Prompt: Describe the role of the 6D Token in the Polygon 6D ecosystem, and provide a code example in Solidity that demonstrates the token's distribution method and allocation.
Generated: DETERMINISTIC_aab22a83718b614d
Batch ID: 20250622_211141
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
 * @title 6D Token Distribution Contract
 * @dev This contract handles the distribution and allocation of the 6D Token
 *      within the Polygon 6D ecosystem. It ensures proper allocation to
 *      stakeholders such as the team, investors, and community.
 */
contract SixDToken {
    // Token details
    string public name = "6D Token";
    string public symbol = "6DT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Address of the contract owner
    address public owner;

    // Mapping to track balances of token holders
    mapping(address => uint256) public balances;

    // Allocation percentages
    uint256 public constant TEAM_ALLOCATION = 20; // 20%
    uint256 public constant INVESTOR_ALLOCATION = 30; // 30%
    uint256 public constant COMMUNITY_ALLOCATION = 50; // 50%

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event TokensDistributed(uint256 teamTokens, uint256 investorTokens, uint256 communityTokens);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract and mint the total supply.
     * @param _totalSupply The total supply of 6D Tokens.
     */
    constructor(uint256 _totalSupply) {
        owner = msg.sender;
        totalSupply = _totalSupply;
        balances[owner] = _totalSupply; // Assign all tokens to the owner initially
    }

    /**
     * @dev Distribute tokens based on predefined allocation percentages.
     * @param teamAddress Address to receive the team allocation.
     * @param investorAddress Address to receive the investor allocation.
     * @param communityAddress Address to receive the community allocation.
     */
    function distributeTokens(
        address teamAddress,
        address investorAddress,
        address communityAddress
    ) external onlyOwner {
        require(teamAddress != address(0), "Invalid team address");
        require(investorAddress != address(0), "Invalid investor address");
        require(communityAddress != address(0), "Invalid community address");

        // Calculate token allocations
        uint256 teamTokens = (totalSupply * TEAM_ALLOCATION) / 100;
        uint256 investorTokens = (totalSupply * INVESTOR_ALLOCATION) / 100;
        uint256 communityTokens = (totalSupply * COMMUNITY_ALLOCATION) / 100;

        // Ensure the owner has enough tokens to distribute
        require(balances[owner] >= (teamTokens + investorTokens + communityTokens), "Insufficient tokens for distribution");

        // Transfer tokens to respective addresses
        _transfer(owner, teamAddress, teamTokens);
        _transfer(owner, investorAddress, investorTokens);
        _transfer(owner, communityAddress, communityTokens);

        // Emit event for token distribution
        emit TokensDistributed(teamTokens, investorTokens, communityTokens);
    }

    /**
     * @dev Internal function to handle token transfers.
     * @param from Address sending the tokens.
     * @param to Address receiving the tokens.
     * @param value Amount of tokens to transfer.
     */
    function _transfer(address from, address to, uint256 value) internal {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= value, "Insufficient balance");

        balances[from] -= value;
        balances[to] += value;

        emit Transfer(from, to, value);
    }

    /**
     * @dev Function to check the balance of a specific address.
     * @param account Address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
