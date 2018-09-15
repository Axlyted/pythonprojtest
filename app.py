from wsgiref.simple_server import make_server

HOST = 'localhost'
PORT = 8080

def on_http_request(environment, set_response_head):
	set_response_head('200 OK', [ ('Content-Type', 'text/plain') ])
	return [ 'hello'.encode('utf-8') ]

with make_server(HOST, PORT, on_http_request) as httpd:
	print('listening on port ' + str(PORT))
	httpd.serve_forever()