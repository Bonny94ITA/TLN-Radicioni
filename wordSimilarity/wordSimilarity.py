import metrics
import csv
import pandas as pd
from nltk.corpus import wordnet as wn
import numpy as np

simLabels = ["Means", "WuPalmer", "shortestPath", "LeacockChodorow"]

def read_file():
	list = []
	with open("./asset/WordSim353.csv") as tsv:
		for line in csv.reader(tsv, delimiter=','):
			list.append(line)
	list.pop(0)
	return list


def get_synsets(item):
	return wn.synsets(item[0]), wn.synsets(item[1])


def computeSimilarity(item, metric):
	senses1, senses2 = get_synsets(item)

	max_similarity = 0.0

	for sense1 in senses1:
		for sense2 in senses2:
			similarity = metric(sense1, sense2)

			if similarity is not None:
				if max_similarity < similarity:
					max_similarity = similarity
	return max_similarity


def computeCorrelations(correlations):
	df = pd.DataFrame(correlations)

	corrs = []
	corrs.append(["Pearson", df.corr()])
	corrs.append(["Spearman", df.corr(method='spearman')])
	return corrs


def printCorrelations(cors):
	text = "CORRELATIONS:\n"
	for cor in cors:
		# outputfile.write("\tWuPalmer: "+sim+" Pearson:"+correlations[0].upper+"\n")
		text += cor[0] + ": \n" + str(cor[1]) + "\n"
	return text + "\n"


def initCorr():
	correlations = {}
	correlations["Means"] = []
	correlations["WP"] = []
	correlations["SP"] = []
	correlations["LC"] = []
	return correlations


def printSimilarity(correlations, words):
	text = ""

	valuesList = list(correlations.values())

	matrix = np.array(valuesList)

	matrix = matrix.transpose()
	
	for r, row in enumerate(matrix):
		text+=words[r][0].upper()+" "+words[r][1].upper()+":\n"		
		for c, col in enumerate(row):
			text += "\t"+simLabels[c]+": "+str(col)+"\n"
		text+="\n"
	
	return text+"\n\n"

def main():
	list = read_file()

	correlations = initCorr()

	with open(("./asset/output.txt"), 'w') as outputfile:
		for item in list:       

			correlations["WP"].append(computeSimilarity(item, metrics.wup_similarity))
			correlations["SP"].append(computeSimilarity(item, metrics.shortestPath))
			correlations["LC"].append(computeSimilarity(item, metrics.LeacockChodorow))
			correlations["Means"].append(float(item[2]))						
		
		outputfile.write(printSimilarity(correlations, list))
		
		corr = computeCorrelations(correlations)
		
		outputfile.write(printCorrelations(corr))


if __name__ == '__main__':
	main()
