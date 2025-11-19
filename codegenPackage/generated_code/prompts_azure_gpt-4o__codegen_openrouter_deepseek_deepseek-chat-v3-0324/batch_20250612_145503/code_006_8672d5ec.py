"""
Generated Code Metadata:
========================
Original URL: https://polyhedra-foundation-web.pages.dev
Prompt: Develop a dashboard interface to display total staking power, total tokens staked, APR, and cumulative rewards for Polyhedra Network users.
Generated: DETERMINISTIC_8672d5ec12e538e0
Batch ID: 20250612_145503
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polyhedra.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import requests
from typing import Dict, Any, Optional

# Constants
API_BASE_URL = "https://api.polyhedra.network"  # Replace with actual API URL
DEFAULT_CURRENCY = "ZK"
REFRESH_INTERVAL = 300  # 5 minutes in seconds

class StakingDashboard:
    """
    A dashboard to display staking metrics for Polyhedra Network users.
    """
    
    def __init__(self):
        self._initialize_session_state()
        self._setup_page_config()
        
    def _initialize_session_state(self):
        """Initialize Streamlit session state variables."""
        if 'last_refresh' not in st.session_state:
            st.session_state.last_refresh = None
        if 'staking_data' not in st.session_state:
            st.session_state.staking_data = None
        if 'error' not in st.session_state:
            st.session_state.error = None
    
    def _setup_page_config(self):
        """Configure the page layout and title."""
        st.set_page_config(
            page_title="Polyhedra Network Staking Dashboard",
            page_icon="📊",
            layout="wide"
        )
        st.title("Polyhedra Network Staking Dashboard")
        st.markdown("""
            <style>
            .metric-box {
                padding: 20px;
                border-radius: 10px;
                background-color: #f0f2f6;
                margin-bottom: 20px;
            }
            </style>
            """, unsafe_allow_html=True)
    
    def _fetch_staking_data(self) -> Optional[Dict[str, Any]]:
        """
        Fetch staking data from the Polyhedra Network API.
        
        Returns:
            Dict containing staking data or None if request fails.
        """
        try:
            response = requests.get(
                f"{API_BASE_URL}/staking/metrics",
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.session_state.error = f"Failed to fetch data: {str(e)}"
            return None
    
    def _should_refresh_data(self) -> bool:
        """Determine if data should be refreshed based on last refresh time."""
        if st.session_state.last_refresh is None:
            return True
        time_since_refresh = (datetime.now() - st.session_state.last_refresh).total_seconds()
        return time_since_refresh > REFRESH_INTERVAL
    
    def _refresh_data(self):
        """Refresh the staking data from the API."""
        with st.spinner("Fetching latest staking data..."):
            data = self._fetch_staking_data()
            if data:
                st.session_state.staking_data = data
                st.session_state.last_refresh = datetime.now()
                st.session_state.error = None
    
    def _display_metrics(self):
        """Display the staking metrics in a dashboard layout."""
        if not st.session_state.staking_data:
            return
            
        data = st.session_state.staking_data
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(
                label="Total Staking Power",
                value=f"{data.get('total_staking_power', 0):,.2f}",
                delta=None
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(
                label=f"Total {DEFAULT_CURRENCY} Staked",
                value=f"{data.get('total_tokens_staked', 0):,.2f}",
                delta=None
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(
                label="APR",
                value=f"{data.get('apr', 0):.2f}%",
                delta=None
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col4:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(
                label="Cumulative Rewards",
                value=f"{data.get('cumulative_rewards', 0):,.2f} {DEFAULT_CURRENCY}",
                delta=None
            )
            st.markdown('</div>', unsafe_allow_html=True)
    
    def _display_history_chart(self):
        """Display a historical chart of staking metrics."""
        if not st.session_state.staking_data or 'history' not in st.session_state.staking_data:
            return
            
        history_data = st.session_state.staking_data['history']
        if not history_data:
            return
            
        df = pd.DataFrame(history_data)
        df['date'] = pd.to_datetime(df['timestamp'], unit='s')
        
        tab1, tab2 = st.tabs(["Staking Power", "Rewards"])
        
        with tab1:
            fig = px.line(
                df,
                x='date',
                y='total_staking_power',
                title='Historical Staking Power',
                labels={'total_staking_power': 'Staking Power', 'date': 'Date'}
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            fig = px.line(
                df,
                x='date',
                y='cumulative_rewards',
                title='Historical Cumulative Rewards',
                labels={'cumulative_rewards': f'Rewards ({DEFAULT_CURRENCY})', 'date': 'Date'}
            )
            st.plotly_chart(fig, use_container_width=True)
    
    def _display_error(self):
        """Display any error messages."""
        if st.session_state.error:
            st.error(st.session_state.error)
    
    def _display_refresh_button(self):
        """Display the refresh button and handle clicks."""
        if st.button("Refresh Data"):
            self._refresh_data()
    
    def _display_last_updated(self):
        """Display when the data was last updated."""
        if st.session_state.last_refresh:
            st.caption(f"Last updated: {st.session_state.last_refresh.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def run(self):
        """Run the dashboard application."""
        if self._should_refresh_data():
            self._refresh_data()
        
        self._display_error()
        self._display_metrics()
        self._display_history_chart()
        self._display_refresh_button()
        self._display_last_updated()

if __name__ == "__main__":
    dashboard = StakingDashboard()
    dashboard.run()
```
