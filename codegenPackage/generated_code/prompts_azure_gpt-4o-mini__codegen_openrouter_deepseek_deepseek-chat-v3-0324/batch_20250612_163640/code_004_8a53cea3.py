"""
Generated Code Metadata:
========================
Original URL: https://shinemedia.com.ng
Prompt: How can I customize the pricing cards on my Brainwave.io landing page for better customer engagement?
Generated: DETERMINISTIC_8a53cea347058054
Batch ID: 20250612_163640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready React component for customizable pricing cards with proper styling and error handling:

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * PricingCard Component
 * @param {Object} props - Component props
 * @param {string} props.title - Card title
 * @param {string} props.description - Card description
 * @param {number} props.price - Monthly price
 * @param {string} props.currency - Currency symbol
 * @param {string} props.period - Billing period
 * @param {Array} props.features - List of features
 * @param {string} props.buttonText - CTA button text
 * @param {string} props.highlightText - Highlight badge text
 * @param {boolean} props.isHighlighted - Whether card is highlighted
 * @param {function} props.onButtonClick - Button click handler
 */
const PricingCard = ({
  title = 'Basic',
  description = 'Essential features to get started',
  price = 0,
  currency = '$',
  period = '/month',
  features = [],
  buttonText = 'Get Started',
  highlightText = 'Popular',
  isHighlighted = false,
  onButtonClick = () => {}
}) => {
  const [isHovered, setIsHovered] = useState(false);

  // Validate props
  if (typeof price !== 'number') {
    console.error('Price must be a number');
    price = 0;
  }

  if (!Array.isArray(features)) {
    console.error('Features must be an array');
    features = [];
  }

  return (
    <div
      className={`relative flex flex-col p-6 bg-white rounded-lg shadow-md transition-all duration-300 ${
        isHighlighted ? 'border-2 border-blue-500' : 'border border-gray-200'
      } ${isHovered ? 'transform scale-105' : ''}`}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      {isHighlighted && (
        <div className="absolute top-0 right-0 -mt-3 -mr-3 bg-blue-500 text-white text-xs font-bold px-3 py-1 rounded-full">
          {highlightText}
        </div>
      )}
      
      <h3 className="text-2xl font-bold text-gray-800 mb-2">{title}</h3>
      <p className="text-gray-600 mb-6">{description}</p>
      
      <div className="mb-6">
        <span className="text-4xl font-bold text-gray-900">
          {currency}{price}
        </span>
        <span className="text-gray-600">{period}</span>
      </div>
      
      <ul className="mb-8 space-y-3">
        {features.map((feature, index) => (
          <li key={index} className="flex items-center">
            <svg className="w-5 h-5 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7" />
            </svg>
            <span className="text-gray-700">{feature}</span>
          </li>
        ))}
      </ul>
      
      <button
        onClick={onButtonClick}
        className={`w-full py-3 px-4 rounded-md font-medium transition-colors ${
          isHighlighted
            ? 'bg-blue-600 hover:bg-blue-700 text-white'
            : 'bg-gray-100 hover:bg-gray-200 text-gray-800'
        }`}
      >
        {buttonText}
      </button>
    </div>
  );
};

PricingCard.propTypes = {
  title: PropTypes.string,
  description: PropTypes.string,
  price: PropTypes.number,
  currency: PropTypes.string,
  period: PropTypes.string,
  features: PropTypes.arrayOf(PropTypes.string),
  buttonText: PropTypes.string,
  highlightText: PropTypes.string,
  isHighlighted: PropTypes.bool,
  onButtonClick: PropTypes.func
};

/**
 * PricingSection Component
 * @param {Object} props - Component props
 * @param {Array} props.plans - Array of pricing plans
 */
const PricingSection = ({ plans = [] }) => {
  const handleButtonClick = (planTitle) => {
    console.log(`Selected plan: ${planTitle}`);
    // Add your analytics or navigation logic here
  };

  return (
    <div className="py-12 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-extrabold text-gray-900 sm:text-4xl">
            Flexible Pricing Plans
          </h2>
          <p className="mt-4 text-xl text-gray-600">
            Choose the perfect plan for your needs
          </p>
        </div>
        
        <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
          {plans.map((plan, index) => (
            <PricingCard
              key={index}
              {...plan}
              onButtonClick={() => handleButtonClick(plan.title)}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

PricingSection.propTypes = {
  plans: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      description: PropTypes.string,
      price: PropTypes.number.isRequired,
      features: PropTypes.arrayOf(PropTypes.string).isRequired,
      isHighlighted: PropTypes.bool
    })
  )
};

// Example usage
const App = () => {
  const pricingPlans = [
    {
      title: 'Basic',
      description: 'Perfect for getting started',
      price: 9,
      features: ['10 projects', '5GB storage', 'Basic support'],
      buttonText: 'Start Free Trial'
    },
    {
      title: 'Pro',
      description: 'For growing businesses',
      price: 29,
      features: ['Unlimited projects', '50GB storage', 'Priority support', 'Advanced analytics'],
      highlightText: 'Most Popular',
      isHighlighted: true,
      buttonText: 'Get Started'
    },
    {
      title: 'Enterprise',
      description: 'For large organizations',
      price: 99,
      features: [
        'Unlimited projects',
        '1TB storage',
        '24/7 support',
        'Dedicated account manager',
        'Custom integrations'
      ],
      buttonText: 'Contact Sales'
    }
  ];

  return <PricingSection plans={pricingPlans} />;
};

export default App;
```
