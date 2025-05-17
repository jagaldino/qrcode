# 🧾 Gerador de QR Codes em Python

Este projeto foi criado com o objetivo de **ajudar meu pai** em uma tarefa que exigia a **geração de vários QR Codes de forma prática e rápida**, com opções de personalização e salvamento automático dos arquivos.

---

## 📌 Funcionalidades

- ✅ Entrada de dados em lista (nome + link)
- ✅ Geração de QR Codes personalizados (tamanho e cores)
- ✅ Salvamento automático em uma pasta `qrcodes/`
- ✅ Nomeação automática dos arquivos (`nome_do_qrcode.png`)
- ✅ Barra de progresso com status
- ✅ Tratamento de erros (URLs inválidas, problemas com pastas, etc.)

---

## 🧑‍💻 Como usar

### 1. Instale as dependências

```bash
pip install qrcode[pil] tqdm
```

> ⚠️ No Windows, execute o terminal como **administrador** para evitar erros de permissão.

### 2. Configure a lista de dados

No arquivo `gerador_qrcodes.py`, edite a variável `dados_qrcodes` com os nomes e links desejados:

```python
dados_qrcodes = [
    {"nome": "empresa_site", "link": "https://www.exemplo.com"},
    {"nome": "contato_whatsapp", "link": "https://wa.me/5599999999999"}
]
```

### 3. Execute o script

```bash
python gerador_qrcodes.py
```

Os QR Codes serão gerados automaticamente na pasta `qrcodes/`.

---

## 🎨 Personalização

Você pode alterar no código:

- 📏 Tamanho (ex: `200x200`, `300x300`)
- 🎨 Cores (cor de fundo e cor do QR)
- ✍️ Nomes dos arquivos
- 📂 Pasta de saída

---

## 🛠 Exemplo de uso

Imagine que você precisa imprimir etiquetas com QR Codes que redirecionem para sites diferentes: um para o site da empresa, outro para o WhatsApp comercial, etc. Basta colocar os links na lista, rodar o script e pronto!

---

## 🤝 Agradecimento

Esse projeto foi feito com carinho para ajudar meu pai em uma demanda específica, mas pode ser útil para qualquer pessoa ou empresa que precise gerar vários QR Codes rapidamente com controle total sobre o resultado final.

---

## 📄 Licença

Este projeto é livre para uso pessoal ou comercial. Créditos são sempre bem-vindos! 😉

```

```
