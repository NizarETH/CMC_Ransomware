from cryptography.fernet import Fernet
import os
import stat


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key


def load_key():
    return open("key.key", "rb").read()


def encrypt_file(file_path, key):
    unprotect_file(file_path)
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    protect_file(file_path)


def decrypt_file(file_path, key):
    unprotect_file(file_path)
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    decrypted_data = fernet.decrypt(data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)


def encrypt_folder(folder_path, key):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)
    protect_folder(folder_path)


def decrypt_folder(folder_path, key):
    unprotect_folder(folder_path)
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)


def protect_folder(folder_path):
    try:
        os.chmod(folder_path, stat.S_IREAD | stat.S_IEXEC)  # => les 2 : Lecture et exécution autorisées
        for root, _, files in os.walk(folder_path):
            for file in files:
                protect_file(os.path.join(root, file))
        print("Le contenu de dossier ne peut pas être modifié ou supprimé.")
    except Exception as e:
        print(f"Erreur {e}")


def unprotect_folder(folder_path):
    try:
        os.chmod(folder_path, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)  # Restauration complète des permissions
        for root, _, files in os.walk(folder_path):
            for file in files:
                unprotect_file(os.path.join(root, file))
        print("Dossier déverrouillé.")
    except Exception as e:
        print(f"Erreur {e}")


def protect_file(file_path):
    os.chmod(file_path, stat.S_IREAD)  # Lecture seule


def unprotect_file(file_path):
    os.chmod(file_path, stat.S_IWRITE | stat.S_IREAD)



if __name__ == "__main__":
    folder = input("Entrez le chemin du dossier : ")
    action = int(input("Voulez-vous chiffrer 1 ou déchiffrer 2 ? "))

    if action == 1:
        key = generate_key()
        encrypt_folder(folder, key)
        print("Chiffrement terminé.")
    elif action == 2:
        key = load_key()
        decrypt_folder(folder, key)
        print("Déchiffrement terminé.")
    else:
        print("Erreur.")