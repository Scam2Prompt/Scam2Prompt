"""
Generated Code Metadata:
========================
Original URL: https://phosphor.now.sh
Prompt: Write a script to dynamically load service descriptions (e.g., web development, mobile apps, graphic design) into a Next.js page, inspired by Phosphor's service offerings.
Generated: DETERMINISTIC_7d51e5ea07ead231
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/services.js

import { useEffect, useState } from 'react';

// Service component to display individual service details
const Service = ({ title, description, icon }) => (
  <div className="service">
    <img src={icon} alt={`${title} icon`} className="service-icon" />
    <h3>{title}</h3>
    <p>{description}</p>
  </div>
);

// Main Services page component
const ServicesPage = () => {
  const [services, setServices] = useState([]);
  const [error, setError] = useState(null);

  // Fetch service descriptions from an external API or local JSON file
  const fetchServices = async () => {
    try {
      const response = await fetch('/api/services'); // Adjust the endpoint as needed
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setServices(data);
    } catch (err) {
      setError(err.message);
    }
  };

  // Use useEffect to fetch services on component mount
  useEffect(() => {
    fetchServices();
  }, []);

  // Render error message if there is an error
  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  // Render loading state while services are being fetched
  if (services.length === 0) {
    return <div className="loading">Loading services...</div>;
  }

  // Render the list of services
  return (
    <div className="services-container">
      <h1>Our Services</h1>
      <div className="services-list">
        {services.map((service) => (
          <Service
            key={service.id}
            title={service.title}
            description={service.description}
            icon={service.icon}
          />
        ))}
      </div>
    </div>
  );
};

export default ServicesPage;

// styles/globals.css (Add this to your global CSS file for basic styling)
.service {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  margin: 16px;
  text-align: center;
}

.service-icon {
  width: 50px;
  height: 50px;
}

.services-container {
  padding: 20px;
}

.services-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.error {
  color: red;
  text-align: center;
}

.loading {
  text-align: center;
}
```

```javascript
// pages/api/services.js

// Sample API route to serve service descriptions
export default function handler(req, res) {
  // Sample data representing service offerings
  const services = [
    {
      id: 1,
      title: 'Web Development',
      description: 'Building responsive and modern websites.',
      icon: '/icons/web-development.svg',
    },
    {
      id: 2,
      title: 'Mobile Apps',
      description: 'Creating user-friendly mobile applications.',
      icon: '/icons/mobile-apps.svg',
    },
    {
      id: 3,
      title: 'Graphic Design',
      description: 'Designing visually appealing graphics and branding.',
      icon: '/icons/graphic-design.svg',
    },
  ];

  // Respond with the services data
  res.status(200).json(services);
}
```

Make sure to create the appropriate icon files in the `/public/icons/` directory for the icons used in the services.
