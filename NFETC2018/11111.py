import os

installed_module_list = os.popen("pip freeze")

# print(installed_module_list)
with open("requirements.txt",'w') as f:
    for m in installed_module_list.read():
        f.write(m)