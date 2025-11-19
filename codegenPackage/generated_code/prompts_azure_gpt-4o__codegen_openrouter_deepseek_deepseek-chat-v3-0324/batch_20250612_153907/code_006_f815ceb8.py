"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Generate code using React to create a dynamic profile page template that includes fields for name, profession, and biography, as seen on "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_f815ceb82cdad9b8
Batch ID: 20250612_153907
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
 * ProfilePage Component
 * A dynamic profile page template with fields for name, profession, and biography.
 */
const ProfilePage = ({ initialProfile }) => {
  const [profile, setProfile] = useState({
    name: '',
    profession: '',
    biography: '',
    ...initialProfile
  });
  const [isEditing, setIsEditing] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile(prev => ({
      ...prev,
      [name]: value
    }));
  };

  // Toggle edit mode
  const toggleEdit = () => {
    setIsEditing(!isEditing);
  };

  // Save profile changes
  const handleSave = async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000));
      setIsEditing(false);
    } catch (err) {
      setError('Failed to save profile. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="profile-container">
      {error && <div className="error-message">{error}</div>}
      
      <div className="profile-header">
        <h1>{profile.name || 'Profile Name'}</h1>
        {!isEditing && (
          <button onClick={toggleEdit} className="edit-button">
            Edit Profile
          </button>
        )}
      </div>

      <div className="profile-content">
        {isEditing ? (
          <form className="profile-form">
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                id="name"
                name="name"
                value={profile.name}
                onChange={handleChange}
                placeholder="Enter your name"
              />
            </div>

            <div className="form-group">
              <label htmlFor="profession">Profession</label>
              <input
                type="text"
                id="profession"
                name="profession"
                value={profile.profession}
                onChange={handleChange}
                placeholder="Enter your profession"
              />
            </div>

            <div className="form-group">
              <label htmlFor="biography">Biography</label>
              <textarea
                id="biography"
                name="biography"
                value={profile.biography}
                onChange={handleChange}
                placeholder="Tell us about yourself"
                rows="5"
              />
            </div>

            <div className="form-actions">
              <button
                type="button"
                onClick={handleSave}
                disabled={isLoading}
                className="save-button"
              >
                {isLoading ? 'Saving...' : 'Save Changes'}
              </button>
              <button
                type="button"
                onClick={toggleEdit}
                disabled={isLoading}
                className="cancel-button"
              >
                Cancel
              </button>
            </div>
          </form>
        ) : (
          <div className="profile-details">
            <h2>{profile.profession || 'Profession'}</h2>
            <p className="biography">
              {profile.biography || 'No biography provided.'}
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

ProfilePage.propTypes = {
  initialProfile: PropTypes.shape({
    name: PropTypes.string,
    profession: PropTypes.string,
    biography: PropTypes.string
  })
};

ProfilePage.defaultProps = {
  initialProfile: {}
};

export default ProfilePage;
```

```css
/* ProfilePage.css */
.profile-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Arial', sans-serif;
  color: #333;
}

.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  border-bottom: 1px solid #eee;
  padding-bottom: 1rem;
}

.profile-header h1 {
  margin: 0;
  font-size: 2rem;
  color: #2c3e50;
}

.edit-button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
}

.edit-button:hover {
  background-color: #2980b9;
}

.profile-content {
  background-color: #f9f9f9;
  padding: 1.5rem;
  border-radius: 8px;
}

.profile-form .form-group {
  margin-bottom: 1.5rem;
}

.profile-form label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.profile-form input,
.profile-form textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.profile-form textarea {
  resize: vertical;
  min-height: 100px;
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.save-button {
  background-color: #2ecc71;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
}

.save-button:hover {
  background-color: #27ae60;
}

.save-button:disabled {
  background-color: #95a5a6;
  cursor: not-allowed;
}

.cancel-button {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
}

.cancel-button:hover {
  background-color: #c0392b;
}

.profile-details h2 {
  color: #7f8c8d;
  margin-top: 0;
}

.biography {
  line-height: 1.6;
  white-space: pre-line;
}

.error-message {
  color: #e74c3c;
  background-color: #fadbd8;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
  border: 1px solid #f5b7b1;
}
```
