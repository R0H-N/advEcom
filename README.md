
---

# 🛒 Enlog E-Commerce API

A robust and secure backend API for an e-commerce application built with Django and Django REST Framework.

This project supports user registration, JWT authentication, product browsing, order placement, and stock management, with admin-only access to product management and full order visibility.

---

## ✅ Features

* JWT-based authentication (Login & Token Refresh)
* Custom user model with additional fields: `address` and `phone`
* Admin-only product management (CRUD)
* Authenticated users can:

  * Register and log in
  * View available products
  * Place orders (multi-item support)
  * View and cancel their unpaid orders
* Stock is automatically reduced when an order is placed
* Admins can view all orders

---

## 🧱 Tech Stack

| Layer       | Technology                                |
| ----------- | ----------------------------------------- |
| Backend     | Django, Django REST Framework             |
| Auth System | SimpleJWT (Token-based)                   |
| Database    | SQLite / PostgreSQL (configurable)        |
| User Model  | CustomUser (extended from `AbstractUser`) |

---

## 👤 User Registration & Authentication

### 🔹 Register

**POST** `/register/`

Registers a new user.

**Request Body:**

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePassword123",
  "first_name": "John",
  "last_name": "Doe",
  "address": "123 Main St, New York",
  "phone": "+1234567890"
}
```

### 🔹 Obtain Token

**POST** `/api/token/`

```json
{
  "username": "john_doe",
  "password": "SecurePassword123"
}
```

### 🔹 Refresh Token

**POST** `/api/token/refresh/`

```json
{
  "refresh": "<your-refresh-token>"
}
```

---

## 📦 Product API

| Action         | Method | Endpoint                 | Access     |
| -------------- | ------ | ------------------------ | ---------- |
| List Products  | GET    | `/products/`             | Public     |
| Product Detail | GET    | `/products/<id>/`        | Public     |
| Create Product | POST   | `/products/create/`      | Admin only |
| Update Product | PUT    | `/products/<id>/update/` | Admin only |
| Delete Product | DELETE | `/products/<id>/delete/` | Admin only |

**Product Payload Example (Admin Only):**

```json
{
  "name": "Wireless Mouse",
  "description": "Bluetooth optical mouse",
  "price": 699.00,
  "stock": 25
}
```

---

## 🛍️ Order API

| Action          | Method | Endpoint               | Access             |
| --------------- | ------ | ---------------------- | ------------------ |
| Create Order    | POST   | `/orders/create/`      | Authenticated user |
| View My Orders  | GET    | `/orders/my-orders/`   | Authenticated user |
| Order Detail    | GET    | `/orders/<id>/`        | Authenticated user |
| Cancel Order    | DELETE | `/orders/<id>/cancel/` | If unpaid          |
| View All Orders | GET    | `/orders/all/`         | Admin only         |

### 🔹 Create Order

```json
{
  "items": [
    { "product": 1, "quantity": 2 },
    { "product": 3, "quantity": 1 }
  ]
}
```

✔ Automatically deducts stock on placement
❌ Cancelling an order does **not** restore stock

---

## 📌 Notes

* Product management is restricted to admin users
* Stock is reduced **immediately** when an order is placed
* Order cancellation is allowed **only if unpaid**
* Order items are linked and created dynamically per order
* `CustomUser` includes `address` and `phone` fields

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/enlog-ecommerce-api.git
cd enlog-ecommerce-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

* Access API: `http://localhost:8000/`
* Admin Panel: `http://localhost:8000/admin/`

---

