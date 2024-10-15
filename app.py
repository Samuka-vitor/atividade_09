# Usamos platform.system() e platform.release() diretamente para obter o nome e a versão do sistema operacional.

import os
import platform
import subprocess

# Obter o nome do sistema operacional
so = platform.system()
versao = platform.release()
print(f"Sistema Operacional: {so} {versao}")


# Para Windows, usamos o comando wmic product get name com subprocess.check_output para listar os programas instalados.

# Listar programas instalados (Windows)
if so == "Windows":
    comando = 'wmic product get name'
    programas = subprocess.check_output(comando, shell=True, text=True)
    print("Programas instalados:")
    print(programas)
else:
    print("Função de listagem de programas não implementada para este sistema operacional.")

