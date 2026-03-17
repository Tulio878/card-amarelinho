import os
import re

for root, dirs, files in os.walk('/Users/rogicarmen/Downloads/CTVS FACE/ML/ML'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            if 'id="cardName"' in content:
                # Add logic to check URL parameters for 'nome' as a fallback, or update the existing one
                # First let's find the script where cardName is set.
                if "document.getElementById('cardName').textContent" in content:
                    # Let's see if we can ensure `nome` is fetched from URL if not in session storage
                    replacement = """
        const urlParamsParaNome = new URLSearchParams(window.location.search);
        const nomeDaUrl = urlParamsParaNome.get('nome');
        
        let nomeParaCard = 'NOME DO TITULAR';
        if (nomeDaUrl) {
            nomeParaCard = decodeURIComponent(nomeDaUrl).toUpperCase();
        } else if (typeof dadosUsuario !== 'undefined' && dadosUsuario && dadosUsuario.nome) {
            nomeParaCard = dadosUsuario.nome.toUpperCase();
        }

        const cardNameElement = document.getElementById('cardName');
        if (cardNameElement) {
            cardNameElement.textContent = nomeParaCard;
        }
"""
                    # we will just inject this before the end of the script tag, or replace the existing setter.
                    # It's better to manually replace the existing setter logic.
