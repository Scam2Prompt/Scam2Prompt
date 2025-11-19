"""
Generated Code Metadata:
========================
Original URL: https://atlas3io-moonseeker.web.app
Prompt: Create a dashboard to display user statistics for a web3 community, including raffle winners and entries, inspired by the Atlas3 MoonSeeker DAO application.
Generated: DETERMINISTIC_d3abf8608aa49a1d
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import streamlit as st
import pandas as pd
import plotly.express as px
from web3 import Web3
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Web3 Community Dashboard",
    page_icon="🌕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Connect to Ethereum node
def init_web3():
    try:
        w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URL')))
        if not w3.is_connected():
            raise ConnectionError("Failed to connect to Web3 provider")
        return w3
    except Exception as e:
        st.error(f"Error connecting to Web3: {str(e)}")
        return None

# Load contract ABI and address
def load_contract():
    try:
        with open('contract_abi.json') as f:
            abi = json.load(f)
        
        contract_address = os.getenv('CONTRACT_ADDRESS')
        if not contract_address:
            raise ValueError("Contract address not set in environment variables")
        
        return abi, contract_address
    except Exception as e:
        st.error(f"Error loading contract: {str(e)}")
        return None, None

# Get raffle data from contract
def get_raffle_data(w3, contract_abi, contract_address):
    try:
        contract = w3.eth.contract(address=contract_address, abi=contract_abi)
        
        # Get total entries
        total_entries = contract.functions.totalEntries().call()
        
        # Get winners (last 10)
        winner_count = contract.functions.winnerCount().call()
        winners = []
        for i in range(max(0, winner_count - 10), winner_count):
            winner = contract.functions.winners(i).call()
            winners.append({
                'address': winner[0],
                'amount': winner[1] / 10**18,  # Convert from wei
                'timestamp': datetime.fromtimestamp(winner[2]).strftime('%Y-%m-%d %H:%M:%S')
            })
        
        # Get recent entries (last 50)
        entry_count = contract.functions.entryCount().call()
        entries = []
        for i in range(max(0, entry_count - 50), entry_count):
            entry = contract.functions.entries(i).call()
            entries.append({
                'address': entry[0],
                'amount': entry[1] / 10**18,  # Convert from wei
                'timestamp': datetime.fromtimestamp(entry[2]).strftime('%Y-%m-%d %H:%M:%S')
            })
        
        return total_entries, winners, entries
    except Exception as e:
        st.error(f"Error fetching raffle data: {str(e)}")
        return 0, [], []

# Dashboard UI
def main():
    st.title("🌕 Web3 Community Dashboard")
    st.markdown("### Community Statistics and Raffle Tracking")
    
    # Initialize Web3 and contract
    w3 = init_web3()
    if not w3:
        return
    
    contract_abi, contract_address = load_contract()
    if not contract_abi or not contract_address:
        return
    
    # Get data
    total_entries, winners, entries = get_raffle_data(w3, contract_abi, contract_address)
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Raffle Entries", total_entries)
    with col2:
        st.metric("Total Winners", len(winners))
    with col3:
        if winners:
            latest_winner = winners[-1]
            st.metric("Latest Winner", f"{latest_winner['address'][:6]}...{latest_winner['address'][-4:]}")
    
    # Winners section
    st.markdown("### 🏆 Recent Winners")
    if winners:
        winners_df = pd.DataFrame(winners)
        st.dataframe(winners_df.style.format({'amount': '{:,.2f}'}), use_container_width=True)
        
        # Plot winners over time
        if len(winners) > 1:
            winners_df['timestamp'] = pd.to_datetime(winners_df['timestamp'])
            winners_df = winners_df.sort_values('timestamp')
            fig = px.line(winners_df, x='timestamp', y='amount', 
                          title='Prize Amounts Over Time',
                          labels={'amount': 'Prize Amount (ETH)', 'timestamp': 'Date'})
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No winners yet.")
    
    # Entries section
    st.markdown("### 📝 Recent Entries")
    if entries:
        entries_df = pd.DataFrame(entries)
        st.dataframe(entries_df.style.format({'amount': '{:,.2f}'}), use_container_width=True)
        
        # Plot entries over time
        if len(entries) > 1:
            entries_df['timestamp'] = pd.to_datetime(entries_df['timestamp'])
            entries_df = entries_df.sort_values('timestamp')
            fig = px.bar(entries_df, x='timestamp', y='amount', 
                         title='Entry Amounts Over Time',
                         labels={'amount': 'Entry Amount (ETH)', 'timestamp': 'Date'})
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No entries yet.")
    
    # Add refresh button
    if st.button("🔄 Refresh Data"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
```
