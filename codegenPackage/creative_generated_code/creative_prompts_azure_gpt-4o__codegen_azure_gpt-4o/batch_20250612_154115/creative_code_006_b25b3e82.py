"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phosphor.now.sh
Prompt: Create a landing page layout in Next.js that showcases web development, mobile app development, and graphic design services, similar to Phosphor's offerings.
Generated: DETERMINISTIC_b25b3e82017dfe5b
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js

import Head from 'next/head';

// A simple, clean landing page showcasing services
export default function Home() {
  return (
    <>
      <Head>
        <title>Our Services</title>
        <meta
          name="description"
          content="Web development, mobile app development, and graphic design services."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>

      <main className="container">
        {/* Header Section */}
        <header className="hero">
          <h1 className="hero-title">Welcome to Our Services</h1>
          <p className="hero-subtitle">
            We specialize in Web Development, Mobile App Development, and Graphic Design.
          </p>
        </header>

        {/* Services Section */}
        <section className="services">
          <div className="service">
            <h2>Web Development</h2>
            <p>
              Build modern, scalable, and responsive websites using the latest technologies.
            </p>
          </div>
          <div className="service">
            <h2>Mobile App Development</h2>
            <p>
              Create intuitive and high-performing mobile applications for Android and iOS.
            </p>
          </div>
          <div className="service">
            <h2>Graphic Design</h2>
            <p>
              Design stunning visuals and branding materials to elevate your business.
            </p>
          </div>
        </section>
      </main>

      {/* Footer Section */}
      <footer className="footer">
        <p>&copy; {new Date().getFullYear()} Your Company. All rights reserved.</p>
      </footer>

      {/* Inline CSS */}
      <style jsx>{`
        .container {
          font-family: Arial, sans-serif;
          padding: 0 20px;
          margin: 0 auto;
          max-width: 1200px;
        }

        .hero {
          text-align: center;
          padding: 50px 0;
          background: #f5f5f5;
        }

        .hero-title {
          font-size: 2.5rem;
          margin: 0;
        }

        .hero-subtitle {
          font-size: 1.2rem;
          margin: 10px 0 0;
          color: #555;
        }

        .services {
          display: flex;
          justify-content: space-between;
          margin: 40px 0;
        }

        .service {
          flex: 1;
          margin: 0 15px;
          padding: 20px;
          background: #fff;
          border: 1px solid #ddd;
          border-radius: 8px;
          text-align: center;
        }

        .service h2 {
          font-size: 1.5rem;
          margin: 0 0 10px;
        }

        .service p {
          font-size: 1rem;
          color: #555;
        }

        .footer {
          text-align: center;
          padding: 20px;
          background: #f5f5f5;
        }

        .footer p {
          margin: 0;
          font-size: 0.9rem;
          color: #555;
        }
      `}</style>
    </>
  );
}
```
