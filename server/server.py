import http.server
import socketserver

#переменная обработки запросов к серверу от клиента
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', 4040), handler) as httpd:
    httpd.serve_forever