# FLACK

FLACK est une simple API Flask pour recevoir et stocker des clés, C'est notamment ce que j'ai utilisé pour le ransomware fait pour mon mémoire pour recevoir les clés génerés

## Description

Cette application Flask reçoit une clé via une requête POST à l'endpoint `/receive_key`. La clé reçue est ensuite sauvegardée dans un fichier texte nommé `received_key.txt`.

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/votre-repo.git
    cd votre-repo
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    ```

3. Installez les dépendances :
    ```bash
    pip install Flask
    ```

## Utilisation

1. Lancez l'application Flask :
    ```bash
    python FLACK.py
    ```

2. Envoyez une requête POST à l'endpoint `/receive_key` avec un champ de formulaire nommé `key`. Par exemple, vous pouvez utiliser `curl` :
    ```bash
    curl -X POST -F "key=your_key_here" http://localhost:5000/receive_key
    ```

3. Si la requête est réussie, vous recevrez une réponse JSON indiquant que la clé a été reçue et stockée. La clé sera sauvegardée dans le fichier `received_key.txt`.

