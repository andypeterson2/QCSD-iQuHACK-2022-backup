# Quantum Dice

A simple single player vs (quantum) house game in which a player bets higher or lower against a truly random dice

# Background

Of the 5 competitiors on this team, involvement was only shown by 3... all of which had never done a hackathon before. We are tired and we are beginners, so we have abandoned our original project in favor of this one for
  1. Time's sake
  2. Our sanity

In this process we have learnd a lot and would like to continue the previous project, but it would be very difficult for us given the circumstances. MIT iQuHACK will definitely be something prepared for more greatly in the future and will be a recoccurring thing for QCSD.

The previous project was as follows:
  >An adaptation of Amit Patel's [mapgen2](https://github.com/redblobgames/mapgen2/) using quantum hardware for randomness. Inspired by [Amit Patel](https://twitter.com/redblobgames)'s article [Polygonal Map Generation for Games](http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation), we sought to reimagine and remake this project in Python and utilize the inherent properties of quantum hardware which allow for creating true randomness.

# Setup

Make sure you have conda installed and run the two following commands

```bash
conda create -n q-dice -c microsoft qsharp

conda activate q-dice
```

To run the game, just run the following:

```bash
python main.py
```