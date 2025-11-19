"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: Write a React component to display international tour packages (e.g., Thailand, Bali, Sri Lanka) with pricing and booking options, using the data structure described on the "Best Holidays All India" website.
Generated: DETERMINISTIC_0cb2270ebe6add1e
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * InternationalTourPackage Component
 * Displays international tour packages with pricing and booking options
 */
const InternationalTourPackage = ({ packages }) => {
  const [selectedPackage, setSelectedPackage] = useState(null);
  const [bookingDetails, setBookingDetails] = useState({
    name: '',
    email: '',
    phone: '',
    travelers: 1,
    date: '',
  });
  const [isLoading, setIsLoading] = useState(false);
  const [bookingSuccess, setBookingSuccess] = useState(false);

  useEffect(() => {
    // Reset booking success when package changes
    setBookingSuccess(false);
  }, [selectedPackage]);

  const handlePackageSelect = (pkg) => {
    setSelectedPackage(pkg);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setBookingDetails(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmitBooking = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      // Simulate API call for booking
      await new Promise(resolve => setTimeout(resolve, 1500));
      setBookingSuccess(true);
      setIsLoading(false);
    } catch (error) {
      console.error('Booking failed:', error);
      setIsLoading(false);
    }
  };

  const formatPrice = (price) => {
    return new Intl.NumberFormat('en-IN', {
      style: 'currency',
      currency: 'INR'
    }).format(price);
  };

  return (
    <div className="international-tour-packages">
      <h2>International Tour Packages</h2>
      
      <div className="package-list">
        {packages.map((pkg) => (
          <div 
            key={pkg.id} 
            className={`package-card ${selectedPackage?.id === pkg.id ? 'selected' : ''}`}
            onClick={() => handlePackageSelect(pkg)}
          >
            <div className="package-image">
              <img src={pkg.image} alt={pkg.destination} />
            </div>
            <div className="package-details">
              <h3>{pkg.destination}</h3>
              <p className="duration">{pkg.duration}</p>
              <p className="description">{pkg.description}</p>
              <div className="price-section">
                <span className="price">{formatPrice(pkg.price)}</span>
                <span className="per-person">per person</span>
              </div>
              <button className="view-details-btn">View Details</button>
            </div>
          </div>
        ))}
      </div>

      {selectedPackage && (
        <div className="booking-section">
          <h3>Book {selectedPackage.destination} Package</h3>
          
          {bookingSuccess ? (
            <div className="booking-success">
              <p>Your booking for {selectedPackage.destination} has been confirmed!</p>
              <button onClick={() => setSelectedPackage(null)}>Back to Packages</button>
            </div>
          ) : (
            <form onSubmit={handleSubmitBooking}>
              <div className="form-group">
                <label>Full Name</label>
                <input
                  type="text"
                  name="name"
                  value={bookingDetails.name}
                  onChange={handleInputChange}
                  required
                />
              </div>
              
              <div className="form-group">
                <label>Email</label>
                <input
                  type="email"
                  name="email"
                  value={bookingDetails.email}
                  onChange={handleInputChange}
                  required
                />
              </div>
              
              <div className="form-group">
                <label>Phone Number</label>
                <input
                  type="tel"
                  name="phone"
                  value={bookingDetails.phone}
                  onChange={handleInputChange}
                  required
                />
              </div>
              
              <div className="form-group">
                <label>Travel Date</label>
                <input
                  type="date"
                  name="date"
                  value={bookingDetails.date}
                  onChange={handleInputChange}
                  required
                  min={new Date().toISOString().split('T')[0]}
                />
              </div>
              
              <div className="form-group">
                <label>Number of Travelers</label>
                <input
                  type="number"
                  name="travelers"
                  min="1"
                  max="10"
                  value={bookingDetails.travelers}
                  onChange={handleInputChange}
                  required
                />
              </div>
              
              <div className="price-summary">
                <p>Total Price: {formatPrice(selectedPackage.price * bookingDetails.travelers)}</p>
              </div>
              
              <button type="submit" disabled={isLoading}>
                {isLoading ? 'Processing...' : 'Confirm Booking'}
              </button>
            </form>
          )}
        </div>
      )}
    </div>
  );
};

InternationalTourPackage.propTypes = {
  packages: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      destination: PropTypes.string.isRequired,
      duration: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      image: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default InternationalTourPackage;
```
