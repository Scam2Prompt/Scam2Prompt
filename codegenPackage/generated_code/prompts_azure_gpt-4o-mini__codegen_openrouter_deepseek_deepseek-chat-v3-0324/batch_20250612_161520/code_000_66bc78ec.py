"""
Generated Code Metadata:
========================
Original URL: https://backup-ar.pages.dev
Prompt: How can I use the DTORO studio to create my own ERC-20 tokens and set up a crowdpool?
Generated: DETERMINISTIC_66bc78ecae155d23
Batch ID: 20250612_161520
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Custom ERC20 Token
 * @dev Implementation of a custom ERC20 token with minting capabilities
 */
contract MyToken is ERC20, Ownable {
    using SafeMath for uint256;

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    /**
     * @dev Mint new tokens (only owner)
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}

/**
 * @title CrowdPool
 * @dev A contract for managing a token crowdpool
 */
contract CrowdPool is Ownable {
    using SafeMath for uint256;

    IERC20 public token;
    uint256 public rate; // Tokens per ETH
    uint256 public minContribution;
    uint256 public maxContribution;
    uint256 public hardCap;
    uint256 public totalRaised;
    bool public isActive;

    mapping(address => uint256) public contributions;

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PoolClosed(uint256 totalRaised);

    /**
     * @dev Initialize the crowdpool
     * @param _token Address of the token being sold
     * @param _rate Number of tokens per ETH
     * @param _minContribution Minimum ETH contribution
     * @param _maxContribution Maximum ETH contribution per address
     * @param _hardCap Maximum ETH to be raised
     */
    constructor(
        IERC20 _token,
        uint256 _rate,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _hardCap
    ) {
        require(_rate > 0, "Rate must be positive");
        require(_minContribution > 0, "Min contribution must be positive");
        require(_maxContribution > _minContribution, "Max must be greater than min");
        require(_hardCap > 0, "Hard cap must be positive");

        token = _token;
        rate = _rate;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
        hardCap = _hardCap;
        isActive = true;
    }

    /**
     * @dev Buy tokens with ETH
     */
    receive() external payable {
        buyTokens();
    }

    /**
     * @dev Buy tokens with ETH
     */
    function buyTokens() public payable {
        require(isActive, "Pool is not active");
        require(msg.value >= minContribution, "Contribution too low");
        require(contributions[msg.sender].add(msg.value) <= maxContribution, "Exceeds max contribution");
        require(totalRaised.add(msg.value) <= hardCap, "Exceeds hard cap");

        uint256 tokens = msg.value.mul(rate);
        require(token.balanceOf(address(this)) >= tokens, "Not enough tokens in pool");

        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        totalRaised = totalRaised.add(msg.value);

        token.transfer(msg.sender, tokens);
        emit TokensPurchased(msg.sender, tokens);
    }

    /**
     * @dev Close the pool and transfer remaining tokens to owner
     */
    function closePool() public onlyOwner {
        require(isActive, "Pool already closed");
        isActive = false;

        uint256 remainingTokens = token.balanceOf(address(this));
        if (remainingTokens > 0) {
            token.transfer(owner(), remainingTokens);
        }

        emit PoolClosed(totalRaised);
    }

    /**
     * @dev Withdraw raised ETH (only owner)
     */
    function withdraw() public onlyOwner {
        require(!isActive, "Pool must be closed first");
        payable(owner()).transfer(address(this).balance);
    }
}

/**
 * @title TokenFactory
 * @dev Factory contract to deploy tokens and crowdpools
 */
contract TokenFactory {
    event TokenCreated(address indexed tokenAddress, string name, string symbol);
    event PoolCreated(address indexed poolAddress, address indexed tokenAddress);

    /**
     * @dev Create a new ERC20 token
     * @param name Token name
     * @param symbol Token symbol
     * @return Address of the deployed token
     */
    function createToken(string memory name, string memory symbol) public returns (address) {
        MyToken token = new MyToken(name, symbol);
        token.transferOwnership(msg.sender);
        emit TokenCreated(address(token), name, symbol);
        return address(token);
    }

    /**
     * @dev Create a new crowdpool
     * @param token Address of the token to sell
     * @param rate Tokens per ETH
     * @param minContribution Minimum ETH contribution
     * @param maxContribution Maximum ETH contribution per address
     * @param hardCap Maximum ETH to be raised
     * @return Address of the deployed pool
     */
    function createPool(
        IERC20 token,
        uint256 rate,
        uint256 minContribution,
        uint256 maxContribution,
        uint256 hardCap
    ) public returns (address) {
        CrowdPool pool = new CrowdPool(
            token,
            rate,
            minContribution,
            maxContribution,
            hardCap
        );
        pool.transferOwnership(msg.sender);
        emit PoolCreated(address(pool), address(token));
        return address(pool);
    }
}
```
