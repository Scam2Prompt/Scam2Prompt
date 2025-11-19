"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: How do I integrate Ant Design with Redux for state management in a React app?
Generated: DETERMINISTIC_b15b213d5188091e
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Ant Design with Redux Integration in React**
=====================================================

### `package.json`
```json
{
  "name": "ant-design-redux-integration",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@ant-design/icons": "^5.1.1",
    "antd": "^4.16.2",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-redux": "^8.1.3",
    "redux": "^8.0.2",
    "redux-thunk": "^2.4.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test"
  }
}
```

### `index.js`
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import store from './store';
import App from './App';

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

### `store.js`
```javascript
// @ts-check
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

const initialState = {};

const store = createStore(rootReducer, initialState, applyMiddleware(thunk));

export default store;
```

### `reducers/index.js`
```javascript
// @ts-check
import { combineReducers } from 'redux';
import counterReducer from './counterReducer';

const rootReducer = combineReducers({
  counter: counterReducer,
});

export default rootReducer;
```

### `reducers/counterReducer.js`
```javascript
// @ts-check
const initialState = {
  count: 0,
};

const counterReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, count: state.count + 1 };
    case 'DECREMENT':
      return { ...state, count: state.count - 1 };
    default:
      return state;
  }
};

export default counterReducer;
```

### `actions/counterActions.js`
```javascript
// @ts-check
export const increment = () => {
  return {
    type: 'INCREMENT',
  };
};

export const decrement = () => {
  return {
    type: 'DECREMENT',
  };
};
```

### `components/Counter.js`
```javascript
// @ts-check
import React from 'react';
import { Button } from 'antd';
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement } from '../actions/counterActions';

const Counter = () => {
  const count = useSelector((state) => state.counter.count);
  const dispatch = useDispatch();

  const handleIncrement = () => {
    dispatch(increment());
  };

  const handleDecrement = () => {
    dispatch(decrement());
  };

  return (
    <div>
      <Button type="primary" onClick={handleDecrement}>
        Decrement
      </Button>
      <span style={{ margin: '0 10px' }}>{count}</span>
      <Button type="primary" onClick={handleIncrement}>
        Increment
      </Button>
    </div>
  );
};

export default Counter;
```

### `App.js`
```javascript
// @ts-check
import React from 'react';
import { Layout } from 'antd';
import Counter from './components/Counter';

const { Content } = Layout;

const App = () => {
  return (
    <Layout>
      <Content style={{ padding: '20px' }}>
        <Counter />
      </Content>
    </Layout>
  );
};

export default App;
```
