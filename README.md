```
## 🚀 Getting Started

Follow these steps to set up and run the project locally:

### 📦 1. Clone the Repository
git clone https://github.com/abir2776/digital-walet.git
cd digital-walet

### 🐍 2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

### 📥 3. Install Project Dependencies
pip install -r requirements.txt

### ⚙️ 4. Run Migrations (if necessary)
python manage.py migrate

### 🏃 5. Start the Development Server
python manage.py runserver

The server will start at: http://127.0.0.1:8000/

---

## 🧾 User Registration

To register a new user, send a POST request to the following endpoint:

POST /api/v1/auth/register

Make sure to include the required fields (e.g., username, email, password) in the request body.

---

## ✅ You're all set!
Now you're ready to explore and build on the Digital Wallet project!
```
