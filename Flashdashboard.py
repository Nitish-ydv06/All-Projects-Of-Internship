from flask import Flask

app = Flask(__name__)

base_style = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #1f1c2c, #928dab);
            color: white;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #00e6e6;
            margin-bottom: 20px;
        }
        .container {
            background: rgba(0, 0, 0, 0.4);
            padding: 20px;
            border-radius: 12px;
            width: 70%;
            margin: auto;
        }
        a {
            text-decoration: none;
            color: #ffcc00;
            font-size: 18px;
        }
        a:hover {
            color: #ffffff;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            padding: 8px;
            margin: 10px;
        }
        .btn {
            display: inline-block;
            background-color: #ffcc00;
            color: #000;
            padding: 10px 18px;
            border-radius: 8px;
            margin-top: 20px;
            font-weight: bold;
        }
        .btn:hover {
            background-color: #ffe680;
        }
        .section-title {
            color: #ffcc00;
            font-size: 24px;
            margin-top: 25px;
        }
    </style>
"""

@app.route("/")
def home():
    return f"""
    {base_style}
    <div class='container'>
        <h1>Welcome to My Portfolio</h1>
        <p>Hello! I'm <b>Nitish Yadav</b>, a Tech Student and Creative Video Editor.</p>
        <ul>
            <li><a href='/resume' class='btn'>View Resume</a></li>
            <li><a href='/projects' class='btn'>View Projects</a></li>
        </ul>
    </div>
    """

@app.route("/resume")
def resume():
    return f"""
    {base_style}
    <div class='container'>
        <h1>Digital Resume</h1>
        
        <div class='section-title'>Personal Details</div>
        <p><b>Name:</b> Nitish Kumar </p>
        <p><b>Goal:</b> Crack Internship at Microsoft by 4th Semester ✔</p>

        <div class='section-title'>Skills</div>
        <ul>
            <li>Python, HTML, CSS, JavaScript (Learning)</li>
            <li>Git & GitHub</li>
            <li>Video Editing</li>
            <li>Linux (Kali Linux Basics)</li>
        </ul>

        <div class='section-title'>Education</div>
        <p>B.Tech – Computer Science Engineering (2024–2028)</p>
        <p>Vivekananda Global University, Jaipur</p>

        <div class='section-title'>Achievements</div>
        <ul>
            <li>Built air quality monitoring system prototype</li>
            <li>Led sustainability project on food waste</li>
            <li>Hackathon participation & project development</li>
        </ul>

        <div class='section-title'>Contact</div>
        <p>Email: <a href="mailto nitishyadav">email</a></p>

        <a href='/' class='btn'>Back to Home</a>
    </div>
    """

@app.route("/projects")
def projects():
    return f"""
    {base_style}
    <div class='container'>
        <h1>My Projects</h1>
        <ul>
            <li>Air Quality Monitoring System using IoT</li>
            <li>Community Sustainability Platform (Hackathon)</li>
            <li>Food Waste Management Research Project</li>
            <li>Voice-Controlled Virtual Assistant (Python)</li>
            <li>Video Editing Showreel</li>
        </ul>
        <a href='/' class='btn'>Back to Home</a>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=False)
