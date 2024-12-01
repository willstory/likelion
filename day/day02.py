name = "홍길동"
intreduce = "안녕하세요"
print("저는 %s 입니다. %s" % (name, intreduce))


fruit = ["사과", "바나나", "체리"]
result = "," .join(fruit)
print(result)

scores = {"국어": 90, "영어": 85, "수학": 95}

print("국어점수 :", scores["국어"])
print("영어점수 :", scores["영어"])
print("수학점수 :", scores["수학"])


text = "  Python Programming Language  "
text = text.strip()
text = text.replace(" ", "")
print(text.upper())

pnumbers = [10, 20, 30, 40, 50, 60, 70, 80]

number = pnumbers[0::2]
print(number)

coordinates = (100, 200, 300)
a, b, c = coordinates
print("x :", a)
print("y :", b)
print("z :", c)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
