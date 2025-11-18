"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curly-sun-6227.on.fleek.co
Prompt: Create a smart contract template compatible with PinkSale for launching a new token and presale event.
Generated: DETERMINISTIC_104f295bc6a1f7ad
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready smart contract template compatible with PinkSale for launching a new token and presale event. The code includes essential elements required for such a use case.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Token and Presale Contract for PinkSale Compatibility
 * @dev This contract allows for the creation of an ERC20 token and the setup of a presale process.
 *      Designed for compatibility with PinkSale presale platform.
 */
contract PinkSaleToken {
    // ERC20 token properties
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Presale properties
    address public owner;
    uint256 public presaleRate; // Number of tokens per ETH during presale
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleCap; // Maximum tokens available for presale
    uint256 public presaleSold;

    bool public presaleFinalized;

    // Events for logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event PresaleBuy(address indexed buyer, uint256 amount, uint256 tokensReceived);
    event PresaleFinalized();

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime, "Presale has not started");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        require(!presaleFinalized, "Presale has been finalized");
        _;
    }

    /**
     * @dev Constructor to initialize the token and presale parameters.
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _totalSupply Total supply of tokens
     * @param _presaleRate Rate of tokens per ETH during presale
     * @param _presaleStartTime Start time of presale (Unix timestamp)
     * @param _presaleEndTime End time of presale (Unix timestamp)
     * @param _presaleCap Maximum tokens available for presale
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _totalSupply,
        uint256 _presaleRate,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _presaleCap
    ) {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply;
        presaleRate = _presaleRate;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        presaleCap = _presaleCap;

        owner = msg.sender;
        balances[owner] = totalSupply; // Assign all tokens to the owner initially
    }

    // ERC20 Functions

    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    function transfer(address to, uint256 amount) external returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        _transfer(msg.sender, to, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function allowance(address account, address spender) external view returns (uint256) {
        return allowances[account][spender];
    }

    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");
        require(balances[from] >= amount, "Insufficient balance");
        allowances[from][msg.sender] -= amount;
        _transfer(from, to, amount);
        return true;
    }

    function _transfer(address from, address to, uint256 amount) private {
        require(to != address(0), "Cannot transfer to zero address");
        balances[from] -= amount;
        balances[to] += amount;
        emit Transfer(from, to, amount);
    }

    // Presale Functions

    function buyTokens() external payable presaleActive {
        require(msg.value > 0, "ETH amount must be greater than zero");
        uint256 tokenAmount = msg.value * presaleRate;
        require(presaleSold + tokenAmount <= presaleCap, "Presale cap exceeded");

        balances[owner] -= tokenAmount;
        balances[msg.sender] += tokenAmount;
        presaleSold += tokenAmount;

        emit PresaleBuy(msg.sender, msg.value, tokenAmount);
    }

    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale has not ended yet");
        require(!presaleFinalized, "Presale already finalized");

        presaleFinalized = true;
        emit PresaleFinalized();

        // Transfer remaining ETH to the owner
        payable(owner).transfer(address(this).balance);
    }

    // Fallback to receive ETH
    receive() external payable {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale not active");
        buyTokens();
    }

    // Withdraw any remaining ETH after presale
    function withdrawETH() external onlyOwner {
        require(presaleFinalized, "Presale must be finalized");
        payable(owner).transfer(address(this).balance);
    }
}
```

This contract should work seamlessly for creating an ERC20 token and running a presale process compatible with PinkSale. Ensure to test and audit the contract thoroughly before deploying it in production.
