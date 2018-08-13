def app(environ, start_response):
    data = b"{\"artifact\": \"sample_app\"}\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
