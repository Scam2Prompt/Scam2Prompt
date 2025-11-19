"""
Generated Code Metadata:
========================
Original URL: https://rhinofinance.com
Prompt: Create a dashboard interface for lawyers to manage disbursement financing requests, inspired by Rhino Finance's services for legal professionals.
Generated: DETERMINISTIC_dbdc4097af86b8d5
Batch ID: 20250612_142640
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
from datetime import datetime
import sqlite3
from sqlite3 import Error

# Database setup
def create_connection():
    """Create a database connection to SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect('disbursements.db')
        return conn
    except Error as e:
        st.error(f"Error connecting to database: {e}")
    return conn

def initialize_database():
    """Initialize the database with required tables"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT,
                    firm TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS disbursements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    case_reference TEXT NOT NULL,
                    amount REAL NOT NULL,
                    purpose TEXT NOT NULL,
                    status TEXT DEFAULT 'Pending',
                    requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    approved_at TIMESTAMP,
                    FOREIGN KEY (client_id) REFERENCES clients (id)
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS payments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    disbursement_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    method TEXT NOT NULL,
                    reference TEXT,
                    FOREIGN KEY (disbursement_id) REFERENCES disbursements (id)
                )
            ''')
            conn.commit()
        except Error as e:
            st.error(f"Error initializing database: {e}")
        finally:
            conn.close()

# Client management functions
def add_client(name, email, phone=None, firm=None):
    """Add a new client to the database"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO clients (name, email, phone, firm)
                VALUES (?, ?, ?, ?)
            ''', (name, email, phone, firm))
            conn.commit()
            st.success("Client added successfully!")
        except Error as e:
            st.error(f"Error adding client: {e}")
        finally:
            conn.close()

def get_clients():
    """Retrieve all clients from the database"""
    conn = create_connection()
    if conn is not None:
        try:
            return pd.read_sql('SELECT * FROM clients ORDER BY name', conn)
        except Error as e:
            st.error(f"Error retrieving clients: {e}")
            return pd.DataFrame()
        finally:
            conn.close()
    return pd.DataFrame()

# Disbursement management functions
def add_disbursement(client_id, case_reference, amount, purpose):
    """Add a new disbursement request"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO disbursements (client_id, case_reference, amount, purpose)
                VALUES (?, ?, ?, ?)
            ''', (client_id, case_reference, amount, purpose))
            conn.commit()
            st.success("Disbursement request submitted successfully!")
        except Error as e:
            st.error(f"Error submitting disbursement: {e}")
        finally:
            conn.close()

def get_disbursements(status_filter=None):
    """Retrieve disbursements with optional status filter"""
    conn = create_connection()
    if conn is not None:
        try:
            query = '''
                SELECT d.id, c.name as client_name, d.case_reference, 
                       d.amount, d.purpose, d.status, d.requested_at, d.approved_at
                FROM disbursements d
                JOIN clients c ON d.client_id = c.id
            '''
            if status_filter:
                query += f" WHERE d.status = '{status_filter}'"
            query += " ORDER BY d.requested_at DESC"
            return pd.read_sql(query, conn)
        except Error as e:
            st.error(f"Error retrieving disbursements: {e}")
            return pd.DataFrame()
        finally:
            conn.close()
    return pd.DataFrame()

def update_disbursement_status(disbursement_id, new_status):
    """Update the status of a disbursement"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            approved_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if new_status == 'Approved' else None
            cursor.execute('''
                UPDATE disbursements 
                SET status = ?, approved_at = ?
                WHERE id = ?
            ''', (new_status, approved_at, disbursement_id))
            conn.commit()
            st.success(f"Disbursement status updated to {new_status}!")
        except Error as e:
            st.error(f"Error updating disbursement: {e}")
        finally:
            conn.close()

# Payment management functions
def add_payment(disbursement_id, amount, method, reference=None):
    """Record a payment for a disbursement"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO payments (disbursement_id, amount, method, reference)
                VALUES (?, ?, ?, ?)
            ''', (disbursement_id, amount, method, reference))
            conn.commit()
            st.success("Payment recorded successfully!")
        except Error as e:
            st.error(f"Error recording payment: {e}")
        finally:
            conn.close()

def get_payments(disbursement_id=None):
    """Retrieve payments with optional disbursement filter"""
    conn = create_connection()
    if conn is not None:
        try:
            query = '''
                SELECT p.id, d.case_reference, c.name as client_name, 
                       p.amount, p.method, p.payment_date, p.reference
                FROM payments p
                JOIN disbursements d ON p.disbursement_id = d.id
                JOIN clients c ON d.client_id = c.id
            '''
            if disbursement_id:
                query += f" WHERE p.disbursement_id = {disbursement_id}"
            query += " ORDER BY p.payment_date DESC"
            return pd.read_sql(query, conn)
        except Error as e:
            st.error(f"Error retrieving payments: {e}")
            return pd.DataFrame()
        finally:
            conn.close()
    return pd.DataFrame()

# Dashboard UI
def main():
    # Initialize database
    initialize_database()
    
    # Set page config
    st.set_page_config(
        page_title="Legal Disbursement Financing Dashboard",
        page_icon="⚖️",
        layout="wide"
    )
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Clients", "Disbursements", "Payments"])
    
    # Dashboard page
    if page == "Dashboard":
        st.title("Disbursement Financing Dashboard")
        
        # Summary statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            pending = get_disbursements('Pending').shape[0]
            st.metric("Pending Requests", pending)
        with col2:
            approved = get_disbursements('Approved').shape[0]
            st.metric("Approved Requests", approved)
        with col3:
            total_amount = get_disbursements().amount.sum()
            st.metric("Total Disbursed", f"${total_amount:,.2f}")
        
        # Recent activity
        st.subheader("Recent Activity")
        recent_disbursements = get_disbursements().head(5)
        st.dataframe(recent_disbursements)
    
    # Clients page
    elif page == "Clients":
        st.title("Client Management")
        
        # Add new client form
        with st.expander("Add New Client"):
            with st.form("client_form"):
                name = st.text_input("Full Name*", max_chars=100)
                email = st.text_input("Email*", max_chars=100)
                phone = st.text_input("Phone", max_chars=20)
                firm = st.text_input("Law Firm", max_chars=100)
                submitted = st.form_submit_button("Add Client")
                
                if submitted:
                    if not name or not email:
                        st.error("Name and email are required fields")
                    else:
                        add_client(name, email, phone, firm)
        
        # Client list
        st.subheader("Client List")
        clients = get_clients()
        st.dataframe(clients)
    
    # Disbursements page
    elif page == "Disbursements":
        st.title("Disbursement Management")
        
        # Add new disbursement form
        with st.expander("New Disbursement Request"):
            with st.form("disbursement_form"):
                clients = get_clients()
                client_id = st.selectbox(
                    "Client*",
                    options=clients['id'],
                    format_func=lambda x: clients[clients['id'] == x]['name
