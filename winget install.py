import os
print ('----------------------------------------------------------')
print (' 1. install')
print (' 2. search')
print ('----------------------------------------------------------')
input_install_1 = (input (' '))
if input_install_1 == '1':
    for number in range(9991):
        input_install_2 = (input ('please enter what you would like to install '))
        if ' ' in input_install_2:
            installcmd = ("winget install '{}'").format(input_install_2)
        else:
            installcmd = ("winget install {}").format(input_install_2)
        stream = (os.popen(installcmd))
        output = stream.read()
        print (output)
        input_install_3 = (input ('retry? [Y/N]'))
        if input_install_3 == 'n':
            print ('ok')
            break
elif input_install_1 == '2':
    input_install_2 = (input ('search term: '))
    if ' ' in input_install_2:
        installcmd = "winget serch '{}'".format(input_install_2)
    else:
        installcmd = "winget search {}".format(input_install_2)
    stream = (os.popen(installcmd))
    output = stream.read()
    print (output)