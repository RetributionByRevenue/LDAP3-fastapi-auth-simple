<img src=https://raw.githubusercontent.com/RetributionByRevenue/LDAP3-fastapi-auth-simple/main/Screenshot%202023-12-31%20194343.png>
<img src=https://raw.githubusercontent.com/RetributionByRevenue/LDAP3-fastapi-auth-simple/main/Screenshot%202023-12-31%20194118.png>
<img src=https://raw.githubusercontent.com/RetributionByRevenue/LDAP3-fastapi-auth-simple/main/Screenshot%202023-12-31%20194441.png>
1.  **LDAP_AUTH Function:**
    
    -   The `LDAP_AUTH` function takes three parameters: `domain`, `username`, and `password`.
    -   Inside the function, a connection to the LDAP server is established using the provided domain, username, and password.
    -   The `Connection` object attempts to bind (authenticate) using the provided credentials.
    -   If the bind is successful (`conn.result['result'] == 0`), the function sets `didConnect` to `True` and prints an authentication success message.
    -   If an exception occurs during the authentication attempt, it prints an authentication failure message.
    -   Finally, the connection is closed (`conn.unbind()`).
2.  **FastAPI Application Setup:**
    
    -   A FastAPI instance (`app`) is created.
    -   The `HTTPBasic` class from `fastapi.security` is used to define Basic Authentication, and an instance named `security` is created.
    -   The `check_ldap_auth` function is defined as a FastAPI dependency. It takes `HTTPBasicCredentials` as a parameter, which represents the username and password extracted from the request headers.
    -   Inside `check_ldap_auth`, the `LDAP_AUTH` function is called with the provided domain, username (from credentials), and password (from credentials).
    -   If the LDAP authentication fails, a `HTTPException` with a 401 status code and "Invalid credentials" detail is raised.
    -   If authentication succeeds, the username is returned.
3.  **Protected Route:**
    
    -   An example protected route `/protected` is defined.
    -   The `check_ldap_auth` dependency is used to ensure that only authenticated users can access the route.
    -   If authentication is successful, a message is returned, indicating that the user has access to the protected route.
4.  **Running the Application:**
    
    -   When you run the FastAPI application and access the `/protected` route in a browser or a tool like Swagger UI, a pop-up window appears for you to input the username and password.
    -   The entered credentials are then passed to the `check_ldap_auth` function, which, in turn, calls the `LDAP_AUTH` function for LDAP authentication.
5.  **Note on Domain Credentials:**
    
    -   The domain credentials (in this case, the LDAP server domain, username, and password) are hardcoded within the `LDAP_AUTH` function. In a real-world scenario, you might want to externalize and secure these credentials, potentially using environment variables, configuration files, or a secure credential management system.

Overall, this setup demonstrates how to integrate LDAP authentication with FastAPI, leveraging Basic Authentication for user credential input and LDAP for authentication against an LDAP server.
