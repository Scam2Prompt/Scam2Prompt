"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vesting-cookie.online
Prompt: How can I use Smart contracts to manage vesting for tokens in a DAO?
Generated: DETERMINISTIC_29ae6de42ff8446c
Batch ID: 20250612_162808
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

contract Token {
    string public name = "VestingToken";
    string public symbol = "VTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * 10 ** uint256(decimals);
        balanceOf[msg.sender] = totalSupply; // Assign total supply to contract creator
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }
}

contract Vesting {
    struct Beneficiary {
        address wallet;
        uint256 totalTokens;
        uint256 releasedTokens;
        uint256 releaseStart;
        uint256 releaseDuration;
        uint256 releaseInterval;
    }

    Token public token;
    mapping(address => Beneficiary) public beneficiaries;

    event TokensReleased(address indexed beneficiary, uint256 amount);

    modifier onlyBeneficiary() {
        require(beneficiaries[msg.sender].wallet == msg.sender, "Not a beneficiary");
        _;
    }

    constructor(Token _token) {
        token = _token;
    }

    function addBeneficiary(
        address _wallet,
        uint256 _totalTokens,
        uint256 _releaseStart,
        uint256 _releaseDuration,
        uint256 _releaseInterval
    ) public {
        require(beneficiaries[_wallet].wallet == address(0), "Beneficiary already exists");
        require(_releaseDuration > 0, "Release duration must be greater than zero");

        beneficiaries[_wallet] = Beneficiary({
            wallet: _wallet,
            totalTokens: _totalTokens,
            releasedTokens: 0,
            releaseStart: _releaseStart,
            releaseDuration: _releaseDuration,
            releaseInterval: _releaseInterval
        });
    }

    function release() public onlyBeneficiary {
        Beneficiary storage beneficiary = beneficiaries[msg.sender];
        require(block.timestamp >= beneficiary.releaseStart, "Vesting has not started");
        
        uint256 vestedAmount = _calculateVestedAmount(beneficiary);
        require(vestedAmount > beneficiary.releasedTokens, "No tokens to release");

        uint256 amountToRelease = vestedAmount - beneficiary.releasedTokens;
        beneficiary.releasedTokens += amountToRelease;
        
        require(token.transfer(beneficiary.wallet, amountToRelease), "Token transfer failed");
        emit TokensReleased(beneficiary.wallet, amountToRelease);
    }

    function _calculateVestedAmount(Beneficiary storage beneficiary) internal view returns (uint256) {
        if (block.timestamp < beneficiary.releaseStart) {
            return 0;
        }
        uint256 timeElapsed = block.timestamp - beneficiary.releaseStart;
        uint256 totalIntervals = timeElapsed / beneficiary.releaseInterval;
        
        if (totalIntervals > beneficiary.releaseDuration / beneficiary.releaseInterval) {
            return beneficiary.totalTokens; // All tokens vested
        }
        return (beneficiary.totalTokens * totalIntervals * beneficiary.releaseInterval) / beneficiary.releaseDuration;
    }
}
```
