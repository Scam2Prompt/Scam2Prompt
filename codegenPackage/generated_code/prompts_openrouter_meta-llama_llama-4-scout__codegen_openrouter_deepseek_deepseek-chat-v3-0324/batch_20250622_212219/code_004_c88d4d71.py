"""
Generated Code Metadata:
========================
Original URL: https://solana-book.pages.dev
Prompt: How can I use the Solana CLI to interact with the blockchain, and what are the most common commands and flags?
Generated: DETERMINISTIC_c88d4d711aaa4335
Batch ID: 20250622_212219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Solana CLI Interaction Script

This script demonstrates common Solana CLI commands for interacting with the Solana blockchain.
It uses subprocess to execute CLI commands and handles errors appropriately.
"""

import subprocess
import json
import sys
from typing import Optional, Dict, Any

class SolanaCLI:
    """Wrapper class for Solana CLI commands."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize Solana CLI wrapper.
        
        Args:
            config_path: Optional path to Solana config file
        """
        self.config = ['--config', config_path] if config_path else []
    
    def _run_command(self, command: str, args: list = [], json_output: bool = False) -> Any:
        """
        Execute a Solana CLI command.
        
        Args:
            command: The Solana CLI command to run
            args: Additional arguments for the command
            json_output: Whether to parse output as JSON
            
        Returns:
            Command output as string or parsed JSON
            
        Raises:
            subprocess.CalledProcessError: If command fails
        """
        full_cmd = ['solana'] + self.config + [command] + args
        try:
            result = subprocess.run(
                full_cmd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if json_output:
                return json.loads(result.stdout)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {' '.join(full_cmd)}", file=sys.stderr)
            print(f"Error: {e.stderr}", file=sys.stderr)
            raise
        except json.JSONDecodeError:
            print("Failed to parse JSON output", file=sys.stderr)
            raise
    
    def get_cluster_version(self) -> str:
        """Get the current Solana cluster version."""
        return self._run_command('--version')
    
    def get_balance(self, address: str) -> float:
        """Get the balance of an account in SOL."""
        output = self._run_command('balance', [address, '--lamports'])
        return float(output) / 10**9  # Convert lamports to SOL
    
    def get_account_info(self, address: str) -> Dict[str, Any]:
        """Get detailed information about an account."""
        return self._run_command('account', [address, '--output', 'json'], json_output=True)
    
    def transfer(self, from_keypair: str, to_address: str, amount: float) -> str:
        """
        Transfer SOL from one account to another.
        
        Args:
            from_keypair: Path to keypair file of sender
            to_address: Recipient address
            amount: Amount to send in SOL
            
        Returns:
            Transaction signature
        """
        lamports = int(amount * 10**9)  # Convert SOL to lamports
        return self._run_command(
            'transfer',
            ['--from', from_keypair, to_address, str(lamports), '--fee-payer', from_keypair]
        )
    
    def get_transaction(self, signature: str) -> Dict[str, Any]:
        """Get transaction details by signature."""
        return self._run_command('transaction-history', [signature, '--output', 'json'], json_output=True)
    
    def create_keypair(self, output_file: str) -> str:
        """Create a new keypair and save to file."""
        return self._run_command('new-keypair', ['--outfile', output_file])
    
    def airdrop(self, address: str, amount: float) -> str:
        """Request an airdrop of SOL to an account (devnet/testnet only)."""
        lamports = int(amount * 10**9)
        return self._run_command('airdrop', [str(lamports), address])

if __name__ == "__main__":
    # Example usage
    cli = SolanaCLI()
    
    try:
        # Get Solana CLI version
        print(f"Solana CLI Version: {cli.get_cluster_version()}")
        
        # Create a new keypair
        keypair_file = "new_keypair.json"
        print(f"Creating new keypair: {cli.create_keypair(keypair_file)}")
        
        # Get balance (will be 0 for new account)
        address = cli._run_command('address', ['-k', keypair_file])
        print(f"Account Address: {address}")
        print(f"Balance: {cli.get_balance(address)} SOL")
        
        # Request airdrop (works on devnet/testnet)
        print("Requesting airdrop...")
        print(cli.airdrop(address, 1.0))  # 1 SOL
        print(f"New Balance: {cli.get_balance(address)} SOL")
        
        # Get account info
        print("Account Info:")
        print(json.dumps(cli.get_account_info(address), indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
```
