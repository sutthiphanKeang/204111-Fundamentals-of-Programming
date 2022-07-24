def pyramid_stairs(n):
    #ใช้ if ดักกรณีที่ input เป็น 0
    if n > 0:
        #ทำส่วนข้างบนที่เป็นรูปแบบที่ล็อกไว้ แต่คุณช่องว่างเข้าไปด้วย
        people = (' '*(5*(n-1)) + '  o  ' + '*'*12 + '  o\n')
        people += (' '*(5*(n-1)) + ' /|\ *' + ' '*10 + '* /|\\\n')
        people += (' '*(5*(n-1)) + ' / \ *' + ' '*10 + '* / \\\n')

    
        #ส่วนที่เป็นส่วนกลางใช้ลูปในการทำ จนถึง n แล้วคุณช่องว่างไปเรื่อยๆ 
        for i in range(2,n + 1):
            people += (' '*(5*(n-i)) + '  o  ' + '*'*6 + ' '*(10 * (i - 1)) + '*'*6 + '  o\n')
            people += (' '*(5*(n-i)) + ' /|\ *' + ' '*(10 * i) + '* /|\\\n')
            people += (' '*(5*(n-i)) + ' / \ *' + ' '*(10 * i) + '* / \\\n')

        
        #ส่วนท้ายที่เป็น*ใช้ลำดับในการหาออกมาเป็นสตร
        people += ('*'*(12+((n*5)*2)))
        print(people)

  
def main():
    n = int(input())
    pyramid_stairs(n)

    
if __name__ == '__main__':
    main()

#630510647
#สุทธิพันธ์ ประนันแปง
#002
#Lab07_EX2

