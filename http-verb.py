#Author Vanshit Malhotra

import requests

verbs = ['GET', 'POST', 'TRACE', 'OPTIONS', 'HEAD', 'PUT', 'DELETE', 'PATCH', 'CONNECT', 'ARBTRY']

webapp = raw_input('Enter the URI to be Tested : ')
print("\n The URI entered by you is : " + webapp )
print
print raw_input("Press any key to continue ..... ")
print "   **********//////////??????//////**************"
print
print "  Testing HTTP Verbs For URI : " + webapp
print('''
                   .-"      "-.
                  /            \
                 |              |
                 |,  .-.  .-.  ,|
                 | )(__/  \__)( |
                 |/     /\     \|
       (@_       (_     ^^     _)
  _     ) \_______\__|IIIIII|__/__________________________
 (_)@8@8{}<________|-\IIIIII/-|___________________________>
        )_/        \          /
       (@           `--------`  Author : Vanshit Malhotra
''')
print "   **********//////////??????//////**************"
print
print "HTTP VERB & STATUS CODE"
for verb in verbs:
        req = requests.request(verb, webapp)
        print verb, req.status_code, req.reason

print
print "HTTP HEADERS for " + webapp + " are :"
print
print req.headers

