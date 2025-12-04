import http.server
import socketserver
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
ip = s.getsockname()[0]
s.close()

with socketserver.TCPServer(("", 0), http.server.SimpleHTTPRequestHandler) as httpd:
    p = httpd.server_address[1]
    print(f"http://127.0.0.1:{p}")
    print(f"http://localhost:{p}")
    print(f"http://{ip}:{p}")
    httpd.serve_forever()