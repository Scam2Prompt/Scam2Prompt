"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Generate code using React to create a dynamic profile page template that includes fields for name, profession, and biography, as seen on "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_f815ceb82cdad9b8
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary packages
import React, { useState } from "react"; // React for building UI and useState for state management
import PropTypes from "prop-types"; // PropTypes for type checking

// ProfilePage Component
const ProfilePage = ({ initialProfile }) => {
  // State management for profile fields
  const [profile, setProfile] = useState(initialProfile);

  // Event handler for updating profile fields
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setProfile((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Profile Page</h1>

      {/* Name Field */}
      <div style={styles.fieldContainer}>
        <label htmlFor="name" style={styles.label}>
          Name:
        </label>
        <input
          type="text"
          id="name"
          name="name"
          value={profile.name}
          onChange={handleInputChange}
          style={styles.input}
        />
      </div>

      {/* Profession Field */}
      <div style={styles.fieldContainer}>
        <label htmlFor="profession" style={styles.label}>
          Profession:
        </label>
        <input
          type="text"
          id="profession"
          name="profession"
          value={profile.profession}
          onChange={handleInputChange}
          style={styles.input}
        />
      </div>

      {/* Biography Field */}
      <div style={styles.fieldContainer}>
        <label htmlFor="biography" style={styles.label}>
          Biography:
        </label>
        <textarea
          id="biography"
          name="biography"
          value={profile.biography}
          onChange={handleInputChange}
          style={styles.textarea}
        ></textarea>
      </div>

      {/* Display Updated Profile */}
      <div style={styles.resultContainer}>
        <h2 style={styles.resultHeading}>Preview</h2>
        <p><strong>Name:</strong> {profile.name}</p>
        <p><strong>Profession:</strong> {profile.profession}</p>
        <p><strong>Biography:</strong> {profile.biography}</p>
      </div>
    </div>
  );
};

// Define PropTypes for type checking
ProfilePage.propTypes = {
  initialProfile: PropTypes.shape({
    name: PropTypes.string,
    profession: PropTypes.string,
    biography: PropTypes.string,
  }),
};

// Set default props
ProfilePage.defaultProps = {
  initialProfile: {
    name: "",
    profession: "",
    biography: "",
  },
};

// Inline Styles
const styles = {
  container: {
    maxWidth: "800px",
    margin: "0 auto",
    padding: "20px",
    fontFamily: "Arial, sans-serif",
  },
  heading: {
    textAlign: "center",
    color: "#333",
  },
  fieldContainer: {
    marginBottom: "15px",
  },
  label: {
    display: "block",
    fontWeight: "bold",
    marginBottom: "5px",
  },
  input: {
    width: "100%",
    padding: "10px",
    fontSize: "16px",
    borderRadius: "4px",
    border: "1px solid #ccc",
  },
  textarea: {
    width: "100%",
    padding: "10px",
    fontSize: "16px",
    borderRadius: "4px",
    border: "1px solid #ccc",
    minHeight: "100px",
  },
  resultContainer: {
    marginTop: "30px",
    padding: "20px",
    border: "1px solid #eee",
    borderRadius: "4px",
    backgroundColor: "#f9f9f9",
  },
  resultHeading: {
    marginBottom: "15px",
    color: "#555",
  },
};

// Export the component
export default ProfilePage;
```

### Usage Example:
```jsx
import React from "react";
import ReactDOM from "react-dom";
import ProfilePage from "./ProfilePage";

// Render the ProfilePage component
ReactDOM.render(
  <ProfilePage initialProfile={{ name: "John Doe", profession: "Photographer", biography: "Capturing the beauty of Sedona and the Verde Valley." }} />,
  document.getElementById("root")
);
```
