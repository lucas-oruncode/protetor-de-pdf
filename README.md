# 📚 Protetor de PDF

Bem-vindo ao **Protetor de PDF**, um microsaas que permite a proteção de PDFs vendidos online. Este sistema personaliza cada PDF inserindo o CPF do cliente comprador em todas as páginas do documento, reduzindo o risco de redistribuição ilegal e protegendo o conteúdo digital.

---

## Funcionalidades

- **Proteção personalizada**: Adiciona o CPF do cliente em todas as páginas do PDF.
- **Interface intuitiva**: Plataforma web simples e fácil de usar.
- **Aplicações diversas**: Compatível com livros, apostilas, artbooks, e outros conteúdos digitais.

---

## Tecnologias Utilizadas

- **Backend**: [Flask](https://flask.palletsprojects.com/) - Framework web para Python.
- **Frontend**: HTML e CSS para a interface do usuário.

## Como Executar o Projeto

### Acesse direto na web: 
 - https://protetor-de-pdf-gjqw.onrender.com


### OU Localmente:

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/lucas-oruncode/protetor-de-pdf.git
   [ Abra o projeto no diretório onde você clonou ]
   ```

2. **Crie um ambiente virtual** (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor Flask**:
   ```bash
   flask run
   ```

5. **Acesse a aplicação**:
   Abra seu navegador e vá para `http://127.0.0.1:5000`.

## Estrutura do Projeto

- `app.py`: Arquivo principal do Flask que contém as rotas e lógica do backend.
- `templates/`: Contém os arquivos HTML para o frontend.
- `static/`: Contém os arquivos CSS.
- `uploads/`: Pasta onde os arquivos PDF enviados são temporariamente armazenados.

## Melhorias Futuras

- Opções adicionais de fontes e tamanhos de texto.
- Envio automático de email, com PDF modificado.


## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).
