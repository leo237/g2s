import csv
with open('train.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		part = []
		for num in row:
			x = format(round(float(num),4))
			part.append(x)
		with open('training.csv', 'a') as writefile:
			csvWriter = csv.writer(writefile)
			csvWriter.writerow(part)