# 🛡️ Python Security & Cryptography Toolkit

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security Domain](https://img.shields.io/badge/Domain-Offensive_%26_Defensive_Security-red?style=for-the-badge&logo=shield)
![Cryptography](https://img.shields.io/badge/Crypto-AES--256_%7C_Fernet_%7C_PBKDF2-4B0082?style=for-the-badge)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-Apache--2.0-blue?style=for-the-badge)

**A modular Python security suite providing cryptographically secure password generation, strength evaluation, password cracking, and symmetric message and file encryption.**

[Sub-Project Repositories](#-individual-project-repositories) • [Core Modules](#-core-modules) • [System Architecture](#%EF%B8%8F-system-architecture) • [Crypto Specs](#-cryptographic-specifications) • [Installation](#-installation--setup) • [Usage Guide](#-usage-guide) • [Disclaimer](#-disclaimer)

</div>

---

## 🔗 Individual Project Repositories

This toolkit consolidates several standalone security & cryptography utilities. You can explore, contribute to, or inspect the standalone repositories for each individual project below:

| Project Module | Description | Repository Link |
| :--- | :--- | :--- |
| 🔑 **Password Generator** | CSPRNG-based password generator with custom rules | [password-generator](https://github.com/just-deva/password-generator) |
| 📊 **Password Strength Evaluator** | Shannon entropy calculator & pattern analyzer | [password-strength-evaluator](https://github.com/just-deva/password-strength-evaluator) |
| 🔓 **Python Password Cracker** | Multi-threaded hash cracker & dictionary audit tool | [python-password-cracker](https://github.com/just-deva/python-password-cracker) |
| ✉️ **Symmetric Message Encryptor** | Authenticated string message encryption engine | [symmetric-message-encryptor](https://github.com/just-deva/symmetric-message-encryptor) |
| 📁 **Symmetric File Encryptor** | PBKDF2 + AES-256 data-at-rest file encryption | [symmetric-file-encryptor](https://github.com/just-deva/symmetric-file-encryptor) |

---

## 📌 Overview

The **Python Security Toolkit** is a security and cryptographic utility designed for security testing, password auditing, and data protection. Built using Python's native Cryptographically Secure Pseudo-Random Number Generator (`secrets`) and standard cryptographic algorithms (`cryptography`, `hashlib`, `PBKDF2HMAC`), this toolkit provides both defensive capabilities and security audit tools.

---

## ⚙️ System Architecture

```mermaid
graph TD
    %% User Layer
    subgraph Controller ["🖥️ Controller Layer"]
        CLI[main.py - Interactive CLI]
    end

    %% Modules
    subgraph Modules ["🔒 Core Security Modules"]
        GEN[1. Password Generator]
        EVAL[2. Password Strength Evaluator]
        CRACK[3. Python Password Cracker]
        SME[4. Symmetric Message Encryptor]
        SFE[5. Symmetric File Encryptor]
    end

    %% Primitives
    subgraph Engine ["⚡ Cryptographic Engine & Primitives"]
        CSPRNG[CSPRNG / secrets module]
        ENTROPY[Shannon Entropy Math Engine]
        KDF[PBKDF2-HMAC-SHA256 Derivation]
        AES[AES-256 / Fernet Cipher Engine]
        HASH[MD5 / SHA-1 / SHA-256 / SHA-512 Engine]
    end

    CLI --> GEN & EVAL & CRACK & SME & SFE
    GEN --> CSPRNG
    EVAL --> ENTROPY
    CRACK --> HASH
    SME & SFE --> KDF --> AES
