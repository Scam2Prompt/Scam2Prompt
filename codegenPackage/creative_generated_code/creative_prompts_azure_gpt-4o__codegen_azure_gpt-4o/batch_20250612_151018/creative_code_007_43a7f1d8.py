"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Generate a React component that uses Ant Design's Card and Avatar components to display user profile information.
Generated: DETERMINISTIC_43a7f1d81f5bf66f
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary React and Ant Design components
import React from 'react';
import PropTypes from 'prop-types';
import { Card, Avatar } from 'antd';

// Destructure Meta subcomponent from Card
const { Meta } = Card;

/**
 * UserProfileCard Component
 * A React component that displays a user's profile information
 * using Ant Design's Card and Avatar components.
 *
 * Props:
 * - name: The name of the user (string, required)
 * - description: A short bio or description of the user (string, optional)
 * - avatarUrl: URL of the user's avatar image (string, required)
 */
const UserProfileCard = ({ name, description, avatarUrl }) => {
  return (
    <Card
      style={{ width: 300, margin: '16px auto' }} // Inline styling for width and centering
      hoverable // Adds hover effect
      bordered // Adds border to the card
    >
      {/* Card content with meta information */}
      <Meta
        avatar={<Avatar src={avatarUrl} />} // Avatar image
        title={name} // User's name
        description={description || 'No description provided.'} // Fallback description
      />
    </Card>
  );
};

// Define PropTypes for the component
UserProfileCard.propTypes = {
  name: PropTypes.string.isRequired, // Name is required
  description: PropTypes.string, // Description is optional
  avatarUrl: PropTypes.string.isRequired, // Avatar URL is required
};

// Define default props for optional props
UserProfileCard.defaultProps = {
  description: '', // Default to empty string if description is not provided
};

// Export the component for reuse
export default UserProfileCard;
```
