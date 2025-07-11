```
## 🚀 Getting Started

Follow these steps to set up and run the project locally:

### 📦 1. Clone the Repository
git clone https://github.com/abir2776/digital-walet.git
cd digital-walet

### 🐍 2. Create and Activate a Virtual Environment
python3 -m venv venv
# For Linux or macOS: source venv/bin/activate  # On Windows, use: venv\Scripts\activate

### 📥 3. Install Project Dependencies
pip install -r requirements.txt

### ⚙️ 4. Run Migrations (if necessary)
python3 manage.py migrate

### 🏃 5. Start the Development Server
python manage.py runserver

The server will start at: http://127.0.0.1:8000/

---
go to http://127.0.0.1:8000/docs/swagger to check all available endpoint 

## 🧾 User Registration

To register a new user, send a POST request to the following endpoint:

POST http://127.0.0.1:8000//api/v1/auth/register Make sure to include the required fields (e.g., email, password, first_name, last_name) in the request body.

After creating user, send a POST request to the following endpoint with email and password to create access and refresh token:
POST http://127.0.0.1:8000//api/v1/token 

After giving authorization with access token send a GET request to the following endpoint to check the balance:
GET http://127.0.0.1:8000//api/v1/wallet/balance

Send POST request with transaction_type,amount,description and transfer_user if transaction_type is TRANSFER to create a transaction:
POST  http://127.0.0.1:8000//api/v1/wallet/transactions

Send GET request to the following endpoint to get the list of transaction:
GET http://127.0.0.1:8000//api/v1/wallet/transactions

---

## ✅ You're all set!
Now you're ready to explore and build on the Digital Wallet project!
```
