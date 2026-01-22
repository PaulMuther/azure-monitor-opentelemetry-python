from endpoint import endpoint_app

if __name__ == '__main__':
    endpoint_app.run(host='localhost', port=5001, threaded=True, debug=True)
