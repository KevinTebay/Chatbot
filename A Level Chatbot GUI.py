import tkinter as tk

# Dictionary for responses
qanda = {
    "assess": "The course is assessed by exams. You will take 2 exams in year 12 and 2 exams in year 13. There's a coding exam on computer, but no essays.",
    "assessment": "The course is assessed by exams. You will take 2 exams in year 12 and 2 exams in year 13. There's a coding exam on computer, but no essays.",
    "career": "Virtually every industry needs computer scientists and the requirements continue to grow from robotics, games design through to competitor analysis and social marketing",
    "code": "We will learn Python as the main programming language.",
    "demand": "Even though there are now more computer scientists entering the job market there is much greater demand for these graduates!",
    "development": "In computer science you will learn how to develop programs/video games/apps.",
    "difference": "Not only can you help charities with their web-presence and fund raising, you can help Open Source projects make a massive difference to millions of lives.",
    "difficult": "It's no more difficult than any other respected A-level.",
    "easy": "It's no more difficult than any other respected A-level. However, most of my students say it is much easier than Maths or Psychology.",
    "exams": "The course is assessed by exams. You will take 2 exams in year 12 and 2 exams in year 13. There's a coding exam on computer, but no essays.",
    "fun": "Yes, it is, according to my year 12 and 13 students.",
    "game": "In CS we will show you the coding and tools to make games.",
    "grade": "Grades are very good in CS, but what's even better are the amazing university offers! CS students from Garden are being offered lower grade tariffs at a wide range of prestigious universities.",
    "hack": "You will be given knowledge that will enable hacking, but we also teach you the ethics so that you are a WHITE hat.",
    "language": "You will learn the Python programming language.",
    "learn": "You will study coding in Python and how computers work. You can also ask about the units we will study.",
    "module": "Your units will include: internet technologies, hardware, security, privacy and data integrity, ethics, databases, programming, and problem solving.",
    "paid": "Computer Science is the best paying degree out of university.",
    "pay": "Computer Science is the best paying degree out of university.",
    "portfolio": "You will get the opportunity to make projects that you can use for Extended Project and to help you get into a great university.",
    "Scratch": "Occasionally we will use Scratch to see how an algorithm works.",
    "study": "Your units will include: internet technologies, hardware, security, privacy and data integrity, ethics, databases, programming, and problem solving.",
    "syllabus": "The syllabus for this course is available at https://drive.google.com/file/d/1CsUYvgH9qYJTO7bdWM6nuJkrNzuMsdId/view",
    "syntax": "What is the meaning of life?",
    "unit": "Your units will include: internet technologies, hardware, security, privacy and data integrity, ethics, databases, programming, and problem solving.",
    "why": "Computer science is the best paid career, you can make the most difference and it's very enjoyable.",
    "who": "Mr Abela & Mr Tebay will be teaching the A-level.",
    "job": "Some common jobs you can do with a computer science degree include: Software Developer, Data Scientist, Artificial Intelligence Engineer, Cybersecurity Analyst, Cloud Engineer, DevOps Engineer, Blockchain Developer, Quantum Computing Specialist, IoT Engineer, Augmented Reality/Virtual Reality Developer, Bioinformatics Scientist, Game Developer, Robotics Engineer, Network Architect, Technical Writer, Ethical Hacker, E-commerce Analyst, Human-Computer Interaction Designer, Healthcare Informatics Specialist, and Educational Technologist. Many other jobs in the 2030s will require a knowledge of AI.",
    "wef": "The World Economic Forum produced this report on jobs in 2030. https://www3.weforum.org/docs/WEF_Future_of_Jobs_2023.pdf",
    "ai": "Artificial Intelligence is a big part of modern computer science. We’ll look at some fundamentals and applications that are transforming industries.",
    "algorithm": "Algorithms are step-by-step instructions for solving problems, and you’ll learn how to design and analyze them as a core skill in CS.",
    "application": "CS has applications in many fields, from healthcare to finance, gaming to social media. We focus on coding and problem-solving to equip you with versatile skills.",
    "career_advancement": "With CS, you can advance in fast-growing fields like AI, cybersecurity, and data science, each offering high-paying jobs and diverse career paths.",
    "collaborate": "Collaboration is essential in CS, whether working in teams to code a program or brainstorming solutions. Group projects will help you develop these skills.",
    "cybersecurity": "Cybersecurity is an exciting area in CS. You’ll gain basic knowledge of protecting systems and the ethical considerations around data security.",
    "databases": "You’ll learn about databases in this course, including how they store, organize, and manage data in applications like social media and e-commerce.",
    "degree": "A degree in CS opens doors to many tech-related fields, but it’s also a great foundation for careers in fields like finance, law, and even medicine.",
    "entrepreneur": "CS skills are perfect for aspiring entrepreneurs, as you'll learn how to build and develop ideas into apps or even businesses.",
    "ethics": "Ethics in CS covers topics like privacy, data integrity, and responsible technology use. We aim to prepare you to be responsible digital citizens.",
    "future": "The future in tech is full of opportunity, with advancements in AI, quantum computing, and more. CS is at the heart of these exciting fields.",
    "hardware": "We’ll study hardware basics, including how computers process information and interact with software, which is crucial knowledge for all CS fields.",
    "innovation": "Innovation is at the heart of CS. You’ll learn to design and create, tackling real-world problems with innovative thinking and coding skills.",
    "internship": "Internships in tech are widely available and provide valuable experience. Many companies seek CS students for positions in development and analysis.",
    "project": "You’ll have the chance to work on projects that demonstrate your programming skills, which are great additions to your portfolio.",
    "robotics": "CS includes areas like robotics, where programming and hardware meet. It’s a fascinating field that combines coding with engineering.",
    "salary": "CS graduates often have some of the highest starting salaries, thanks to the demand for skills in AI, cybersecurity, and software development.",
    "social_impact": "CS skills allow you to make a positive impact, from working on environmental projects to improving healthcare systems with better data management.",
    "software": "You’ll learn to create software in this course, developing programs that solve real problems and exploring fields like web and app development.",
    "study_tips": "Regular practice with coding problems and reviewing key concepts are essential for success in CS. Remember, consistent effort makes all the difference!",
    "technology": "You’ll get to learn about the latest in technology trends, from AI to blockchain, and explore how these innovations are shaping the future.",
    "web": "Web development is one of the key applications of CS skills. We cover the basics of creating and managing websites, which is a useful and in-demand skill."
}

# Function to process questions
def questionprocess(sentence):
    sentence = sentence.strip("?")
    for word in sentence.split():
        if word[0:-1].lower() in qanda.keys():
            return qanda.get(word[0:-1].lower())
        elif word[0:-2].lower() in qanda.keys():
            return qanda.get(word[0:-2].lower())
        elif word[0:-3].lower() in qanda.keys():
            return qanda.get(word[0:-3].lower())
        elif word[0:-3].lower() + "e" in qanda.keys():
            return qanda.get(word[0:-3].lower() + "e")
        elif word.lower() in qanda.keys():
            return qanda.get(word.lower())
    return "Sorry, I'm not the smartest chatbot... Perhaps ask Mr Tebay or Mr Abela."

# Function to display response
def get_response():
    question = entry.get()
    response = questionprocess(question)
    response_text.config(state="normal")  # Enable text widget for editing
    response_text.insert(tk.END, "You: " + question + "\n")
    response_text.insert(tk.END, "Chatbot: " + response + "\n\n")
    response_text.config(state="disabled")  # Disable text widget after editing
    entry.delete(0, tk.END)  # Clear the entry box

# Initialize Tkinter window
root = tk.Tk()
root.title("CS Chatbot")
root.geometry("500x500")

# Chat log display
response_text = tk.Text(root, wrap="word", height=20, state="disabled")
response_text.pack(pady=10)

# Entry widget for typing questions
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Send button
send_button = tk.Button(root, text="Ask", command=get_response)
send_button.pack(pady=5)

# Display welcome message
response_text.config(state="normal")
response_text.insert(tk.END, "_________   _________ _________ .__            __ ___.           __\n")
response_text.insert(tk.END, "\_   ___ \ /   _____/ \_   ___ \|  |__ _____ _/  |\_ |__   _____/  |_\n")
response_text.insert(tk.END, "/    \  \/ \_____  \  /    \  \/|  |  \\__  \\   __\ __ \ /  _ \   __\n")
response_text.insert(tk.END, "\     \____/        \ \     \___|   Y  \/ __ \|  | | \_\ (  <_> )  |\n")
response_text.insert(tk.END, " \______  /_______  /  \______  /___|  (____  /__| |___  /\____/|__|\n")
response_text.insert(tk.END, "       \/        \/          \/     \/     \/         \/\n\n")
response_text.insert(tk.END, "Welcome to the CS Chatbot! Ask me anything about A-level Computer Science.\n\n")
response_text.config(state="disabled")

root.mainloop()
