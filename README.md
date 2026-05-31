# Django Blogging Platform

A simple, beginner-friendly blogging website built with **Django** and **Bootstrap 5**.

## Features

✨ **User Authentication**
- User Registration
- User Login/Logout
- Profile dropdown in navbar

📝 **Blog Functionality**
- Create blog posts (authenticated users only)
- View all blog posts on home page
- View detailed post pages
- Edit your own posts
- Delete your own posts

🎨 **User Interface**
- Responsive Bootstrap 5 design
- Mobile-friendly layout
- Beautiful hero section on home page
- Blog post cards with hover effects
- Clean, modern design
- Bootstrap alert messages for success/error feedback

🔐 **Security**
- Django built-in authentication
- User authorization (users can only edit/delete their own posts)
- CSRF protection
- Password validation

## Project Structure

```
.
├── first/                    # Main project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── home/                     # Main app
│   ├── models.py            # BlogPost model
│   ├── views.py             # View logic
│   ├── urls.py              # App URL routing
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin configuration
│   └── migrations/          # Database migrations
├── templates/               # HTML templates
│   ├── base.html            # Base template with navbar/footer
│   ├── index.html           # Home page with all posts
│   ├── register.html        # User registration
│   ├── login.html           # User login
│   ├── create_post.html     # Create new post
│   ├── edit_post.html       # Edit existing post
│   ├── delete_post.html     # Delete post confirmation
│   └── post_detail.html     # Single post detail view
├── static/                  # Static files (CSS, JS, images)
├── db.sqlite3               # SQLite database (not in git)
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not in git)
├── .env.example             # Template for .env
└── .gitignore               # Git ignore rules
```

## Technology Stack

- **Backend**: Django 6.0.5
- **Frontend**: Bootstrap 5
- **Database**: SQLite
- **Python**: 3.14+

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd first
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example file
cp .env.example .env

# Edit .env with your settings (if needed)
# The default values should work for development
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### 7. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### As a Regular User
1. Visit the home page
2. Click "Register" to create a new account
3. Login with your credentials
4. Click "Create Post" to write a blog post
5. View all posts on the home page
6. Click "Read More" to view a full post
7. If it's your post, you can edit or delete it
8. Access your profile dropdown by clicking your username in the navbar

### As an Admin
1. Visit `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials
3. Manage users, posts, and site content

## API Endpoints

| URL | View | Purpose |
|-----|------|---------|
| `/` | index | Home page - display all posts |
| `/register/` | register | User registration |
| `/login/` | login_view | User login |
| `/logout/` | logout_view | User logout |
| `/post/create/` | create_post | Create new post |
| `/post/<id>/` | post_detail | View single post |
| `/post/<id>/edit/` | edit_post | Edit your post |
| `/post/<id>/delete/` | delete_post | Delete your post |
| `/admin/` | Django Admin | Admin panel |

## Database Models

### BlogPost
```python
- title (CharField): Post title
- content (TextField): Post content
- author (ForeignKey): Author (User)
- created_at (DateTimeField): Creation timestamp
- updated_at (DateTimeField): Last update timestamp
```

## Environment Variables (.env)

```env
SECRET_KEY=your-secret-key-here
DEBUG=True  # Set to False in production
ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=sqlite:///db.sqlite3

# Optional email settings
# EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=your-email@gmail.com
# EMAIL_HOST_PASSWORD=your-app-password
```

## Important Notes

- ⚠️ **Never commit `.env` file** - It contains sensitive information
- ⚠️ **Never commit `db.sqlite3`** - Database file will be regenerated
- ✅ **Always commit `.env.example`** - So others know what variables are needed
- 🔐 Keep your `SECRET_KEY` secret in production
- 🧪 Set `DEBUG=False` before deploying to production

## Features for Future Enhancement

- Comment system on posts
- Like/favorite posts
- Search functionality
- Categories/Tags
- Email notifications
- Post scheduling
- Rich text editor (TinyMCE, CKEditor)
- Social media sharing
- User profiles with bio
- Pagination for posts

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository.

---

Happy Blogging! 📝✨
