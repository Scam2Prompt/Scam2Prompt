"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ie.pages.dev
Prompt: Write a Solidity smart contract to implement tokenomics similar to WienerAI, including allocations for presale, staking, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_20de9232995ed124
Batch ID: 20250612_152235
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
 * @title WienerAI Tokenomics Smart Contract
 * @dev Implements tokenomics with allocations for presale, staking, community rewards,
 * liquidity, and marketing. Includes mechanisms for minting and distribution.
 */
contract WienerAIToken {
    // ERC20 standard variables
    string public name = "WienerAI Token";
    string public symbol = "WAI";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    address public owner;

    // Allocation percentages (in basis points - 10000 basis points = 100%)
    uint16 public constant PRESALE_ALLOCATION = 3000; // 30%
    uint16 public constant STAKING_ALLOCATION = 2500; // 25%
    uint16 public constant COMMUNITY_REWARDS_ALLOCATION = 2000; // 20%
    uint16 public constant LIQUIDITY_ALLOCATION = 1500; // 15%
    uint16 public constant MARKETING_ALLOCATION = 1000; // 10%

    // Allocation addresses
    address public presaleAddress;
    address public stakingAddress;
    address public communityRewardsAddress;
    address public liquidityAddress;
    address public marketingAddress;

    // Mapping for balances
    mapping(address => uint256) public balances;
    // Mapping for allowances
    mapping(address => mapping(address => uint256)) public allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract. Total supply is minted to the specified allocations.
     * @param _totalSupply The total supply of tokens.
     * @param _presaleAddress Address for presale allocation.
     * @param _stakingAddress Address for staking allocation.
     * @param _communityRewardsAddress Address for community rewards allocation.
     * @param _liquidityAddress Address for liquidity allocation.
     * @param _marketingAddress Address for marketing allocation.
     */
    constructor(
        uint256 _totalSupply,
        address _presaleAddress,
        address _stakingAddress,
        address _communityRewardsAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) {
        require(
            _presaleAddress != address(0) &&
            _stakingAddress != address(0) &&
            _communityRewardsAddress != address(0) &&
            _liquidityAddress != address(0) &&
            _marketingAddress != address(0),
            "Invalid allocation addresses"
        );

        owner = msg.sender;
        totalSupply = _totalSupply;

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        communityRewardsAddress = _communityRewardsAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;

        // Mint tokens to each allocation address based on defined percentages
        _mint(presaleAddress, (_totalSupply * PRESALE_ALLOCATION) / 10000);
        _mint(stakingAddress, (_totalSupply * STAKING_ALLOCATION) / 10000);
        _mint(communityRewardsAddress, (_totalSupply * COMMUNITY_REWARDS_ALLOCATION) / 10000);
        _mint(liquidityAddress, (_totalSupply * LIQUIDITY_ALLOCATION) / 10000);
        _mint(marketingAddress, (_totalSupply * MARKETING_ALLOCATION) / 10000);
    }

    /**
     * @dev Internal function to mint tokens to an address.
     * @param _to Address to receive the tokens.
     * @param _amount Amount of tokens to mint.
     */
    function _mint(address _to, uint256 _amount) internal {
        require(_to != address(0), "Mint to the zero address");
        balances[_to] += _amount;
        emit Transfer(address(0), _to, _amount);
    }

    /**
     * @dev Transfers tokens from one address to another.
     * @param _to Address to transfer tokens to.
     * @param _amount Amount of tokens to transfer.
     * @return Success status.
     */
    function transfer(address _to, uint256 _amount) external returns (bool) {
        require(_to != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;
        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    /**
     * @dev Approves a spender to use tokens on behalf of the owner.
     * @param _spender Address to approve.
     * @param _amount Amount of tokens to approve.
     * @return Success status.
     */
    function approve(address _spender, uint256 _amount) external returns (bool) {
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of an owner (allowance-based).
     * @param _from Address to transfer tokens from.
     * @param _to Address to transfer tokens to.
     * @param _amount Amount of tokens to transfer.
     * @return Success status.
     */
    function transferFrom(address _from, address _to, uint256 _amount) external returns (bool) {
        require(_to != address(0), "Transfer to the zero address");
        require(balances[_from] >= _amount, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _amount, "Allowance exceeded");

        balances[_from] -= _amount;
        balances[_to] += _amount;
        allowances[_from][msg.sender] -= _amount;
        emit Transfer(_from, _to, _amount);
        return true;
    }

    /**
     * @dev Allows the owner to update allocation addresses.
     * @param _presaleAddress New presale address.
     * @param _stakingAddress New staking address.
     * @param _communityRewardsAddress New community rewards address.
     * @param _liquidityAddress New liquidity address.
     * @param _marketingAddress New marketing address.
     */
    function updateAllocationAddresses(
        address _presaleAddress,
        address _stakingAddress,
        address _communityRewardsAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) external onlyOwner {
        require(
            _presaleAddress != address(0) &&
            _stakingAddress != address(0) &&
            _communityRewardsAddress != address(0) &&
            _liquidityAddress != address(0) &&
            _marketingAddress != address(0),
            "Invalid allocation addresses"
        );

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        communityRewardsAddress = _communityRewardsAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;
    }
}
```
