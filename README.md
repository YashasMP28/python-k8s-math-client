🌐 Python Kubernetes Math Client (Invoker)
📌 Project Overview
This project implements a Python client application that interacts with the Kubernetes workload (math-evaluator) deployed on Minikube.
It sends math expressions, invokes the workload, and retrieves results.


🚀 Features

Acts as a client-side invoker for the math evaluator workload.
Written in Python with clean modular structure.
Communicates with Kubernetes Job using kubectl.
Lightweight, simple, and follows Twelve-Factor App principles.


📂 Project Structure
bash
Copy code
k8s-math-client/
│── client.py          # Python client to invoke the workload
│── requirements.txt   # Python dependencies
└── README.md          # Project documentation


🛠️ Technologies Used

Python 3.10
kubectl CLI
Kubernetes (Minikube)
Docker
Git + GitHub
VS Code


⚡ Setup Instructions

1️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
2️⃣ Run the Client
bash
Copy code
python client.py "10*(5+2)-3"
3️⃣ Expected Output
vbnet
Copy code
Sending expression to Kubernetes workload...
Expression: 10*(5+2)-3
Result: 67


📖 Example Workflow

Client runs client.py "math expression".
Client creates a Kubernetes Job based on workload image.
Workload executes the expression and outputs the result.
Client fetches Job logs and displays the result back to the user.


📌 Project Requirements Reference

Separate project for the client app.
Invokes workload running in Minikube Kubernetes Job.
Follows Twelve-Factor App principles.
Uses Python virtual environment, GitHub, and VS Code.


👨‍💻 Author
Yashas M.P
