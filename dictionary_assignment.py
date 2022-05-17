LeeEunJi = {"name":"eunji", "age":"21", "birthday":"2002년 8월 17일", "sex":"여자", "phone_number":"010-6284-4144"}
print(LeeEunJi)
KangMinJeong = {"name":"minjeong", "age":"21", "birthday":"2002년 2월 17일", "sex":"여자", "phone_number":"010-2191-3897"}
print(KangMinJeong)
KimYoungHee = {"name":"younghee", "age":"20", "birthday":"2003년 8월 17일", "sex":"여자", "phone_number":"010-1234-5678"}
print(KimYoungHee)

name = [1, 2, 3]
name[0] = LeeEunJi.get('name')
name[1] = KangMinJeong.get('name')
name[2] = KimYoungHee.get('name')
age = [1, 2, 3]
age[0] = LeeEunJi.get('age')
age[1] = KangMinJeong.get('age')
age[2] = KimYoungHee.get('age')
birthday = [1, 2, 3]
birthday[0] = LeeEunJi.get('birthday')
birthday[1] = KangMinJeong.get('birthday')
birthday[2] = KimYoungHee.get('birthday')
sex = [1, 2, 3]
sex[0] = LeeEunJi.get('sex')
sex[1] = KangMinJeong.get('sex')
sex[2] = KimYoungHee.get('sex')
phone_number = [1, 2, 3]
phone_number[0] = LeeEunJi.get('phone_number')
phone_number[1] = KangMinJeong.get('phone_number')
phone_number[2] = KimYoungHee.get('phone_number')
print(name)
print(age)
print(birthday)
print(sex)
print(phone_number)