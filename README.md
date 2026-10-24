🚑 ResQRoute — Ambulance Shortest Path Finder
ResQRoute is a Python-based ambulance route-finding project that demonstrates how graph algorithms can help identify a shortest route between two locations. It includes a command-line version and a Flask-based web interface concept for selecting locations and viewing route results.
📌 Project Overview
In emergency response, choosing an efficient route can help reduce travel distance. ResQRoute models a small road network as a graph, where locations are nodes and roads are weighted edges representing distance in kilometres.

The project demonstrates:
- Finding a shortest path with Dijkstra's algorithm
- Exploring possible routes with Depth-First Search (DFS)
- Comparing routes by distance and number of hops
- Estimating travel time using an assumed average speed
- Presenting route information through a command-line interface and a web UI
Important: This is an academic/demo project using a predefined sample road network. It does not use live maps, real traffic, GPS, or emergency-service data and should not be used for real emergency navigation.

✨ Features
- Shortest Route Calculation — Uses Dijkstra's algorithm to find a minimum-distance route.
- All Possible Routes — Uses DFS to enumerate routes without repeating a node within a route.
- Route Comparison — Sorts routes by distance and identifies the shortest option.
- Distance and ETA — Displays route distance and an estimated travel time based on a fixed assumed speed.
- Location Selection — The Flask app defines sample locations such as Ambulance Station, Main Road, City Road, Hospital Road, and City Hospital.
- Web Interface — Includes a dark-themed HTML interface with origin/destination selectors, route steps, distance, ETA, stops, and route comparisons.
- Input Validation — The command-line version checks node IDs and prevents selecting the same source and destination.
🛠️ Technologies Used
- Python 3
- Flask — Web application framework
- HTML, CSS, JavaScript — Web interface
- heapq — Priority queue for Dijkstra's algorithm
- Graph Algorithms — Dijkstra's shortest path and DFS route enumeration
🧠 Algorithms Used
1. Dijkstra's Algorithm
Dijkstra's algorithm finds the shortest path in a graph with non-negative edge weights. It maintains the best known distance to each node and uses a priority queue to process the closest unprocessed node.

Used for: Calculating the minimum-distance route between a source and destination.
2. Depth-First Search (DFS)
DFS explores paths by visiting connected nodes while avoiding nodes already present in the current path. When it reaches the destination, it records that route and its total distance.

Used for: Listing possible routes and sorting them by distance.

Note: The number of possible routes can grow rapidly as a graph becomes larger, so enumerating every route is intended for this small demonstration network.
📂 Project Structure
A suggested structure for the Flask version is:
ResQRoute/
├── app.py
├── dijkstra.py
├── resqroute.py
├── resqroute_ui.html
├── templates/
│   └── index.html
├── static/
│   └── ambulance_bg.jpg       # Optional background image used by the UI
├── Run ResQRoute.bat          # Windows launcher (expects a local venv)
└── README.md
- app.py — Flask application and sample road network.
- dijkstra.py — Intended location for graph route functions used by the Flask app.
- resqroute.py — Standalone command-line route-finding demonstration.
- resqroute_ui.html — HTML/CSS/JavaScript interface.
- Run ResQRoute.bat — Windows launcher configured to run app.py with venv\Scripts\python.exe.
⚙️ Installation
Prerequisites
- Python 3.10 or later recommended
- pip
- A modern web browser (for the web interface)
1. Open the project folder
cd path/to/ResQRoute
2. Create and activate a virtual environment (recommended)
Windows:
python -m venv venv
venv\Scripts\activate
macOS/Linux:
python3 -m venv venv
source venv/bin/activate
3. Install Flask
python -m pip install Flask
▶️ Run the Project
Option A: Command-line version
Run:
python resqroute.py
Enter the source and destination node IDs shown on the screen. The program displays the possible routes, the shortest route, distance, and estimated travel time.
Option B: Flask web version
Run:
python app.py
Then open:
http://127.0.0.1:5000
On Windows, Run ResQRoute.bat is provided as a launcher, provided the expected virtual environment and Flask app files are in place.
⚠️ Setup compatibility note
The uploaded files may need to be aligned before the Flask version runs:
1. app.py imports dijkstra(graph, start, end) and find_all_routes(graph, start, end) from dijkstra.py. Ensure dijkstra.py defines these two functions with signatures and graph format compatible with app.py. The uploaded dijkstra.py currently contains a separate example implementation with a different function signature.
2. Flask's render_template("index.html", ...) expects the page at templates/index.html. The uploaded UI file is named resqroute_ui.html; place the intended page at templates/index.html or update the Flask code to use the matching template.
3. The HTML references static/ambulance_bg.jpg as a background image. This asset is optional for the page's layout, but the background image will not appear unless the file is provided at that path.
🗺️ Sample Road Network
The Flask app uses this sample network:
- Ambulance Station ↔ Main Road: 4 km
- Ambulance Station ↔ City Road: 2 km
- Main Road ↔ Hospital Road: 3 km
- City Road ↔ Hospital Road: 5 km
- Hospital Road ↔ City Hospital: 2 km
For this network, the shortest route from Ambulance Station to City Hospital is:

Ambulance Station → Main Road → Hospital Road → City Hospital

Total distance: 9 km

Using the Flask app's assumed average speed of 40 km/h, estimated travel time is 13.5 minutes. This is a mathematical estimate, not a live traffic prediction.
🔮 Future Improvements
- Use real map data and geospatial road networks.
- Add live traffic and road-closure information.
- Integrate GPS-based location input.
- Add multiple hospitals and ambulance stations.
- Improve handling of unreachable destinations and invalid form inputs.
- Add automated tests for graph algorithms and route calculations.
- Separate configuration, algorithm logic, and UI into maintainable modules.
🎯 Learning Outcomes
This project provides practical experience with:
- Graph representation using adjacency lists
- Shortest-path algorithms and priority queues
- DFS and path enumeration
- Python functions and modular code
- Flask routes and HTML templates
- Displaying algorithm results in a user interface
Project: ResQRoute — Ambulance Shortest Path Finder
Category: Graph Algorithms / Emergency Route Planning Demo
Languages: Python, HTML, CSS, JavaScript
