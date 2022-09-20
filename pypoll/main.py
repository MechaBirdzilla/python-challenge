import csv
import sys

# define location of csv file
budgetdata_csv = "./Resources/election_data.csv"


def write(line):
    with open("results.txt", "a") as outfile:
        print(line)
        print(line, file=outfile)


# open csv file with "," as delimiter
with open(budgetdata_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # remove header from the data
    header = next(csvreader)

    candidates = {}

    for (id, county, candidate) in csvreader:
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

    total_votes = sum(candidates.values())
    write("Election Results")
    write("---------------------------")
    write("Total Votes: " + str(total_votes))
    write("---------------------------")
    winner = None

    for (name, votes) in candidates.items():

        write((name) + ": " + str(round(votes/total_votes * 100, 2)) +
              "% (" + str(votes) + ")")
        if winner == None or votes > winner[1]:
            winner = (name, votes)

    write("---------------------------")
    write("Winner: " + winner[0])
    write("---------------------------")
