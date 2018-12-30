import webbrowser, sys, pyperclip

sys.argv #['maipt.py', 'asaas', 'saaasa', 'saas']

#check if command line arguments were passed
if len(sys.argv)>1:
    #['maipt.py', 'asaas', 'saaasa', 'saas'] -> 'asaas saaasa saas'
    address=' '.join(sys.argv[1:])
else:
    address=pyperclip.paste()

url='https://www.google.co.in/maps/place/'
webbrowser.open(url+address)
