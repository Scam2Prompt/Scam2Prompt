"""
Generated Code Metadata:
========================
Original URL: https://fearlesstools.pages.dev
Prompt: Design a simple user interface for a browser extension to interact with Substrate-based dApps, inspired by Fearless Wallet's browser extension sign feature.
Generated: DETERMINISTIC_e9f7d54b2eb2f1c9
Batch ID: 20250622_204650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// ExtensionPopup.tsx - Main popup UI component for the extension
import React, { useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import { ExtensionProvider, useExtension } from './ExtensionContext';
import { SignerPayloadJSON } from '@polkadot/types/types';
import './styles.css';

interface TransactionRequest {
  id: string;
  payload: SignerPayloadJSON;
  origin: string;
}

const PopupApp: React.FC = () => {
  const { requests, approveRequest, rejectRequest } = useExtension();
  const [activeTabId, setActiveTabId] = useState<number | null>(null);

  useEffect(() => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs[0]?.id) setActiveTabId(tabs[0].id);
    });
  }, []);

  const handleApprove = (requestId: string) => {
    if (activeTabId) {
      approveRequest(requestId, activeTabId);
    }
  };

  const handleReject = (requestId: string) => {
    if (activeTabId) {
      rejectRequest(requestId, activeTabId);
    }
  };

  return (
    <div className="extension-popup">
      <header className="header">
        <h1>Substrate Signer</h1>
      </header>

      <div className="content">
        {requests.length === 0 ? (
          <div className="empty-state">
            <p>No pending requests</p>
          </div>
        ) : (
          <div className="requests-list">
            {requests.map((request: TransactionRequest) => (
              <div key={request.id} className="request-card">
                <div className="request-header">
                  <span className="origin">{request.origin}</span>
                </div>
                <div className="request-details">
                  <div className="detail-row">
                    <span>Method:</span>
                    <span>{request.payload.method}</span>
                  </div>
                  <div className="detail-row">
                    <span>Sender:</span>
                    <span className="address">{request.payload.address}</span>
                  </div>
                </div>
                <div className="request-actions">
                  <button
                    className="btn reject"
                    onClick={() => handleReject(request.id)}
                  >
                    Reject
                  </button>
                  <button
                    className="btn approve"
                    onClick={() => handleApprove(request.id)}
                  >
                    Approve
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

// ExtensionContext.tsx - Context for managing extension state
import React, { createContext, useContext, useEffect, useReducer } from 'react';

type Action =
  | { type: 'ADD_REQUEST'; payload: TransactionRequest }
  | { type: 'REMOVE_REQUEST'; payload: string };

interface State {
  requests: TransactionRequest[];
}

const initialState: State = {
  requests: [],
};

const reducer = (state: State, action: Action): State => {
  switch (action.type) {
    case 'ADD_REQUEST':
      return { ...state, requests: [...state.requests, action.payload] };
    case 'REMOVE_REQUEST':
      return {
        ...state,
        requests: state.requests.filter((req) => req.id !== action.payload),
      };
    default:
      return state;
  }
};

interface ExtensionContextType {
  requests: TransactionRequest[];
  approveRequest: (requestId: string, tabId: number) => void;
  rejectRequest: (requestId: string, tabId: number) => void;
}

const ExtensionContext = createContext<ExtensionContextType | undefined>(
  undefined
);

export const ExtensionProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  const approveRequest = (requestId: string, tabId: number) => {
    chrome.runtime.sendMessage({
      type: 'APPROVE_REQUEST',
      requestId,
      tabId,
    });
    dispatch({ type: 'REMOVE_REQUEST', payload: requestId });
  };

  const rejectRequest = (requestId: string, tabId: number) => {
    chrome.runtime.sendMessage({
      type: 'REJECT_REQUEST',
      requestId,
      tabId,
    });
    dispatch({ type: 'REMOVE_REQUEST', payload: requestId });
  };

  useEffect(() => {
    const listener = (
      message: any,
      _sender: chrome.runtime.MessageSender,
      _sendResponse: (response?: any) => void
    ) => {
      if (message.type === 'NEW_REQUEST') {
        dispatch({
          type: 'ADD_REQUEST',
          payload: message.request,
        });
      }
    };

    chrome.runtime.onMessage.addListener(listener);
    return () => chrome.runtime.onMessage.removeListener(listener);
  }, []);

  return (
    <ExtensionContext.Provider
      value={{
        requests: state.requests,
        approveRequest,
        rejectRequest,
      }}
    >
      {children}
    </ExtensionContext.Provider>
  );
};

export const useExtension = () => {
  const context = useContext(ExtensionContext);
  if (context === undefined) {
    throw new Error('useExtension must be used within an ExtensionProvider');
  }
  return context;
};

// Background script - handles communication between content scripts and UI
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'SIGN_REQUEST') {
    const request: TransactionRequest = {
      id: Date.now().toString(),
      payload: message.payload,
      origin: new URL(sender.url || '').origin,
    };

    chrome.runtime.sendMessage({
      type: 'NEW_REQUEST',
      request,
    });
  }
});

// styles.css - Basic styling for the extension popup
.extension-popup {
  width: 360px;
  padding: 16px;
  font-family: 'Inter', sans-serif;
  color: #333;
}

.header {
  margin-bottom: 20px;
  text-align: center;
}

.header h1 {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
}

.content {
  max-height: 500px;
  overflow-y: auto;
}

.empty-state {
  text-align: center;
  padding: 20px;
  color: #666;
}

.requests-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.request-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 12px;
}

.request-header {
  margin-bottom: 12px;
}

.origin {
  font-weight: 500;
  color: #555;
}

.request-details {
  margin-bottom: 16px;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  font-size: 14px;
}

.address {
  font-family: monospace;
  word-break: break-all;
}

.request-actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}

.btn {
  padding: 6px 12px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  font-weight: 500;
}

.approve {
  background-color: #4CAF50;
  color: white;
}

.reject {
  background-color: #f44336;
  color: white;
}

// Entry point for the extension UI
const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(
    <React.StrictMode>
      <ExtensionProvider>
        <PopupApp />
      </ExtensionProvider>
    </React.StrictMode>
  );
}
```
