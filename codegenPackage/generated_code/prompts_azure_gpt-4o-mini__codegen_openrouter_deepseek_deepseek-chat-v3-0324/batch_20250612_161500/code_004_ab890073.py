"""
Generated Code Metadata:
========================
Original URL: https://roost-ch9.pages.dev
Prompt: Describe the process of participating in the $ROOST presale and how the funds will be allocated according to the tokenomics.
Generated: DETERMINISTIC_ab890073e1b54716
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Smart Contract for ROOST Token Presale with Tokenomics Allocation

from vyper.interfaces import ERC20

implements: ERC20

# Token Details
name: public(String[32])
symbol: public(String[32])
decimals: public(uint8)

# Token Supply
total_supply: public(uint256)
presale_supply: public(uint256)
team_supply: public(uint256)
marketing_supply: public(uint256)
liquidity_supply: public(uint256)
community_supply: public(uint256)

# Addresses
owner: public(address)
presale_address: public(address)
team_address: public(address)
marketing_address: public(address)
liquidity_address: public(address)
community_address: public(address)

# Presale Parameters
presale_start: public(uint256)
presale_end: public(uint256)
presale_rate: public(uint256)  # tokens per ETH
presale_goal: public(uint256)  # in ETH
presale_cap: public(uint256)   # in ETH
presale_raised: public(uint256)

# Balances and Allowances
balances: HashMap[address, uint256]
allowed: HashMap[address, HashMap[address, uint256]]

# Events
Transfer: event({_from: indexed(address), _to: indexed(address), _value: uint256})
Approval: event({_owner: indexed(address), _spender: indexed(address), _value: uint256})
PresaleContribution: event({_contributor: indexed(address), _amount: uint256, _tokens: uint256})
PresaleFinalized: event({_raised: uint256, _tokens_sold: uint256})

@external
def __init__():
    self.name = "ROOST Token"
    self.symbol = "ROOST"
    self.decimals = 18
    
    # Total supply: 100 million tokens
    total_supply: uint256 = 100000000 * 10 ** 18
    self.total_supply = total_supply
    
    # Tokenomics allocation
    self.presale_supply = total_supply * 40 // 100  # 40% for presale
    self.team_supply = total_supply * 15 // 100     # 15% for team (vested)
    self.marketing_supply = total_supply * 15 // 100 # 15% for marketing
    self.liquidity_supply = total_supply * 20 // 100 # 20% for liquidity
    self.community_supply = total_supply * 10 // 100 # 10% for community
    
    # Set owner
    self.owner = msg.sender
    
    # Mint initial allocations
    self.balances[self.owner] = (
        self.team_supply + 
        self.marketing_supply + 
        self.liquidity_supply + 
        self.community_supply
    )
    log Transfer(ZERO_ADDRESS, self.owner, self.balances[self.owner])
    
    # Presale parameters (to be set by owner)
    self.presale_rate = 0
    self.presale_goal = 0
    self.presale_cap = 0
    self.presale_raised = 0

@external
@payable
def contribute_to_presale():
    """
    Allows users to contribute ETH to the presale and receive ROOST tokens.
    """
    # Check presale is active
    assert block.timestamp >= self.presale_start, "Presale has not started"
    assert block.timestamp <= self.presale_end, "Presale has ended"
    assert self.presale_raised < self.presale_cap, "Presale cap reached"
    
    amount: uint256 = msg.value
    assert amount > 0, "Must send ETH to participate"
    
    # Calculate tokens
    tokens: uint256 = amount * self.presale_rate
    
    # Check presale supply
    assert tokens <= self.presale_supply, "Not enough tokens remaining in presale"
    
    # Update balances
    self.presale_supply -= tokens
    self.presale_raised += amount
    self.balances[msg.sender] += tokens
    
    # Log events
    log Transfer(ZERO_ADDRESS, msg.sender, tokens)
    log PresaleContribution(msg.sender, amount, tokens)

@external
def finalize_presale():
    """
    Finalizes the presale after it ends. Can only be called by owner.
    Distributes remaining tokens according to tokenomics.
    """
    assert msg.sender == self.owner, "Only owner can finalize"
    assert block.timestamp > self.presale_end, "Presale not ended yet"
    
    # Distribute remaining presale supply proportionally
    remaining_presale: uint256 = self.presale_supply
    if remaining_presale > 0:
        # Add to liquidity pool
        liquidity_share: uint256 = remaining_presale * 50 // 100
        self.balances[self.liquidity_address] += liquidity_share
        log Transfer(ZERO_ADDRESS, self.liquidity_address, liquidity_share)
        
        # Add to marketing
        marketing_share: uint256 = remaining_presale * 30 // 100
        self.balances[self.marketing_address] += marketing_share
        log Transfer(ZERO_ADDRESS, self.marketing_address, marketing_share)
        
        # Add to community
        community_share: uint256 = remaining_presale * 20 // 100
        self.balances[self.community_address] += community_share
        log Transfer(ZERO_ADDRESS, self.community_address, community_share)
        
        self.presale_supply = 0
    
    log PresaleFinalized(self.presale_raised, self.presale_supply)

@external
def set_presale_parameters(
    _start: uint256,
    _end: uint256,
    _rate: uint256,
    _goal: uint256,
    _cap: uint256,
    _presale_address: address
):
    """
    Sets presale parameters. Can only be called by owner.
    """
    assert msg.sender == self.owner, "Only owner can set parameters"
    assert _start < _end, "Start must be before end"
    assert _rate > 0, "Rate must be positive"
    assert _cap > _goal, "Cap must be greater than goal"
    
    self.presale_start = _start
    self.presale_end = _end
    self.presale_rate = _rate
    self.presale_goal = _goal
    self.presale_cap = _cap
    self.presale_address = _presale_address

@external
def set_allocation_addresses(
    _team: address,
    _marketing: address,
    _liquidity: address,
    _community: address
):
    """
    Sets allocation addresses. Can only be called by owner.
    """
    assert msg.sender == self.owner, "Only owner can set addresses"
    self.team_address = _team
    self.marketing_address = _marketing
    self.liquidity_address = _liquidity
    self.community_address = _community

# Standard ERC20 functions
@view
@external
def balanceOf(_owner: address) -> uint256:
    return self.balances[_owner]

@external
def transfer(_to: address, _value: uint256) -> bool:
    assert _to != ZERO_ADDRESS, "Invalid recipient"
    assert self.balances[msg.sender] >= _value, "Insufficient balance"
    
    self.balances[msg.sender] -= _value
    self.balances[_to] += _value
    
    log Transfer(msg.sender, _to, _value)
    return True

@external
def transferFrom(_from: address, _to: address, _value: uint256) -> bool:
    assert _to != ZERO_ADDRESS, "Invalid recipient"
    assert self.balances[_from] >= _value, "Insufficient balance"
    assert self.allowed[_from][msg.sender] >= _value, "Allowance exceeded"
    
    self.balances[_from] -= _value
    self.balances[_to] += _value
    self.allowed[_from][msg.sender] -= _value
    
    log Transfer(_from, _to, _value)
    return True

@external
def approve(_spender: address, _value: uint256) -> bool:
    self.allowed[msg.sender][_spender] = _value
    log Approval(msg.sender, _spender, _value)
    return True

@view
@external
def allowance(_owner: address, _spender: address) -> uint256:
    return self.allowed[_owner][_spender]
```
