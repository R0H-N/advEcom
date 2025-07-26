

---

````markdown
# 🛒 Enlog E-Commerce API

A robust and secure backend API for an e-commerce application built with Django and Django REST Framework.  
Supports user registration, authentication, product listing, order placement, and stock management.

---

## ✅ Features

- JWT-based user authentication
- Admin-only product management (CRUD)
- Authenticated users can:
  - View available products
  - Place orders with multiple items
  - View their order history
  - Cancel unpaid orders
- Admins can view all orders
- Automatic stock deduction on order placement

---

## 🧱 Tech Stack

- Python & Django
- Django REST Framework
- SimpleJWT for authentication
- SQLite / PostgreSQL (configurable)

---

## 📦 Product API

### 🔹 List Products  
`GET /products/`  
Returns all available products. *(Public)*

---

### 🔹 Product Detail  
`GET /products/<id>/`  
Returns details of a specific product. *(Public)*

---

### 🔹 Create Product  
`POST /products/create/`  
**Admin only**  
**Headers:** `Authorization: Bearer <token>`  
**Body:**
```json
{
  "name": "Mouse",
  "description": "Wireless optical mouse",
  "price": 699.00,
  "stock": 20
}
````

---

### 🔹 Update Product

`PUT /products/<id>/update/`
**Admin only**

---

### 🔹 Delete Product

`DELETE /products/<id>/delete/`
**Admin only**

---

## 🛍️ Order API

### 🔹 Create Order

`POST /orders/create/`
**Headers:** `Authorization: Bearer <token>`
**Body:**

```json
{
  "items": [
    { "product": 1, "quantity": 2 },
    { "product": 3, "quantity": 1 }
  ]
}
```

Automatically deducts ordered quantities from product stock.

---

### 🔹 View My Orders

`GET /orders/my-orders/`
Lists all orders of the authenticated user.

---

### 🔹 Order Detail

`GET /orders/<id>/`
Returns details of a specific order (owned by the user).

---

### 🔹 Cancel Order

`DELETE /orders/<id>/cancel/`
Allowed only if the order is unpaid and belongs to the requesting user.

---

### 🔹 View All Orders

`GET /orders/all/`
**Admin only**
Returns a list of all orders in the system.

---

## 🔐 Authentication

### Obtain Token

`POST /api/token/`

```json
{
  "username": "user1",
  "password": "securepassword"
}
```

### Refresh Token

`POST /api/token/refresh/`

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

Access API at: `http://localhost:8000/`

Admin panel: `http://localhost:8000/admin/`

---

## 📌 Notes

* Product creation, update, and deletion are restricted to admin users.
* Product stock is reduced immediately upon order placement.
* Cancelling an order does not restore product stock.

---

