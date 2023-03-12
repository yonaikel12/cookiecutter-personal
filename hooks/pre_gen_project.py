print("hello world")


import subprocess
#subproceso para instalar las librerias de requirements.txt
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import os
import sys

#si el nombre de project slug comienza por x arroja el mensaje
project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template.{RESET_ALL}")

    sys.exit(1)

print(f"{MESSAGE_COLOR}Lets do it! Youre are going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")
