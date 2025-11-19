"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Write a GraphQL query and ReasonReact component to fetch and display user data, following the approach described in Joe Previte's tutorial on integrating GraphQL with ReasonReact.
Generated: DETERMINISTIC_a327a43c004523c8
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```reason
// Import necessary modules from ReasonReact and GraphQL
open ReasonReact;
open Graphql;

type user = {
  id: string,
  name: string,
  email: string,
};

// Define the GraphQL query to fetch user data
let userQuery = 
  {|
    query {
      users {
        id
        name
        email
      }
    }
  |};

// Define a ReasonReact component to fetch and display user data
[@react.component]
let make = () => {
  // State to hold user data and loading status
  let (users, setUsers) = React.useState(() => None);
  let (loading, setLoading) = React.useState(() => true);
  let (error, setError) = React.useState(() => None);

  // Fetch user data when the component mounts
  React.useEffect1(() => {
    // Function to fetch data
    let fetchData = async () => {
      try {
        // Make the GraphQL request
        let response = await Graphql.request(userQuery);
        // Update state with the fetched user data
        switch response {
        | Ok(data) => 
          setUsers(Some(data.users));
          setLoading(false);
        | Error(err) => 
          setError(Some(err));
          setLoading(false);
        };
      } catch (err) {
        // Handle any unexpected errors
        setError(Some(err));
        setLoading(false);
      };
    };

    fetchData();
    // Cleanup function (if needed)
    None;
  }, [||]);

  // Render loading state, error state, or user data
  switch (loading, error, users) {
  | (true, _, _) => <div>Loading...</div>
  | (_, Some(err), _) => <div>Error: {err}</div>
  | (_, None, Some(users)) => {
      <div>
        <h1>User List</h1>
        <ul>
          {users
            |> List.map(user => 
              <li key={user.id}>
                {user.name} - {user.email}
              </li>
            )}
        </ul>
      </div>
    }
  | _ => <div>No users found.</div>
  };
};
```
