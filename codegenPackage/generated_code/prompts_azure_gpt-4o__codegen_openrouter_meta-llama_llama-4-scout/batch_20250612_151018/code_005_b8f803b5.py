"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Write a GraphQL query and ReasonReact code snippet to display a list of articles, similar to the "Latest Articles" section on Joe Previte's website.
Generated: DETERMINISTIC_b8f803b5eed00113
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### GraphQL Query

```graphql
query LatestArticles {
  articles(orderBy: { field: createdAt, direction: DESC }, first: 5) {
    edges {
      node {
        id
        title
        slug
        excerpt
        createdAt
      }
    }
  }
}
```

### ReasonReact Code Snippet

```reason
// Article.re
[@derive(reactComponent)]
let make = (~article) => {
  <div className="article">
    <h2> {article.title} </h2>
    <p> {article.excerpt} </p>
    <p>
      {"Read more" |> Js.String2.camelCase}
      <a href={"/articles/" ++ article.slug}> →</a>
    </p>
  </div>
};

// LatestArticles.re
[@derive(reactComponent)]
let make = () => {
  let articles = ref([]);

  GraphQL.queries.LatestArticles.use()
  |> React.useEffect(() => {
    switch ($0) {
    | Some(data) => articles := data.articles.edges |> List.map(~f=.node)
    | None => ()
    };
  });

  <div className="latest-articles">
    <h2> Latest Articles </h2>
    <ul>
      {articles |> List.map((article) => {
        <li key={article.id}>
          <Article article />
        </li>
      })}
    </ul>
  </div>
};
```

### Error Handling with GraphQL Query

```reason
// LatestArticles.re (with error handling)
[@derive(reactComponent)]
let make = () => {
  let articles = ref([]);
  let error = ref(None);

  GraphQL.queries.LatestArticles.use()
  |> React.useEffect(() => {
    switch ($0) {
    | Some(data) => articles := data.articles.edges |> List.map(~f=.node)
    | None =>
        error := Some("Failed to fetch articles. Please try again later.")
    };
  });

  <div className="latest-articles">
    <h2> Latest Articles </h2>
    {error |> Option.map((err) => {
      <p style="color: red;"> {err} </p>
    })}
    <ul>
      {articles |> List.map((article) => {
        <li key={article.id}>
          <Article article />
        </li>
      })}
    </ul>
  </div>
};
```

### bs-graphql-ppx Configuration

```json
// bsconfig.json
{
  "graphql": {
    "queries": {
      "LatestArticles": "./queries/LatestArticles.graphql"
    }
  }
}
```
