print("bye world")

#incializar un repositorio de git automaticamente
# aqui no es necesario importar os

import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git','init']) #inicializa el repositorio
subprocess.call(['git','add', '*']) #agrega todos los archivos que se encuentren
subprocess.call(['git','commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! CReate and have fun!{RESET_ALL}")
