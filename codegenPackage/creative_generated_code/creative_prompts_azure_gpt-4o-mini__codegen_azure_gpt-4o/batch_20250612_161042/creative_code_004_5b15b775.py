"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Suggest a library for building an interactive event schedule for the Celestia festival that includes music and art performances.
Generated: DETERMINISTIC_5b15b775c6e9c3be
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script leveraging the `streamlit` library to create an interactive event schedule for the Celestia festival:

```python
# Import necessary libraries
import streamlit as st
import pandas as pd

# Title and description of the event scheduler application
st.title("Celestia Festival Event Scheduler")
st.markdown("Welcome to the interactive event schedule for Celestia Festival! Browse and explore music and art performances.")

# Sample data representing the event schedule
# Create a DataFrame to simulate event data
event_data = {
    "Event Name": ["Galaxy Groove", "Stellar Portraits", "Aurora Symphony", "Nebula Art"],
    "Category": ["Music", "Art", "Music", "Art"],
    "Date": ["2023-12-01", "2023-12-01", "2023-12-02", "2023-12-02"],
    "Time": ["18:00", "14:00", "20:00", "15:00"],
    "Location": ["Main Stage", "Art Zone", "Main Stage", "Art Zone"],
}

# Convert the data to a Pandas DataFrame
events_df = pd.DataFrame(event_data)

# Sidebar for filtering events
st.sidebar.header("Filter Events")
selected_category = st.sidebar.selectbox("Select Category", options=["All"] + list(events_df["Category"].unique()))
selected_date = st.sidebar.selectbox("Select Date", options=["All"] + list(events_df["Date"].unique()))

# Apply filters to the event schedule
filtered_events = events_df.copy()
if selected_category != "All":
    filtered_events = filtered_events[filtered_events["Category"] == selected_category]
if selected_date != "All":
    filtered_events = filtered_events[filtered_events["Date"] == selected_date]

# Display filtered event schedule
st.subheader("Event Schedule")
if filtered_events.empty:
    st.warning("No events match the selected filters. Please try again.")
else:
    st.dataframe(filtered_events)

# Allow users to select an event for more details
st.subheader("Event Details")
selected_event = st.selectbox("Select an Event", options=["None"] + list(filtered_events["Event Name"]))

if selected_event != "None":
    event_details = filtered_events[filtered_events["Event Name"] == selected_event].iloc[0]
    st.text(f"Event Name: {event_details['Event Name']}")
    st.text(f"Category: {event_details['Category']}")
    st.text(f"Date: {event_details['Date']}")
    st.text(f"Time: {event_details['Time']}")
    st.text(f"Location: {event_details['Location']}")

# Footer
st.markdown("---")
st.markdown("Thank you for exploring the Celestia Festival schedule!")
```

### Key Notes:
- Install required library:
  ```
  pip install streamlit pandas
  ```
- Run this code using:
  ```
  streamlit run <filename>.py
  ```
