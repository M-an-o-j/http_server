from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the directory from which files will be served
FILE_DIRECTORY = "./"
IP_ADDRESS = "192.168.43.9"

# Define the HTTP request handler class
class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    # Override the do_GET method to handle GET requests
    def do_GET(self):
        # Set the directory to serve files from
        self.directory = FILE_DIRECTORY

        # Call the parent class method to handle the request
        return SimpleHTTPRequestHandler.do_GET(self)

# Create an HTTP server with the defined request handler
def run_server():
    server_address = (IP_ADDRESS, 8080)  # Use port 8080
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    print(f"Server is running on ip {IP_ADDRESS}:8080...")
    httpd.serve_forever()

if __name__ == '__main__':
    # Start the HTTP server and watch for file changes
    run_server()
