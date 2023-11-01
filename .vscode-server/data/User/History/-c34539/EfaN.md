### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is a dynamically typed, multi-purpose programming language known for its readability and extensive standard library, while JavaScript is also dynamically typed but primarily used for web development in browsers, with a focus on asynchronous programming and a different syntax structure.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
You can use the 'get' method, or the 'try...except' block.

- What is a unit test?
A unit test is a type of software testing in which individual components or units of a software application are tested in isolation to ensure that they work as intended.

- What is an integration test?
An integration test is a type of software testing that focuses on verifying the interactions and interoperability between multiple components, modules, or services within a software system.

- What is the role of web application framework, like Flask?
A web application framework, such as Flask, serves as a foundational structure for web development, providing tools and conventions for routing, request handling, response generation, and more. It simplifies the process of building web applications by offering a set of pre-defined patterns and components, helping developers create reliable, maintainable, and feature-rich web applications efficiently.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  I would choose to pass information as a parameter in a route URL (e.g., '/foods/pretzel') when the data in the URL is a fundamental part of the resource being requested and when clean, user-friendly URLs are important. I would opt for URL query parameters (e.g., 'foods?type=pretzel') when the data is optional, filters or modifies results, or when flexibility for customization without altering the core route structure is needed.

- How do you collect data from a URL placeholder parameter using Flask?

- How do you collect data from the query string using Flask?

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?

- What is the session object in Flask?

- What does Flask's `jsonify()` do?
