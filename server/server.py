import http.server
import socketserver

#переменная обработки запросов к серверу от клиента
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 1111), handler) as httpd:
    httpd.serve_forever