print("두 수를 입력하시오.")
a,b = input().split() 
a,b = int(a), int(b)
x,y = a,b

while x%y!= 0:
	temp = x%y
	x = y
	y = temp 
#while 문 실행 결과, x와 y의 최대공약수 y에 대입.

ablcm =a*b//y 
#a와 b의 곱을 a와 b의 최대공약수로 나누어 a와 b의 최소공배수 구함

print(ablcm)


