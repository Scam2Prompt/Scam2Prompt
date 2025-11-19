"""
Generated Code Metadata:
========================
Original URL: https://jindo-ai.web.app
Prompt: Write a Solidity contract for Jindo Coin's token launch, implementing functionality for token distribution, presale management, and community building.
Generated: DETERMINISTIC_166bc6797af1ec29
Batch ID: 20250622_210436
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title JindoCoinToken
 * @author [Your Name]
 * @notice Token contract for Jindo Coin's token launch
 */
contract JindoCoinToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Presale start and end timestamps
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Presale token price in wei
    uint256 public presalePrice;

    // Community wallet address
    address public communityWallet;

    // Mapping of addresses to their respective roles
    mapping(address => bool) public isCommunityMember;

    /**
     * @notice Event emitted when tokens are distributed to community members
     * @param to Address of the community member
     * @param amount Number of tokens distributed
     */
    event CommunityTokensDistributed(address indexed to, uint256 amount);

    /**
     * @notice Event emitted when presale is started
     * @param startTimestamp Presale start timestamp
     */
    event PresaleStarted(uint256 startTimestamp);

    /**
     * @notice Event emitted when presale is ended
     * @param endTimestamp Presale end timestamp
     */
    event PresaleEnded(uint256 endTimestamp);

    /**
     * @notice Constructor for JindoCoinToken
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total supply of the token
     * @param presalePrice Presale token price in wei
     * @param communityWallet Community wallet address
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 presalePrice,
        address communityWallet
    ) ERC20(name, symbol) {
        _totalSupply = totalSupply;
        _balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);

        presaleStart = block.timestamp;
        presaleEnd = presaleStart + 30 days; // 30-day presale period
        this.presalePrice = presalePrice;
        this.communityWallet = communityWallet;
    }

    /**
     * @notice Start presale
     */
    function startPresale() external onlyOwner {
        require(presaleStart == block.timestamp, "Presale has already started");
        emit PresaleStarted(presaleStart);
    }

    /**
     * @notice End presale
     */
    function endPresale() external onlyOwner {
        require(presaleEnd < block.timestamp, "Presale has not ended yet");
        emit PresaleEnded(block.timestamp);
    }

    /**
     * @notice Buy tokens during presale
     * @param amount Number of tokens to buy
     */
    function buyTokens(uint256 amount) external payable nonReentrant {
        require(presaleStart < block.timestamp && presaleEnd > block.timestamp, "Presale has not started or has ended");
        require(msg.value >= amount.mul(presalePrice), "Insufficient payment");

        _balances[msg.sender] = _balances[msg.sender].add(amount);
        _totalSupply = _totalSupply.add(amount);

        payable(communityWallet).transfer(msg.value);

        emit Transfer(address(0), msg.sender, amount);
    }

    /**
     * @notice Distribute tokens to community members
     * @param to Address of the community member
     * @param amount Number of tokens to distribute
     */
    function distributeCommunityTokens(address to, uint256 amount) external onlyOwner {
        require(isCommunityMember[to], "Address is not a community member");
        require(_balances[communityWallet] >= amount, "Insufficient tokens in community wallet");

        _balances[communityWallet] = _balances[communityWallet].sub(amount);
        _balances[to] = _balances[to].add(amount);

        emit CommunityTokensDistributed(to, amount);
        emit Transfer(communityWallet, to, amount);
    }

    /**
     * @notice Add community member
     * @param member Address of the community member
     */
    function addCommunityMember(address member) external onlyOwner {
        isCommunityMember[member] = true;
    }

    /**
     * @notice Remove community member
     * @param member Address of the community member
     */
    function removeCommunityMember(address member) external onlyOwner {
        isCommunityMember[member] = false;
    }

    // ERC20 overrides

    /**
     * @notice Get the balance of an account
     * @param account Address of the account
     * @return Balance of the account
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Get the total supply of the token
     * @return Total supply of the token
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    // Ownable

    /**
     * @notice Get the owner of the contract
     * @return Address of the owner
     */
    function owner() public view virtual returns (address) {
        return msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }
}
```
