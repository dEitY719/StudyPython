source_file_list = ['AAA.c.o', 'BBB.o', 'CCC.c.o', 'DDD.c.obj', 'EEE.o', 'FFF.c.o']
converted_file_list = []

for filename in source_file_list:
    # 파일 확장자를 추출합니다.
    extension = filename.split('.')[-1]

    # 파일 이름에서 마지막 두 부분(확장자 포함)을 제거하고, ".s" 확장자를 추가합니다.
    new_filename = filename.rsplit('.', 2)[0] + '.s'

    # 변환된 파일 이름을 converted_file_list에 추가합니다.
    converted_file_list.append(new_filename)

print(converted_file_list)
