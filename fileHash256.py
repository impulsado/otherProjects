# --- IMPORT MODULES
import os
import hashlib


# --- CREATE FUNCTIONS
def banner():
    # Print banner
    print("")
    print("##################################")
    print("     FILE HASH-256 by impulsado   ")
    print("##################################")
    print("")
    return


def findFile(usr_path,usr_file):
    # Search the file in the path and return True if exists.
    files_and_directories = os.listdir(usr_path)
    if usr_file in files_and_directories:
        return True
    else:
        return False


def createFile(usr_path,usr_file):
    # Create file in the path the user specified in askDestination().
    usr_file_n = os.path.join(usr_path, usr_file)
    file = open(usr_file_n,"w")
    file.close()
    return


def openFiles(usr_path_o,usr_file_o,usr_path_n,usr_file_n):
    # Open files and call hashFile().
    usr_file_o = os.path.join(usr_path_o, usr_file_o)
    usr_file_n = os.path.join(usr_path_n, usr_file_n)
    file_o = open(usr_file_o)
    file_n = open(usr_file_n,"a")
    hashFile(file_o,file_n)
    file_o.close()
    file_n.close()
    return


def hashFile(file_o,file_n):
    # Recibe the old and the new file. Hash every line and append it into the new file.
    # It uses SHA256.
    for line_o in file_o:
        line_oo = line_o.strip()  # Remove "\n"
        hash_object = hashlib.sha256(line_oo.encode("utf-8"))
    file_n.write(hash_object.hexdigest())
    print("=== FILE HASED SUCESSFULLY! ===")
    return


def askFileToHash():
    # Requests the path and name of the file. If it does not exist returns False, else returns True
    print("=== FILE YOU WANT TO HASH ===")
    usr_path = input("File Path: ")
    usr_file = input("File Name: ")
    ch1 = findFile(usr_path,usr_file)
    if ch1 == False:
        print("No such file!")
        return False, usr_path, usr_file
    print("")  #Aesthetic
    return ch1, usr_path, usr_file


def askDestination():
    # Requests the path and name of the new file. If it exist returns False, else returns True.
    # Returns usr_path and usr_file too.
    print("=== NEW FILE WHERE YOU WANT TO SAVE THE HASH ===")
    usr_path = input("Path File: ")
    usr_file = input("File Name: ")
    ch2 = findFile(usr_path,usr_file)
    if ch2 == True:
        print("The file already exists!")
        return False, usr_path, usr_file
    print("")  #Aesthetic
    return ch2, usr_path, usr_file


def main():
    banner()

    ch1,usr_path_o,usr_file_o = askFileToHash()
    if ch1 == False:
        return
    
    ch2,usr_path_n,usr_file_n = askDestination()
    if ch2 == True:
        return

    createFile(usr_path_n,usr_file_n)

    openFiles(usr_path_o,usr_file_o,usr_path_n,usr_file_n)
    return


# --- MAIN PROGRAM
main()