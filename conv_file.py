import os
from datetime import datetime

def load_conversion_rules(file_path):
    """
    변환 규칙 파일을 읽어와 규칙 리스트를 반환합니다.

    Parameters:
    - file_path (str): 변환 규칙 파일의 경로

    Returns:
    - rules (list): 변환 규칙을 담은 리스트
    """
    rules = []
    with open(file_path, 'r') as f:
        for line_number, line in enumerate(f, start=1):
            parts = line.split()
            if len(parts) == 2:
                before, after = parts
                after = after.rstrip("\n")
                rules.append([before, after, line_number])
            else:
                print(f"해당 줄을 건너뜁니다: {line.strip()} - 올바르지 않은 형식")
    return rules

def find_duplicate_rules(rules):
    """
    중복된 변환 규칙을 찾아 리스트로 반환합니다.

    Parameters:
    - rules (list): 변환 규칙 리스트

    Returns:
    - duplicates (list): 중복된 변환 규칙을 담은 리스트
    """
    unique_rules = set()
    duplicates = []

    for before, after, line_number in rules:
        if (before, after) in unique_rules:
            duplicates.append((before, after, line_number))
        else:
            unique_rules.add((before, after))

    return duplicates

def validate_conversion_rules(rules):
    """
    중복된 변환 규칙을 검증하고 중복된 경우 경고를 출력합니다.

    Parameters:
    - rules (list): 변환 규칙 리스트

    Returns:
    - is_valid (bool): 변환 규칙이 중복되지 않았는지 여부
    """
    duplicates = find_duplicate_rules(rules)
    is_valid = len(duplicates) == 0

    for duplicate in duplicates:
        before, after, line_number = duplicate
        print(f"경고: 중복된 변환 규칙 - {before} {after} (라인번호: {line_number})")

    return is_valid

def convert_file(file_path, conversion_rules, output_directory):
    """
    대상 파일을 변환하고 변환된 내용을 새 파일에 저장합니다.

    Parameters:
    - file_path (str): 대상 파일의 경로
    - conversion_rules (list): 변환 규칙 리스트
    - output_directory (str): 출력 파일이 생성될 디렉토리 경로
    """
    with open(file_path, 'r') as f1:
        output_file_name = "{}_conv.c".format(os.path.splitext(os.path.basename(file_path))[0])
        output_file_path = os.path.join(output_directory, output_file_name)
        
        with open(output_file_path, 'w') as f2:
            for line in f1:
                for before, after, _ in conversion_rules:  # _는 line_number를 무시하기 위해 사용됩니다.
                    line = line.replace(before, after)
                f2.write(line)


def generate_target_files(directory, extension=".c", exclude_pattern="_conv.c"):
    """
    지정된 디렉토리에서 대상 파일 목록을 생성합니다.

    Parameters:
    - directory (str): 대상 파일을 찾을 디렉토리 경로
    - extension (str): 대상 파일의 확장자 (기본값: ".c")
    - exclude_pattern (str): 제외할 파일의 패턴 (기본값: "_conv.c")

    Returns:
    - target_files (list): 대상 파일 경로를 담은 리스트
    """
    target_files = []
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for file in filenames:
            _, file_extension = os.path.splitext(file)
            if file_extension == extension and not file.endswith(exclude_pattern):
                target_files.append(os.path.join(dirpath, file))
    return target_files

def main():
    directory = '/home/silkwave/apps/python'
    today_date = datetime.today().strftime('%Y%m%d')
    output_directory = os.path.join(directory, 'conv', today_date)

    print("output_directory  " + output_directory)
    
    # 출력 디렉토리가 없으면 생성
    os.makedirs(output_directory, exist_ok=True)
    
    # 변환 규칙 로드
    conversion_rules_file = os.path.join(directory, 'fwconv')
    rules = load_conversion_rules(conversion_rules_file)

    # 중복 규칙 검증
    if validate_conversion_rules(rules):
        # 중복이 없으면 변환 규칙을 적용하고 작업을 진행합니다.
        target_files = generate_target_files(directory, exclude_pattern="_conv.c")

        # 대상 파일 변환 반복 처리
        for file_path in target_files:
            print(file_path)
            convert_file(file_path, rules, output_directory)
    else:
        print("변환 규칙에 중복이 있어 작업을 진행할 수 없습니다.")

if __name__ == "__main__":
    main()
