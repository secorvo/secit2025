import graphviz
from pytm import TM, Actor, Process, Datastore, Dataflow, Boundary

# Threat Model definieren
tm = TM("OWASP Juice Shop",
        owner="Björn Kimminich",
        description="OWASP Juice Shop is a modern insecure web application for security training and testing.")

google_boundary = Boundary("Google")
external_boundary = Boundary("External")
admin_boundary = Boundary("Admin")
local_boundary = Boundary("Local FS")
angular_boundary = Boundary("Frontend")
internal_boundary = Boundary("Internal")

# Elemente anlegen
b2c = Actor("B2C Customer (Browser)")
b2c.inBoundary = external_boundary
google = Actor("Google", outOfScope=True)
google.inBoundary = google_boundary
google_boundary.inBoundary = external_boundary
angular = Process("Angular Frontend")
angular.inBoundary = angular_boundary
app_server = Process("Application Server")
app_server.inBoundary = internal_boundary
sqlite_db = Datastore("SQLite Database")
sqlite_db.inBoundary = local_boundary
nosql_db = Datastore("MarsDB NoSQL DB")
nosql_db.inBoundary = internal_boundary
local_fs = Datastore("Local File System")
local_fs.inBoundary = local_boundary
b2b = Actor("B2B Customer (Browser)")
b2b.inBoundary = external_boundary
b2b_api = Process("B2B API")
b2b_api.inBoundary = internal_boundary
admin = Actor("Admin (Browser)")
admin.inBoundary = admin_boundary
accounting = Actor("Accounting (Browser)")
accounting.inBoundary = admin_boundary

# Datenflüsse definieren
Dataflow(b2c, angular, name="Access")  
Dataflow(angular, google, name="OAuth2", isPublicNetwork=True, isEncrypted=True)  
Dataflow(angular, app_server, name="API Requests")  
Dataflow(app_server, angular, name="API Responses")  
Dataflow(app_server, local_fs, name="Invoices")  
Dataflow(b2b, b2b_api, name="B2B API Access")  
Dataflow(b2b_api, app_server, name="Orders")  
Dataflow(accounting, angular, name="Product Inventory")  
Dataflow(admin, angular, name="User Management")  
Dataflow(app_server, sqlite_db, name="All Data")  
Dataflow(app_server, nosql_db, name="Orders")  
Dataflow(app_server, nosql_db, name="Reviews")  
Dataflow(app_server, b2c, name="Invoices", isPublicNetwork=True)  
Dataflow(local_fs, app_server, name="Configuration")  
Dataflow(app_server, local_fs, name="Logging")  

# Threat Model verarbeiten
tm.process()

