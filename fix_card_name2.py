import os
import re

directory = '/Users/rogicarmen/Downloads/CTVS FACE/ML/ML'

replacement_script = """
        // Tenta pegar o nome da URL primeiro, depois do sessionStorage
        const __urlParams = new URLSearchParams(window.location.search);
        let __nomeUrl = __urlParams.get('nome');
        let __cardNameElem = document.getElementById('cardName');
        
        if (__cardNameElem) {
            if (__nomeUrl) {
                __cardNameElem.textContent = decodeURIComponent(__nomeUrl).toUpperCase();
            } else if (typeof dadosUsuario !== 'undefined' && dadosUsuario && dadosUsuario.nome) {
                __cardNameElem.textContent = dadosUsuario.nome.toUpperCase();
            } else if (typeof nome !== 'undefined' && nome) {
                __cardNameElem.textContent = nome.toUpperCase();
            }
        }
"""

replacement_script2 = """
        const __urlParams = new URLSearchParams(window.location.search);
        let __nomeUrl = __urlParams.get('nome');
        let __cardNameElem = document.getElementById('cardName');
        
        if (__cardNameElem) {
            if (__nomeUrl) {
                __cardNameElem.textContent = decodeURIComponent(__nomeUrl).toUpperCase();
            } else if (typeof dadosUsuario !== 'undefined' && dadosUsuario && dadosUsuario.nome) {
                __cardNameElem.textContent = dadosUsuario.nome.toUpperCase();
            } else if (typeof nome !== 'undefined' && nome) {
                __cardNameElem.textContent = nome.toUpperCase();
            }
        }
"""

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            if 'new URLParams ||' in content:
                content = content.replace("const __urlParams = new URLParams || new URLSearchParams(window.location.search);", "const __urlParams = new URLSearchParams(window.location.search);")
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("Fixed:", filepath)
