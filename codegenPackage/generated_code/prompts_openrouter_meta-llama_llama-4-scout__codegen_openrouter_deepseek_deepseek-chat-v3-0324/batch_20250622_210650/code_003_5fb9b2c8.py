"""
Generated Code Metadata:
========================
Original URL: https://nashekrashe.com
Prompt: Design a UI/UX system for a promo site using Figma, incorporating best practices in component organization, similar to the approach demonstrated in the Brickify Figma Template by NasheKrashe.
Generated: DETERMINISTIC_5fb9b2c80fa7b2f9
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Figma UI/UX System for Promo Site

// Main App Component
const PromoSite = () => {
  return (
    <div className="promo-site">
      <Header />
      <HeroSection />
      <Features />
      <Testimonials />
      <Pricing />
      <Footer />
    </div>
  );
};

// Header Component
const Header = () => {
  return (
    <header className="header">
      <Logo />
      <Navigation />
      <CTAButton text="Get Started" />
    </header>
  );
};

// Hero Section Component
const HeroSection = () => {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1>Your Awesome Product</h1>
        <p>Revolutionary solution for your needs</p>
        <div className="hero-cta">
          <CTAButton text="Try for Free" primary />
          <CTAButton text="Learn More" />
        </div>
      </div>
      <HeroImage />
    </section>
  );
};

// Features Component
const Features = () => {
  const features = [
    {
      icon: <FeatureIcon1 />,
      title: "Feature One",
      description: "Description of feature one"
    },
    {
      icon: <FeatureIcon2 />,
      title: "Feature Two",
      description: "Description of feature two"
    },
    {
      icon: <FeatureIcon3 />,
      title: "Feature Three",
      description: "Description of feature three"
    }
  ];

  return (
    <section className="features">
      <h2>Key Features</h2>
      <div className="features-grid">
        {features.map((feature, index) => (
          <FeatureCard 
            key={index}
            icon={feature.icon}
            title={feature.title}
            description={feature.description}
          />
        ))}
      </div>
    </section>
  );
};

// Testimonials Component
const Testimonials = () => {
  const testimonials = [
    {
      quote: "This product changed my life!",
      author: "John Doe",
      role: "CEO, Company"
    },
    {
      quote: "Incredible value for the price.",
      author: "Jane Smith",
      role: "Marketing Director"
    }
  ];

  return (
    <section className="testimonials">
      <h2>What Our Customers Say</h2>
      <div className="testimonial-cards">
        {testimonials.map((testimonial, index) => (
          <TestimonialCard
            key={index}
            quote={testimonial.quote}
            author={testimonial.author}
            role={testimonial.role}
          />
        ))}
      </div>
    </section>
  );
};

// Pricing Component
const Pricing = () => {
  const plans = [
    {
      name: "Basic",
      price: "$9",
      features: ["Feature 1", "Feature 2", "Feature 3"],
      ctaText: "Get Started"
    },
    {
      name: "Pro",
      price: "$29",
      features: ["All Basic features", "Feature 4", "Feature 5"],
      ctaText: "Buy Now",
      highlighted: true
    },
    {
      name: "Enterprise",
      price: "Custom",
      features: ["All Pro features", "Dedicated support", "Custom solutions"],
      ctaText: "Contact Us"
    }
  ];

  return (
    <section className="pricing">
      <h2>Simple, Transparent Pricing</h2>
      <div className="pricing-plans">
        {plans.map((plan, index) => (
          <PricingCard
            key={index}
            name={plan.name}
            price={plan.price}
            features={plan.features}
            ctaText={plan.ctaText}
            highlighted={plan.highlighted}
          />
        ))}
      </div>
    </section>
  );
};

// Footer Component
const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <Logo />
        <FooterLinks />
        <SocialLinks />
        <Copyright />
      </div>
    </footer>
  );
};

// Reusable Components
const CTAButton = ({ text, primary = false }) => {
  return (
    <button className={`cta-button ${primary ? 'primary' : ''}`}>
      {text}
    </button>
  );
};

const FeatureCard = ({ icon, title, description }) => {
  return (
    <div className="feature-card">
      <div className="feature-icon">{icon}</div>
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
};

const TestimonialCard = ({ quote, author, role }) => {
  return (
    <div className="testimonial-card">
      <blockquote>{quote}</blockquote>
      <div className="author-info">
        <p className="author-name">{author}</p>
        <p className="author-role">{role}</p>
      </div>
    </div>
  );
};

const PricingCard = ({ name, price, features, ctaText, highlighted = false }) => {
  return (
    <div className={`pricing-card ${highlighted ? 'highlighted' : ''}`}>
      <h3>{name}</h3>
      <div className="price">{price}</div>
      <ul className="features-list">
        {features.map((feature, index) => (
          <li key={index}>{feature}</li>
        ))}
      </ul>
      <CTAButton text={ctaText} primary={highlighted} />
    </div>
  );
};

// Export the main component
export default PromoSite;
```
