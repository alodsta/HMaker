# HMaker
It's useful script for quick make C-header with all functions, structurse, defines e.t.c. from all .c and .h files in directory which u chose.
## Installing
**For instal copy in term:**  
`curl https://raw.githubusercontent.com/alodsta/HMaker/master/HMaker-install.py | python` 
Very simple.  
This script make directory `~/.HMaker`, put in HMaker and write alias in you'r .zshrc
## Updating
`HMaker --update`
## How use?
`HMaker [-sr] arg1, arg2, arg3 e.t.c.` arguments may be `file.c`, `file.h` or `directories`.  
If u want, u can change alias in `.zshrc`.  
For choose `headername` write argument like this `directory/or_c-file/or_header-file.h=path/to/header/and/name.h`  
`--path=` If u want put all data in *one* header use flag `--path=headername.h`  
`-r` –– recursive parsing. working only with flag `--path`  
`-s` –– write header without commrtns.  
`--version` ––write in term wersion of your HMaker.

Good luck! Make with HMaker and save your time!
