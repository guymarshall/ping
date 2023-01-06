import webbrowser

# add ip address loops to this list and check for 500 or 404 to stop resources quickly being used up
urls = ['http://www.example.com', 'http://www.example2.com', 'http://www.example3.com']

for url in urls:
    webbrowser.open_new_tab(url)
