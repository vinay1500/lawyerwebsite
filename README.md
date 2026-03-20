# Lawyer Website

A professional law firm website built with Flask, HTML templates, and static assets for showcasing legal services, team profiles, blog content, and client contact flows.

## Live Website

**Website:** https://patrialaw.online

---

## Topics

`flask` `python` `law-firm-website` `legal-services` `jinja-templates` `html` `css` `responsive-design` `business-website` `portfolio-project`

---

## Screenshots

> Add all screenshots inside a `screenshots/` folder in the project root.

### Home Page
![Home Page](./screenshots/home-page.png)

### About Page
![About Page](./screenshots/about-page.png)

### Practice Areas
![Practice Areas](./screenshots/practice-areas.png)

### Team Section
![Team Section](./screenshots/team-section.png)

### Blog Page
![Blog Page](./screenshots/blog-page.png)

### Contact Page
![Contact Page](./screenshots/contact-page.png)

---

## Overview

Lawyer Website is a multi-page legal services website designed for a law practice to present its brand, practice areas, legal team, blog content, and contact information in a structured and professional format.

The project follows a server-rendered Flask architecture using reusable HTML templates and static frontend assets. It is intended to support client trust-building, service discovery, and lead generation through a polished public-facing web presence.

---

## Live Pages / Sections

The live site currently includes the following major sections:

- Home
- About Us
- Practice Areas
- Blog
- Join Us
- Contact

Additional sections visible on the live site include legal team content, client testimonials, and practice-area detail content.  

---

## Architecture Summary

This project follows a Flask-based server-rendered architecture.

### Core structure

- `app.py`  
  Main Flask application entry point that defines routes and renders templates.

- `templates/`  
  Stores the HTML templates for the main pages and reusable layout pieces.

- `static/`  
  Contains CSS, JavaScript, images, and other static frontend assets.

- `requirements.txt`  
  Python dependency list for setting up the Flask environment.

### Template organization

The `templates/` directory includes page-level and reusable templates such as:

- `base.html`
- `index.html`
- `about.html`
- `practice.html`
- `practice_details.html`
- `blog.html`
- `single-blog.html`
- `contact.html`
- `join.html`
- `header.html`
- `footer.html`
- `social_media_links.html`
- `core_team.html`
- `managing_partner.html`
- `meetourpeople.html`

### Rendering flow

1. A request hits the Flask route in `app.py`
2. Flask renders the appropriate Jinja/HTML template
3. Shared layout elements are reused through common templates
4. Static CSS/JS/assets are loaded from the `static/` directory
5. Users browse content pages such as services, team, blog, and contact

---

## Feature List

- Multi-page law firm website
- Flask-based backend routing
- Server-rendered template architecture
- Reusable layout components
- Practice area showcase pages
- Lawyer/team presentation sections
- Blog and single-article page structure
- Contact and inquiry-oriented pages
- Social media links integration
- Professional business website structure

---

## Tech Stack

- Python
- Flask
- HTML
- CSS / SCSS
- JavaScript
- Jinja-style template rendering

---

## Folder Structure

```bash
lawyerwebsite/
├── __pycache__/
├── lawyer/
├── static/
├── templates/
│   ├── about.html
│   ├── appointment_area.html
│   ├── base.html
│   ├── blog.html
│   ├── contact.html
│   ├── content.html
│   ├── core_team.html
│   ├── footer.html
│   ├── header.html
│   ├── index.html
│   ├── join.html
│   ├── lawyers_description.html
│   ├── managing_partner.html
│   ├── meetourpeople.html
│   ├── photo_gallery.html
│   ├── practice.html
│   ├── practice_details.html
│   ├── single-blog.html
│   └── social_media_links.html
├── app.py
├── requirements.txt
└── README.md

### Getting Started
## Prerequisites

# Make sure you have installed:

Python 3

pip

# Clone the repository
git clone https://github.com/vinay1500/lawyerwebsite.git
cd lawyerwebsite
# Create a virtual environment
python -m venv venv
# Activate the virtual environment
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
# Run the Flask app
python app.py

Then open the local server in your browser.

Use Cases

## This website is suitable for:

law firms

solo legal practitioners

legal consultancy websites

service-based professional websites

portfolio presentation for freelance web development

## Future Improvements

Add appointment booking form with backend submission handling

Add admin panel for blog and content updates

Store contact inquiries in a database

Integrate email notifications for contact form submissions

Add SEO metadata for every page

Add structured schema for legal services and local business

Improve mobile responsiveness further

Add CMS or dashboard for non-technical content editing

Add search/filtering for blog posts or legal services

Add analytics and conversion tracking

License

This project is shared for portfolio, learning, and demonstration purposes.
