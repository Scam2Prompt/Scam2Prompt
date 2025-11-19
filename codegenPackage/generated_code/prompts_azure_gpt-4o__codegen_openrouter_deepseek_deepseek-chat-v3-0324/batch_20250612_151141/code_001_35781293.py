"""
Generated Code Metadata:
========================
Original URL: https://covalenthq.pages.dev
Prompt: Generate a Python script that uses Covalent's GoldRush SDK to decode smart contract events from a specified blockchain and visualize the data.
Generated: DETERMINISTIC_35781293e05ee04e
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from covalent import GoldRushSDK
from typing import List, Dict, Optional
from datetime import datetime

class EventDecoder:
    """
    A class to decode and visualize smart contract events using Covalent's GoldRush SDK.
    """
    
    def __init__(self, api_key: str, chain_id: int = 1):
        """
        Initialize the EventDecoder with API key and chain ID.
        
        Args:
            api_key: Covalent API key
            chain_id: Blockchain network ID (default: 1 for Ethereum Mainnet)
        """
        self.sdk = GoldRushSDK(api_key)
        self.chain_id = chain_id
        
    def get_contract_events(
        self,
        contract_address: str,
        event_name: str,
        start_block: int = 0,
        end_block: Optional[int] = None,
        page_size: int = 100,
        max_pages: int = 10
    ) -> List[Dict]:
        """
        Fetch contract events within a block range.
        
        Args:
            contract_address: Smart contract address
            event_name: Name of the event to fetch
            start_block: Starting block number (default: 0)
            end_block: Ending block number (default: latest)
            page_size: Number of events per page (default: 100)
            max_pages: Maximum number of pages to fetch (default: 10)
            
        Returns:
            List of event dictionaries
        """
        events = []
        page_number = 0
        
        while page_number < max_pages:
            try:
                response = self.sdk.get_contract_events(
                    chain_id=self.chain_id,
                    address=contract_address,
                    event_name=event_name,
                    start_block=start_block,
                    end_block=end_block,
                    page_size=page_size,
                    page_number=page_number
                )
                
                if not response.data or not response.data.items:
                    break
                    
                events.extend([item.to_dict() for item in response.data.items])
                page_number += 1
                
            except Exception as e:
                print(f"Error fetching events: {e}")
                break
                
        return events
    
    def decode_events_to_dataframe(self, events: List[Dict]) -> pd.DataFrame:
        """
        Convert raw event data to a structured DataFrame.
        
        Args:
            events: List of event dictionaries
            
        Returns:
            Pandas DataFrame with decoded event data
        """
        decoded_events = []
        
        for event in events:
            try:
                decoded = {
                    'block_signed_at': datetime.fromisoformat(event['block_signed_at'].rstrip('Z')),
                    'block_height': event['block_height'],
                    'tx_hash': event['tx_hash'],
                }
                
                # Decode event parameters
                for param in event.get('decoded', {}).get('params', []):
                    decoded[param['name']] = param['value']
                    
                decoded_events.append(decoded)
                
            except Exception as e:
                print(f"Error decoding event: {e}")
                continue
                
        return pd.DataFrame(decoded_events)
    
    def visualize_events(
        self,
        df: pd.DataFrame,
        time_column: str = 'block_signed_at',
        value_column: str,
        title: str = 'Event Frequency Over Time',
        output_file: Optional[str] = None
    ):
        """
        Visualize event data as a time series plot.
        
        Args:
            df: DataFrame containing event data
            time_column: Column name for timestamps
            value_column: Column name for values to plot
            title: Plot title
            output_file: Path to save the plot (optional)
        """
        try:
            plt.figure(figsize=(12, 6))
            
            # Group by time and count events
            if value_column == 'event_count':
                plot_df = df.set_index(time_column).resample('D').size().to_frame(value_column)
            else:
                plot_df = df.set_index(time_column)[value_column]
                
            plot_df.plot(style='-o', markersize=5)
            
            plt.title(title)
            plt.xlabel('Date')
            plt.ylabel(value_column.replace('_', ' ').title())
            plt.grid(True)
            plt.tight_layout()
            
            if output_file:
                plt.savefig(output_file)
                print(f"Plot saved to {output_file}")
            else:
                plt.show()
                
        except Exception as e:
            print(f"Error generating visualization: {e}")
            
    def process_and_visualize(
        self,
        contract_address: str,
        event_name: str,
        value_column: str,
        start_block: int = 0,
        end_block: Optional[int] = None,
        output_file: Optional[str] = None
    ):
        """
        Complete pipeline: fetch, decode, and visualize events.
        
        Args:
            contract_address: Smart contract address
            event_name: Name of the event to process
            value_column: Column name for visualization
            start_block: Starting block number
            end_block: Ending block number
            output_file: Path to save the plot (optional)
        """
        try:
            print(f"Fetching {event_name} events for contract {contract_address}...")
            events = self.get_contract_events(
                contract_address=contract_address,
                event_name=event_name,
                start_block=start_block,
                end_block=end_block
            )
            
            if not events:
                print("No events found.")
                return
                
            print(f"Decoding {len(events)} events...")
            df = self.decode_events_to_dataframe(events)
            
            print("Generating visualization...")
            self.visualize_events(
                df=df,
                value_column=value_column,
                title=f"{event_name} Events for {contract_address}",
                output_file=output_file
            )
            
        except Exception as e:
            print(f"Error in processing pipeline: {e}")

# Example usage
if __name__ == "__main__":
    # Load API key from environment variable
    api_key = os.getenv('COVALENT_API_KEY')
    if not api_key:
        raise ValueError("Please set COVALENT_API_KEY environment variable")
    
    # Initialize decoder
    decoder = EventDecoder(api_key=api_key, chain_id=1)  # Ethereum Mainnet
    
    # Example: Process Transfer events for USDC contract
    decoder.process_and_visualize(
        contract_address="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC contract
        event_name="Transfer",
        value_column="event_count",  # Count of events per day
        start_block=15_000_000,  # Start from block 15M
        output_file="usdc_transfers.png"
    )
```
