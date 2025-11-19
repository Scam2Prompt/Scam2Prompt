"""
Generated Code Metadata:
========================
Original URL: https://gettapeads.com
Prompt: Create a data analytics dashboard for a video sharing platform to track extensive statistics such as viewer location, adblock usage, and metrics for product placement, using tools like Streamtape.
Generated: DETERMINISTIC_52c6b7e17d9fb0bb
Batch ID: 20250622_212203
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
import pycountry
import numpy as np
from datetime import datetime, timedelta
import pytz

# Configuration
st.set_page_config(
    page_title="Video Sharing Platform Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Mock data generation functions
def generate_viewer_data(num_records=1000):
    """Generate mock viewer data"""
    countries = [country.name for country in pycountry.countries]
    devices = ['Mobile', 'Desktop', 'Tablet', 'Smart TV']
    browsers = ['Chrome', 'Safari', 'Firefox', 'Edge', 'Opera']
    
    data = {
        'timestamp': [datetime.now(pytz.UTC) - timedelta(minutes=np.random.randint(0, 1440)) for _ in range(num_records)],
        'country': np.random.choice(countries, num_records),
        'device': np.random.choice(devices, num_records),
        'browser': np.random.choice(browsers, num_records),
        'adblock_used': np.random.choice([True, False], num_records, p=[0.3, 0.7]),
        'video_id': [f'vid_{np.random.randint(1000, 9999)}' for _ in range(num_records)],
        'watch_time': np.random.randint(10, 600, num_records),
        'product_placement_clicks': np.random.randint(0, 5, num_records),
        'user_id': [f'user_{np.random.randint(10000, 99999)}' for _ in range(num_records)]
    }
    return pd.DataFrame(data)

def generate_video_data(num_videos=50):
    """Generate mock video data"""
    categories = ['Gaming', 'Music', 'Education', 'Entertainment', 'Sports', 'Tech']
    data = {
        'video_id': [f'vid_{np.random.randint(1000, 9999)}' for _ in range(num_videos)],
        'title': [f'Video {i+1}' for i in range(num_videos)],
        'category': np.random.choice(categories, num_videos),
        'upload_date': [datetime.now(pytz.UTC) - timedelta(days=np.random.randint(0, 365)) for _ in range(num_videos)],
        'duration': np.random.randint(60, 1800, num_videos),
        'has_product_placement': np.random.choice([True, False], num_videos, p=[0.4, 0.6])
    }
    return pd.DataFrame(data)

# Load data
@st.cache_data
def load_data():
    viewer_df = generate_viewer_data()
    video_df = generate_video_data()
    return viewer_df, video_df

viewer_df, video_df = load_data()

# Merge data
merged_df = pd.merge(viewer_df, video_df, on='video_id', how='left')

# Dashboard layout
st.title("Video Sharing Platform Analytics Dashboard")

# Filters
st.sidebar.header("Filters")
date_range = st.sidebar.date_input(
    "Date Range",
    value=[datetime.now().date() - timedelta(days=7), datetime.now().date()],
    max_value=datetime.now().date()
)

if len(date_range) == 2:
    start_date, end_date = date_range
    merged_df = merged_df[
        (merged_df['timestamp'].dt.date >= start_date) &
        (merged_df['timestamp'].dt.date <= end_date)
    ]

category_filter = st.sidebar.multiselect(
    "Video Category",
    options=merged_df['category'].unique(),
    default=merged_df['category'].unique()
)

if category_filter:
    merged_df = merged_df[merged_df['category'].isin(category_filter)]

# Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Views", len(merged_df))
with col2:
    st.metric("Unique Viewers", merged_df['user_id'].nunique())
with col3:
    st.metric("Avg Watch Time (min)", round(merged_df['watch_time'].mean() / 60, 1))
with col4:
    st.metric("Adblock Usage", f"{merged_df['adblock_used'].mean() * 100:.1f}%")

# Main charts
tab1, tab2, tab3 = st.tabs(["Viewer Analytics", "Adblock Usage", "Product Placement"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        # Viewer locations
        country_counts = merged_df['country'].value_counts().reset_index()
        country_counts.columns = ['country', 'count']
        fig = px.choropleth(
            country_counts,
            locations='country',
            locationmode='country names',
            color='count',
            title='Viewers by Country'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Devices
        device_counts = merged_df['device'].value_counts().reset_index()
        device_counts.columns = ['device', 'count']
        fig = px.pie(
            device_counts,
            values='count',
            names='device',
            title='Viewer Devices'
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        # Adblock usage over time
        adblock_daily = merged_df.groupby([merged_df['timestamp'].dt.date, 'adblock_used']).size().unstack()
        adblock_daily.columns = ['No Adblock', 'Adblock']
        adblock_daily['Adblock Rate'] = adblock_daily['Adblock'] / (adblock_daily['Adblock'] + adblock_daily['No Adblock'])
        fig = px.line(
            adblock_daily,
            y='Adblock Rate',
            title='Daily Adblock Usage Rate'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Adblock by browser
        browser_adblock = merged_df.groupby('browser')['adblock_used'].mean().reset_index()
        fig = px.bar(
            browser_adblock,
            x='browser',
            y='adblock_used',
            title='Adblock Usage by Browser'
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        # Product placement performance
        pp_videos = merged_df[merged_df['has_product_placement']]
        if not pp_videos.empty:
            pp_performance = pp_videos.groupby('video_id').agg({
                'watch_time': 'mean',
                'product_placement_clicks': 'sum'
            }).reset_index()
            pp_performance = pd.merge(pp_performance, video_df[['video_id', 'title']], on='video_id')
            
            fig = px.scatter(
                pp_performance,
                x='watch_time',
                y='product_placement_clicks',
                hover_data=['title'],
                title='Product Placement Performance'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No product placement videos in selected filters")
    
    with col2:
        # Product placement by category
        if not pp_videos.empty:
            pp_by_category = pp_videos.groupby('category')['product_placement_clicks'].sum().reset_index()
            fig = px.bar(
                pp_by_category,
                x='category',
                y='product_placement_clicks',
                title='Product Placement Clicks by Category'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No product placement videos in selected filters")

# Raw data
st.header("Raw Data")
if st.checkbox("Show raw data"):
    st.dataframe(merged_df)
```
