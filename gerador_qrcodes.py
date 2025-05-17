import os
import json
import qrcode
from qrcode.image.pil import PilImage
from tqdm import tqdm

# ==========================
# CONFIGURAÇÕES DO USUÁRIO
# ==========================

# Lista de entrada: você pode modificar ou carregar via input ou JSON
dados_qrcodes = [
    {"nome": "google", "link": "https://www.google.com"},
    {"nome": "openai", "link": "https://www.openai.com"},
]

# Tamanho do QR Code (pixels)
tamanho_pixels = 100

# Cores personalizáveis
cor_frente = "black"   # ex: 'black', 'blue', '#123456'
cor_fundo = "white"    # ex: 'white', 'yellow', '#ffcc00'

# ==========================
# FUNÇÕES AUXILIARES
# ==========================

def criar_pasta(pasta):
    try:
        os.makedirs(pasta, exist_ok=True)
    except Exception as e:
        print(f"Erro ao criar a pasta '{pasta}': {e}")
        exit(1)

def validar_url(url):
    return url.startswith("http://") or url.startswith("https://")

def gerar_qrcode(nome, url, tamanho, cor_fg, cor_bg, destino):
    try:
        if not validar_url(url):
            raise ValueError("URL inválida")

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img: PilImage = qr.make_image(fill_color=cor_fg, back_color=cor_bg)
        img = img.resize((tamanho, tamanho))
        img.save(os.path.join(destino, f"{nome}.png"))
    except Exception as e:
        print(f"Erro ao gerar QR Code '{nome}': {e}")

# ==========================
# EXECUÇÃO PRINCIPAL
# ==========================

def main():
    pasta_saida = "qrcodes"
    criar_pasta(pasta_saida)

    print(f"\n📦 Gerando QR Codes para {len(dados_qrcodes)} itens...\n")
    for item in tqdm(dados_qrcodes, desc="Progresso", unit="QR"):
        nome = item.get("nome")
        url = item.get("link")
        if nome and url:
            gerar_qrcode(nome, url, tamanho_pixels, cor_frente, cor_fundo, pasta_saida)
        else:
            print(f"Entrada inválida: {item}")

    print(f"\n✅ Todos os QR Codes foram salvos em: '{pasta_saida}/'")

if __name__ == "__main__":
    main()
