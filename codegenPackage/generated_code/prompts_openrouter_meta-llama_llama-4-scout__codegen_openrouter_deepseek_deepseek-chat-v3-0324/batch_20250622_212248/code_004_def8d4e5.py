"""
Generated Code Metadata:
========================
Original URL: https://richnaturalfoods.com
Prompt: Create a CSS snippet for styling a responsive navigation menu similar to the one on richnaturalfoods.com, adapting it for a gaming site theme.
Generated: DETERMINISTIC_def8d4e5bc8aa949
Batch ID: 20250622_212248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Responsive Gaming Navigation Menu */
.navbar {
    background-color: #1a1a2e;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
}

.navbar-brand {
    color: #e94560;
    font-size: 1.8rem;
    font-weight: 700;
    text-decoration: none;
    font-family: 'Orbitron', sans-serif;
    text-shadow: 0 0 5px rgba(233, 69, 96, 0.7);
}

.navbar-nav {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-item {
    margin-left: 1.5rem;
}

.nav-link {
    color: #f8f8f8;
    text-decoration: none;
    font-size: 1.1rem;
    font-weight: 500;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: all 0.3s ease;
    font-family: 'Rajdhani', sans-serif;
}

.nav-link:hover {
    color: #e94560;
    background-color: rgba(233, 69, 96, 0.1);
    transform: translateY(-2px);
}

.active {
    color: #e94560;
    border-bottom: 2px solid #e94560;
}

.menu-toggle {
    display: none;
    cursor: pointer;
    color: #f8f8f8;
    font-size: 1.5rem;
}

/* Responsive Styles */
@media (max-width: 768px) {
    .navbar {
        flex-direction: column;
        align-items: flex-start;
        padding: 1rem;
    }

    .navbar-nav {
        flex-direction: column;
        width: 100%;
        display: none;
    }

    .navbar-nav.active {
        display: flex;
    }

    .nav-item {
        margin: 0.5rem 0;
    }

    .menu-toggle {
        display: block;
        position: absolute;
        top: 1rem;
        right: 1rem;
    }

    .nav-link {
        padding: 0.8rem;
        width: 100%;
    }
}

/* Animation for menu items */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.nav-item {
    animation: slideIn 0.3s ease forwards;
}

.nav-item:nth-child(1) { animation-delay: 0.1s; }
.nav-item:nth-child(2) { animation-delay: 0.2s; }
.nav-item:nth-child(3) { animation-delay: 0.3s; }
.nav-item:nth-child(4) { animation-delay: 0.4s; }
.nav-item:nth-child(5) { animation-delay: 0.5s; }
```
