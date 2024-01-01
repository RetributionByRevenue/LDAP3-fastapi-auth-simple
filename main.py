from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from ldap3 import Server, Connection, ALL

def LDAP_AUTH(domain,username,password):
    didConnect=False
    try:
        # Define the server and connection settings
        server = Server(f"ldap://{domain}", get_info=ALL)
        conn = Connection(server, user=f"{username}@{domain}", password=password, auto_bind=True)
        # Attempt to bind (authenticate) the user
        conn.bind()
        # Check if the bind was successful
        if conn.result['result'] == 0:
            print("Authentication successful")
            didConnect = True
    except:
            print("Authentication failed")
    finally:
        # Don't forget to close the connection when you're done
        try:
            conn.unbind()
        except:
            ''
    return didConnect

app = FastAPI()

# Define the HTTPBasic authentication scheme
security = HTTPBasic()


# Dependency to check LDAP authentication
def check_ldap_auth(credentials: HTTPBasicCredentials = Depends(security)):
    domain = "mycompany.com"
    if not LDAP_AUTH(domain, credentials.username, credentials.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username


# Example protected route using the dependency
@app.get("/protected")
async def protected_route(username: str = Depends(check_ldap_auth)):
    return {"message": f"Hello, {username}! You have access to this protected route."}
