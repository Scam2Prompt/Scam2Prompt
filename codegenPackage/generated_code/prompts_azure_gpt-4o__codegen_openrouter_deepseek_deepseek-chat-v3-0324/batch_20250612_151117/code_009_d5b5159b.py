"""
Generated Code Metadata:
========================
Original URL: https://ytyyyy.pages.dev
Prompt: Develop a dashboard interface to display active and closed Allo campaigns, along with the user's participation status and earned points.
Generated: DETERMINISTIC_d5b5159b9f91716a
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import streamlit as st
from datetime import datetime
import pandas as pd
import json
from typing import List, Dict, Optional

# Mock database functions
def get_user_campaigns(user_id: str) -> List[Dict]:
    """Mock function to fetch user's campaign participation data"""
    return [
        {
            "campaign_id": "camp1",
            "title": "Social Media Campaign",
            "status": "active",
            "user_participation": True,
            "points_earned": 150,
            "start_date": "2023-01-15",
            "end_date": "2023-03-15"
        },
        {
            "campaign_id": "camp2",
            "title": "Product Feedback",
            "status": "closed",
            "user_participation": True,
            "points_earned": 75,
            "start_date": "2022-11-01",
            "end_date": "2022-12-31"
        },
        {
            "campaign_id": "camp3",
            "title": "Beta Testing",
            "status": "active",
            "user_participation": False,
            "points_earned": 0,
            "start_date": "2023-02-01",
            "end_date": "2023-04-30"
        }
    ]

def get_all_campaigns() -> List[Dict]:
    """Mock function to fetch all available campaigns"""
    return [
        {
            "campaign_id": "camp1",
            "title": "Social Media Campaign",
            "status": "active",
            "total_participants": 245,
            "total_points": 5000,
            "start_date": "2023-01-15",
            "end_date": "2023-03-15"
        },
        {
            "campaign_id": "camp2",
            "title": "Product Feedback",
            "status": "closed",
            "total_participants": 189,
            "total_points": 2500,
            "start_date": "2022-11-01",
            "end_date": "2022-12-31"
        },
        {
            "campaign_id": "camp3",
            "title": "Beta Testing",
            "status": "active",
            "total_participants": 312,
            "total_points": 7500,
            "start_date": "2023-02-01",
            "end_date": "2023-04-30"
        },
        {
            "campaign_id": "camp4",
            "title": "Referral Program",
            "status": "active",
            "total_participants": 421,
            "total_points": 10000,
            "start_date": "2023-01-01",
            "end_date": "2023-06-30"
        }
    ]

def get_user_points(user_id: str) -> int:
    """Mock function to fetch user's total points"""
    return 225

def display_campaign_card(campaign: Dict, user_data: Optional[Dict] = None) -> None:
    """Display a single campaign card with relevant information"""
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader(campaign["title"])
            st.caption(f"Status: {campaign['status'].capitalize()}")
            st.caption(f"Participants: {campaign.get('total_participants', 'N/A')}")
            
            if user_data:
                participation_status = "✅ Participating" if user_data["user_participation"] else "❌ Not participating"
                st.caption(participation_status)
                if user_data["user_participation"]:
                    st.caption(f"Your points: {user_data['points_earned']}")
            
        with col2:
            if campaign["status"] == "active" and (not user_data or not user_data["user_participation"]):
                if st.button("Join", key=f"join_{campaign['campaign_id']}"):
                    st.success(f"Successfully joined {campaign['title']}!")
            
        st.progress(0.7 if campaign["status"] == "active" else 1.0)
        st.caption(f"Duration: {campaign['start_date']} to {campaign['end_date']}")

def main():
    """Main dashboard function"""
    st.set_page_config(page_title="Allo Campaign Dashboard", layout="wide")
    
    # Mock user ID - in production this would come from auth
    user_id = "user123"
    
    try:
        # Fetch data
        user_campaigns = get_user_campaigns(user_id)
        all_campaigns = get_all_campaigns()
        total_points = get_user_points(user_id)
        
        # Create a mapping of campaign_id to user participation data
        user_campaign_map = {camp["campaign_id"]: camp for camp in user_campaigns}
        
        # Dashboard header
        st.title("Allo Campaign Dashboard")
        st.header(f"Your Points: {total_points}")
        
        # Active campaigns section
        st.header("Active Campaigns")
        active_campaigns = [camp for camp in all_campaigns if camp["status"] == "active"]
        
        if not active_campaigns:
            st.info("No active campaigns at the moment.")
        else:
            for campaign in active_campaigns:
                user_data = user_campaign_map.get(campaign["campaign_id"])
                display_campaign_card(campaign, user_data)
        
        # Closed campaigns section
        st.header("Closed Campaigns")
        closed_campaigns = [camp for camp in all_campaigns if camp["status"] == "closed"]
        
        if not closed_campaigns:
            st.info("No closed campaigns to display.")
        else:
            for campaign in closed_campaigns:
                user_data = user_campaign_map.get(campaign["campaign_id"])
                display_campaign_card(campaign, user_data)
        
        # Add some space at the bottom
        st.write("")
        st.write("")
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please try again later or contact support if the problem persists.")

if __name__ == "__main__":
    main()
```
