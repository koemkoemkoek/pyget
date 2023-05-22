import os
def printstartscreen():
    print ('----------------------------------------------------------')
    print (' 1. install a application')
    print (' 2. list all applications')
    print (' 3. update a application')
    print (' 4. uninstall a aplication')
    print (' 5. exit')
    print ('----------------------------------------------------------')
def upgrade():
    stream = (os.popen('winget upgrade'))
    upgrade = stream.read()
    print (upgrade)
    inputforupgrade = (input ('coppy and paste the one you want to upgrade '))
    if (' ') in inputforupgrade:
        upgradecmd = "winget upgrade '{}'".format(inputforupgrade)
    else:
        upgradecmd = "winget upgrade {}".format(inputforupgrade)
    stream = (os.popen(upgradecmd))
    upgrade = stream.read()
    print (upgrade)
def list():
    stream = (os.popen('winget list'))
    out = stream.read()
    print (out)
def install():
    print ('----------------------------------------------------------')
    print (' 1. install')
    print (' 2. search')
    print (' 3. exit')
    print ('----------------------------------------------------------')
    input_install_1 = (input (' '))
    if input_install_1 == '1':
         for number in range(999):
             input_install_2 = (input ('please enter what you would like to install '))
             if ' ' in input_install_2:
                 installcmd = ("winget install '{}'").format(input_install_2)
             else:
                 installcmd = ("winget install {}").format(input_install_2)
             stream = (os.popen(installcmd))
             outputok = stream.read()
             print (outputok)
             input_install_3 = (input ('retry? [Y/N]'))
             if input_install_3 == 'n' or 'N':
                 print ('ok')
                 break
    elif input_install_1 == '2':
        input_install_2 = (input ('search term: '))
        if ' ' in input_install_2:
            installcmd = "winget search '{}'".format(input_install_2)
        else:
            installcmd = "winget search {}".format(input_install_2)
        stream = (os.popen(installcmd))
        omething = (stream.read())
        print (omething)
def uninstall():
    print ('----------------------------------------------------------')
    print (' 1. list and uninstall')
    print (' 2. only uninstall')
    print (' 3. only list')
    print (' 4. exit')
    print ('----------------------------------------------------------')
    input_startscreen_deinstall = (input (' '))
    if input_startscreen_deinstall == '3':
     stream = (os.popen('winget list'))
     out = stream.read()
     print (out)
    elif input_startscreen_deinstall == '1':
     stream = (os.popen('winget list'))
     out = stream.read()
     print (out)
     inputfordeinstall = (input ('coppy and paste the one you want to uninstall: '))
     if " " in inputfordeinstall:
        deinstallcmd = ("winget uninstall '{}'").format(inputfordeinstall)
     else:
        deinstallcmd = ("winget uninstall {}").format(inputfordeinstall)
     YN = (input ('ARE YOU SURE? [Y/N]'))
     if YN == 'y' or 'Y':
         print ('uninstalling please wait...')
         stream = (os.popen(deinstallcmd))
         out = (stream.read)
    elif input_startscreen_deinstall == '2':
     inputfordeinstall = (input ('deinstall: '))
     if ' ' in inputfordeinstall:
         uninstallcmd = ("winget uninstall '{}'").format(inputfordeinstall)
     else:
         uninstallcmd = ("winget uninstall {}").format(inputfordeinstall)
     YN = (input ('[Y/N]'))
     if YN == "y" or 'Y':
         stream = (os.popen (uninstallcmd))
         out = (stream.read)
         print (out)
    if input_startscreen_deinstall == '4':
        print ('exit...')
while True:
    printstartscreen()
    select = (input (''))
    if select == '1':
     install()
    elif select == '2':
     list()
    elif select == '3':
     upgrade()
    elif select == '4':
     uninstall()
    elif select == '5':
        break
