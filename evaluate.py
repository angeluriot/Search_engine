def evaluate(results, expected, epsilon = 10e-8):

	precision = 0.
	recall = 0.
	f_score = 0.

	for i in range(len(results)):
		if results[i] in expected:
			precision += 1.
			recall += 1.

	recall /= float(len(expected))
	precision /= float(len(results))
	f_score = 2. / ((1. / (recall + epsilon)) + (1. / (precision + epsilon)))

	return precision, recall, f_score

def evaluate_all(results, queries):

	precision = 0.
	recall = 0.
	f_score = 0.

	for i in range(len(queries)):
		if len(queries[i].results) != 0:
			p, r, f = evaluate(results[i], queries[i].results)
			precision += p
			recall += r
			f_score += f

	precision /= float(len(queries))
	recall /= float(len(queries))
	f_score /= float(len(queries))

	return precision, recall, f_score
