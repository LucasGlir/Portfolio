def e_dist(s1,s2,m,n):
	if m==0:
		return n
	if n==0:
 		return m
	if s1[m-1] == s2[n-1]:
		return e_dist(s1,s2,m-1,n-1)
	return 1 + min(e_dist(s1,s2,m,n-1), e_dist(s1,s2,m-1,n), e_dist(s1,s2,m-1,n-1))


s1 = input()
s2 = input()
print(e_dist(s1,s2,len(s1),len(s2)))
