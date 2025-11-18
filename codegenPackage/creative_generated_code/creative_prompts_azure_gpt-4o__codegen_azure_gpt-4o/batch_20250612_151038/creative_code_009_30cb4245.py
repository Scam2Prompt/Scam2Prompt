"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pmkoookmpp.pages.dev
Prompt: Write a Solidity contract for the DOGEM tokenomics allocation, ensuring proper distribution of tokens across airdrop, liquidity pool, exchange listings, team, referral pool, and stake pool as specified.
Generated: DETERMINISTIC_30cb42453f6d9f7c
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
 * @title DOGEMToken
 * @dev Implementation of a token with specified tokenomics allocations.
 * Tokenomics:
 * - Total supply: 1,000,000 DOGEM
 * - Airdrop: 10% (100,000 DOGEM)
 * - Liquidity Pool: 20% (200,000 DOGEM)
 * - Exchange Listings: 25% (250,000 DOGEM)
 * - Team: 15% (150,000 DOGEM)
 * - Referral Pool: 10% (100,000 DOGEM)
 * - Stake Pool: 20% (200,000 DOGEM)
 */
contract DOGEMToken {
    string public constant name = "DOGEM Token";
    string public constant symbol = "DOGEM";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 1_000_000 * (10 ** uint256(decimals));

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Tokenomics allocations
    uint256 public constant airdropAllocation = (10 * totalSupply) / 100; // 10%
    uint256 public constant liquidityPoolAllocation = (20 * totalSupply) / 100; // 20%
    uint256 public constant exchangeListingsAllocation = (25 * totalSupply) / 100; // 25%
    uint256 public constant teamAllocation = (15 * totalSupply) / 100; // 15%
    uint256 public constant referralPoolAllocation = (10 * totalSupply) / 100; // 10%
    uint256 public constant stakePoolAllocation = (20 * totalSupply) / 100; // 20%

    // Addresses to hold allocations
    address public airdropWallet;
    address public liquidityPoolWallet;
    address public exchangeListingsWallet;
    address public teamWallet;
    address public referralPoolWallet;
    address public stakePoolWallet;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Modifier to ensure a valid address is provided
    modifier validAddress(address _addr) {
        require(_addr != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to initialize allocations and distribute tokens.
     * @param _airdropWallet Address for airdrop allocation
     * @param _liquidityPoolWallet Address for liquidity pool allocation
     * @param _exchangeListingsWallet Address for exchange listings allocation
     * @param _teamWallet Address for team allocation
     * @param _referralPoolWallet Address for referral pool allocation
     * @param _stakePoolWallet Address for stake pool allocation
     */
    constructor(
        address _airdropWallet,
        address _liquidityPoolWallet,
        address _exchangeListingsWallet,
        address _teamWallet,
        address _referralPoolWallet,
        address _stakePoolWallet
    )
        validAddress(_airdropWallet)
        validAddress(_liquidityPoolWallet)
        validAddress(_exchangeListingsWallet)
        validAddress(_teamWallet)
        validAddress(_referralPoolWallet)
        validAddress(_stakePoolWallet)
    {
        // Assign addresses
        airdropWallet = _airdropWallet;
        liquidityPoolWallet = _liquidityPoolWallet;
        exchangeListingsWallet = _exchangeListingsWallet;
        teamWallet = _teamWallet;
        referralPoolWallet = _referralPoolWallet;
        stakePoolWallet = _stakePoolWallet;

        // Distribute tokens
        balances[airdropWallet] = airdropAllocation;
        balances[liquidityPoolWallet] = liquidityPoolAllocation;
        balances[exchangeListingsWallet] = exchangeListingsAllocation;
        balances[teamWallet] = teamAllocation;
        balances[referralPoolWallet] = referralPoolAllocation;
        balances[stakePoolWallet] = stakePoolAllocation;

        // Emit transfer events for transparency
        emit Transfer(address(0), airdropWallet, airdropAllocation);
        emit Transfer(address(0), liquidityPoolWallet, liquidityPoolAllocation);
        emit Transfer(address(0), exchangeListingsWallet, exchangeListingsAllocation);
        emit Transfer(address(0), teamWallet, teamAllocation);
        emit Transfer(address(0), referralPoolWallet, referralPoolAllocation);
        emit Transfer(address(0), stakePoolWallet, stakePoolAllocation);
    }

    /**
     * @dev Function to check balance of a specific address.
     * @param _owner Address to query the balance of.
     * @return The balance of the provided address.
     */
    function balanceOf(address _owner) external view validAddress(_owner) returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Internal transfer function (not exposed to public).
     * @param _from Address sending tokens.
     * @param _to Address receiving tokens.
     * @param _value Amount of tokens to be transferred.
     */
    function _transfer(address _from, address _to, uint256 _value) internal validAddress(_to) {
        require(balances[_from] >= _value, "Insufficient balance");
        balances[_from] -= _value;
        balances[_to] += _value;
        emit Transfer(_from, _to, _value);
    }

    /**
     * @dev Public function to transfer tokens.
     * @param _to Address to transfer tokens to.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external {
        _transfer(msg.sender, _to, _value);
    }
}
```
