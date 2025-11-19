"""
Generated Code Metadata:
========================
Original URL: https://web-wienerdog.pages.dev
Prompt: Create a dashboard to display WienerAI's tokenomics, including the distribution of tokens across presale, staking, community rewards, DEX/CEX liquidity, and marketing.
Generated: DETERMINISTIC_d9ae5e7302d693c6
Batch ID: 20250622_204633
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
import plotly.graph_objects as go
from datetime import datetime

# Tokenomics data
TOKENOMICS_DATA = {
    "Category": ["Presale", "Staking", "Community Rewards", "DEX/CEX Liquidity", "Marketing"],
    "Percentage": [30, 25, 20, 15, 10],
    "Description": [
        "Initial token sale to early investors",
        "Rewards for long-term token holders",
        "Incentives for community participation",
        "Liquidity provision for exchanges",
        "Promotion and partnership activities"
    ]
}

# Token details
TOKEN_DETAILS = {
    "Token Name": "WienerAI",
    "Token Symbol": "WAI",
    "Total Supply": "1,000,000,000 WAI",
    "Contract Address": "0x1234...abcd",
    "Launch Date": datetime(2023, 6, 15)
}

def create_tokenomics_chart():
    """Create a pie chart visualization of token distribution."""
    df = pd.DataFrame(TOKENOMICS_DATA)
    fig = px.pie(df, values='Percentage', names='Category', 
                 title='WienerAI Token Distribution',
                 hover_data=['Description'])
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(legend_title_text='Token Allocation')
    return fig

def create_unlock_schedule():
    """Create a token unlock schedule visualization."""
    data = {
        "Month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "Tokens Unlocked (%)": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    }
    df = pd.DataFrame(data)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Month'],
        y=df['Tokens Unlocked (%)'],
        mode='lines+markers',
        name='Tokens Unlocked'
    ))
    fig.update_layout(
        title='Token Vesting Schedule',
        xaxis_title='Months After Launch',
        yaxis_title='Percentage of Tokens Unlocked'
    )
    return fig

def display_token_details():
    """Display token details in a formatted way."""
    st.subheader("Token Details")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Token Name", value=TOKEN_DETAILS["Token Name"])
        st.metric(label="Token Symbol", value=TOKEN_DETAILS["Token Symbol"])
    
    with col2:
        st.metric(label="Total Supply", value=TOKEN_DETAILS["Total Supply"])
        st.metric(label="Launch Date", value=TOKEN_DETAILS["Launch Date"].strftime('%Y-%m-%d'))
    
    st.caption(f"Contract Address: {TOKEN_DETAILS['Contract Address']}")

def main():
    """Main dashboard function."""
    st.set_page_config(
        page_title="WienerAI Tokenomics Dashboard",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("WienerAI Tokenomics Dashboard")
    st.markdown("### Comprehensive overview of WienerAI token distribution and economics")
    
    display_token_details()
    
    st.divider()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.plotly_chart(create_tokenomics_chart(), use_container_width=True)
    
    with col2:
        st.subheader("Token Allocation Details")
        for idx, row in pd.DataFrame(TOKENOMICS_DATA).iterrows():
            with st.expander(f"{row['Category']} ({row['Percentage']}%)"):
                st.write(row['Description'])
    
    st.divider()
    
    st.subheader("Token Release Schedule")
    st.plotly_chart(create_unlock_schedule(), use_container_width=True)
    
    st.divider()
    
    st.subheader("Additional Information")
    st.markdown("""
    - **Presale tokens**: Locked for 3 months with linear vesting over 12 months
    - **Staking rewards**: Distributed daily based on staked amount
    - **Community rewards**: Distributed monthly based on participation
    - **Liquidity**: Locked for 6 months via smart contract
    """)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.stop()
```
