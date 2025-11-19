"""
Generated Code Metadata:
========================
Original URL: https://lusogamer.com
Prompt: "Create a simple app using a no-code platform that mimics the functionality of 'Your Liker' or 'Pautang Peso' from LusoGamer."
Generated: DETERMINISTIC_760f2a53efd75397
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import streamlit as st
import pandas as pd
from datetime import datetime

# Set up the Streamlit app
st.set_page_config(page_title="Loan Tracker App", layout="wide")

# Initialize session state for data persistence
if 'loans' not in st.session_state:
    st.session_state.loans = pd.DataFrame(columns=['Name', 'Amount', 'Date', 'Status'])

# App title and description
st.title("💰 Loan Tracker App")
st.markdown("""
A simple app to track loans between friends, similar to 'Your Liker' or 'Pautang Peso'.
""")

# Sidebar for adding new loans
with st.sidebar:
    st.header("Add New Loan")
    name = st.text_input("Borrower Name")
    amount = st.number_input("Loan Amount", min_value=0.0, step=0.01)
    date = st.date_input("Loan Date", datetime.now().date())
    
    if st.button("Add Loan"):
        if name and amount > 0:
            new_loan = pd.DataFrame({
                'Name': [name],
                'Amount': [amount],
                'Date': [date],
                'Status': ['Pending']
            })
            st.session_state.loans = pd.concat([st.session_state.loans, new_loan], ignore_index=True)
            st.success("Loan added successfully!")
        else:
            st.error("Please enter valid name and amount")

# Main content area
st.header("Loan Records")

# Display loans table with action buttons
if not st.session_state.loans.empty:
    # Create a copy to avoid modifying during iteration
    loans_df = st.session_state.loans.copy()
    
    # Add action buttons
    loans_df['Actions'] = ""
    for idx, row in loans_df.iterrows():
        if st.button(f"Mark Paid ✅", key=f"paid_{idx}"):
            st.session_state.loans.at[idx, 'Status'] = 'Paid'
            st.rerun()
        if st.button(f"Delete ❌", key=f"delete_{idx}"):
            st.session_state.loans = st.session_state.loans.drop(index=idx)
            st.rerun()
    
    # Display the table
    st.dataframe(loans_df.drop(columns=['Actions']), use_container_width=True)
    
    # Summary statistics
    st.subheader("Summary")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Loans", f"₱{st.session_state.loans['Amount'].sum():.2f}")
    with col2:
        pending = st.session_state.loans[st.session_state.loans['Status'] == 'Pending']
        st.metric("Pending Loans", f"₱{pending['Amount'].sum():.2f}")
    with col3:
        paid = st.session_state.loans[st.session_state.loans['Status'] == 'Paid']
        st.metric("Paid Loans", f"₱{paid['Amount'].sum():.2f}")
else:
    st.info("No loans recorded yet. Add one using the sidebar!")
```
