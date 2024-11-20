# CrewAI Agent For Travel Planner

Welcome to the **CrewAI Agent For Travel Planner** repository! This project demonstrates the implementation of a multi-agent AI system designed to collaboratively plan a travel itinerary. The repository showcases the core components of CrewAI and provides an example workflow for a travel planning agent. Below is a detailed guide to understanding, installing, and running the code.

![Crew AI Architecture](/resources/crew_ai_arc.png)

---

## **Repository Overview**

This repository implements a **travel planner** using CrewAI principles. It highlights five key components:

1. **Agents**: Independent AI entities designed to perform specific tasks.
2. **Tasks**: Defined objectives for each agent to execute.
3. **Tools**: Functional modules that agents use to accomplish tasks.
4. **Process**: The sequential or coordinated execution of tasks.
5. **Crew**: The overarching manager that orchestrates agents, tasks, tools, and processes.

### **How the Travel Planner Works**

The system simulates a team of AI agents collaborating to plan a trip. It performs the following steps:
1. **Destination Analysis**: Identifying suitable destinations based on user preferences.
2. **City Guide Compilation**: Providing detailed insights about a chosen destination.
3. **Itinerary Creation**: Generating a structured day-by-day itinerary.


![Travel Planner Architecture](/resources/travel_planner_ai_agent.png)

### **Key Files and Their Roles**

- **`agents.py`**: Defines the three agents:
  - **Destination Analyst Agent**: Suggests and evaluates travel destinations.
  - **City Guide Agent**: Provides comprehensive information about a selected city.
  - **Itinerary Agent**: Plans the day-to-day activities for the trip.
  
- **`tasks.py`**: Contains the tasks for the agents, with each agent responsible for one specific task:
  - Analyze destinations.
  - Create a city guide.
  - Generate an itinerary.

- **`tools/`**: Includes tools that agents use to solve their tasks:
  - **Search Tool**: Performs searches for destination data.
  - **Browser Tool**: Retrieves additional online resources.
  - **Calculator Tool**: Assists with budgeting and distance calculations.

- **`main.py`**: The entry point of the application. It:
  - Initializes agents, tasks, and tools.
  - Defines the **process** (the sequential flow of tasks).
  - Leverages the **Crew** to manage the entire process.

---

## **Installation and Setup**

Follow the steps below to set up and run the application:

### **Prerequisites**
- Python 3.8 or later
- OpenAI API Key (add to `.env` file)

### **Steps to Install**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/trojrobert/crewai_agent_demo.git
   cd crewai_agent_demo
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

6. **Run the Application**
   ```bash
   python main.py
   ```

---

## **Understanding CrewAI**

CrewAI is a framework designed to orchestrate collaborative AI systems. It structures problem-solving into the following components:

- **Agents**: Autonomous AI entities with specific roles.
- **Tasks**: Defined objectives that guide agents' actions.
- **Tools**: Functional modules that enhance agents' capabilities.
- **Process**: A workflow or sequence of actions for solving complex problems.
- **Crew**: A manager that ensures effective coordination between agents, tasks, tools, and processes.

### **Example Workflow: Travel Planning**

1. **Agents** perform tasks with assigned tools.
2. **Tasks** are executed sequentially or in parallel, as defined in the **process**.
3. **Tools** like search, browser, and calculator enhance the agents’ problem-solving abilities.
4. The **Crew** coordinates the entire workflow, ensuring agents interact effectively to achieve the travel planning goal.

---

## **How the Travel Planner Example Works**

- The **Crew** initializes agents, tasks, and tools, assigning the appropriate resources to each agent.
- The **Process** begins by:
  1. Running the **Destination Analyst Agent** to recommend destinations.
  2. Utilizing the **City Guide Agent** to gather detailed insights on the chosen destination.
  3. Engaging the **Itinerary Agent** to build a day-by-day plan.
- The results are output sequentially to form a complete travel plan.

---

## **Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Submit a pull request for review.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Support**

For questions or issues, feel free to open an issue in the repository or contact the author via GitHub.

Happy coding! 🌍✨
