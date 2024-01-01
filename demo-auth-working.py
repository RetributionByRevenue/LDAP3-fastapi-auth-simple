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
        
domain = "mycompany.com" #or just use domain controller ipaddress
username = "mruffolo"    #my domain username
password = "!!!aaaaPassword"
test=LDAP_AUTH(domain, username, password)
print(test)