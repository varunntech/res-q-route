from flask import Flask, render_template, request

from dijkstra import dijkstra, find_all_routes


app = Flask(__name__)


# Road network
graph = {

    "Ambulance Station": [
        ("Main Road", 4),
        ("City Road", 2)
    ],

    "Main Road": [
        ("Ambulance Station", 4),
        ("Hospital Road", 3)
    ],

    "City Road": [
        ("Ambulance Station", 2),
        ("Hospital Road", 5)
    ],

    "Hospital Road": [
        ("Main Road", 3),
        ("City Road", 5),
        ("City Hospital", 2)
    ],

    "City Hospital": [
        ("Hospital Road", 2)
    ]
}


@app.route("/", methods=["GET", "POST"])
def home():

    distance = None
    path = None
    start = None
    end = None
    time = None
    all_routes = None

    if request.method == "POST":

        start = request.form["start"]
        end = request.form["end"]

        distance, path = dijkstra(graph, start, end)
        all_routes = find_all_routes(graph, start, end)

        # Average ambulance speed = 40 km/hour
        time = (distance / 40) * 60

    locations = list(graph.keys())

    return render_template(
        "index.html",
        locations=locations,
        distance=distance,
        path=path,
        start=start,
        end=end,
        time=time,
        all_routes=all_routes
    )


if __name__ == "__main__":
    app.run(debug=True)