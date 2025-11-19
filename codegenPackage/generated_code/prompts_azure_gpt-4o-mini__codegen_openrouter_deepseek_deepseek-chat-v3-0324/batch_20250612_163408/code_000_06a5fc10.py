"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-47--gracious-swanson-bcc8c1.netlify.app
Prompt: Generate a React component for a front-end application that displays user profiles, similar to the examples provided by Tim Mansell.
Generated: DETERMINISTIC_06a5fc1027db8fa5
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * UserProfile Component
 * Displays a user profile with avatar, name, bio, and social links.
 * 
 * @param {Object} props - Component props
 * @param {string} props.avatarUrl - URL of the user's avatar image
 * @param {string} props.name - User's full name
 * @param {string} props.bio - User's biography
 * @param {Object[]} props.socialLinks - Array of social links
 * @param {string} props.socialLinks[].name - Name of the social platform
 * @param {string} props.socialLinks[].url - URL to the user's profile
 * @param {string} props.socialLinks[].icon - Icon class for the platform
 * @param {string} [props.theme='light'] - Theme of the profile (light/dark)
 */
const UserProfile = ({ 
  avatarUrl, 
  name, 
  bio, 
  socialLinks, 
  theme = 'light' 
}) => {
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Validate required props
    if (!avatarUrl || !name) {
      setError('Avatar URL and name are required');
      setIsLoading(false);
      return;
    }

    // Simulate loading for demo purposes
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 500);

    return () => clearTimeout(timer);
  }, [avatarUrl, name]);

  if (error) {
    return (
      <div className={`user-profile user-profile--error user-profile--${theme}`}>
        <div className="user-profile__error">
          <p>Error loading profile: {error}</p>
        </div>
      </div>
    );
  }

  if (isLoading) {
    return (
      <div className={`user-profile user-profile--loading user-profile--${theme}`}>
        <div className="user-profile__loading">
          <div className="user-profile__loading-spinner"></div>
          <p>Loading profile...</p>
        </div>
      </div>
    );
  }

  return (
    <div className={`user-profile user-profile--${theme}`}>
      <div className="user-profile__avatar-container">
        <img 
          src={avatarUrl} 
          alt={`${name}'s avatar`} 
          className="user-profile__avatar"
          onError={() => setError('Failed to load avatar image')}
        />
      </div>

      <div className="user-profile__content">
        <h2 className="user-profile__name">{name}</h2>
        {bio && <p className="user-profile__bio">{bio}</p>}

        {socialLinks && socialLinks.length > 0 && (
          <div className="user-profile__social-links">
            {socialLinks.map((link, index) => (
              <a
                key={index}
                href={link.url}
                target="_blank"
                rel="noopener noreferrer"
                className="user-profile__social-link"
                aria-label={`${name}'s ${link.name} profile`}
              >
                <i className={link.icon}></i>
              </a>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

UserProfile.propTypes = {
  avatarUrl: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  bio: PropTypes.string,
  socialLinks: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string.isRequired,
      url: PropTypes.string.isRequired,
      icon: PropTypes.string.isRequired,
    })
  ),
  theme: PropTypes.oneOf(['light', 'dark']),
};

export default UserProfile;
```

```css
/* UserProfile.css */
.user-profile {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: all 0.3s ease;
}

.user-profile--light {
  background-color: #ffffff;
  color: #333333;
}

.user-profile--dark {
  background-color: #333333;
  color: #ffffff;
}

.user-profile__avatar-container {
  margin-bottom: 1.5rem;
}

.user-profile__avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #4a90e2;
}

.user-profile__name {
  margin: 0 0 1rem;
  font-size: 1.5rem;
  font-weight: 600;
}

.user-profile__bio {
  margin: 0 0 1.5rem;
  color: inherit;
  opacity: 0.8;
  line-height: 1.5;
}

.user-profile__social-links {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.user-profile__social-link {
  color: inherit;
  font-size: 1.2rem;
  transition: color 0.2s ease;
}

.user-profile__social-link:hover {
  color: #4a90e2;
}

.user-profile--loading .user-profile__loading-spinner {
  border: 3px solid rgba(0, 0, 0, 0.1);
  border-radius: 50%;
  border-top: 3px solid #4a90e2;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.user-profile--error .user-profile__error {
  color: #e74c3c;
  font-weight: 500;
}
```
