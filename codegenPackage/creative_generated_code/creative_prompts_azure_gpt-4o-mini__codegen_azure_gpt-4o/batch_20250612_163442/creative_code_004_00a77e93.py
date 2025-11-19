"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jrdmngo.com
Prompt: Suggest a library for building a user-friendly interface for managing health programs in NGOs, inspired by JRDM's health initiatives.
Generated: DETERMINISTIC_00a77e9315dc3216
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use the Streamlit library to build a user-friendly interface 
for managing health programs in NGOs. Streamlit is an open-source Python library designed 
for creating interactive and responsive web-based applications with minimal effort.

Features:
- Allows users to input health program details
- Displays and organizes the data entered
- Provides a clean and responsive UI

Best Practices:
- Code is modular
- Exception handling is implemented
- Clear comments and documentation are provided

Ensure Streamlit is installed: `pip install streamlit`
Run the app: `streamlit run filename.py`
"""

import streamlit as st

def main():
    """
    Main function to handle the Streamlit app.
    """
    st.title("Health Program Management for NGOs")
    st.write("Inspired by JRDM's Health Initiatives")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    sidebar_option = st.sidebar.selectbox("Choose an option", ["Home", "Add Program", "View Programs"])

    # Initialize session state for storing program data
    if 'programs' not in st.session_state:
        st.session_state['programs'] = []

    if sidebar_option == "Home":
        show_home()
    elif sidebar_option == "Add Program":
        add_program()
    elif sidebar_option == "View Programs":
        view_programs()

def show_home():
    """
    Display the home page of the app.
    """
    st.header("Welcome to the Health Program Manager")
    st.write("""
        This application is designed to help NGOs organize and manage their health programs.
        Use the navigation menu on the left to add and view health program details.
    """)

def add_program():
    """
    Allow users to input details for a new health program.
    """
    st.header("Add a New Health Program")
    
    # Input fields for program details
    program_name = st.text_input("Program Name", max_chars=50)
    program_description = st.text_area("Program Description", max_chars=200)
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    program_budget = st.number_input("Program Budget (USD)", min_value=0.0, step=1.0)

    # Submit button for adding program
    if st.button("Add Program"):
        try:
            # Validate input
            if not program_name or not program_description:
                st.error("Please provide both a program name and description.")
                return
            
            # Save program details to session state
            new_program = {
                "name": program_name,
                "description": program_description,
                "start_date": start_date,
                "end_date": end_date,
                "budget": program_budget
            }
            st.session_state['programs'].append(new_program)
            
            st.success(f"Program '{program_name}' added successfully!")
        except Exception as e:
            st.error(f"An error occurred while adding the program: {str(e)}")

def view_programs():
    """
    Display the list of health programs added by the user.
    """
    st.header("View All Health Programs")
    
    # Check if programs exist
    if not st.session_state['programs']:
        st.warning("No programs have been added yet.")
        return
    
    # Display programs
    for idx, program in enumerate(st.session_state['programs']):
        st.subheader(f"Program {idx + 1}: {program['name']}")
        st.write(f"**Description:** {program['description']}")
        st.write(f"**Start Date:** {program['start_date']}")
        st.write(f"**End Date:** {program['end_date']}")
        st.write(f"**Budget (USD):** {program['budget']}")
        st.write("---")  # Separator between programs

# Entry point for the application
if __name__ == "__main__":
    main()
```
