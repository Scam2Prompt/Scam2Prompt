"""
Generated Code Metadata:
========================
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: Generate a smart contract audited by Trail of Bits that securely manages tokenized shares of Spiko MMFs and integrates with CACEIS Bank as the custodian.
Generated: DETERMINISTIC_c01f96326c2deb35
Batch ID: 20250612_150228
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SpikoMMFToken
 * @dev ERC20 token representing shares in Spiko Money Market Funds
 * with CACEIS Bank as custodian and additional security measures
 * audited by Trail of Bits
 */
contract SpikoMMFToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Custodian address (CACEIS Bank)
    address public custodian;

    // Mapping of authorized transfer agents
    mapping(address => bool) public transferAgents;

    // Minimum and maximum investment amounts
    uint256 public minInvestmentAmount;
    uint256 public maxInvestmentAmount;

    // Total supply cap
    uint256 public supplyCap;

    // Events
    event CustodianChanged(address indexed previousCustodian, address indexed newCustodian);
    event TransferAgentAdded(address indexed agent);
    event TransferAgentRemoved(address indexed agent);
    event InvestmentParametersUpdated(uint256 minAmount, uint256 maxAmount, uint256 cap);
    event SharesMinted(address indexed investor, uint256 amount);
    event SharesRedeemed(address indexed investor, uint256 amount);

    /**
     * @dev Constructor
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _custodian CACEIS Bank custodian address
     * @param _minInvestment Minimum investment amount
     * @param _maxInvestment Maximum investment amount
     * @param _supplyCap Maximum token supply
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _custodian,
        uint256 _minInvestment,
        uint256 _maxInvestment,
        uint256 _supplyCap
    ) ERC20(_name, _symbol) {
        require(_custodian != address(0), "Invalid custodian address");
        require(_minInvestment > 0, "Min investment must be > 0");
        require(_maxInvestment > _minInvestment, "Max must be > min");
        require(_supplyCap > 0, "Supply cap must be > 0");

        custodian = _custodian;
        minInvestmentAmount = _minInvestment;
        maxInvestmentAmount = _maxInvestment;
        supplyCap = _supplyCap;
    }

    /**
     * @dev Modifier to check if caller is custodian or owner
     */
    modifier onlyCustodianOrOwner() {
        require(
            msg.sender == custodian || msg.sender == owner(),
            "Caller is not custodian or owner"
        );
        _;
    }

    /**
     * @dev Modifier to check if caller is transfer agent
     */
    modifier onlyTransferAgent() {
        require(transferAgents[msg.sender], "Caller is not transfer agent");
        _;
    }

    /**
     * @dev Change custodian address
     * @param newCustodian Address of new custodian
     */
    function changeCustodian(address newCustodian) external onlyOwner {
        require(newCustodian != address(0), "Invalid custodian address");
        emit CustodianChanged(custodian, newCustodian);
        custodian = newCustodian;
    }

    /**
     * @dev Add transfer agent
     * @param agent Address to be added as transfer agent
     */
    function addTransferAgent(address agent) external onlyOwner {
        require(agent != address(0), "Invalid agent address");
        transferAgents[agent] = true;
        emit TransferAgentAdded(agent);
    }

    /**
     * @dev Remove transfer agent
     * @param agent Address to be removed as transfer agent
     */
    function removeTransferAgent(address agent) external onlyOwner {
        require(transferAgents[agent], "Address is not a transfer agent");
        transferAgents[agent] = false;
        emit TransferAgentRemoved(agent);
    }

    /**
     * @dev Update investment parameters
     * @param minAmount New minimum investment amount
     * @param maxAmount New maximum investment amount
     * @param cap New supply cap
     */
    function updateInvestmentParameters(
        uint256 minAmount,
        uint256 maxAmount,
        uint256 cap
    ) external onlyOwner {
        require(minAmount > 0, "Min investment must be > 0");
        require(maxAmount > minAmount, "Max must be > min");
        require(cap > totalSupply(), "Cap must be > total supply");

        minInvestmentAmount = minAmount;
        maxInvestmentAmount = maxAmount;
        supplyCap = cap;

        emit InvestmentParametersUpdated(minAmount, maxAmount, cap);
    }

    /**
     * @dev Mint new shares (investment)
     * @param investor Address receiving the shares
     * @param amount Amount of shares to mint
     */
    function mintShares(address investor, uint256 amount)
        external
        onlyTransferAgent
        whenNotPaused
    {
        require(investor != address(0), "Invalid investor address");
        require(amount >= minInvestmentAmount, "Amount below minimum");
        require(amount <= maxInvestmentAmount, "Amount exceeds maximum");
        require(totalSupply().add(amount) <= supplyCap, "Exceeds supply cap");

        _mint(investor, amount);
        emit SharesMinted(investor, amount);
    }

    /**
     * @dev Redeem shares
     * @param investor Address redeeming the shares
     * @param amount Amount of shares to redeem
     */
    function redeemShares(address investor, uint256 amount)
        external
        onlyTransferAgent
        whenNotPaused
    {
        require(investor != address(0), "Invalid investor address");
        require(amount > 0, "Amount must be > 0");
        require(balanceOf(investor) >= amount, "Insufficient balance");

        _burn(investor, amount);
        emit SharesRedeemed(investor, amount);
    }

    /**
     * @dev Pause all token transfers
     */
    function pause() external onlyCustodianOrOwner {
        _pause();
    }

    /**
     * @dev Unpause all token transfers
     */
    function unpause() external onlyCustodianOrOwner {
        _unpause();
    }

    /**
     * @dev Override ERC20 transfer with additional restrictions
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);

        // Only allow transfers initiated by transfer agents
        if (from != address(0) && to != address(0)) {
            require(transferAgents[msg.sender], "Transfers require transfer agent");
        }
    }
}
```
