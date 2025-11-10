# Library Book Management System

A comprehensive web-based Library Book Management System designed to automate daily library tasks, streamline record-keeping, and provide efficient operations with role-based access control and secure data management.

## Problem Statement

Libraries often face challenges in manually tracking book issuance, returns, due dates, and maintaining accurate records. Traditional paper-based methods are:
- Time-consuming and error-prone
- Difficult to quickly locate book availability
- Challenging for tracking overdue details
- Inefficient for both librarians and students

This system addresses these issues by providing an automated, web-based solution for efficient library operations.

## Key Features

### 1. Book Catalog Management
- Add, update, and delete book details (title, author, ISBN, category)
- Search and filter books by author, title, or subject
- Manage multiple copies of the same book
- Track book location and shelf information

### 2. Book Issuance & Return Tracking
- Record issuance of books to students
- Track return dates and automatically calculate due dates
- Generate issuance and return receipts
- Maintain complete book transaction history

### 3. Overdue & Fine Calculation
- Automatic detection of overdue books
- Fine calculation based on overdue duration
- Fine payment tracking and receipt generation
- Automated reminders for overdue books

### 4. User Authentication & Roles
- Secure login system for librarians and students
- Role-based access control:
  - **Librarians**: Full access to inventory, user management, and reports
  - **Students**: View issued books, track due dates, pay fines
- Password encryption and session management

### 5. Student Book Records
- Maintain comprehensive history of books issued to each student
- Quick retrieval of borrowing patterns
- View current issued books and their due dates
- Access personal fine and payment history

### 6. Reports & Notifications
- Reports on available, issued, and overdue books
- Notifications/reminders for upcoming due dates
- Email alerts for overdue books
- Statistical reports on library usage

### 7. Data Security & Backup
- Secure handling of student and book records
- Backup and restore functionality for library data
- Encrypted database storage
- Audit trails for all transactions

### 8. Scalability
- Ability to manage a large library database
- Support for multiple concurrent users
- Optimized database queries for performance
- Cloud-ready architecture

## Technology Stack

### Backend
- **Framework**: Flask (Python) or Node.js
- **Database**: MySQL/PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Email Service**: SMTP for notifications

### Frontend
- **HTML5** for structure
- **CSS3** for styling (Bootstrap/Tailwind CSS)
- **JavaScript** (Vanilla or React) for interactivity
- **Responsive design** for mobile compatibility

### Additional Tools
- **Version Control**: Git & GitHub
- **API Documentation**: Swagger/OpenAPI
- **Testing**: Pytest/Jest
- **Deployment**: Docker, AWS/Heroku

## Project Structure

```
Library-Book-Management-System/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── models/
│   │   ├── book.py
│   │   ├── user.py
│   │   ├── issuance.py
│   │   └── fine.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── books.py
│   │   ├── issuance.py
│   │   └── reports.py
│   └── utils/
│       ├── database.py
│       ├── validators.py
│       └── email_service.py
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── main.js
│   │   └── api.js
│   ├── pages/
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── books.html
│   │   └── reports.html
│   └── images/
├── database/
│   ├── schema.sql
│   ├── seed_data.sql
│   └── backup.sql
├── documentation/
│   ├── API_DOCUMENTATION.md
│   ├── USER_GUIDE.md
│   ├── INSTALLATION.md
│   └── DATABASE_DESIGN.md
├── .gitignore
├── README.md
├── LICENSE
└── docker-compose.yml
```

## Installation & Setup

### Prerequisites
- Python 3.8+ / Node.js 14+
- MySQL 5.7+ / PostgreSQL 10+
- Git

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Library-Book-Management-System.git
cd Library-Book-Management-System
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

4. Configure database:
- Create a database named `library_management`
- Update `config.py` with your database credentials
- Run migrations: `python manage.py migrate`

5. Run the application:
```bash
python app.py
```

The backend will be available at `http://localhost:5000`

### Frontend Setup

1. Open the frontend folder:
```bash
cd frontend
```

2. Open `index.html` in a web browser or use a local server:
```bash
python -m http.server 8000
```

The frontend will be available at `http://localhost:8000`

## Database Schema

### Key Tables
- **Users**: Stores user information (librarians and students)
- **Books**: Contains book catalog information
- **Issuance**: Records book issuance transactions
- **Returns**: Tracks book returns
- **Fines**: Manages fine calculations and payments
- **Notifications**: Stores notification history

For detailed schema, refer to `database/schema.sql`

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/register` - User registration (admin only)

### Books
- `GET /api/books` - List all books
- `POST /api/books` - Add new book (librarian only)
- `PUT /api/books/:id` - Update book details
- `DELETE /api/books/:id` - Delete book
- `GET /api/books/search` - Search books

### Issuance
- `POST /api/issuance` - Issue a book
- `GET /api/issuance/:studentId` - Get student's issued books
- `POST /api/issuance/return/:id` - Return a book

### Reports
- `GET /api/reports/available-books` - Available books report
- `GET /api/reports/issued-books` - Issued books report
- `GET /api/reports/overdue-books` - Overdue books report
- `GET /api/reports/fine-collection` - Fine collection report

## User Roles & Permissions

### Librarian
- Manage book catalog (add, update, delete)
- Issue and return books
- View all reports
- Manage student accounts
- Calculate and manage fines
- Generate notifications

### Student
- View available books
- View issued books
- Track due dates
- View personal fines
- Pay fines online
- View borrowing history

## Security Features

1. **Authentication**: Secure login with password hashing
2. **Authorization**: Role-based access control (RBAC)
3. **Encryption**: SSL/TLS for data transmission
4. **SQL Injection Prevention**: Parameterized queries
5. **CSRF Protection**: Anti-CSRF tokens
6. **Session Management**: Secure session handling
7. **Audit Logging**: All transactions logged

## Testing

Run tests using:
```bash
pytest backend/tests/
```

For coverage report:
```bash
pytest --cov=backend backend/tests/
```

## Deployment

### Docker
```bash
docker-compose up
```

### Heroku
```bash
heroku login
heroku create your-app-name
git push heroku main
```

## Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support & Contact

For support, email: support@librarymgmt.com

For issues and feature requests, please use the [GitHub Issues](https://github.com/yourusername/Library-Book-Management-System/issues) section.

## Roadmap

- [ ] Mobile application (React Native/Flutter)
- [ ] Advanced analytics and BI reports
- [ ] Integration with payment gateways
- [ ] QR code based book tracking
- [ ] Integration with student information system
- [ ] Multi-language support
- [ ] RFID integration

## Acknowledgments

Thank you to all contributors and the open-source community for their support and contributions.

---

**Last Updated**: November 2025
**Version**: 1.0.0
