def app(environ, start_response):
    status = '200 OK'
    data = ''
    for line in environ["QUERY_STRING"].split("&"):
        data = data+line+"\n"
    headers = [ ('Content-type', 'text/plain') ]
    body = 'Hello, world!'
    start_response(status, headers)
    return [data]
