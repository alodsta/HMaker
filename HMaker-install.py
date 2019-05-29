import os
import commands

if not os.path.isdir('/Users/' + os.getlogin() + '/.HMaker'):
    os.mkdir('/Users/' + os.getlogin() + '/.HMaker')
open('/Users/' + os.getlogin() + '/.HMaker/HMaker', 'w').write('\n'.join(commands.getoutput('curl https://raw.githubusercontent.com/alodsta/HMaker/master/HMaker').split('\n')[3:]))
fa = open('/Users/' + os.getlogin() + '/.zshrc', 'a')
fr = open('/Users/' + os.getlogin() + '/.zshrc', 'r')
if not "alias HMaker='python ~/.HMaker/HMaker'" in fr.read():
    fa.write("alias HMaker='python ~/.HMaker/HMaker'")
os.system('zsh -c "source ~/.zshrc"')
