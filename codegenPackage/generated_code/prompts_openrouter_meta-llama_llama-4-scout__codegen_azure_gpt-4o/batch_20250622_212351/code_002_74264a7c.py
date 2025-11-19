"""
Generated Code Metadata:
========================
Original URL: https://centrifuge.onl
Prompt: "Generate a smart contract code for creating a tokenized fund on Centrifuge's platform, incorporating transparency and real-time data access features."
Generated: DETERMINISTIC_74264a7cb6d0e8e5
Batch ID: 20250622_212351
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
 * @title Tokenized Fund Smart Contract
 * @dev This contract creates a tokenized fund on Centrifuge's platform, incorporating transparency and real-time data access.
 */
contract TokenizedFund {
    // State variables
    string public fundName; // Name of the fund
    string public fundSymbol; // Symbol of the fund
    uint256 public totalSupply; // Total supply of tokens
    address public manager; // Address of the fund manager

    mapping(address => uint256) public balances; // Mapping to track token balances
    mapping(address => bool) public investors; // Mapping to track registered investors

    event Transfer(address indexed from, address indexed to, uint256 value); // Event for token transfers
    event InvestorRegistered(address indexed investor); // Event for investor registration
    event FundUpdated(string dataHash, uint256 timestamp); // Event for real-time data updates

    modifier onlyManager() {
        require(msg.sender == manager, "Only the manager can perform this action");
        _;
    }

    modifier onlyInvestor() {
        require(investors[msg.sender], "Only registered investors can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the fund.
     * @param _fundName Name of the fund.
     * @param _fundSymbol Symbol of the fund.
     * @param _initialSupply Initial supply of tokens.
     */
    constructor(string memory _fundName, string memory _fundSymbol, uint256 _initialSupply) {
        fundName = _fundName;
        fundSymbol = _fundSymbol;
        totalSupply = _initialSupply;
        manager = msg.sender;
        balances[manager] = _initialSupply; // Assign all tokens to the manager initially
    }

    /**
     * @dev Function to register an investor.
     * @param _investor Address of the investor to register.
     */
    function registerInvestor(address _investor) external onlyManager {
        require(!investors[_investor], "Investor is already registered");
        investors[_investor] = true;
        emit InvestorRegistered(_investor);
    }

    /**
     * @dev Function to transfer tokens.
     * @param _to Address to transfer tokens to.
     * @param _amount Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _amount) external onlyInvestor {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        require(_to != address(0), "Invalid recipient address");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        emit Transfer(msg.sender, _to, _amount);
    }

    /**
     * @dev Function to update fund data for transparency.
     * @param _dataHash Hash of the updated data (e.g., IPFS hash).
     */
    function updateFundData(string memory _dataHash) external onlyManager {
        emit FundUpdated(_dataHash, block.timestamp);
    }

    /**
     * @dev Function to get the balance of an address.
     * @param _account Address to query the balance of.
     * @return Balance of the given address.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }
}
```
