import my_package

# 패키지 초기화 메시지가 출력됩니다.
# "my_package 패키지가 초기화되었습니다."

# 패키지 내 모듈 함수 호출
my_package.module_a.function_a()  # "function_a from module_a"
my_package.module_b.function_b()  # "function_b from module_b"

# 패키지 수준의 변수 사용
print(my_package.package_variable)  # "이 변수는 my_package 전체에서 사용 가능합니다."

# 패키지 공용 함수 호출
my_package.common_function()  # "my_package의 공용 함수입니다."