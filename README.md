# python-for-devops

# Health Calculator API

## 🌍 Déploiement sur Azure
L'application est déployée via une **pipeline CI/CD GitHub Actions** sur **Azure App Service** et est accessible à l'URL suivante :

🔗 **[Health Calculator API](https://health-calculator-app-msi2doa-cprigent1-exb7feakamgjf3d3.francecentral-01.azurewebsites.net/)**

---

## 🧪 Tester l'API

### 🔹 **1. Tester avec `curl`**
#### **Calcul de l'IMC (BMI)**
```sh
curl -X POST -H "Content-Type: application/json" -d '{"height": 1.75, "weight": 70}' https://health-calculator-app-msi2doa-cprigent1-exb7feakamgjf3d3.francecentral-01.azurewebsites.net/bmi
```

#### **Calcul du BMR**
```sh
curl -X POST -H "Content-Type: application/json" -d '{"height": 175, "weight": 70, "age": 25, "gender": "male"}' https://health-calculator-app-msi2doa-cprigent1-exb7feakamgjf3d3.francecentral-01.azurewebsites.net/bmr
```

### 🔹 **2. Tester avec Postman**
- Ouvrez **Postman**.
- Créez une **requête POST**.
- **Ajoutez l'URL** (`/bmi` ou `/bmr`).
- **Body** en JSON :
  ```json
  {
      "height": 1.75,
      "weight": 70
  }
  ```
- Cliquez sur **"Send"** pour voir la réponse.

### 🔹 **3. Tester avec un navigateur**
Allez sur :
```
https://health-calculator-app-msi2doa-cprigent1-exb7feakamgjf3d3.francecentral-01.azurewebsites.net/
```
Si l'application tourne correctement, vous devriez voir un message d'accueil.

---

## 🛠️ Builder l'application en local

### 🔹 **1. Cloner le dépôt**
```sh
 git clone https://github.com/<votre-repo>/health-calculator.git
 cd health-calculator
```

### 🔹 **2. Installer l'environnement Python**
Assurez-vous d'avoir Python 3.9 ou supérieur :
```sh
python -m venv my_venv
source my_venv/bin/activate  # (Windows: my_venv\Scripts\activate)
pip install -r requirements.txt
```

### 🔹 **3. Lancer l'API en local**
```sh
make run
```
L'API sera disponible sur `http://127.0.0.1:5000/`

### 🔹 **4. Exécuter les tests unitaires**
```sh
make test
```

---

## 🐳 Exécution avec Docker

### 🔹 **1. Construire et exécuter le conteneur**
```sh
make build
make run-docker
```
L'API sera accessible via `http://localhost:5000/`

### 🔹 **2. Pousser l'image sur GitHub Container Registry (GHCR)**
```sh
docker tag health-calculator ghcr.io/<votre-utilisateur>/health-calculator:latest
docker push ghcr.io/<votre-utilisateur>/health-calculator:latest
```

---

## 🚀 Déploiement sur Azure

### 🔹 **1. Configurer Azure App Service**
1. Créez une **Web App** sur Azure avec Docker.
2. Configurez l'image comme : `ghcr.io/<votre-utilisateur>/health-calculator:latest`
3. Ajoutez un secret `GHCR_PAT` à GitHub pour l'authentification.

### 🔹 **2. Déclencher le déploiement via GitHub Actions**
Poussez les modifications sur `main` pour exécuter la CI/CD automatiquement :
```sh
git add .
git commit -m "Déploiement sur Azure"
git push origin main
```

Une fois le déploiement terminé, l'API sera accessible à :
```
https://<votre-app>.azurewebsites.net/
```

---
