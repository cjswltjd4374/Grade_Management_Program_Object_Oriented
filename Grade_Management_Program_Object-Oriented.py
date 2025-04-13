##########################
# 프로그램명: 성적처리프로그램 (객체지향 프로그램 버전) 
# 작성자: 소프트웨어학부/2022041023/천지성
# 작성일: 2025.04.13
# 프로그램 설명:  5명의 학생과 각 학생의 세 개의 교과목(영어, C-언어, 파이썬)에 대하여 키보드로부터 입력받아
# 총점, 평균, 학점, 등수를 계산하는 프로그램

class Student:              # 학생들의 정보를 저장하는 클래스
    def __init__(self, stdnum, name, engscr, c_scr, pyscr):
        self.stdnum = stdnum                            # 학생들의 학번을 저장하는 멤버 변수
        self.name = name                                # 학생들의 이름을 저장하는 멤버 변수
        self.engscr = engscr                            # 학생들의 영어 성적을 저장하는 멤버 변수
        self.c_scr = c_scr                              # 학생들의 C언어 성적을 저장하는 멤버 변수
        self.pyscr = pyscr                              # 학생들의 파이썬 성적을 저장하는 멤버 변수
        self.sumtotal = engscr + c_scr + pyscr          # 학생들의 세 과목의 성적의 합을 저장하는 멤버 변수
        self.avg = round(self.sumtotal / 3, 1)          # 학생들의 세 과목의 평균을 소수점 1번째 자리까지 저장하는 멤버 변수
        self.grd = self.score()                         # 학생들의 성적을 계산하는 함수를 멤버 함수로 선언
        self.rnk = 0

    def score(self):                                    # 학생들의 성적을 계산하는 함수, 멤버 변수를 사용하여 기존의 코드를 간략화함
        if self.avg>=90 and self.avg<=100:
            return 'A'
        elif self.avg>=80 and self.avg<90:
            return 'B'
        elif self.avg>=70 and self.avg<80:
            return 'C'
        elif self.avg>=60 and self.avg<70:
            return 'D'
        else:
            return 'F'

class GradeManager:                                     # 성적관리 함수를 저장하는 클래스
    def __init__(self):
        self.students = []                              # 학생 수가 2명이기 때문에 리스트 형태로 선언

    def Input_Value(self):                              # 학생의 학번, 이름, 영어, C언어, 파이썬 성적을 입력받는 함수
        for _ in range(2):
            stdnum = input("학번 : ")
            name = input("이름 : ")
            engscr = int(input("영어 : "))
            c_scr = int(input("C-언어 : "))
            pyscr = int(input("파이썬 : "))
            self.students.append(Student(stdnum, name, engscr, c_scr, pyscr))       # 입력받은 정보를 객체 Student의 멤버 변수를 활용하여 객체 students에 저장
        self.rank()
    
    def rank(self):                                             # 학생들의 평균 성적으로 등수를 결정하고, 리스트에 등수를 입력한 순서대로 작성하는 함수 ex) [10, 50 , 30, 90, 70]
        sorted_students = sorted(self.students, reverse=True)   #ex) [90, 70, 50, 30, 10]
        for k, student in enumerate(sorted_students):           #[5, 4, 3, 1, 2]
            student.rnk  = k + 1                                

    def prt(self):                      # 학번, 이름, 영어/C-언어/파이썬, 총점, 평균, 학점, 등수 를 출력 양식과 함께 출력하는 함수
        print("\t\t성적관리 프로그램" + "\n" + "="*80)
        print("학번"+"\t\t이름"+"\t\t영어"+"\tC-언어"+"\t파이썬"+"\t총점"+"\t평균"+"\t학점"+"\t등수")
        print("="*80)
        for student in self.students:
            print((student.stdnum) + "\t" + student.name + "\t\t" + student.engscr + "\t" + student.c_scr + "\t" + student.pyscr + "\t" + student.summ + "\t" + student.avg + "\t" + student.grd + "\t" + student.rnk + '\n')
        print("="*80 + '\n')

        sorted_by_total = sorted(self.students, reverse=True)
        print("총점 내림차순 정렬 결과 : ", end=' ')
        for j in sorted_by_total:
            print(j.sumtotal + ' ', end=' ')
        print('\n')
        print("평균 점수가 80점이 넘는 학생 수 : " + self.check_80 + "명" + '\n\n')

    def check_80(self):               # 학생들의 평균 성적 중 80점이 넘는 학생의 수를 카운트 하는 함수
        return len([s for s in self.students if s.avg >= 80])

    def Delete_Data(self):            # 리스트에 저장된 데이터를 삭제하는 함수
        self.students.clear()
        print("입력되었던 데이터가 모두 지워졌습니다." + '\n\n')

    def find_std(self, name):           # 찾고자 하는 학생의 이름을 입력하고 저장되어있는 학생 정보의 이름과 일치하는지 확인하는 함수, 일치할 시 학번과 이름을 출력
        found = [s for s in self.students if s.name == name]
        if not found:
            print("찾고 있는 학생이 없습니다.\n")
        else:
            for s in found:
                print(f"{s.stdnum}\t{s.name}\n")

def main():                             # 메인 함수 부분으로 정의하여 이 함수 정의 아래 부터 프로그램의 시작점임을 알림
    manager = GradeManager()            # 성적 관리를 저장하는 함수를 manager 로 객체화 호출
    while True:                         # 종료 메뉴를 고를 때까지 반복
        print("<성적관리 프로그램>" + '\n' + "1. 학생 정보 등록"+'\n'+"2. 학생 정보 출력" + '\n' + "3. 학생 정보 제거" + '\n' +"4. 학생 찾기 (이름으로 검색)" + '\n' + "5. 종료" + '\n')
        tmpnum = input("메뉴를 고르시오. : ")
        print('\n')

        if tmpnum == "1":               # 1번 메뉴 선택시 만약 입력된 값이 있다면 아래 문구 출력, 입력된 내용이 없다면 manager 객체의 InputValue 함수 호출
            if manager.students:
                print("이미 데이터 입력되었습니다. 다시 입력하려면 먼저 기존 데이터를 삭제해야 합니다." + '\n\n')
                continue
            manager.Input_Value()
            continue

        elif tmpnum == "2":             # 2번 메뉴 선택시 만약 입력된 값이 없다면 아래 문구 출력, 입력된 내용이 있다면 manager 객체의 prt 함수 호출
            if not manager.students:
                print("저장된 데이터가 없습니다. 새 데이터를 입력해주십시오." + '\n\n')
                continue
            manager.prt()
            continue

        elif tmpnum == "3":             # 3번 메뉴 선택시 만약 입력된 값이 없다면 아래 문구 출력, 입력된 내용이 있다면 manager 객체의 Delete_Data 함수 호출 
            if not manager.students:
                print("저장된 데이터가 없습니다." + '\n\n')
                continue
            manager.Delete_Data()
            continue

        elif tmpnum == "4":             # 4번 메뉴 선택시 만약 입력된 값이 없다면 아래 문구 출력, 입력된 내용이 있다면 찾고자 하는 학생의 이름을 임시 저장, manager 객체의 find_std 함수 호출 
            if not manager.students:
                print("저장된 데이터가 없어 학생 정보를 찾을 수 없습니다." + '\n\n')
                continue
            name = input("찾으려는 학생의 이름을 입력하십시오. : ")
            print('\n')
            manager.find_std(name)
            continue

        elif tmpnum == "5":             # 5번 메뉴 선택시 반복문을 종료함으로써 프로그램을 종료함
            break
        else:                           # 메뉴의 범위 외의 선택을 했을 시 문구 출력
            print("잘못된 입력입니다.\n")
            continue

if __name__ == "__main__":              # __name__의 역할은 뒤의 "__main__" 이라는 이름을 가진 함수가 나오면 그 부분부터 프로그램을 시작하겠다고 판단함
    main()