Code for GSoC application - Debian.

MATPLOTLIB:

matplotlib/vcs_graph.py -

The VCS-graph.py retrieves all values stored in the table 'history.sources_count' and plots a single graph that is "Number of packages vs Date". The graph is labelled accordingly.

matplotlib/graphs.py plots -

3 graphs: 
(a) Number of packages in each distribution (pie chart) 
(b) Number of bugs in each type of severity (pie chart) 
(c) Number of bugs modified each year (bar chart).

FLOT

Graph plotted: Number of bugs modified each year (bar chart)

flot with json:

create_json.py fetches data from the database and dumps it in data.json, test_json.html reads the data and plots a bar chart using flot.

flot with csv:

create_csv.py fetches data from the database and creates data_csv.csv, test_csv.html reads the data and plots a bar chart using flot.


-- Haven't fixed overlapping labels.
