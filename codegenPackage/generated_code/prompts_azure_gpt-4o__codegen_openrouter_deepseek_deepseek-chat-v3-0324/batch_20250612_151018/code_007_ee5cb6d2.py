"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Generate a GraphQL query and ReasonReact component to display articles like those listed on Joe Previte's site.
Generated: DETERMINISTIC_ee5cb6d22db0834c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```reason
module GetArticles = [%graphql
  {|
    query GetArticles {
      articles(orderBy: publishedAt_DESC) {
        id
        title
        slug
        excerpt
        publishedAt
      }
    }
  |}
];

module ArticlesQuery = ReasonApollo.CreateQuery(GetArticles);

[@react.component]
let make = () => {
  <ArticlesQuery>
    ...{({result}) =>
      switch (result) {
      | Loading => <div> {React.string("Loading...")} </div>
      | Error(error) =>
        <div> {React.string("Error: " ++ error##message)} </div>
      | Data(data) =>
        <div className="space-y-8">
          {data##articles
           ->Belt.Array.map(article =>
               <div key={article##id} className="border-b pb-8">
                 <h2 className="text-xl font-bold mb-2">
                   <a
                     href={"/articles/" ++ article##slug}
                     className="hover:underline">
                     {React.string(article##title)}
                   </a>
                 </h2>
                 <p className="text-gray-600 mb-2">
                   {React.string(article##excerpt)}
                 </p>
                 <time className="text-sm text-gray-500">
                   {React.string(article##publishedAt)}
                 </time>
               </div>
             )
           ->React.array}
        </div>
      }
    }
  </ArticlesQuery>;
};
```
