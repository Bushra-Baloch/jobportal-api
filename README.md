 Job Portal API

A real-world Django REST Framework API that connects **companies** with **job applicants**. Built with JWT authentication, role-based permissions, and full CRUD operations.



 🚀 Features

- ✅ JWT Authentication (Signup/Login)
- ✅ Custom User model with `company` and `applicant` roles
- ✅ Company can create, update, delete jobs
- ✅ Applicant can view and apply for jobs
- ✅ Application history for applicants
- ✅ Role-based access control
- ✅ Clean API structure using DRF (Django REST Framework)


📂 Endpoints Summary

 🔐 Authentication
| Method | URL                    | Description       |
|--------|------------------------|-------------------|
| POST   | `/api/signup/`         | Signup (company/applicant) |
| POST   | `/api/login/`          | JWT Token login   |

 💼 Job
| Method | URL                    | Description       |
|--------|------------------------|-------------------|
| POST   | `/api/jobs/create/`    | Company: Post job |
| GET    | `/api/jobs/`           | List all jobs     |
| GET/PUT/DELETE |
