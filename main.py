def solution(a):
	binary_format = bin(a)
	list_of_1 = [i for i, x in enumerate(binary_format) if x == '1']
	c = 0
	for item in list_of_1[:len(list_of_1) - 1]:
		next_item = list_of_1[list_of_1.index(item) + 1]
		distance = abs(item - next_item) - 1
		if distance >= 1 and distance > c:
			c = distance
	return c


result = solution(129)
print(result)
