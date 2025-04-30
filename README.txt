Basic Cryptography Project

Project Overview:
This project demonstrates symmetric encryption using the AES algorithm in Python. The script, crypto_project.py, encrypts a message ("Hello, friend!") into a random string and decrypts it back to the original message using the pycryptodome library. I developed the script on my Windows laptop, transferred it to a Kali Linux VM, and executed it in a virtual environment.

Process:
- I wrote the script on my Windows laptop and saved it in C:\SharedFolder.
- I faced permissions issues on Windows when trying to use a shared folder with Kali, so I used drag-and-drop to transfer the file to my Kali VM.
- In Kali, I set up a virtual environment (myenv) and installed pycryptodome.
- I encountered issues with the script not running due to Windows line endings (CRLF). I fixed this by installing dos2unix and converting the file to Linux line endings (LF).
- I activated the virtual environment and ran the script using python3 crypto_project.py, which successfully encrypted and decrypted the message.

Challenges and Solutions:
- I couldn’t get the shared folder to work due to permissions issues on Windows and mounting problems in Kali. I used drag-and-drop as a workaround.
- The script initially failed to run because I ran it directly (e.g., ./crypto_project.py) instead of using python3. I learned to use python3 crypto_project.py to execute Python scripts.
- The file kept disappearing from VMware’s drag-and-drop cache directories. I used the find command to locate it and moved it to my home directory.
- I had to use dos2unix to fix line-ending issues that caused syntax errors.

What I Learned:
This project taught me how to troubleshoot cross-platform issues, such as permissions on Windows and line endings between Windows and Linux. I gained experience with Linux commands like find, mv, and dos2unix, and learned how to set up and use a virtual environment in Kali. I also improved my understanding of symmetric encryption using AES and the pycryptodome library.
