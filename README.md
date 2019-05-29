# HMaker
It's usefull script for quick make C-header with all functions, structurse, defines e.t.c. from all .c and .h fielse in directory which u chose.
## Installing
**For instal copy in term:**  
`curl https://raw.githubusercontent.com/alodsta/HMaker/master/HMaker-install.py | python` 
Very simple. This script make directory `~/.HMaker`, put in HMaker and write alias in you'r .zshrc
## Updating
`HMaker --update`
## How use?
`HMaker "path/to/directory/with_srcs" "path/to/directory/where/you_want_put_your.h"`  
If u want, u can change alias in `.zshrc`.
If you skipping one or both arguments, HMaker will thinks that they `.`.
If you'll specify both arguments as directories, then HMaker will names your header file seems like directory with srcs and put header in directory what you wrote second. It means that `HMaker` == `HMaker .` == `HMaker . .`  
`HMaker -s [path, name.h]` -- write header without c-files names in comment.
