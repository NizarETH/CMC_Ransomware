# CMC Ransomware

## Description
Ce projet est un **ransomware** en Python conçu pour démontrer comment les ransomwares fonctionnent. Il chiffre tous les fichiers d'un dossier et empêche leur suppression ou modification jusqu'à ce qu'ils soient déchiffrés avec une clé spécifique.

⚠ **Ce projet est uniquement à des fins pédagogiques. Il ne doit pas être utilisé à des fins malveillantes.**

## Fonctionnalités
- Génération et stockage d'une clé de chiffrement (`key.key`)
- Chiffrement des fichiers d'un dossier avec la bibliothèque `cryptography.fernet`
- Protection des fichiers contre la modification et la suppression
- Déchiffrement des fichiers après récupération de la clé
- Alerte via **popup** si un fichier chiffré est ouvert

## Installation
1. **Cloner le dépôt**
   ```sh
   git clone https://github.com/NizarETH/CMC_Ransomware.git
   cd CMC_Ransomware
   ```
2. **Installer les dépendances**
   ```sh
   pip install cryptography
   ```

## Utilisation
1. **Exécuter le script**
   ```sh
   python main.py
   ```
2. **Choisir une option**
   - `1` : Chiffrement des fichiers dans un dossier
   - `2` : Déchiffrement des fichiers
3. **Saisir le chemin du dossier cible**

## Prévention contre les ransomwares
- Faire des **sauvegardes régulières** de ses fichiers
- Ne pas ouvrir des **pièces jointes suspectes**
- Maintenir son **système à jour**
- Utiliser un **antivirus efficace**

## Licence
Ce projet est sous licence MIT. Il est destiné à l'apprentissage et la sensibilisation à la cybersécurité.

