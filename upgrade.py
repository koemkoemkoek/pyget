import os
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