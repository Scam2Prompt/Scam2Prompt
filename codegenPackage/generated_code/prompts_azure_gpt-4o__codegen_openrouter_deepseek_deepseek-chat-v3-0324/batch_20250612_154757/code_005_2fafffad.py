"""
Generated Code Metadata:
========================
Original URL: https://letswalrus.vercel.app
Prompt: Create a basic "Getting Started" page using Sui Walrus that highlights its ease of use and learning capabilities.
Generated: DETERMINISTIC_2fafffadddd6d82c
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import streamlit as st
from PIL import Image

def main():
    # Configure the page
    st.set_page_config(
        page_title="Sui Walrus - Getting Started",
        page_icon="🦭",
        layout="wide"
    )

    # Custom CSS for styling
    st.markdown("""
    <style>
        .main {
            max-width: 1000px;
            padding: 2rem;
        }
        .header {
            color: #4a8bfc;
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        .subheader {
            color: #4a8bfc;
            font-size: 1.5rem;
            margin-top: 1.5rem;
        }
        .feature-card {
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
            background-color: #f8f9fa;
        }
        .code-block {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 5px;
            font-family: monospace;
            margin: 1rem 0;
        }
        .cta-button {
            background-color: #4a8bfc !important;
            color: white !important;
            font-weight: bold;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            border: none;
            margin-top: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header section
    st.markdown('<div class="header">🦭 Getting Started with Sui Walrus</div>', unsafe_allow_html=True)
    st.markdown("Sui Walrus makes blockchain development simple, intuitive, and accessible for everyone.")
    
    # Hero image (placeholder - replace with actual image path)
    try:
        # In a real app, you would use: image = Image.open("path/to/your/image.png")
        # For demo purposes, we'll create a blank image
        image = Image.new('RGB', (800, 400), color='#4a8bfc')
        st.image(image, caption="Sui Walrus in Action", use_column_width=True)
    except Exception as e:
        st.error(f"Could not load image: {str(e)}")

    # Key Features section
    st.markdown('<div class="subheader">Why Choose Sui Walrus?</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown('<div class="feature-card">'
                        '<h3>🚀 Easy Setup</h3>'
                        '<p>Get started with just a few commands. No complex configurations needed.</p>'
                        '</div>', unsafe_allow_html=True)
            
        with st.container():
            st.markdown('<div class="feature-card">'
                        '<h3>📚 Comprehensive Docs</h3>'
                        '<p>Clear documentation with examples for every feature.</p>'
                        '</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="feature-card">'
                        '<h3>🔧 Developer Friendly</h3>'
                        '<p>Tools and utilities that make development a breeze.</p>'
                        '</div>', unsafe_allow_html=True)
            
        with st.container():
            st.markdown('<div class="feature-card">'
                        '<h3>🌍 Active Community</h3>'
                        '<p>Join thousands of developers building on Sui.</p>'
                        '</div>', unsafe_allow_html=True)

    # Quick Start section
    st.markdown('<div class="subheader">Quick Start</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Install Sui Walrus with pip:
    """)
    st.markdown('<div class="code-block">pip install sui-walrus</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Basic usage example:
    """)
    st.code("""
    from sui_walrus import WalrusClient

    # Connect to the Sui network
    client = WalrusClient()

    # Create a new wallet
    wallet = client.create_wallet()

    print(f"Your new wallet address: {wallet.address}")
    """, language="python")

    # Call to Action
    st.markdown("""
    Ready to dive in?
    """)
    if st.button('Explore Documentation', key='docs_button', help='Click to view full documentation'):
        # In a real app, this would link to your docs
        st.success("Redirecting to documentation... (this is a demo)")
    
    if st.button('Join Community', key='community_button', help='Click to join the community'):
        # In a real app, this would link to your community
        st.success("Redirecting to community... (this is a demo)")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 2rem;">
        © 2023 Sui Walrus | Open Source Project
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
```
