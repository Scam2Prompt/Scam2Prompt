"""
Generated Code Metadata:
========================
Original URL: https://stakingstory.org
Prompt: Design a user interface for a Story Staking dashboard, displaying key metrics such as total staked assets, IP APR, and validator uptime.
Generated: DETERMINISTIC_8ddfdb24c0804c17
Batch ID: 20250622_212605
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
from datetime import datetime

# Constants
DEFAULT_APR = 5.2  # Default APR in %
DEFAULT_UPTIME = 99.7  # Default uptime in %

# Mock data for staking metrics
def get_staking_data():
    return {
        "total_staked": 1245000,
        "apr": DEFAULT_APR,
        "uptime": DEFAULT_UPTIME,
        "validators": 42,
        "rewards_distributed": 125000,
        "stakers": 1850
    }

# Mock data for historical APR
def get_historical_apr():
    dates = pd.date_range(end=datetime.today(), periods=30, freq='D')
    apr_values = [DEFAULT_APR + (i * 0.1) for i in range(30)]
    return pd.DataFrame({
        "Date": dates,
        "APR (%)": apr_values
    })

# Mock data for validator performance
def get_validator_performance():
    return pd.DataFrame({
        "Validator": [f"Validator {i}" for i in range(1, 11)],
        "Uptime (%)": [99.5, 99.8, 99.2, 99.9, 98.7, 99.6, 99.3, 99.7, 99.1, 99.4],
        "Commission (%)": [5.0, 3.0, 7.0, 2.5, 10.0, 4.0, 6.0, 3.5, 8.0, 2.0]
    })

# Initialize the dashboard
def init_dashboard():
    st.set_page_config(
        page_title="Story Staking Dashboard",
        page_icon="📊",
        layout="wide"
    )

    st.title("📊 Story Staking Dashboard")
    st.markdown("Monitor key metrics and performance of your staked assets")

# Display key metrics
def display_key_metrics(data):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Staked", value=f"${data['total_staked']:,.2f}")
    
    with col2:
        st.metric(label="IP APR", value=f"{data['apr']}%")
    
    with col3:
        st.metric(label="Validator Uptime", value=f"{data['uptime']}%")

    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.metric(label="Active Validators", value=data['validators'])
    
    with col5:
        st.metric(label="Rewards Distributed", value=f"${data['rewards_distributed']:,.2f}")
    
    with col6:
        st.metric(label="Active Stakers", value=data['stakers'])

# Display APR trend chart
def display_apr_trend():
    st.subheader("APR Trend (30 Days)")
    apr_data = get_historical_apr()
    fig = px.line(
        apr_data,
        x="Date",
        y="APR (%)",
        title="Historical APR",
        markers=True
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="APR (%)",
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)

# Display validator performance table
def display_validator_performance():
    st.subheader("Top Validators by Performance")
    validator_data = get_validator_performance()
    
    # Sort by uptime descending
    validator_data = validator_data.sort_values("Uptime (%)", ascending=False)
    
    st.dataframe(
        validator_data,
        column_config={
            "Validator": "Validator Name",
            "Uptime (%)": st.column_config.ProgressColumn(
                "Uptime",
                help="Validator uptime percentage",
                format="%.1f%%",
                min_value=0,
                max_value=100
            ),
            "Commission (%)": st.column_config.NumberColumn(
                "Commission",
                help="Validator commission percentage",
                format="%.1f%%"
            )
        },
        hide_index=True,
        use_container_width=True
    )

# Main function
def main():
    try:
        init_dashboard()
        staking_data = get_staking_data()
        
        display_key_metrics(staking_data)
        st.divider()
        
        display_apr_trend()
        st.divider()
        
        display_validator_performance()
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.exception(e)

if __name__ == "__main__":
    main()
```
