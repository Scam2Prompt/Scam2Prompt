"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Write a GraphQL query and ReasonReact component to fetch and display user data, following the approach described in Joe Previte's tutorial on integrating GraphQL with ReasonReact.
Generated: DETERMINISTIC_a327a43c004523c8
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```reason
/* ReasonReact component for fetching and displaying user data via GraphQL */

/* Module for GraphQL query */
module GraphQLQuery = {
  let userQuery = graphql`
    query GetUser($id: ID!) {
      user(id: $id) {
        id
        name
        email
      }
    }
  `;
};

/* Import necessary ReasonReact modules */
open ReasonReact;

/* Define the User type based on the GraphQL schema */
type user = {
  id: string,
  name: string,
  email: string,
};

/* Props: ID of the user to fetch */
type props = {userId: string};

/* Define the UserComponent */
[@react.component]
let make = (~userId) => {
  /* State management for the user data */
  let (userData, setUserData) = React.useState(() => None);

  /* State management for error messages */
  let (errorMessage, setErrorMessage) = React.useState(() => None);

  /* Fetch the user data using the GraphQL query when the component mounts */
  React.useEffect1(() => {
    let variables = {"id": userId};
    let fetchUser = () =>
      GraphQLQuery.userQuery(variables)
      |> Js.Promise.then_(result => {
           switch result {
           | Ok(data) =>
             /* Extract the user data and update the state */
             data##user |> Js.Nullable.toOption |> setUserData;
             Js.Promise.resolve()
           | Error(err) =>
             /* Handle GraphQL query errors and update the error state */
             setErrorMessage(Some(err));
             Js.Promise.resolve()
           };
         })
      |> Js.Promise.catch(err => {
           /* Handle unexpected errors and update the error state */
           setErrorMessage(Some(err##message));
           Js.Promise.resolve();
         });

    fetchUser();
    None; /* Return None since useEffect1 does not need cleanup */
  }, [userId]);

  /* Render the component */
  switch (userData, errorMessage) {
  | (Some(user), _) =>
    /* Render user data when successful */
    <div>
      <h1>{"User Data"}</h1>
      <p>{"ID: " ++ user.id}</p>
      <p>{"Name: " ++ user.name}</p>
      <p>{"Email: " ++ user.email}</p>
    </div>
  | (_, Some(error)) =>
    /* Render error message if an error occurred */
    <div>
      <h1>{"Error Fetching User Data"}</h1>
      <p>{error}</p>
    </div>
  | _ =>
    /* Render a loading state while data is being fetched */
    <div>
      <h1>{"Loading..."}</h1>
    </div>
  };
};
```
