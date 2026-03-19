import math
import os
import re
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_mail import Mail, Message   # Import Flask-Mail

app = Flask(__name__)

# MySQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/lawyer_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress warnings

db = SQLAlchemy(app)

app.secret_key = "YourSecretKeyHere"

# Database Models
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.Date, nullable=False)

class ContactForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)  # Add phone
    date = db.Column(db.String(50), nullable=False)   # Add date
    message = db.Column(db.Text, nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

def paginate_images(images, page, images_per_page=6):
    start_index = (page - 1) * images_per_page
    end_index = start_index + images_per_page
    return images[start_index:end_index]


@app.route('/about')
def about():
    all_images = [
        'assets/img/gallery/1.png',
        'assets/img/gallery/1.png',
        'assets/img/gallery/1.png',
        'assets/img/gallery/2.png',
        'assets/img/gallery/2.png',
        'assets/img/gallery/2.png',
        'assets/img/gallery/2.png',
        'assets/img/gallery/5.png',
        'assets/img/gallery/2.png',
        'assets/img/gallery/4.png',
        'assets/img/gallery/2.png',
        'assets/img/gallery/3.png',
        'assets/img/gallery/5.png',
        'assets/img/gallery/6.png',
        'assets/img/gallery/2.png',
        'assets/img/gallery/1.png',

        
        # ... add all your images
    ]
    page = request.args.get('page', default=1, type=int)
    images_per_page = 6
    total_pages = math.ceil(len(all_images) / images_per_page)
    current_page_images = paginate_images(all_images, page, images_per_page)

    lawyers = [
        {
            'image': 'assets/img/lawyersmugshot/1.png',
            'name': 'Lawyer 1',
            'title': 'Senior Associate',
            'experience': '10+ years',
            'expertise': 'Corporate Law',
            'description': '...'
        },
        {
            'image': 'assets/img/lawyersmugshot/2.png',
            'name': 'Lawyer 2',
            'title': 'Senior Associate',
            'experience': '15+ years',
            'expertise': 'Corporate Law',
            'description': '...'
        },
        {
            'image': 'assets/img/lawyersmugshot/3.png',
            'name': 'Lawyer 1',
            'title': 'Senior Associate',
            'experience': '10+ years',
            'expertise': 'Corporate Law',
            'description': '...'
        },
        {
            'image': 'assets/img/lawyersmugshot/4.png',
            'name': 'Lawyer 1',
            'title': 'Senior Associate',
            'experience': '10+ years',
            'expertise': 'Corporate Law',
            'description': '...'
        },
        {
            'image': 'assets/img/lawyersmugshot/5.png',
            'name': 'Lawyer 1',
            'title': 'Senior Associate',
            'experience': '10+ years',
            'expertise': 'Corporate Law',
            'description': '...'
        },
        {
            'image': 'assets/img/lawyersmugshot/6.png',
            'name': 'Lawyer 1',
            'title': 'Senior Associate',
            'experience': '10+ years',
            'expertise': 'Corporate Law',
            'description': '...'
        },

        # Add more lawyers
    ]
    images = ['assets/img/gallery/1.png','assets/img/gallery/2.png','assets/img/gallery/3.png','assets/img/gallery/4.png','assets/img/gallery/5.png','assets/img/gallery/6.png']
    return render_template('about.html', lawyers=lawyers, images=current_page_images, current_page=page, total_pages=total_pages)
    #return render_template('about.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')

# route for taking learn more to different pages for explation
@app.route('/practice_details/<area_name>')
def practice_details(area_name):
    return render_template('practice_details.html', area_name=area_name)

@app.route('/blog')
def blog():
    # posts = BlogPost.query.all()
    # return render_template('blog.html', posts=posts)
    return render_template('blog.html') # Ensure 'blog.html' is the correct template name.

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    # post = BlogPost.query.get_or_404(post_id)
    # return render_template('blog-details.html', post=post)
    return render_template('blog-details.html', post_id=post_id) # Ensure 'blog-details.html' is the correct template name.

@app.route('/join')
def join():
    return render_template('join.html') #create join.html file inside templates folder.


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        contact_form = ContactForm(name=name, email=email, subject=subject, message=message)
        db.session.add(contact_form)
        db.session.commit()

        return "Thank you for your message!"
    return render_template('contact.html')


# for form submission in the joinus.html
UPLOAD_FOLDER = 'uploads'  # Create this folder in your project directory
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/internship', methods=['GET', 'POST'])
def submit_internship():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        university = request.form['university']
        degree = request.form['degree']
        year = request.form['year']
        cover_letter = request.form['cover_letter']

        if 'resume' not in request.files:
            return 'No file part'

        resume = request.files['resume']

        if resume.filename == '':
            return 'No selected file'

        if resume and resume.filename.endswith('.pdf'):
            filename = f"{name.replace(' ', '_')}_resume.pdf" #Create a unique file name
            resume.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Store the application data (e.g., in a database or file)
            # ...

            # Send a confirmation email
            # ...

            return "Application submitted successfully!"
        else:
          return "Invalid file type. Please upload a PDF."

    return render_template('join.html') # Ensure 'join.html' is the right template name.

# this is for the consultation form handling
# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'#'your_mail_server'  # e.g., smtp.gmail.com
app.config['MAIL_PORT'] = 465  # Or 587
app.config['MAIL_USE_SSL'] = True  # Or TLS
app.config['MAIL_USERNAME'] = 'vinaygautam@gmail.com'
app.config['MAIL_PASSWORD'] = 'achalagautam'
app.config['MAIL_DEFAULT_SENDER'] = 'vinaygautam021@gmail.com'

mail = Mail(app)

@app.route('/submit_consultation', methods=['POST'])
def submit_consultation():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        message = request.form['message']

        # Server-side validation
        email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
        phone_regex = r"^{9}$"

        if name.strip() == '':
            flash('Please enter your name.', 'error')
            return redirect(url_for('index'))

        if not re.match(email_regex, email):
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('index'))
        print(phone_regex)
        #if not re.match(phone_regex, phone):
        #    #print(phone_regex)
        #    flash('Please enter a valid 10-digit Indian phone number.', 'error')
        #    return redirect(url_for('index'))

        if date.strip() == '':
            flash('Please select an appointment date.', 'error')
            return redirect(url_for('index'))

        if message.strip() == '':
            flash('Please enter your message.', 'error')
            return redirect(url_for('index'))


        # Store in database
        new_consultation = ContactForm(name=name, email=email, phone=phone, date=date, message=message)
        db.session.add(new_consultation)
        db.session.commit()

        # Send email to yourself
        msg_to_admin = Message("New Consultation Request", recipients=["your_email@gmail.com"])
        msg_to_admin.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nMessage: {message}"
        try:
            mail.send(msg_to_admin)
        except Exception as e:
            print(f"Error sending email to admin: {e}")

        # Send confirmation email to user
        msg_to_user = Message("Consultation Request Received", recipients=[email])
        msg_to_user.body = "Your consultation request has been received. We will reach out to you soon."
        try:
            mail.send(msg_to_user)
        except Exception as e:
            print(f"Error sending email to user: {e}")

        # Flash a success message
        flash("Consultation request submitted successfully!", "success")  # Use flash

        return redirect(url_for('index'))  # Redirect to index
    return redirect(url_for('index'))


if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)