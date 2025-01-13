import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# Load the dataset and add decade column
df = pd.read_csv("spotify_data.csv")

def decade_function(year):
    return (year // 10) * 10
df["decade"] = df["year"].apply(decade_function)

# Function for random tracks
def random_track_analysis():
    random_index = random.randint(0, len(df) - 1)
    random_track = df.iloc[random_index]

    # Track details
    track_name = random_track["name"]
    track_artist = random_track["artists"]
    track_year = random_track["year"]
    track_danceability = random_track["danceability"]
    track_energy = random_track["energy"]
    track_popularity = random_track["popularity"]

    # Print track details
    print(f"Random Track: {track_name} by {track_artist}")
    print(f"Year: {track_year}")
    print(f"Danceability: {track_danceability}, Energy: {track_energy}, Popularity: {track_popularity}")

if __name__ == "__main__":
    random_track_analysis()