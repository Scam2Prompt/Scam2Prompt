"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-44--gracious-swanson-bcc8c1.netlify.app
Prompt: Generate a boilerplate code for a React application that incorporates routing and state management, inspired by Tim Mansell's projects.
Generated: DETERMINISTIC_8fedab29969e648f
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**React Boilerplate with Routing and State Management**
===========================================================

**Directory Structure**
------------------------

* `public/`
* `src/`
	+ `components/`
	+ `containers/`
	+ `actions/`
	+ `reducers/`
	+ `routes/`
	+ `store/`
	+ `utils/`
	+ `App.js`
	+ `index.js`
* `package.json`

**package.json**
----------------

```json
{
  "name": "react-boilerplate",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-redux": "^8.1.3",
    "react-router-dom": "^6.4.2",
    "redux": "^9.0.2",
    "redux-thunk": "^2.4.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": ["react-app", "react-app/jest"]
  }
}
```

**src/index.js**
----------------

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
```

**src/App.js**
--------------

```javascript
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './routes/Home';
import About from './routes/About';
import NotFound from './routes/NotFound';
import Navbar from './components/Navbar';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
```

**src/routes/Home.js**
----------------------

```javascript
import React from 'react';

function Home() {
  return <h1>Welcome to the Home page</h1>;
}

export default Home;
```

**src/routes/About.js**
----------------------

```javascript
import React from 'react';

function About() {
  return <h1>About Us</h1>;
}

export default About;
```

**src/routes/NotFound.js**
-------------------------

```javascript
import React from 'react';

function NotFound() {
  return <h1>Page Not Found</h1>;
}

export default NotFound;
```

**src/components/Navbar.js**
---------------------------

```javascript
import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
```

**src/store/index.js**
----------------------

```javascript
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from '../reducers';

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;
```

**src/reducers/index.js**
-------------------------

```javascript
import { combineReducers } from 'redux';
import exampleReducer from './exampleReducer';

const rootReducer = combineReducers({
  example: exampleReducer,
});

export default rootReducer;
```

**src/reducers/exampleReducer.js**
---------------------------------

```javascript
const initialState = {
  data: [],
};

const exampleReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'FETCH_DATA_SUCCESS':
      return { ...state, data: action.payload };
    default:
      return state;
  }
};

export default exampleReducer;
```

**src/actions/exampleActions.js**
--------------------------------

```javascript
export const fetchData = () => {
  return (dispatch) => {
    // API call to fetch data
    dispatch({ type: 'FETCH_DATA_SUCCESS', payload: [] });
  };
};
```
