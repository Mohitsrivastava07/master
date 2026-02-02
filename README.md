🏦 Bank Management System (Streamlit)
----------------------------------------------
* A simple and interactive **Bank Management System** built using **Python and Streamlit**.  
This project allows users to create bank accounts, deposit and withdraw money, check account balances, and generate QR codes for account details — all through a clean sidebar-based interface.

* The application uses **session-based in-memory storage**, making it ideal for beginners learning Python, Streamlit, and basic backend logic.

✨ Features
----------------------------------------------
* 🆕 Account creation with unique account numbers  
* 💰 Deposit money securely  
* 💸 Withdraw money with balance validation  
* 🔐 PIN-protected balance inquiry  
* 📷 QR code generation for account details  
* 📊 Preloaded sample user accounts  
* 📁 Session-based temporary data storage  
* 🧭 Sidebar navigation menu  

🛠️ Technologies Used
----------------------------------------------
* **Python 3**
* **Streamlit**
* **qrcode**
* **Pillow (PIL)**
* **VS Code** (recommended

🔐 Default Test Accounts
---------------------------------------------
Name	  Account   Number	  PIN	Balance
Mohit	  10242	    123@	    1024.45
Naitik	21457	    1234@	    1028.46
Ayush	  45876	    12345@	  1030.48

📋 How It Works
----------------------------------------------
🔹 Account Creation
* Enter a unique username and PIN
* A 5-digit random account number is generated
* Initial balance is set to 0.0

🔹 Deposit
* Enter username, account number, and PIN
* Deposit any positive amount

🔹 Withdrawal
* Withdraw money if sufficient balance is available

🔹 Balance Inquiry
* View your current balance securely

🔹 QR Code Generation
* Generates a QR code containing:
* Username
* Account Number
* PIN
* Balance
* Saved as <username>_QR.png

📷 QR Code Functionality
-----------------------------------------------
* Users can generate a QR code containing:
* Account Holder Name
* Account Number
* Current Balance
* The QR code is displayed directly in the application and can be scanned to view account details.

⚠️ Important Notes
-----------------------------------------------
* Data is stored only in session memory
* Restarting the app will reset all data
* No real database is used
* Intended for educational and learning purposes

🌱 Future Enhancements
-----------------------------------------------
* Database integration (MySQL / SQLite)
* User authentication system
* Transaction history
* Admin dashboard
* Improved UI with custom CSS

🚀 How to Run the Project
----------------------------------------------
1️⃣ Install Python
* Make sure Python **3.8 or higher** is installed.

* Check version:
      bash
python --version

2️⃣ Go to same file/folder
* where BankManagementSystemApp.py is available

3️⃣ Type in Terminal/bash
* streamlit run filename.py
* on this filename is BankManagementSystemApp
* The application will open automatically in your browser:
* 👉 http://localhost:8501


👨‍💻 Author
-----------------------------------------------
Name --> Mohit Kumar Srivastava
                      Developer

🔗 LinkedIn Profile URL
------------------------------------------------
* 👉 https://www.linkedin.com/in/mohit-kumar-79770b39b/
