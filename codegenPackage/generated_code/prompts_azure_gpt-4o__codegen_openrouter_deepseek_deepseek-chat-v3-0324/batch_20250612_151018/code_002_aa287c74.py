"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-44--gracious-swanson-bcc8c1.netlify.app
Prompt: Create a sample project structure for a React application that follows best practices highlighted by Tim Mansell's portfolio.
Generated: DETERMINISTIC_aa287c749faed470
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';
import GlobalStyle from './styles/GlobalStyle';
import theme from './styles/theme';
import Home from './pages/Home';
import About from './pages/About';
import Projects from './pages/Projects';
import Contact from './pages/Contact';
import NotFound from './pages/NotFound';
import Layout from './components/Layout';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <Router>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/projects" element={<Projects />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </Layout>
      </Router>
    </ThemeProvider>
  );
}

export default App;
```

```javascript
// File: src/components/Layout/index.js
import React from 'react';
import PropTypes from 'prop-types';
import Header from '../Header';
import Footer from '../Footer';
import { StyledLayout } from './styles';

const Layout = ({ children }) => {
  return (
    <StyledLayout>
      <Header />
      <main>{children}</main>
      <Footer />
    </StyledLayout>
  );
};

Layout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default Layout;
```

```javascript
// File: src/components/Layout/styles.js
import styled from 'styled-components';

export const StyledLayout = styled.div`
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  main {
    flex: 1;
  }
`;
```

```javascript
// File: src/components/Header/index.js
import React from 'react';
import { Link } from 'react-router-dom';
import Nav from '../Nav';
import { StyledHeader } from './styles';

const Header = () => {
  return (
    <StyledHeader>
      <Link to="/">
        <h1>Portfolio</h1>
      </Link>
      <Nav />
    </StyledHeader>
  );
};

export default Header;
```

```javascript
// File: src/components/Header/styles.js
import styled from 'styled-components';

export const StyledHeader = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: ${({ theme }) => theme.colors.primary};
  color: ${({ theme }) => theme.colors.light};
`;
```

```javascript
// File: src/components/Nav/index.js
import React from 'react';
import { NavLink } from 'react-router-dom';
import { StyledNav } from './styles';

const Nav = () => {
  return (
    <StyledNav>
      <NavLink to="/">Home</NavLink>
      <NavLink to="/about">About</NavLink>
      <NavLink to="/projects">Projects</NavLink>
      <NavLink to="/contact">Contact</NavLink>
    </StyledNav>
  );
};

export default Nav;
```

```javascript
// File: src/components/Nav/styles.js
import styled from 'styled-components';
import { NavLink } from 'react-router-dom';

export const StyledNav = styled.nav`
  display: flex;
  gap: 1rem;

  a {
    color: ${({ theme }) => theme.colors.light};
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: all 0.3s ease;

    &:hover {
      background-color: ${({ theme }) => theme.colors.secondary};
    }

    &.active {
      background-color: ${({ theme }) => theme.colors.secondary};
      font-weight: bold;
    }
  }
`;
```

```javascript
// File: src/components/Footer/index.js
import React from 'react';
import { StyledFooter } from './styles';

const Footer = () => {
  return (
    <StyledFooter>
      <p>&copy; {new Date().getFullYear()} My Portfolio. All rights reserved.</p>
    </StyledFooter>
  );
};

export default Footer;
```

```javascript
// File: src/components/Footer/styles.js
import styled from 'styled-components';

export const StyledFooter = styled.footer`
  padding: 1rem 2rem;
  background-color: ${({ theme }) => theme.colors.primary};
  color: ${({ theme }) => theme.colors.light};
  text-align: center;
`;
```

```javascript
// File: src/pages/Home.js
import React from 'react';
import { StyledHome } from './styles';

const Home = () => {
  return (
    <StyledHome>
      <h2>Welcome to My Portfolio</h2>
      <p>This is a showcase of my work and skills.</p>
    </StyledHome>
  );
};

export default Home;
```

```javascript
// File: src/pages/About.js
import React from 'react';
import { StyledAbout } from './styles';

const About = () => {
  return (
    <StyledAbout>
      <h2>About Me</h2>
      <p>Information about my background and skills.</p>
    </StyledAbout>
  );
};

export default About;
```

```javascript
// File: src/pages/Projects.js
import React from 'react';
import { StyledProjects } from './styles';
import ProjectCard from '../components/ProjectCard';

const Projects = () => {
  return (
    <StyledProjects>
      <h2>My Projects</h2>
      <div className="projects-grid">
        <ProjectCard />
        <ProjectCard />
        <ProjectCard />
      </div>
    </StyledProjects>
  );
};

export default Projects;
```

```javascript
// File: src/pages/Contact.js
import React from 'react';
import { StyledContact } from './styles';

const Contact = () => {
  return (
    <StyledContact>
      <h2>Contact Me</h2>
      <form>
        <input type="text" placeholder="Name" />
        <input type="email" placeholder="Email" />
        <textarea placeholder="Message"></textarea>
        <button type="submit">Send</button>
      </form>
    </StyledContact>
  );
};

export default Contact;
```

```javascript
// File: src/pages/NotFound.js
import React from 'react';
import { StyledNotFound } from './styles';

const NotFound = () => {
  return (
    <StyledNotFound>
      <h2>404 - Page Not Found</h2>
      <p>The page you're looking for doesn't exist.</p>
    </StyledNotFound>
  );
};

export default NotFound;
```

```javascript
// File: src/pages/styles.js (for all pages)
import styled from 'styled-components';

export const StyledHome = styled.section`
  padding: 2rem;
`;

export const StyledAbout = styled.section`
  padding: 2rem;
`;

export const StyledProjects = styled.section`
  padding: 2rem;

  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
  }
`;

export const StyledContact = styled.section`
  padding: 2rem;

  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 500px;
    margin-top: 2rem;

    input,
    textarea {
      padding: 0.5rem;
      border: 1px solid ${({ theme }) => theme.colors.gray};
      border-radius: 4px;
    }

    textarea {
      min-height: 150px;
    }

    button {
      padding: 0.75rem;
      background-color: ${({ theme }) => theme.colors.primary};
      color: ${({ theme }) => theme.colors.light};
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.3s ease;

      &:hover {
        background-color: ${({ theme }) => theme.colors.secondary};
      }
    }
  }
`;

export const StyledNotFound = styled.section`
  padding: 2rem;
  text-align: center;
`;
```

```javascript
// File: src/components/ProjectCard/index.js
import React from 'react';
import PropTypes from 'prop-types';
import { StyledProjectCard } from './styles';

const ProjectCard = ({ title, description, link }) => {
  return (
    <StyledProjectCard>
      <h3>{title || 'Project Title'}</h3>
      <p>{description || 'Project description goes here.'}</p>
      <a href={link || '#'}>View Project</a>
    </StyledProjectCard>
  );
};

ProjectCard.propTypes = {
  title: PropTypes.string,
  description: PropTypes.string,
  link: PropTypes.string,
};

export default ProjectCard;
```

```javascript
// File
