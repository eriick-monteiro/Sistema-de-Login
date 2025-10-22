# Nome do Projeto

## 🛠️ Tecnologias Utilizadas

### Front-end
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-yellow?style=for-the-badge&logo=python&logoColor=blue)


### Ferramentas
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-white?style=for-the-badge&logo=flask&logoColor=black)

---

## 🚀 Como rodar o projeto

### ✅ Pré-requisitos

### .env
Certifique-se de ter o arquivo `.env` com o seguinte conteúdo:

```js
SITE_NAME = "Site Teste"
DB_NAME = 'database'
TABLE_NAME = 'users'

SECRET_KEY = 'hashed_token'
// To generate:
// import secrets
// print(secrets.token_hex(32))
```


### Criação do Ambiente Virtual (venv)
```bash
$ python3 -m venv venv
```

### Ativando o Ambiente Virtual
```bash
# Linux / macOS
$ source venv/bin/activate

# Windows
$ .\venv\Scripts\activate
```

### 📦 Instalar dependências

```bash
pip install -r requirements.txt
```

### 📥 Clonar o repositório
```bash
git clone https://github.com/eriick-monteiro/Sistema-de-Login.git
cd Sistema-de-Login
```

### ▶️ Rodar em ambiente de desenvolvimento

```bash
python3 app.py
```

Por padrão o Flask vai rodar em:
👉 http://localhost:5000



### 📸 Preview

