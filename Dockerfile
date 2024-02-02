# Définissez l'image de base
FROM python:3.11

# Définissez le répertoire de travail
WORKDIR /app

# Copiez le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt /app/

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste des fichiers dans le répertoire de travail
COPY main.py credentials.py /app/

# Commande par défaut pour exécuter votre application
CMD ["python", "main.py"]
