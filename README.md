# Cholonto-Rush - On-Road Bike Service Platform

A comprehensive Django-based web application for on-road bike maintenance and emergency services. This platform connects bike owners with certified mechanics and service centers for quick roadside assistance and professional bike maintenance services.

## 🚀 Features

### Core Functionality
- **User Authentication & Management**: Complete user registration, login, and profile management
- **Service Catalog**: Browse and book various bike maintenance services
- **Service Centers**: Find and connect with nearby service centers
- **Agent Management**: Professional mechanics and service agents
- **Shopping Cart & Orders**: E-commerce functionality for service booking
- **Problem Reporting**: Report bike issues with GPS location and photo uploads
- **Order Tracking**: Real-time order status updates and agent assignment

### Service Categories
- **Emergency Services**:
  - Flat tire repair
  - Battery jumpstart
  - Fuel emergency delivery
  - Engine diagnostics

- **Maintenance Services**:
  - Oil top-up and change
  - Carburetor modification
  - Throttle adjustment
  - Brake system checks
  - Chain maintenance

### Advanced Features
- **GPS Integration**: Location-based service center and agent finding
- **Photo Upload**: Problem documentation with image attachments
- **Priority System**: Urgent, high, medium, and low priority problem classification
- **Status Tracking**: Complete order and problem lifecycle management
- **Responsive Design**: Mobile-friendly interface with Bootstrap 5

## 🛠️ Technology Stack

- **Backend**: Django 4.2.25
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Forms**: Django Crispy Forms with Bootstrap 5 styling
- **API**: Django REST Framework
- **Image Processing**: Pillow
- **Authentication**: Django's built-in authentication system

## 📁 Project Structure

```
tuktuksite/
├── accounts/           # User authentication and profiles
├── agents/            # Service agent management
├── cart/              # Shopping cart functionality
├── centers/           # Service center management
├── core/              # Main application views and templates
├── orders/            # Order management and tracking
├── reports/           # Problem reporting system
├── services/          # Service catalog and categories
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
└── tuktuksite/        # Django project settings
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Project--Proposal
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Seed demo data (optional)**
   ```bash
   python manage.py seed_demo
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📱 Usage

### For Customers
1. **Register/Login**: Create an account or sign in
2. **Browse Services**: View available maintenance services
3. **Find Centers**: Locate nearby service centers
4. **Book Services**: Add services to cart and place orders
5. **Report Problems**: Submit bike issues with photos and location
6. **Track Orders**: Monitor order status and agent assignments

### For Service Centers
1. **Manage Services**: Add and update service offerings
2. **Agent Management**: Assign and manage service agents
3. **Order Processing**: Handle incoming service requests
4. **Problem Resolution**: Respond to customer problem reports

### For Agents
1. **View Assignments**: See assigned orders and problems
2. **Update Status**: Mark orders as completed or in progress
3. **Customer Communication**: Respond to customer queries

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root for production settings:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Database Configuration
For production, update `settings.py` to use PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 📦 Deployment

### Using Heroku
1. Install Heroku CLI
2. Create a `Procfile`:
   ```
   web: gunicorn tuktuksite.wsgi --log-file -
   ```
3. Add PostgreSQL addon
4. Deploy:
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

### Using Docker
1. Create a `Dockerfile`
2. Create a `docker-compose.yml`
3. Build and run:
   ```bash
   docker-compose up --build
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Development Team**: Project Proposal Team
- **Framework**: Django 4.2.25
- **UI/UX**: Bootstrap 5 with custom styling

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔄 Version History

- **v1.0.0** - Initial release with core functionality
- **v1.1.0** - Added problem reporting system
- **v1.2.0** - Enhanced order tracking and agent assignment

---

**Cholonto-Rush** - Your trusted partner for on-road bike maintenance and emergency services! 🏍️