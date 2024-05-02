#Armaghan and Areeb
# PA 9
##########

import math
import networkx as nx
import matplotlib.pyplot as plt
import pandas
import pandas as pd

# load data and split into columns
movies= pd.read_csv("/Users/armaghanejaz/Downloads/actionMovies2006.txt", header=None, sep='|',names=['Movie', 'Actors'])


# function to format names
def format_actor_names(actor_names_str):
    # Split the string to separate individual actors
    actors_list = actor_names_str.split('/')
    formatted_names = []  # Initialize an empty list

    # Iterate over each name in the list
    for name in actors_list:
        # Check if the name contains a comma
        if ',' in name:
            # Name contains a comma, proceed with splitting
            last_name, first_name = name.split(', ')
            # Format name as "First Name Last Name" and add to the list
            formatted_name = f"{first_name} {last_name}"
        else:
            # Name does not contain a comma, use it as is
            formatted_name = name
        formatted_names.append(formatted_name.strip())  # Strip whitespace and add to list

    return formatted_names

# Function to obtain the names of the movies
def print_path_details(G, path):
    print("Shortest path:")
    # Loops through each actor in our chosen graph and obtains movies that link them
    for i in range(len(path) - 1):
        actor1 = path[i]
        actor2 = path[i + 1]
        movies = G[actor1][actor2]['movies']  # Retrieve the list of movies from the edge
        # prints out the names
        print(f"{actor1} -> {actor2} through movie(s): {', '.join(movies)}")
    print(f"Total path length (number of movies): {len(path) - 1}")





# Apply the function to each row in the 'Actors' column
movies['Actors'] = movies['Actors'].apply(format_actor_names)

print(movies.head())

# initialize graph
G = nx.Graph()

# Iterate over each row process each movie
for index, row in movies.iterrows():
    actors = row['Actors']  # Get the list of actors for the current movie
    movie = row['Movie']  # Get the movie title

    # Add nodes for each actor if they do not exist already
    for actor in actors:
        if actor not in G:
            G.add_node(actor)

    # Add edges between all pairs of actors in this movie
    for actor1 in actors:
        for actor2 in actors:
            if actor1 != actor2:  # Ensure we're not creating a loop
                # Add an edge between actor1 and actor2 with the movie as the edge
                if G.has_edge(actor1, actor2):
                    # If the edge already exists, append this movie to the list of movies they've co-starred in
                    G[actor1][actor2]['movies'].append(movie)
                else:
                    # Otherwise create new edge
                    G.add_edge(actor1, actor2, movies=[movie])

actor1 = "George Peppard"
actor2 = "Kevin Bacon"

# Find and print the shortest path and its length
try:
    path = nx.shortest_path(G, source=actor1, target=actor2) # obtain Shortest path
    print(f"Shortest path between {actor1} and {actor2}:") # Print the details by calling the function
    print_path_details(G, path)
except nx.NetworkXNoPath:
    print(f"No path between {actor1} and {actor2}")

actor1 = "Robert Downey Jr."
actor2 = "Charlie Brewer"

# Find and print the shortest path and its length
try:
    path = nx.shortest_path(G, source=actor1, target=actor2) # obtain shortest path
    print(f"Shortest path between {actor1} and {actor2}:") # Print the details by calling the function
    print_path_details(G, path)
except nx.NetworkXNoPath:
    print(f"No path between {actor1} and {actor2}")

actor1 = "Tom Cruise"
actor2 = "Angelina Jolie"

# Find and print the shortest path and its length
# Find and print the shortest path and its length
try:
    path = nx.shortest_path(G, source=actor1, target=actor2) # obtain shortest path
    print(f"Shortest path between {actor1} and {actor2}:") # Print the details by calling the function
    print_path_details(G, path)
except nx.NetworkXNoPath:
    print(f"No path between {actor1} and {actor2}")

