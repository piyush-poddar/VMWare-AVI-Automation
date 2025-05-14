# 🛠️ VMware AVI Automation - Tenant Creation via Python

This project demonstrates how to automate the creation of a new **tenant** on a VMware AVI Load Balancer Controller using Python and the `requests` library. The script replicates the behavior of a successful POST request from Postman.

---

## 📌 Task Overview

- **Objective**: POST a tenant with your name to the VMware AVI Load Balancer using Postman and automate the same using Python.
- **VMware AVI Controller URL**: `https://35.200.176.139/`

---

## 🧪 Requirements

- Python 3.x
- `requests` library

You can install dependencies using:

```bash
pip install requests
```

## 🚀 How to Run

Step 1: Clone the Repository

```bash
git clone https://github.com/piyush-poddar/VMWare-AVI-Automation.git
cd VMWare-AVI-Automation
```

Step 2: Run the Script

```bash
python add_tenant.py
```

This will:

- Log in to the AVI Load Balancer

- Retrieve the CSRF token and session cookies

- Create a new tenant with the name test-tenant

- Print the response status and JSON result