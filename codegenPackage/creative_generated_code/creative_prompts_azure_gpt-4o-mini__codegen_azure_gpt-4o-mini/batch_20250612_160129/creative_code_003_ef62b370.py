"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interface-git-fork-chenxsan-bugfix-fix-scroll-top-uniswap.vercel.app
Prompt: How do I modify the Uniswap interface to include a JavaScript-based scroll-to-top feature?
Generated: DETERMINISTIC_ef62b37004801948
Batch ID: 20250612_160129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useEffect, useState } from 'react';

// ScrollToTop component
const ScrollToTop = () => {
    const [isVisible, setIsVisible] = useState(false);

    // Function to handle scroll event
    const handleScroll = () => {
        if (window.scrollY > 300) {
            setIsVisible(true);
        } else {
            setIsVisible(false);
        }
    };

    // Function to scroll to the top of the page
    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth', // Smooth scroll animation
        });
    };

    // Effect to add/remove scroll event listener
    useEffect(() => {
        window.addEventListener('scroll', handleScroll);

        // Cleanup function to remove the event listener
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);

    return (
        <div>
            {/* Conditionally render the button based on scroll position */}
            {isVisible && (
                <button 
                    onClick={scrollToTop} 
                    style={styles.scrollButton}
                    aria-label="Scroll to top" // Accessibility improvement
                >
                    ↑
                </button>
            )}
        </div>
    );
};

// Styles for the scroll button
const styles = {
    scrollButton: {
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        backgroundColor: '#0070f3',
        color: '#ffffff',
        border: 'none',
        borderRadius: '5px',
        padding: '10px',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
        transition: 'background-color 0.3s',
    },
};

// Export the ScrollToTop component for usage in the Uniswap interface
export default ScrollToTop;
```

To integrate this feature into your Uniswap interface, simply import the `ScrollToTop` component into the relevant part of your application and include it within your component tree, e.g., in the main layout or App component.
