from flask import Flask, render_template
from config.links import SOCIAL_LINKS

app = Flask(__name__)

@app.route('/')
def home():
    # Data that will be passed to the template
    data = {
        'name': 'Chaitanya Kulkarni',
        'title': 'Software Engineer & Data Analyst',
        'location': 'Banglore, India',
        'about': '''Experienced Web Developer and Power BI specialist with a strong focus on data-driven solutions. 
                   Currently advancing towards expertise in Data Science and Artificial Intelligence.''',
        'experience': [
            {
                'company': 'Snowman Logistics Pvt Ltd',
                'position': 'Graduate Engineer Trainee',
                'period': '2024 - Current',
                'description': '''Worked on building internal tools for the company in Python,
                Java . Contributed to the development of a web application for the company in React,
                Node.js, for internal business operations 
                leveraged my skills in data analysis to build dashboards for the company , to track 
                the performance of the company and to make data driven decision.
                ''',
                'technologies': ['React', 'Mysql', 'Spring Boot/Java','Python','Power BI']
            },
           
            # Add more experience entries here
        ],
        'projects': [
            {
                'name': 'Consultly',
                'description': 'A platform to build and grow your online business',
                'technologies': ['Java', 'Spring Boot', 'Mysql',]
            },
            {
                'name': 'M',
                'description': 'Browser extension that records everything happening in web application',
                'technologies': ['TypeScript', 'Browser Extension']
            }
            # Add more projects here
        ],
        'skills': ['Python', 'Java', 'React/Node.js', 'Mysql', 'Spring Boot/Java', 'C/C++'],
        'education': [
            {
                'college': 'Jain University',
                'degree': 'Master of Computer Applications',
                'period': '2024 - 2026',
                'description': 'Completed B.E. in Computer Engineering with focus on software development and data structures. Participated in various technical competitions and workshops.',
                'courses': ['Data Structures', 'Algorithms', 'Database Management', 'Web Development']
            },
            {
                'college': 'Acharya Institute of Technology',
                'degree': 'Bachelor In Computer Applications',
                'period': '2019 - 2022',
                'description': 'Completed BCA with focus on Computer Science',
                'courses': ['Physics', 'Chemistry', 'Mathematics']
            },
            {
                'college': 'Acharya Institute of Technology',
                'degree': 'Bachelor In Computer Applications',
                'period': '2019 - 2022',
                'description': 'Completed BCA with focus on Computer Science',
                'courses': ['Physics', 'Chemistry', 'Mathematics']
            }
        ]
    }
    return render_template('index.html', data=data, social_links=SOCIAL_LINKS)

if __name__ == '__main__':
    app.run(debug=True) 